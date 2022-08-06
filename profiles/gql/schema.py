from dataclasses import fields
from django.contrib.auth.models import User, Group
from graphene_django.types import DjangoObjectType
import graphene

class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ("password",)

class GroupType(DjangoObjectType):
    class Meta:
        model = Group

class CreateGroupMutation(graphene.Mutation):
    group = graphene.Field(GroupType)
    class Arguments:
        name = graphene.String(required=True)
    
    @classmethod
    def mutate(cls,root,info,name):
        group = Group.objects.create(name=name)

        return CreateGroupMutation(group=group)

class UserConnection(graphene.relay.Connection):
    class Meta:
        node = UserType

class Query(graphene.ObjectType):
    users = graphene.relay.ConnectionField(UserConnection)
    groups = graphene.List(GroupType)

    def resolve_users(root,info,**kwargs):
        return User.objects.all()
    
    def resolve_groups(root,info,**kwargs):
        return Group.objects.all()

class Mutation(graphene.ObjectType):
    createGroup = CreateGroupMutation.Field()