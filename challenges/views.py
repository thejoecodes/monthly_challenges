from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request):
    return HttpResponse("")

def february(request):
    return HttpResponse('You are on Fire!')

def monthly_challenge(request, month):
    challenge_text = None
    if month == 'January':
        challenge_text ='Earn AWS Certification'
    elif month == 'February':
        challenge_text = 'Finish React'
    elif month == 'March':
        challenge_text = 'Build a '
    return HttpResponse()