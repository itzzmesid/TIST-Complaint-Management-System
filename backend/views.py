from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'backend/index.html')



@login_required(login_url='login')
def menu(request):
    return render(request, 'backend/menu.html')