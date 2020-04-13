"""Schema Graphene Platzigram2"""

#Django
from users.schema import Query

#Utilities
import graphene


class Query(Query, graphene.ObjectType):
    pass


schema =  graphene.Schema(query=Query)