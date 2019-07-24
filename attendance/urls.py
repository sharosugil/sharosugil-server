from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

app_name = 'attendance'
urlpatterns = [
    path('meeting/', MeetingList.as_view()),
    path('meeting/<int:pk>/', MeetingDetail.as_view()),
    path('person/', PersonList.as_view()),
    path('person/<int:pk>/', PersonDetail.as_view()),
    path('checking/', CheckingList.as_view()),
    path('checking/<int:pk>/', CheckingDetail.as_view()),
    path('index1/', IndexView1.as_view(), name="index1"),
    path('index2/', IndexView2.as_view(), name="index2"),
]