from django.contrib import admin
from .models import Blog


# Register the refactored blog model.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "text", "code"]
