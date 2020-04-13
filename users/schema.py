"""Schema Users"""

#Django
from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User
from .serializers import UserSerializer
from graphene import relay, Schema
from graphene_django.rest_framework.mutation import SerializerMutation


#Utilities
import graphene


class UserType(SerializerMutation):
    class Meta:
        serializer_class = UserSerializer


class UserConnection(relay.Connection):
    class Meta:
        node = UserType



class Query(object):
    """Query graphql relay connection"""

    all_users = relay.ConnectionField(UserConnection)
    #all_posts = graphene.List(PostType)

    user = graphene.Field(
        UserType,
        id=graphene.Int(),
        nombre=graphene.String()
    )

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_client(self, info, **kwargs):
        id = kwargs.get('id')
        nombre = kwargs.get('username')

        if id is not None:
            return User.objects.get(pk=id)
        if nombre is not None:
            return User.objects.get(nombre=nombre)
        return None





