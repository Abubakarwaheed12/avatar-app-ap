from django.contrib import admin
from user.models import User, Add_Appointment, Add_Event
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserModelAdmin(BaseUserAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'tc', 'image', 'is_admin',)
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password',)}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone',)}),  # Updated
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'phone', 'tc', 'password', 'image'),  # Updated
        }),
    )
    search_fields = ('email',)
    ordering = ('email', 'id',)
    filter_horizontal = ()

admin.site.register(User, UserModelAdmin)
admin.site.register(Add_Appointment)
admin.site.register(Add_Event)
