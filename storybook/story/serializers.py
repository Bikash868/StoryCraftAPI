from rest_framework import serializers
from .models import StoryContent

class StoryContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryContent
        fields = ['title', 'content']