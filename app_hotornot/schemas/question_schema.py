import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from itertools import chain

from ..models import Question, QuestionMultiple, QuestionOpen, QuestionYesOrNo

class BaseQuestion(graphene.Interface):
  id = graphene.Int()
  order = graphene.Int()
  question_text = graphene.String()


class QuestionMultipleType(DjangoObjectType):
  options = graphene.String()
  class Meta:
    model = QuestionMultiple
    interfaces = [ BaseQuestion ]

class QuestionOpenType(DjangoObjectType):
  class Meta:
    model = QuestionOpen
    interfaces = [ BaseQuestion ]

class QuestionYesOrNoType(DjangoObjectType):
  class Meta:
    model = QuestionYesOrNo
    interfaces = [ BaseQuestion ]

class AllQuesetions(graphene.ObjectType):
  all_questions = graphene.List(BaseQuestion)

  def resolve_all_questions(self, info, **kwargs):

    multi_questions = QuestionMultiple.objects.all()
    yes_no_questions = QuestionYesOrNo.objects.all()
    open_questions = QuestionOpen.objects.all()

    all_questions = sorted(
      chain(
        multi_questions, 
        yes_no_questions, 
        open_questions
      ),key=lambda instance: instance.order)

    return all_questions

