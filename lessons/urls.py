# myproject/lessons/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import LessonViewSet

router = DefaultRouter()
router.register(r'lessons', LessonViewSet)

urlpatterns = router.urls
