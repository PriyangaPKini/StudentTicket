"""stPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns


# from . rtOfficer import views as officerDisplay
from students import views
from complaint import views as ComplaintView
from rtOfficer import views as officerDisplay
urlpatterns = [
    path('complaint/', ComplaintView.ComplaintList.as_view()),

    path('students/', views.StudentList.as_view()),

    path('rto/', include('rtOfficer.urls')),

    path('',  admin.site.urls),


    # path('', officerDisplay.ApplicationList.as_view()),


]
