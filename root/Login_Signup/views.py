from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def log_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login-signup.html', {'login': form})
    
    elif request.method == 'POST':
        info = LoginForm(request.POST)
        if info.is_valid():
            username = info.cleaned_data['username']
            password = info.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('view_post')
        
        messages.error(request, 'Invalid username or password')
        return render(request, 'login-signup.html', {'login': info})
