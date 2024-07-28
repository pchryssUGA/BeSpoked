from django.shortcuts import render, HttpResponse, redirect
from app.models import Manager, Product, Salesperson, Sale, Discount, Customer


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
        q = None
        if request.POST.get('view_type') == 'Products':
            q = Product.objects.all()
        elif request.POST.get('view_type') == 'Salespersons':
            q = Salesperson.objects.all()
        elif request.POST.get('view_type') == 'Customers':
            q = Customer.objects.all()
        elif request.POST.get('view_type') == 'Sales':
            q = Sale.objects.all()
        elif request.POST.get('view_type') == 'Discounts':
            q = Discount.objects.all()
        for val in q:
            print(val)
        return render(request, 'view.html', {'values': q})
    return redirect(request, 'manager.html')


