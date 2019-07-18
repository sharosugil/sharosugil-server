from .models import *
from rest_framework import serializers

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ['title', 'meeting_date', 'checking_set']
    
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'department', 'attend', 'late', 'absent']
    
class CheckingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checking
        fields = ['meeting', 'person', 'check_date']