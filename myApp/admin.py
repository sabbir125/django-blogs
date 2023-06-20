from django.contrib import admin
from .models import My_blogs


# Register your models here.
@admin.register(My_blogs)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title",
                    "text",
                    "code"]
