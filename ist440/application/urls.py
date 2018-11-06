from . import views
from django.urls import path

app_name = 'application'
urlpatterns = [
    path('emergency-room/', views.emergency_room, name='emergency-room'),
    path('local-family-medical-practitioner/', views.local_family_medical_practitioner, name='local-family-medical-practitioner'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('urgent-care/', views.urgent_care, name='urgent-care'),
    path('', views.main_menu, name='main-menu'),
]
