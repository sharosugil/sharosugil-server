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

    def get_context_data(self, **kwargs):
        context = super(IndexView1, self).get_context_data(**kwargs)
        context['member_list'] = Person.objects.all()
        context['meeting_list'] = Meeting.objects.order_by('-meeting_date')[:3]
        return context
    

class IndexView2(generic.TemplateView):
    template_name = 'attendance/testPage2.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView2, self).get_context_data(**kwargs)
        context['member_list'] = Person.objects.all()
        context['meeting_list'] = Meeting.objects.order_by('-meeting_date')[:3]
        return context




class TestView(generic.TemplateView):
    template_name = 'attendance/test.html'

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        context['member_list'] = Person.objects.all()
        context['meeting_list'] = Meeting.objects.order_by('-meeting_date')[:3]
        return context


class TestTemplateView(generic.TemplateView):
    template_name = 'attendance/testtemplate.html'

    def get_context_data(self, **kwargs):
        context = super(TestTemplateView, self).get_context_data(**kwargs)
        context['member_list1'] = Person.objects.all()[:4]
        context['member_list2'] = Person.objects.all()[4:]
        return context

    