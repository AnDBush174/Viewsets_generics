# myproject/lessons/serializers.py
from rest_framework import serializers
from .models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'course', 'title', 'content',
                  'order']  # Перечислите здесь все поля модели, которые хотите отображать
