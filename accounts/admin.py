from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Customer

# Extend the UserAdmin for customization if needed
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('username',)

# Unregister the default UserAdmin and register the custom one
try:
    admin.site.unregister(User)  # Unregister only if it's already registered
except admin.sites.NotRegistered:
    pass  # If it's not registered, just pass

admin.site.register(User, CustomUserAdmin)

# Register the Customer model
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'created_at')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('created_at',)
    ordering = ('created_at',)
