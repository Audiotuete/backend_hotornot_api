from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, BooleanField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from app_hotornot.models import QuestionOpen, QuestionYesOrNo, QuestionMultiple, UserAnswerOpen, UserAnswerYesOrNo, UserAnswerMultiple


class User(AbstractUser):

  # First Name and Last Name do not cover name patterns
  # around the globe.
  name = CharField(_("Name of User"), blank=True, max_length=255)

  # COMMENT OUT AT NEW DEPLOY (then migrate without creating migrations afterwards uncomment and makemigrations)
  push_notifications = BooleanField(("Push notfications enabled"), default=True)
  reg_code = CharField(("Registration Code"),max_length=8, null=True, blank=True)
  # COMMENT OUT AT NEW DEPLOY

  def get_absolute_url(self):
    return reverse("users:detail", kwargs={"username": self.username})
  
  def __str__(self):
    return self.username

  # COMMENT OUT AT NEW DEPLOY
  def save(self, *args, **kwargs):
    # If Question doesn't already exist create an (empty) UserAnswer entry for each User in the database upfront.
    if self.pk is None:

      super(User, self).save(*args, **kwargs)
      
      open_questions = QuestionOpen.objects.all()
      multiple_choice_questions = QuestionMultiple.objects.all()
      yes_or_no_questions = QuestionYesOrNo.objects.all()

      useranswer_list = []
 
      for new_question in open_questions:
        useranswer_list.append(UserAnswerOpen(user = self, question = new_question))
      UserAnswerOpen.objects.bulk_create(useranswer_list)

      useranswer_list = []
 
      for new_question in multiple_choice_questions:
        useranswer_list.append(UserAnswerMultiple(user = self, question = new_question))
      UserAnswerMultiple.objects.bulk_create(useranswer_list)
      
      useranswer_list = []  

      for new_question in yes_or_no_questions:
        useranswer_list.append(UserAnswerYesOrNo(user = self, question = new_question))
      
      UserAnswerYesOrNo.objects.bulk_create(useranswer_list)
      useranswer_list = []  

    # End
    else:
      super(User, self).save(*args, **kwargs)
  # COMMENT OUT AT NEW DEPLOY


