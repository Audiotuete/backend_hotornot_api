from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, BooleanField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from app_hotornot.models import Question, UserAnswer

class User(AbstractUser):

  # First Name and Last Name do not cover name patterns
  # around the globe.
  name = CharField(_("Name of User"), blank=True, max_length=255)
  push_notifications = BooleanField(("Push notfications enabled"), default=True)
  reg_code = CharField(("Registration Code"),max_length=8, null=True, blank=True)

  def get_absolute_url(self):
    return reverse("users:detail", kwargs={"username": self.username})

  def __str__(self):
    return self.username

  def save(self, *args, **kwargs):
    # If Question doesn't already exist create an (empty) UserAnswer entry for each User in the database upfront.
    if self.pk is None:

      super(User, self).save(*args, **kwargs)
      
      all_questions = Question.objects.all()
      useranswer_list = []
      
      for new_question in all_questions:
        useranswer_list.append(UserAnswer(user = self, question = new_question))
      
      UserAnswer.objects.bulk_create(useranswer_list)
    # End
    else:
      super(User, self).save(*args, **kwargs)


