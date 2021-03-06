from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls.base import reverse

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
    "december": None #"Write a Comprehensive Review of the Journey from the Monthly Summaries"
}

# Create your views here.

# Creates an unordered list of months
def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html",{
        "months": months
    })

    


# handles months in integers
def monthly_challenge_by_numbers(request, month):
    months = list(monthly_challenges.keys()) # Converts the monthly_challenges dictionary above to a list

    if month > len(months):
        return HttpResponseNotFound("<h1>This Month is Not Supported</h1>")

    forward_month = months[month -1]
    forward_path = reverse('monthly-challenge',args=[forward_month])
    return HttpResponseRedirect(forward_path)

# handles months in strings
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        #response_data = render_to_string("challenges/challenge.html")
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
    