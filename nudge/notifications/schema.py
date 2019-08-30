import graphene
from graphene_django import DjangoObjectType
from .models import Topic


class TopicType(DjangoObjectType):
    class Meta:
        model = Topic


class Query(graphene.ObjectType):
    topics = graphene.List(TopicType)

    def resolve_topics(self, info, **kwargs):
        return Topic.objects.all()


class CreateTopic(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    name = graphene.String()

    class Arguments:
        url = graphene.String()
        name = graphene.String()

    def mutate(self, info, url, name):
        topic = Topic(url=url, name=name)
        topic.save()

        return CreateTopic(
            url=url,
            name=name
        )


class Mutation(graphene.ObjectType):
    create_topic = CreateTopic.Field()
