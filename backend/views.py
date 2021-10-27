from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# from accounts.decorators import allowed_users
import backend

# Create your views here.
def index(request):
    return render(request, 'backend/index.html')


@login_required(login_url='login')
def menu(request):
    return render(request, 'backend/menu.html')

@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def dashboard(request):
    return render(request, 'backend/dashboard.html')