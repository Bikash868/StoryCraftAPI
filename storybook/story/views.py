from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response

from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *


@permission_classes((AllowAny))
class Register(APIView):
    def post(self, request):
        username = request.data.get("name")
        password = request.data.get("password")
        genre = request.data.get("genre")
        email = request.data.get("email")

        if not username or not password or not email:
            return Response({
                "Error": "Name, Password and Email are required field"
            }, status = status.HTTP_400_BAD_REQUEST)
        
        existing_user = UserProfile.objects().filter(email = email).first()

        if not existing_user:
            return Response({
                "Error": "User already exist"
            }, status = status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        UserProfile.objects.create(
            user = user,
            email = email,
            genre = genre
        )

        return Response({
            "Message": "User created Successfully"
        }, status = status.HTTP_200_OK)

@permission_classes((AllowAny))
class Login(APIView):
    def post(self, request):
        if not request.data:
            return Response({
                "Error": "Username and Password are required"
            }, status = status.HTTP_400_BAD_REQUEST)
        
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({
                "Error": "Invalid username or password"
            }, status = status.HTTP_404_NOT_FOUND)
        
        user = authenticate(username=username,password=password)
        token,_ = Token.objects.get_or_create(user = user)

        return Response({
            "Token": token.key
        }, status = status.HTTP_200_OK)
    

class UserStoriesView(APIView):
    def get(self, request):
        user = request.user
        matched_stories = MatchUserStory.objects.filter(user=user).values_list('story', flat=True)
        return Response({
            "stories": StoryContent.objects.filter(id__in=matched_stories)
        }, status = status.HTTP_200_OK)
    

class CreateStory(APIView):
    def post(self, request):
        user = request.user

        # Chatgpt intergration here
        story = StoryContent.objects.get_or_create(
            title='story title',
            content='This is demo content'
        )
        MatchUserStory.objects.get_or_create(user=user, story=story)

        return Response({
            "Message": "Story created successfully",
            "story": StoryContentSerializer(story)
        }, status=status.HTTP_200_OK)


