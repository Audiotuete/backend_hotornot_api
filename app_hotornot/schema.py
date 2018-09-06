import graphene

# from .schemas.user_schema import Query as UserQuery
# from .schemas.user_schema import Mutation as UserMutation

from .schemas.useranswer_schema import Query as UserAnswerQuery
from .schemas.useranswer_schema import Mutation as UserAnswerMutation


class Query(
  # user.schema.Query,
  # QuestionQuery,
  UserAnswerQuery,
  graphene.ObjectType
):
  pass

class Mutation(
  UserAnswerMutation,
  graphene.ObjectType
):
  pass

schema = graphene.Schema(query=Query, mutation=Mutation)