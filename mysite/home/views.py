from django.shortcuts import render
from django.http import HttpResponse
from .models import Service  # Import your Service model

def home(request):
    if request.method == "POST":
        # Process form data here
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Received message from {name} ({email}): {message}")

        # Optionally, save the data to a database, or send an email
        # For now, we just print it and show a thank you message on the page.

        thank_you_message = f"Thank you for your message, {name}!"
        return render(request, 'home/index.html', {'thank_you_message': thank_you_message})

    # Fetch the services from the database
    services = Service.objects.all()  # Get all services from the database

    about_content = "We are a leading provider of awesome solutions."

    # Render the page with services and about content
    return render(request, 'home/index.html', {
        'about_content': about_content,
        'services': services  # Pass services to the template
    })
