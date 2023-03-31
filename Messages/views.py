from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def message(request):
    return render(request, 'message.html')
def success(request):
    messages.success(request, 'This is Success Message')
    return render(request, 'message.html')
def info(request):
    messages.info(request, 'This is Info message')
    return render(request, 'message.html')
def error(request):
    messages.error(request, 'This is Error message')
    return render(request, 'message.html')
def warning(request):
    messages.warning(request, 'This is Warning message')
    return render(request, 'message.html')


