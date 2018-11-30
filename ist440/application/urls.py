from . import views
from django.urls import include, path

app_name = 'application'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('confirm-delete-insurance-card/<insurance_card_id>/', views.confirm_delete_insurance_card, name='confirm-delete-insurance-card'),
    path('delete-insurance-card/<insurance_card_id>/', views.delete_insurance_card, name='delete-insurance-card'),
    path('edit-insurance-card/<insurance_card_id>/', views.edit_insurance_card, name='edit-insurance-card'),
    path('emergency-room/', views.emergency_room, name='emergency-room'),
    path('end/', views.end, name='end'),
    path('local-family-medical-practitioner/', views.local_family_medical_practitioner, name='local-family-medical-practitioner'),
    path('need-medical-assistance/', views.need_medical_assistance, name='need-medical-assistance'),
    path('new-insurance-card/', views.new_insurance_card, name='new-insurance-card'),
    path('question-1/', views.question_1, name='question-1'),
    path('question-2/', views.question_2, name='question-2'),
    path('question-3/', views.question_3, name='question-3'),
    path('register/', views.register, name='register'),
    path('urgent-care/', views.urgent_care, name='urgent-care'),
    path('view-insurance-cards/', views.view_insurance_cards, name='view-insurance-cards'),
    path('', views.main_menu, name='main-menu'),
]
