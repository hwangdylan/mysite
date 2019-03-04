from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm
from .models import Contact

# Create your views here.
def contact_create_view(request):
    my_form = ContactForm()
    if request.method == "POST":
        my_form = ContactForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Contact.objects.create(**my_form.cleaned_data)
    context = {
        "form":my_form 
    }
    return render(request, "contactform.html", context)
# def contact_create_view(request, *args, **kwargs):
#     form = ContactForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ContactForm()
#     context = {
#             'form': form
#     }
#     return render(request, "contactform.html", context)

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})
