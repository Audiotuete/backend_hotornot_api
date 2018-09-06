import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

class UserType(DjangoObjectType):
  class Meta:
    model = get_user_model()

class Query (graphene.ObjectType):
  users = graphene.List(UserType)

  def resolve_users(self, info, **kwargs):
    return User.objects.all()

