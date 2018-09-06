from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from backend_hotornot_api.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()

CUSTOM_USER_FIELDS = (
    (None, {'fields': ('reg_code', 'push_notifications',)}),
)

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]
