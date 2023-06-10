from rest_framework import serializers
from django.utils import timezone
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'timestamp', 'title', 'description', 'due_date', 'tags', 'status')

    def create(self, validated_data):
        if validated_data.get('due_date') and validated_data['due_date'] < timezone.now().date():
            raise serializers.ValidationError("Due Date cannot be before Timestamp created.")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if validated_data.get('due_date') and validated_data['due_date'] < timezone.now().date():
            raise serializers.ValidationError("Due Date cannot be before Timestamp created.")
        return super().update(instance, validated_data)
