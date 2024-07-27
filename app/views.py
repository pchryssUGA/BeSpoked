from django.shortcuts import render, HttpResponse

# Create your views here.

# Main portal view. Allows employees/managers find their respective portal
def home(request):
    return render(request, "home.html")