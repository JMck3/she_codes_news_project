from django.contrib import admin

from django.contrib import admin
from .models import NewsStory
from .forms import StoryForm

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username',]

admin.site.register(NewsStory) 
