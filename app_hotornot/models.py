from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from ordered_model.models import OrderedModel


# class Poll(models.Model):
#   name = models.CharField(max_length=50)
#   description = models.TextField(max_length=250)
  
#   def __str__(self):
#     return self.name


class Question(OrderedModel):
  # poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
  question_text = models.TextField(max_length=250)
  question_videolink = models.CharField(max_length=150, null=True, blank=True)
  question_imagelink = models.CharField(max_length=150, null=True, blank=True)
  pub_date = models.DateTimeField(auto_now_add=True)

  order_class_path = __module__ + '.Question'
  # position = PositionField(collection='poll', parent_link='question_ptr')

  class Meta:
    ordering = ('order',)
    # abstract = True

  def __str__(self):
    return self.question_text

  def save(self, *args, **kwargs):
    User = get_user_model()
    # If User doesn't already exist create an (empty) UserAnswer entry for each Question in the database upfront.
    if self.pk is None:
      super(Question, self).save(*args, **kwargs)
      
      all_users = User.objects.all()
      useranswer_list = []
      # for a_user in all_users:
      #     useranswer_list.append(UserAnswer(user = a_user, question = self))

      # UserAnswer.objects.bulk_create(useranswer_list)     

      subclass_name = self.__class__.__name__
      
      if subclass_name == 'QuestionYesOrNo':
        for a_user in all_users:
          useranswer_list.append(UserAnswerYesOrNo(user = a_user, question = self))

        UserAnswerYesOrNo.objects.bulk_create(useranswer_list)

      elif subclass_name == 'QuestionOpen':
        for a_user in all_users:
  
          useranswer_list.append(UserAnswerOpen(user = a_user, question = self))

        UserAnswerOpen.objects.bulk_create(useranswer_list)

      elif subclass_name == 'QuestionMultiple':
        for a_user in all_users:
          useranswer_list.append(UserAnswerMultiple(user = a_user, question = self))

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
  user = models.ForeignKey(settings.AUTH_USER_MODEL, default=0, on_delete=models.CASCADE)
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
  answer_value = models.IntegerField(default=-1, validators=[MaxValueValidator(2), MinValueValidator(0)])
  answer_note = models.TextField(max_length=250, null=True, blank=True)

class UserAnswerOpen(UserAnswer):
  question = models.ForeignKey('QuestionOpen', on_delete=models.CASCADE )
  answer_text = models.TextField(max_length=250, null=True, blank=True)

class UserAnswerMultiple(UserAnswer):
  question = models.ForeignKey('QuestionMultiple', on_delete=models.CASCADE )
  answer_choice_key = models.IntegerField(default=-1, validators=[MinValueValidator(0)])
  # option_set = models.ForeignKey('OptionSet', on_delete=models.CASCADE, default=1 )
  # option = models.ForeignKey('Option', on_delete=models.CASCADE )

# class OptionSet(models.Model):
#   set_name = models.CharField(max_length=150, null=True, blank=True)

#   def __str__(self):
#     return str(self.set_name)





 


