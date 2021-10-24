from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

def login(request):
    return render(request, 'accounts/login.html')


def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST) #Getting the POST DATA
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request, 'accounts/signup.html', context)







