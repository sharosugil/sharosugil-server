from django.db import models


class Meeting(models.Model):
    title = models.CharField(max_length=50)
    meeting_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Person(models.Model):
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    membernumber = models.CharField(max_length=20, default="member0")

    attend = models.IntegerField(default=0, blank=True)
    late = models.IntegerField(default=0, blank=True)
    absent = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name



class Checking(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    check_date = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(default=0)

    def __str__(self):
        return self.person.name + "'s check of " + self.meeting.title 
