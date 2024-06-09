from django.shortcuts import render, redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages


#........................... Login.....................
def log_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:  # if already login then no need to be in the login page
            return redirect('view_post')

        form = LoginForm()
        return render(request, 'login_logout.html', {'login': form})
    
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
    


#.......................... Logout..............................
def log_out(request):
    logout(request)
    messages.info(request,f'You have been logged out.')
    return redirect('login_page')


#...................... Registration ............................

def sign_up(request):
    if request.method=='GET':
        print("============= GET =============")
        form=RegisterForm()
        return render(request,'sign_up.html',{'form':form})
    
    if request.method=='POST':
        print("============= POST =============")
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
        else:
            return render(request,'sign_up.html',{'form':form})

