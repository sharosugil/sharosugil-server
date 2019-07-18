from django.contrib import admin
from .models import *


class CheckingInline(admin.TabularInline):
    model = Checking
    extra = 0

class MeetingAdmin(admin.ModelAdmin):
    list_display = ['title', 'meeting_date']
    inlines = [CheckingInline]

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'attend', 'late', 'absent']
    inlines = [CheckingInline]


admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Person, PersonAdmin)
