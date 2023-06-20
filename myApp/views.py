import base64
from django.shortcuts import render
from .serializers import MY_BlogSerializer,UserRegistrationSerializer
from .models import My_blogs
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.authentication  import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes




@api_view(["POST"])
def register_api_view(request):
    if request.method == "POST":
        serializer = UserRegistrationSerializer(data=request.data)
        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "User Created"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])

def get_all_blogView(request, pk=None):
    if request.method == "GET":
        id = pk
        # id=request.data.get("id")
        # if id is not None:
        #     stu = My_blogs.objects.get(id=id)
        #     serializer = MY_BlogSerializer(stu)
        #     return Response(serializer.data)

        stu = My_blogs.objects.all()
        serializer = MY_BlogSerializer(stu, many=True)
        return Response(serializer.data)


@api_view(["POST"])
def post_blogView(request,pk=None):
    if request.method == "POST":
        data = request.data
        print(data)

        serializer = MY_BlogSerializer(data=data)
        # print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(["PUT"])
def update_blogView(request,pk=None):
    if request.method == "PUT":
        id = pk
        stu = My_blogs.objects.get(id=id)
        serializer = MY_BlogSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_blogView(request,pk=None):

    if request.method == "DELETE":
        id = pk
        stu = My_blogs.objects.get(id=id)
        stu.delete()
        return Response({"msg": "Data Deleted"})
















