from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('testset/<int:pk>', views.testSet, name='testSet'),
]