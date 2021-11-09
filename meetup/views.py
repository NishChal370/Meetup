from django.http.response import HttpResponse
from django.shortcuts import render
from meetup.forms import RegistrationForms
from meetup.models import Meetup, Participant
# Create your views here.

def index(request):
    meetings= Meetup.objects.all() #calling data from database
    return render(request, 'meetups/index.html', {
        'meetings' : meetings
    }) 

def meetup_details(request, meetup_slug):
    print(meetup_slug)
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            print("->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(selected_meetup)
            registration_forms = RegistrationForms()
        else :
            registration_forms = RegistrationForms(request.POST)
            if registration_forms.is_valid():
                user_email = registration_forms.cleaned_data['email']
                participant,_= Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return render(request, 'meetups/meetup-configuration.html')

        return render(request, 'meetups/meetup-details.html',{
                'meetup_found': True,
                'meetup_image': selected_meetup.image.url,
                'meetup_title': selected_meetup.title,
                'meetup_description': selected_meetup.description,
                'meetup_slug':meetup_slug,
                'meetup_location': selected_meetup.location,
                'participants_list': selected_meetup.participants,
                'form': registration_forms,
            })

        
                
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html',{
            'meetup_found': False
        })