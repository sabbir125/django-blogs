from rest_framework import serializers

from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    """Serializer for `Blog` instances."""

    class Meta:
        model = Blog
        exclude = ["id"]
