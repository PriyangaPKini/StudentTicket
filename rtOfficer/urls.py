from django.urls import path,include


from rtOfficer import views

urlpatterns = [
    path('pending', views.ApplicationList.as_view()),


]