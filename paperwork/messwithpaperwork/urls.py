from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('testset/<int:pk>', views.testSet, name='testSet'),
    path('delete_testset/<int:pk>', views.delete_testset, name='delete_testset'),
    path('add_testset', views.add_testset, name='add_testset'),
]