from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse

monthly_challenges ={
    "january":"Earn AWS Certification",
    "february": "Finish on the Django Course/Creating the Monthly Challenges App",
    "march":"Review Javascript Fundermentals, Learn React and Make the Monthly Challenges App Front End",
    "april":"Learn Docker",
    "may":"Start Blogging",
    "june":"Grow my Twitter Audience @kokallj",
    "july":"Start Looking for a Dev Job (Fullstack, Django Backend heavy)",
    "august":"Start on Data Engineering",
    "september":"Create a libary of Data Engineering Resources",
    "october":"Create/Build a Blog Site",
    "november":"Compile thoughts and resources on Data Engineering/Data Science/Django and React",
    "december": "Write a Comprehensive Review of the Journey from the Monthly Summaries"
}

# Create your views here.

def monthly_challenge_by_numbers(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This Month is Not Supported")
    