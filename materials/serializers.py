# myproject/courses/serializers.py
from rest_framework import serializers
from myproject.courses.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'instructor', 'description', 'created_at']
