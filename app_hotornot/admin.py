from django.contrib import admin

from .models import Question, UserAnswer

class UserAnswerAdmin(admin.ModelAdmin):
  model = UserAnswer
  list_display = [ 'user', 'question', 'answer_value', 'answer_note']

  def has_add_permission(self, request):
    return False

admin.site.register(Question)
admin.site.register(UserAnswer, UserAnswerAdmin)