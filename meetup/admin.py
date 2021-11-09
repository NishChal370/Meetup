from django.contrib import admin

from meetup.models import Location, Meetup, Participant

# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display= ('title', 'slug', 'description', 'location', 'date', 'organize_email', 'image')


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)