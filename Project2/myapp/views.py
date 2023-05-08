
from django.shortcuts import render, redirect
from .forms import InputForm
from .models import InputData

def input_view(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = InputForm()
    return render(request, 'input.html', {'form': form})

def success_view(request):
    try:
        data = InputData.objects.all()
    except InputData.DoesNotExist:
        data = None
    return render(request, 'success.html', {'data': data})
