from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'Tasks'

router = routers.SimpleRouter()
router.register('tasks', views.TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls))
]
