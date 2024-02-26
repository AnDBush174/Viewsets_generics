# myproject/myproject/urls.py
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from courses.views import CourseViewSet
from lessons.views import LessonViewSet
from users.views import UserViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
