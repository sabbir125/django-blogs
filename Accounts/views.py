from django.shortcuts import render
from .serializers import UserSerializer,SignupSerializer
from rest_framework.generics import ListAPIView,UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomNewUser


#create user profile view
class UserProfileView(ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        user = self.request.user

        if user is not None:
            print(user)
            return CustomNewUser.objects.filter(id=user.id)



class UserProfileUpdateView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = CustomNewUser.objects.all()


class SingupView(APIView):
    
    def post(self,request,format=None):

        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors)