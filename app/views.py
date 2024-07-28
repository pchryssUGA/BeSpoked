from django.shortcuts import render, HttpResponse, redirect
from app.models import Manager


# Manager View
def manager(request):
    if request.method == 'POST':
        q = Manager.objects.all()
        q = q.filter(username=request.POST.get('username'))
        for man in q:
            if man.password == request.POST.get('password'):
                return render(request, 'manager.html', {'man': man})
    return redirect(login)

# Login portal for salespersons
def login(request):
    return render(request, 'login.html')

def view(request):
    if request.method == 'POST':
        return render(request, 'view.html')
    return redirect(request, 'manager.html')


