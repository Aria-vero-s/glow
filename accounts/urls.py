from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_customer, name='register'),
    path('register-staff/', views.register_staff, name='register_staff'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('staff-dashboard/', views.staff_dashboard, name='staff_dashboard'),
]
