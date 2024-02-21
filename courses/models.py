# myproject/courses/models.py
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    preview = models.ImageField(upload_to='previews/')
    description = models.TextField()


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    preview = models.ImageField(upload_to='previews/')
    video_link = models.URLField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return self.name
