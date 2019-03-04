from django.shortcuts import render

# Create your views here.
def classes_view(request, *args, **kwargs):
    return render(request, "classes.html", {})
