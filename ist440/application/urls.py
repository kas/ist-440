from . import views
from django.urls import include, path

app_name = 'application'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('emergency-room/', views.emergency_room, name='emergency-room'),
    path('local-family-medical-practitioner/', views.local_family_medical_practitioner, name='local-family-medical-practitioner'),
    path('register/', views.register, name='register'),
    path('urgent-care/', views.urgent_care, name='urgent-care'),
    path('', views.main_menu, name='main-menu'),
]
