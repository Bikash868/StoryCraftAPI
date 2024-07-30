from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=100, null = False)
    genre = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.name

class StoryContent(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.CharField(max_length=1000, null=False, blank=False)

    def __str__(self) -> str:
        return self.title

class MatchUserStory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    story = models.ForeignKey(StoryContent, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return 'sdfsdfs'

