
from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', APIEmployee, basename='')
urlpatterns = router.urls