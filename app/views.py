from django.shortcuts import render, HttpResponse, redirect
from app.models import Manager, Product, Salesperson, Sale, Discount, Customer


# Manager View
def manager(request):
    if request.method == 'POST':
        q = Manager.objects.all()
        q = q.filter(username=request.POST.get('username')).first()
        if q.password == request.POST.get('password'):
            return render(request, 'manager.html', {'man': q})
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
        q = None
        if request.POST.get('edit_type') == 'Product':
            q = Product.objects.all()
            print(q)
            q = q.filter(id=int(request.POST.get('edit_id'))).first()
        elif request.POST.get('view_type') == 'Salesperson':
            q = Salesperson.objects.all()
            q = q.filter(id=int(request.POST.get('edit_id'))).first()
        elif request.POST.get('view_type') == 'Customer':
            q = Customer.objects.all()
            q = q.filter(id=int(request.POST.get('edit_id'))).first()
        elif request.POST.get('view_type') == 'Sale':
            q = Sale.objects.all()
            q = q.filter(id=int(request.POST.get('edit_id'))).first()
        elif request.POST.get('view_type') == 'Discount':
            q = Discount.objects.all()
            q = q.filter(id=int(request.POST.get('edit_id'))).first()
        return render(request, 'edit.html', {'value' : q})
    return redirect(request, 'manager.html')

