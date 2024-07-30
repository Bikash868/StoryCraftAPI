from django.urls import path
from story.views import Login, Register, UserStoriesView, CreateStory


urlpatterns = [
    path('register', Register.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),

    path('all',UserStoriesView.as_view(), name='all_stories'),
    path('create',CreateStory.as_view(),name='create-story')
]