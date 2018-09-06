from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField


class Question(models.Model):
  question_text = models.TextField(max_length=250)
  question_videolink = models.CharField(max_length=150, null=True, blank=True)
  question_imagelink = models.CharField(max_length=150, null=True, blank=True)
  pub_date = models.DateTimeField(auto_now_add=True)
  # answers = models.ManyToManyField(User, through='User_Answer', unique=True)

  class Meta:
    abstract = True

  def __str__(self):
    return self.question_text


  def save(self, *args, **kwargs):
    User = get_user_model()
    # If User doesn't already exist create an (empty) UserAnswer entry for each Question in the database upfront.
    if self.pk is None:
      super(Question, self).save(*args, **kwargs)
      
      all_users = User.objects.all()
      useranswer_list = []

      subclass_name = self.__class__.__name__
      
      if subclass_name == 'QuestionYesOrNo':
        for new_user in all_users:
          useranswer_list.append(UserAnswerYesOrNo(user = new_user, question = self))

        UserAnswerYesOrNo.objects.bulk_create(useranswer_list)

      elif subclass_name == 'QuestionOpen':
        for new_user in all_users:
          useranswer_list.append(UserAnswerOpen(user = new_user, question = self))

        UserAnswerOpen.objects.bulk_create(useranswer_list)

      elif subclass_name == 'QuestionMultiple':
        for new_user in all_users:
          useranswer_list.append(UserAnswerMultiple(user = new_user, question = self))

        UserAnswerMultiple.objects.bulk_create(useranswer_list)
      else:
          pass
    # End
    else:
      super(Question, self).save(*args, **kwargs)

class QuestionYesOrNo(Question):
  pass

class QuestionOpen(Question):
  pass

class QuestionMultiple(Question):
  options = ArrayField(models.CharField(max_length=150, blank=True), default=list, null=True, size=4)

class UserAnswer(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
  first_touched = models.DateTimeField(null=True, blank=True)
  last_touched = models.DateTimeField(auto_now=True)
  count_touched = models.PositiveIntegerField(default=0)

  class Meta:
    abstract = True
    unique_together = ['user', 'question']

  def __str__(self):
    return str(self.user)

class UserAnswerYesOrNo(UserAnswer):
  question = models.ForeignKey('QuestionYesOrNo', on_delete=models.CASCADE )
  answer_value = models.IntegerField(default=-1, validators=[MaxValueValidator(2), MinValueValidator(-1)])
  answer_note = models.TextField(max_length=250, null=True, blank=True)

class UserAnswerOpen(UserAnswer):
  question = models.ForeignKey('QuestionOpen', on_delete=models.CASCADE )
  answer_text = models.TextField(max_length=250, null=True, blank=True)

class UserAnswerMultiple(UserAnswer):
  question = models.ForeignKey('QuestionMultiple', on_delete=models.CASCADE )
  # option = models.ForeignKey('Option', on_delete=models.CASCADE )

 


