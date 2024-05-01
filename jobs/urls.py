from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.JobsAPIView.as_view())
]