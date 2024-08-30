from rest_framework import serializers
from .models import Todo
from users.serializers import GetUsersSerializer

class TodoSerializer(serializers.ModelSerializer):

    owner = GetUsersSerializer()

    class Meta:
        model = Todo
        fields = ("id", "label", "is_done", "owner", "created_at", "deleted_at")
