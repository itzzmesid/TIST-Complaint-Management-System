from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.contrib import messages
from backend.forms import ComplaintForm
from backend.models import Complaint
from django.db.models import Count, Q

def index(request):
    return render(request, 'backend/index.html')

@login_required(login_url='login')
def menu(request):
    return render(request, 'backend/menu.html')

#This page will be used to display all the ongoing complaints and must be visible to only admins
@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def dashboard(request):

    coms = Complaint.objects.all
    args = {'coms':coms}
    return render(request, 'backend/dashboard.html', args)

@login_required
def RegisterComplaint(request):
  
    if request.method == 'POST':
        form=ComplaintForm(request.POST)
        if form.is_valid():
               instance = form.save(commit=False)
               instance.user = request.user
            #    mail=request.user.email
            #    print(mail)
            #    send_mail('Hi \n Complaint has been Received', 'Thank you for letting us know of your concern, Have a Cookie while we explore into this matter. \n Dont Reply to this mail', 'testerpython13@gmail.com', [mail],fail_silently=False)
               instance.save()
               
               messages.success(request,"Your complaint has been registered ! Kindly wait till it get resolved :)")
               return redirect('menu')
    else:
        
        form=ComplaintForm(request.POST)

    context={'form':form}
    return render(request,'backend/complaintform.html',context)

@login_required
def CheckStatus(request):
    c=Complaint.objects.filter(user=request.user)
    # c=Complaint.objects.filter(user=request.user).exclude(status='1')
    # result=Complaint.objects.filter(user=request.user).exclude(Q(status='3') | Q(status='2'))
    args={'c':c}
    return render(request,'backend/status.html',args)
