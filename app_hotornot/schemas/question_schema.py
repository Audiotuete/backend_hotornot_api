import graphene
from graphene_django import DjangoObjectType

from ..models import Question

class QuestionType(DjangoObjectType):
  class Meta:
    model = Question

class Query(graphene.ObjectType):
  questions = graphene.List(QuestionType)

  def resolve_questions(self, info, **kwargs):
    print(Question.objects.all())
    return Question.objects.all()


