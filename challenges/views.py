from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def monthly_challenge_by_numbers(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text ='Earn AWS Certification'
    elif month == 'february':
        challenge_text = 'Finish on the Django Course/Creating the Monthly Challenges App'
    elif month == 'march':
        challenge_text = 'Learn React and Make the Monthly Challenges App Front End'
    elif month == 'april':
        challenge_text = 'Learn Docker'
    elif month == 'may':
        challenge_text = 'Start Blogging'
    elif month == 'june':
        challenge_text = 'Grow my Twitter Audience @kokallj'
    else:
        return HttpResponseNotFound("This Month is Not Supported")
    return HttpResponse(challenge_text)