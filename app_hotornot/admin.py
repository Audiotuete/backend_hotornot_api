from django.contrib import admin

from .models import QuestionOpen, QuestionYesOrNo, QuestionMultiple, UserAnswerOpen, UserAnswerYesOrNo, UserAnswerMultiple

class UserAnswerOpenAdmin(admin.ModelAdmin):
  model = UserAnswerOpen
  list_display = [ 'user', 'question' ]
  actions = None

  def has_add_permission(self, request):
    return False
  def has_delete_permission(self, request, obj=None):
    return False

class UserAnswerYesOrNoAdmin(admin.ModelAdmin):
  model = UserAnswerYesOrNo
  list_display = [ 'user', 'question', 'answer_value', 'answer_note' ]
  actions = None

  def has_add_permission(self, request):
    return False
  def has_delete_permission(self, request, obj=None):
    return False

class UserAnswerMultipleAdmin(admin.ModelAdmin):
  model = UserAnswerMultiple
  list_display = [ 'user', 'question' ]
  actions = None

  def has_add_permission(self, request):
    return False
  def has_delete_permission(self, request, obj=None):
    return False

admin.site.register(QuestionOpen)
admin.site.register(QuestionYesOrNo)
admin.site.register(QuestionMultiple)
admin.site.register(UserAnswerOpen, UserAnswerOpenAdmin)
admin.site.register(UserAnswerYesOrNo, UserAnswerYesOrNoAdmin)
admin.site.register(UserAnswerMultiple, UserAnswerMultipleAdmin)