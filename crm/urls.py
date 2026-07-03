from django.urls import path

from . import views

app_name = 'crm'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contacts/', views.contact_list, name='contact_list'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('add/', views.add_contact, name='add_contact'),
    path('contact/<int:pk>/add-interaction/', views.add_interaction, name='add_interaction'),
]
