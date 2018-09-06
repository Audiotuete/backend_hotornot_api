import graphene
import datetime
from graphene_django import DjangoObjectType

from ..models import UserAnswer
from .user_schema import UserType
from .question_schema import QuestionType


class UserAnswerType(DjangoObjectType):
  class Meta:
    model = UserAnswer

class Query(graphene.ObjectType):
  user_answers = graphene.List(UserAnswerType)

  def resolve_user_answers(self, info, **kwargs):
    return UserAnswer.objects.all()

class UpdateUserAnswer(graphene.Mutation):
  user = graphene.Field(UserType)
  question = graphene.Field(QuestionType)
  answer_value = graphene.Int()
  answer_note = graphene.String()
  first_touched = graphene.types.datetime.DateTime()
  last_touched = graphene.types.datetime.DateTime()
  count_touched = graphene.Int()
  pass
  
  class Arguments:
    question_id = graphene.Int(required=True)
    answer_value = graphene.Int(required=True)
    answer_note = graphene.String(required=True)

  def mutate(self, info, question_id, answer_value, answer_note):
    user = info.context.user
    if user.is_anonymous:
      raise Exception('You must be logged to vote!')
    
    answer = UserAnswer.objects.filter(question_id=question_id, user_id=user.id).first()
    if not answer:
      raise Exception('Invalid Link!')
    
    if not answer_value <= 2 and answer_value >= -1:
      raise Exception('Answer_value range is from -1 to 2')
    
    answer.answer_value = answer_value
    answer.answer_note = answer_note
    if answer.first_touched == None:
      answer.first_touched = datetime.datetime.now()
    answer.count_touched += 1
    answer.save()

    return UpdateUserAnswer(
      user = answer.user,
      question = answer.question,
      answer_value = answer.answer_value,
      answer_note = answer.answer_note,
      first_touched = answer.first_touched,
      last_touched = answer.last_touched,
      count_touched = answer.count_touched
    )

class Mutation(graphene.ObjectType):
    update_user_answer = UpdateUserAnswer.Field()

