from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

class Question(models.Model):
  question_text = models.TextField(max_length=250)
  question_videolink = models.CharField(max_length=150, null=True, blank=True)
  question_imagelink = models.CharField(max_length=150, null=True, blank=True)
  pub_date = models.DateTimeField(auto_now_add=True)
  # answers = models.ManyToManyField(User, through='User_Answer', unique=True)

  def __str__(self):
    return self.question_text

  def save(self, *args, **kwargs):
    User = get_user_model()
    # If User doesn't already exist create an (empty) UserAnswer entry for each Question in the database upfront.
    if self.pk is None:
      super(Question, self).save(*args, **kwargs)
      

      all_users = User.objects.all()
 
      useranswer_list = []
      
      for new_user in all_users:
        useranswer_list.append(UserAnswer(user = new_user, question = self))
      
      UserAnswer.objects.bulk_create(useranswer_list)
    # End
    else:
      super(Question, self).save(*args, **kwargs)

class UserAnswer(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
  question = models.ForeignKey('Question', on_delete=models.CASCADE )
  answer_value = models.IntegerField(default=-1, validators=[MaxValueValidator(2), MinValueValidator(-1)])
  answer_note = models.TextField(max_length=250, null=True, blank=True)
  first_touched = models.DateTimeField(null=True, blank=True)
  last_touched = models.DateTimeField(auto_now=True)
  count_touched = models.PositiveIntegerField(default=0)

  class Meta:
        unique_together = ['user', 'question']

  def __str__(self):
    return str(self.user)

