from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from mainapp.forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from datetime import datetime, timedelta
from django.db.models import F
from django.db import connection, connections, transaction

from .forms import (
   AdminProfileForm
)
from .models import (
    AdminProfile,
    AllCounters,

)

# Create your views here.

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'Accounts/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('homepage')
            else:
                messages.info(request,'Username or Password is incorrect')
                return render(request, 'Accounts/login.html')
        context = {}
        return render(request, 'Accounts/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request,'index.html')

@login_required(login_url='login')
def viewadmins(request):
    allAdmin = AdminProfile.objects.all()
    adminform = AdminProfileForm(request.POST or None)
    totalAdmin = AdminProfile.objects.all().count()
    startdate = datetime.today()
    enddate = startdate - timedelta(days=14)
    context = {
        "allAdmin": allAdmin,
        "adminform":adminform,
        "totalAdmin": totalAdmin,
        "startdate": startdate,
        "enddate": enddate,
    }
    return render(request, "addedAdmins/viewAdmins.html", context)


def createAdmins(request):
    alladmins = AdminProfile.objects.all()#filter(distributer=request.user.username)
    currentcounter = AllCounters.objects.filter(name="addedadmins").first()
    adminform = AdminProfileForm(request.POST or None)
    # print(adminform)
    context = {
         "alladmins": alladmins,
        "currentcounter": currentcounter.counter,
        "adminform": adminform,                                           
    }
    if request.method == "POST":
        if adminform.is_valid():
            testallowed = adminform.cleaned_data.get('testallowed')
            adminform.save()
            adminform = AdminProfileForm()
            invoiceCounter = AllCounters.objects.filter(name="addedadmins").first()
            invoiceCounter.counter = F("counter") + 1
            invoiceCounter.save()
            adminform = AdminProfileForm()
            messages.success(request, "Admin Added successfully")         
        else:
            messages.warning(request, "Error Adding Admin!")
            adminform = AdminProfileForm(request.POST)
    return render(request, "addedAdmins/createAdmins.html", context)


@login_required
def addtoadmindb(request):
    setParam = request.GET.get("sqlParam", None)
    if setParam:
        cursor = connection.cursor()
        cursor.execute(setParam)

    else:
        return HttpResponse("no setParam")

    return redirect("viewadmins")

@login_required
def removeadmin(request):
    setParam = request.GET.get("sqlParam", None)
    if setParam:
        cursor = connection.cursor()
        cursor.execute(setParam)
    else:
        return HttpResponse("no setParam")

    return redirect("viewadmins")


@login_required
def editAdmin(request):
    alladmins = AdminProfile.objects.all()#filter(distributer=request.user.username)
    currentcounter = AllCounters.objects.filter(name="addedadmins").first()
    adminform = AdminProfileForm(request.POST or None)
    # print(adminform)
    context = {
         "alladmins": alladmins,
        "currentcounter": currentcounter.counter,
        "adminform": adminform,                                           
    }
    if request.method == "POST":
        if adminform.is_valid():
            testallowed = adminform.cleaned_data.get('testallowed')
            adminform.save()
            adminform = AdminProfileForm()
            invoiceCounter = AllCounters.objects.filter(name="addedadmins").first()
            invoiceCounter.counter = F("counter") + 1
            invoiceCounter.save()
            adminform = AdminProfileForm()
            messages.success(request, "Admin Added successfully")         
        else:
            messages.warning(request, "Error Adding Admin!")
            adminform = AdminProfileForm(request.POST)
    return render(request, "addedAdmins/editAdmin.html", context)
