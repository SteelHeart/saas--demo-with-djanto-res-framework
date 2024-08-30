from django.shortcuts import render
from rest_framework import status
# from rest_framework.generics import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from utilities.utils import ResponseInfo
from .serializers import TodoSerializer
from .models import Todo


class TodoListView(APIView):

    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)


    def __init__(self, *args, **kwargs):
        self.response_format = ResponseInfo().response


    def get(self, request, *args, **kwargs):
       print(request.data)
       return Todo.objects.filter(owner=request.user).values_list(flat=True)
    

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(owner=request.user)
            self.response_format["data"] = serializer.data

        return Response(self.response_format, status=self.response_format["status_code"])

    

class TodoDetailView(APIView):

    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)


    def __init__(self, *args, **kwargs):
        self.response_format = ResponseInfo().response


    def get(self, request, id, *args, **kwargs):
        return Todo.objects.filter(owner=request.user).values_list(flat=True)
    

    def put(self, request, id, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(is_done=True)
            self.response_format["data"] = serializer.data
        return Response(self.response_format, status=self.response_format["status_code"])
    

    def delete(self, request, id, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(deleted_at=True)
            self.response_format["data"] = serializer.data
        return Response(self.response_format, status=self.response_format["status_code"])