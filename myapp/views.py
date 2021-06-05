from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .form import PersonalInformationForm, LogInForm, SignUpForm
from .models import PersonalInformation
from django.contrib import messages
import requests


# from django.contrib.auth.forms import AuthenticationForm

@login_required(login_url='/login/')
def create(request, id=None):
    """
    This view is for the  '/create' url.
    """
    if request.method == 'POST':
        if id:
            obj = PersonalInformation.objects.get(id=id)
            form = PersonalInformationForm(request.POST, instance=obj)
        else:
            form = PersonalInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    elif id:
        obj = PersonalInformation.objects.get(id=id)
        data = {'name': obj.name, 'email': obj.email,
                'std': obj.std, 'roll': obj.roll, 'sub': obj.sub}
        form = PersonalInformationForm(data)
        return render(request, 'update.html', {'form': form})
    else:
        form = PersonalInformationForm()
        return render(request, 'create.html', {'form': form})

@login_required(login_url='/login/')
def home(request):
    """
    This view is for the  '/' url.
    """
    data = PersonalInformation.objects.all()
    return render(request, 'home.html', {'data': data})


@login_required(login_url='/login/')
def delete(request, id):
    """
    This view is for the  '/delete/<int:id>' url.
    """
    obj = PersonalInformation.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect("/")
    return render(request, 'delete.html')


def log_in(request):
    """
    This view is for the  '/login' url.
    """
    if request.method == 'POST':
        form = LogInForm(request.POST)

        if form.is_valid():

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': '6LcBSYEaAAAAAFr5v2GvuIhsEmrBf-_5VavGonnc',
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            ''' End reCAPTCHA validation '''

            if result['success']:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user:
                    request.session['username'] = username
                    login(request, user)
                    return redirect("/")
                else:
                    messages.error(request, 'Invalid Credentials, Please try again.')
                    return redirect('login')
            else:
                messages.error(request, 'Invalid reCAPTCHA, Please try again.')
                return redirect('login')
    else:
        form = LogInForm()
        return render(request, 'login.html', {'form': form})


@login_required(login_url='/login/')
def log_out(request):
    """
    This view is for the  '/logout' url.
    """
    del request.session['username']
    logout(request)
    return redirect('/')


def signup(request):
    """
    This view is for the  '/signup' url.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
