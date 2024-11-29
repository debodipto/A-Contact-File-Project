from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Contact
from .forms import ContactForm

# View to render the contact list
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})

# View to handle adding a new contact
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')  # Redirect to the contact list page
    else:
        form = ContactForm()
    return render(request, 'add_contact.html', {'form': form})

# View to handle updating an existing contact
def update_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'update_contact.html', {'form': form, 'contact': contact})

# View to handle deleting a contact
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'delete_contact.html', {'contact': contact})
