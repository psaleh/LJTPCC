from django.shortcuts import render
from django.conf import settings

from .forms import ContactForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm

    return render(request, "index.html", {'form': form})
