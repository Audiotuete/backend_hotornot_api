import graphene
import graphql_jwt


from .schemas.question_schema import Query as QuestionQuery
from .schemas.question_schema import QuestionMultipleType, QuestionOpenType, QuestionYesOrNoType


from .schemas.user_schema import Query as UserQuery
from .schemas.user_schema import Mutation as UserMutation
# from .schemas.user_schema import Mutation as UserMutation

from .schemas.useranswer_schema import Query as UserAnswerQuery
from .schemas.useranswer_schema import Mutation as UserAnswerMutation


class Query(
  UserQuery,
  QuestionQuery,
  UserAnswerQuery,
  graphene.ObjectType
):
  pass

class Mutation(
  UserMutation,
  UserAnswerMutation,
  graphene.ObjectType
):
  token_auth = graphql_jwt.ObtainJSONWebToken.Field()
  verify_token = graphql_jwt.Verify.Field()
  refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, types=[QuestionMultipleType, QuestionOpenType, QuestionYesOrNoType, ], mutation=Mutation)