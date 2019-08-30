import graphene
import notifications.schema


class Query(notifications.schema.Query, graphene.ObjectType):
    pass


class Mutation(notifications.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
