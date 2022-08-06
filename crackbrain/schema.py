import graphene
import profiles.gql.schema

class Query(
    profiles.gql.schema.Query,
    graphene.ObjectType
    ):
    pass

class Mutation(
    profiles.gql.schema.Mutation,
    graphene.ObjectType
    ):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)