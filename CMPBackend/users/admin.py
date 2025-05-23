from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Personaliza la visualización de los campos en el admin
    list_display = UserAdmin.list_display + ('is_student', 'is_admin_user',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_student', 'is_admin_user')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_student', 'is_admin_user',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)