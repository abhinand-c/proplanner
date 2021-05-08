from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate

from . import models, forms
# Create your views here.

def signup(request):
    """     User sign up view. Redirects authenticated users to home page   """
    next = request.POST.get('next', '/')
    if(request.user.is_authenticated):
        return redirect('home')
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()                                  # If Sign up is valid, user is created
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)           # authenticate username and password
            login(request, user)
            next = request.POST.get('next', '/')
            return redirect(next)
    else:
        form = forms.SignUpForm()
    return render(request, 'common/form.html', {'form': form, 'next':next,'title':'Sign up',})

def home(request):
    return redirect('task:task')
