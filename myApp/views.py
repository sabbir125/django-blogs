from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Blog
from .serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    """CRUD viewset for blog posts.

    Authenticated users can create, update, and delete entries; list and
    retrieve are open to everyone.
    """

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # future extension: associate the creating user as author
        serializer.save()
