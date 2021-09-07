from django.shortcuts import render, HttpResponseRedirect
from .models import Report
from .forms import ReportForm, signupForm, loginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

# home page
def homepage(request):

    return render(request, 'myintern/index.html')

# report form
def formInput(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReportForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Report successfully saved to database !! ')
                form.save()
                form = ReportForm()
        else:
            form = ReportForm()
        context = {'form': form}
        return render(request, 'myintern/form-inputs.html', context)
    else:
        return HttpResponseRedirect('/')    

# login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = loginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !! ')
                    return HttpResponseRedirect('/')
        else:
            form = loginForm()
        context = {'form': form}
        return render(request, 'myintern/authentication-login1.html', context)

    else:
        return HttpResponseRedirect('/')


# signup
def user_register(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Account has been created .')   
            form.save()
            form = signupForm()
    else:
        form = signupForm()
    context = {'form': form}

    return render(request, 'myintern/authentication-register1.html', context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')