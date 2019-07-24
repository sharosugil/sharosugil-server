from rest_framework import generics
from django.views import generic
from django.shortcuts import render

from .models import *
from .serializers import *


class MeetingList(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    

class MeetingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    
class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    

class CheckingList(generics.ListCreateAPIView):
    queryset = Checking.objects.all()
    serializer_class = CheckingSerializer
    
    
class CheckingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checking.objects.all()
    serializer_class = CheckingSerializer


class IndexView1(generic.TemplateView):
    template_name = 'attendance/testPage1.html'


class IndexView2(generic.TemplateView):
    template_name = 'attendance/testPage2.html'