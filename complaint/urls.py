from django.urls import path, include
from complaint import views as ComplaintView

urlpatterns = [
    path('complaint/', ComplaintView.ComplaintList.as_view()),

]
