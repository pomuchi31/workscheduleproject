from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',  views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('personalinfo_input/', views.personalinfo_input, name='personalinfo_input'),
    path('surveyCalendar/', views.surveyCalendar_view, name='surveyCalendar'),    
]
