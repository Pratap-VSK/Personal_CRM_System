from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm, InteractionForm
from .models import Contact


def home(request):
    if request.user.is_authenticated:
        return redirect('crm:dashboard')
    return render(request, 'crm/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('crm:dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    total_contacts = Contact.objects.filter(user=request.user).count()
    return render(request, 'crm/dashboard.html', {'total_contacts': total_contacts})


@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'crm/contact_list.html', {'contacts': contacts})


@login_required
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, id=pk, user=request.user)
    interactions = contact.interactions.all().order_by('-date')
    return render(request, 'crm/contact_detail.html', {'contact': contact, 'interactions': interactions})


@login_required
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('crm:contact_list')
    else:
        form = ContactForm()
    return render(request, 'crm/form.html', {'form': form, 'title': 'Add Contact'})


@login_required
def add_interaction(request, pk):
    contact = get_object_or_404(Contact, id=pk, user=request.user)
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            interaction = form.save(commit=False)
            interaction.contact = contact
            interaction.save()
            return redirect('crm:contact_detail', pk=contact.id)
    else:
        form = InteractionForm()
    return render(request, 'crm/form.html', {'form': form, 'title': f'Add Interaction for {contact.name}'})
