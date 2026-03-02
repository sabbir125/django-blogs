from .serializers import UserSerializer,SignupSerializer
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import CustomNewUser


#create user profile view
class UserProfileView(ListAPIView):
    """Return the profile of the currently authenticated user."""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return CustomNewUser.objects.filter(id=user.id)



class UserProfileUpdateView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = CustomNewUser.objects.all()


class SignupView(APIView):
    """Create a new user account."""

    def post(self, request, format=None):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors)