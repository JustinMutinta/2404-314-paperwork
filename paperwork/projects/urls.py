from django.urls import path
from . import views

# from paperwork.paperwork.urls import urlpatterns

urlpatterns = [
    path('projects/', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
]