from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user


@unauthenticated_user
def loginpage(request):
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
        
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('menu')
            else:
                messages.info(request, 'Incorrect Email or Password')
                # return render(request, 'accounts/login.html')
        context = {}
        return render(request, 'accounts/login.html', context)


# In menu template, dont forget to add logout button. And use {{request.user} in template to get username}
def logoutUser(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)  # Getting the POST DATA
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')  # to get username
            messages.success(request, 'Hi'+" " + user +'Your account was created successfully!')
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
