from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
import requests



EVENT_SERVICE_URL = 'http://event_service:8002/api/events/'
RSVP_SERVICE_URL = 'http://rsvp_service:8003/api/rsvps/'


def home(request):
    return render(request, 'home.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def event_list(request):
    try:
        res = requests.get(EVENT_SERVICE_URL)
        events = res.json()
    except Exception:
        events = []
    return render(request, 'event_list.html', {'events': events})


@login_required
def rsvp_list(request):
    try:
        res = requests.get(RSVP_SERVICE_URL)
        rsvps = res.json()
    except Exception:
        rsvps = []
    return render(request, 'rsvp_list.html', {'rsvps': rsvps})