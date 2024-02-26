# myproject/courses/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from myproject.materials.views import CourseViewSet

router = DefaultRouter()
router.register(r'materials', CourseViewSet)

urlpatterns = router.urls

