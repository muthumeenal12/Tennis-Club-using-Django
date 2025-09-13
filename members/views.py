from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
import requests
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from members.models import Member
from .forms import JoinRequestForm
# Create your views here.
@login_required
def members(request):
    mymembers = Member.objects.all()
   
    return render(request,'myFirstPage.html',{'mymembers':mymembers})

         
        
        
def home(request):
    quote_api = 'https://zenquotes.io/api/random'
    try:
        response = requests.get(quote_api)
        response.raise_for_status() #for bad responses
        quote_data = response.json()[0]
        quote_text  = quote_data['q']
        quote_author = quote_data['a']
        quote = f'{quote_text} - {quote_author}'
    except (requests.RequestException, KeyError, IndexError) as e:
        quote = '"Tennis is not just a sport, it\'s a way of life." – Arthur Ashe.'   
    return render(request, 'home.html', {'quote': quote})


@login_required
def join(request):
    if request.method == "POST":
        form = JoinRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("join_thanks"))
        else:
            print(form.errors)
    else:
        form = JoinRequestForm()
    return render(request, "join.html", {"form": form})

def join_thanks(request):
    return render(request, "join_thanks.html")

def contact(request):
    return render(request, "contact.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
        # If not valid, fall through to render with errors
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {"form": form})

def logout_view(request):
    """Log the user out via GET or POST and redirect to home with a message."""
    if request.user.is_authenticated:
        auth_logout(request)
        messages.success(request, 'Logged out successfully.')
    return redirect('home')