# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PersonalinfoModelForm, ShiftAvailabilityForm, PersonalinfoModelForm, CalendarDateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import PersonalinfoModel, CalendarDate
from .forms import PersonalinfoModelForm
from django.template import loader
from django.http import HttpResponse

# 以降のコードは変更なし


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to your desired page after login
            return redirect('home')
        else:
            error_message = "username または passwordが間違っています"
    else:
        error_message = ""
        login_user = request.user
    return render(request, 'login.html', {'error_message': error_message, 'login_user':login_user})


def user_list(request):
    users = User.objects.all()  
    return render(request, 'user_list.html', {'users': users})


def home(request):
    login_user = request.user
    return render(request, 'home.html', {'login_user':login_user})

def personalinfo_input(request):
    user_info = PersonalinfoModel.objects.filter(user=request.user).first()  
    if request.method == 'POST':
        if user_info:
            form = PersonalinfoModelForm(request.POST, instance=user_info)
        else:
            form = PersonalinfoModelForm(request.POST)
        
        if form.is_valid():
            user_info = form.save(commit=False)
            user_info.user = request.user
            user_info.save()
            return redirect('home')
    else:
        if user_info:
            form = PersonalinfoModelForm(instance=user_info)
        else:
            form = PersonalinfoModelForm()

    return render(request, 'personalinfo.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def form_input(request):
    print("form_input view reached")
    if request.method == 'POST':
        form = ShiftAvailabilityForm(request.POST)
        if form.is_valid():
            # フォームが有効な場合、データを保存
            shift_availability = form.save(commit=False)
            shift_availability.user = request.user  # ログインユーザーを関連付け
            shift_availability.save()
            return redirect('shift_availability_input')  # フォームの再表示
    else:
        form = ShiftAvailabilityForm()

    return render(request, 'availability.html', {'form': form})


def surveyCalendar_view(request):
    return render(request, "surveyCalendar.html")
   