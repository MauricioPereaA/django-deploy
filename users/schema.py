"""Schema Users"""

#Django
from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User
from .serializers import UserSerializer
from graphene import relay, Schema
from graphene_django.rest_framework.mutation import SerializerMutation


#Utilities
import graphene

#SqlAlchemy
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


class UserType(SerializerMutation):
    class Meta:
        serializer_class = UserSerializer


class UserConnection(relay.Connection):
    class Meta:
        node = UserType

class UserMDBType(SerializerMutation):
    class Meta:
        serializer_class = UserSerializer


class UserMDBConnection(relay.Connection):
    class Meta:
        node = UserType


class Query(object):
    """Query graphql relay connection"""

    all_users = relay.ConnectionField(UserConnection)
    #all_posts = graphene.List(PostType)
    all_usersMDB = relay.ConnectionField(UserMDBConnection)

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
    
    def resolve_all_usersMDB(self, info, **kwargs):
        uri = 'mysql+pymysql://root:password@127.0.0.1:3306/platzigram'
        engine = create_engine(uri)
        conn = engine.connect().connection
        session = sessionmaker(bind=engine)()
        query = "select * from users"
        val = redis.get(query)
        if val:
            return val
        my_vals = []
        for x in session.execute(query):

            my_vals.append(dict(id=x.id, nombre=x.nombre, edad=x.edad))
            
        return my_vals

    def resolve_clientMDB(self, info, **kwargs):
        id = kwargs.get('id')
        nombre = kwargs.get('nombre')
        edad = kwargs.get('edad')

        if id is not None:
            return Client.objects.get(pk=id)

        if nombre is not None:
            return Client.objects.get(nombre=nombre)




