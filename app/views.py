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
        table_type = None
        if request.POST.get('view_type') == 'Products':
            q = Product.objects.all()
            table_type = 'product'
        elif request.POST.get('view_type') == 'Salespersons':
            q = Salesperson.objects.all()
            table_type = 'salesperson'
        elif request.POST.get('view_type') == 'Customers':
            q = Customer.objects.all()
            table_type = 'customer'
        elif request.POST.get('view_type') == 'Sales':
            q = Sale.objects.all()
            table_type = 'sale'
        elif request.POST.get('view_type') == 'Discounts':
            q = Discount.objects.all()
            table_type = 'discount'
        return render(request, 'view.html', {'values': q, 'table_type': table_type})
    return redirect(request, 'manager.html')

def edit(request):
    if request.method == 'POST':
        return render(request, 'edit.html')
