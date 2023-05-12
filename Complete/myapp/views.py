from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MyData

def add_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not name or not email or not message:
            # Show an error message if any of the fields are missing
            messages.error(request, 'All fields are required.')
        else:
            try:
                MyData.objects.create(name=name, email=email, message=message)
                messages.success(request, 'Your data has been saved.')
                return redirect('view_data')
            except:
                # Show an error message if there is a problem saving the data
                messages.error(request, 'An error occurred while saving your data.')

    # Render the add_data.html template with any error messages
    return render(request, 'add_data.html')


def view_data(request):
    data = MyData.objects.all()
    return render(request, 'view_data.html', {'data': data})
