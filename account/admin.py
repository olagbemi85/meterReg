from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import *
from .models import *


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserFormUpdate
    add_form = UserForm
    list_display = ('email', 'phone_number', 'first_name', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('first_name', 'email', 'phone_number', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'last_login', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {'fields': ('first_name', 'phone_number', 'email', 'password1', 'password2')}),
    )
    search_fields = ('email', 'first_name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if is_superuser:
            form.base_fields['is_superuser'].disabled = True
        return form

#admin.site.register(User, UserAdmin)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['stateName']


@admin.register(LGA)
class LGAAdmin(admin.ModelAdmin):
    list_display =['localGovName']