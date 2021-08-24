from django.urls import path
from .import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # /news/ local host 8000 in our case
    path('<int:pk>/', views.StoryView.as_view(), name='story'), # /news/ int is the primary key for unique story
    path('add-story/', views.AddStoryView.as_view(), name='newStory') # /news/add-story/ addstory view where we add new story
]
