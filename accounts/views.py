from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomerRegistrationForm, StaffRegistrationForm, LoginForm
from accounts.models import User

# Registration for Customers
def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to homepage
    else:
        form = CustomerRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

# Login
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirect to homepage
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

# Logout
def logout_user(request):
    logout(request)
    return redirect('accounts:login')

# Profile (for Customers)
@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

# Decorator for staff permissions
def staff_check(user):
    return user.is_staff

# CRUD View Placeholder for Staff
@user_passes_test(staff_check)
def staff_dashboard(request):
    # Optionally, display a list of existing staff users
    staff_users = User.objects.filter(is_staff=True)

    return render(request, 'accounts/staff_dashboard.html', {
        'staff_users': staff_users,
    })

# Separate view for creating new staff member
@user_passes_test(staff_check)
def create_staff(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new staff user
            return redirect('accounts:staff_dashboard')  # Redirect to the staff dashboard after saving
    else:
        form = StaffRegistrationForm()

    return render(request, 'accounts/create_staff.html', {
        'form': form,
    })