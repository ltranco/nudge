import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from accounts.schema import UserType
from .models import Topic


class TopicType(DjangoObjectType):
    class Meta:
        model = Topic


class Query(graphene.ObjectType):
    topics = graphene.List(TopicType)

    @login_required
    def resolve_topics(self, info, **kwargs):
        user = info.context.user
        if not user:
            return Topic.objects.none()
        elif user.is_superuser:
            return Topic.objects.all()
        else:
            return Topic.objects.filter(owner=user)


class CreateTopic(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    name = graphene.String()
    owner = graphene.Field(UserType)

    class Arguments:
        url = graphene.String()
        name = graphene.String()

    def mutate(self, info, url, name):
        user = info.context.user or None

        topic = Topic(url=url, name=name, owner=user)
        topic.save()

        return CreateTopic(
            url=topic.url,
            name=topic.name,
            owner=topic.owner
        )


class Mutation(graphene.ObjectType):
    create_topic = CreateTopic.Field()
