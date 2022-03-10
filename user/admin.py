from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User)
class UserAdmin(UserAdmin):
    
    """ User Admin """
    
 
    fieldsets =(
        (
            "Custom Profile",
            {
                "fields":(
                    'username',
                    'password',
                    'email',
                    "profile_img",
                    'tag',
                    'login_method'
                )
            }
        ),
    )
    
    list_display = ('username','email','tag')