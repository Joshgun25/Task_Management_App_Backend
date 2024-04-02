from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'author', 'author_username', 'title', 'description', 'deadline', 'created_at']
