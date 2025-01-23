from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_customer, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('staff-dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('create-staff/', views.create_staff, name='create_staff'),
]
