from django.shortcuts import render
from .models import Member
def index(request):
    mem=Member.objects.all()
    return render(request, 'index.html', {'mem':mem})
def add_view(request):
    # Your view logic here
    return render(request, 'add.html')

def add(request):
  return render(request, 'add.html')