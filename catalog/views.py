from django.shortcuts import render
from .models import Reloj
from django.views import generic
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .forms import ContactForm

# Create your views here.

def index(request):
    """
    View function for home page of site.
    """
    return render(
        request,
        'index.html',
    )

class WatchesView(generic.ListView):
    """
    View class for watches page.
    """
    model = Reloj
    template_name = '../templates/listProducts.html'
    context_object_name = 'watches_list'

class WatchDetailView(generic.DetailView):
    """
    View class for single watch page.
    """
    model = Reloj
    template_name = '../templates/watchDetail.html'
    context_object_name = 'watch'


def contact(request):
    """
    View function for contact form.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(form.cleaned_data['Asunto'] + " - " +  form.cleaned_data['Correo'],
                form.cleaned_data['Mensaje'],
                'lendinez1990@gmail.com',
                ['lendinez1990@gmail.com'],
            )
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
