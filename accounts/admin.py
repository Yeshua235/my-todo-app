from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model =  CustomUser
    list_display = [
        'email',
        'username',
        'first_name',
        'last_name',
        'is_staff',        
    ]
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields':('first_name','last_name',)}),)


admin.site.register(CustomUser, CustomUserAdmin)
