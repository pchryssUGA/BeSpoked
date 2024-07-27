from django.shortcuts import render, HttpResponse

# Create your views here.

# Main portal view. Allows employees/managers find their respective portal
def home(request):
    return render(request, "home.html")

# Login portal for salespersons
def login(request):
    
    if request.method == 'POST':
        type = request.POST.get('login_type')
        return render(request, 'login.html', {"type":type})
    return render(request, "base.html")

