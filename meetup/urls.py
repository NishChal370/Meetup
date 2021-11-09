from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='Home'),
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-detail')
]