from django.contrib import admin
from django.urls import path, include


from students import views

urlpatterns = [
    path('', views.StudentList.as_view(), name='create'),
    path('<int:code>/', views.IndividualView.as_view()),


]
