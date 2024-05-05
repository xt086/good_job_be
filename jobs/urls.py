# from django.urls import path
# from . import views

# urlpatterns = [
#     path('get/', views.getData),
#     path('create/', views.postData)
# ]

from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', APIJobs, basename='')
urlpatterns = router.urls