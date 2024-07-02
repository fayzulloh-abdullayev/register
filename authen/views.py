# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Ro\'yxatdan o\'tdingiz va tizimga muvoffaqiyatli kirdingiz!")
            return redirect('login')  # Replace 'home' with your desired URL name after successful login
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Tizimga muvoffaqiyatli kirdingiz!')
                return redirect('home')  # Replace 'home' with your desired URL name after successful login
            else:
                messages.error(request, "Noto'g'ri foydalanuvchi nomi yoki parol!")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})




def home(request):
    return render(request=request,template_name='home.html')