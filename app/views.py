from django.shortcuts import render, HttpResponse, redirect
from app.models import Manager, Product, Salesperson, Sale, Discount, Customer


# Manager View
def manager(request):
    if request.method == 'POST':
        if request.POST.get('status') == 'signing_in':
            q = Manager.objects.all()
            q = q.filter(username=request.POST.get('username')).first()
            if q.password == request.POST.get('password'):
                return render(request, 'manager.html', {'man': q})
        elif request.POST.get('status') == 'logged_in':
            q = Manager.objects.all().filter(id=int(request.POST.get('manager_id'))).first()
            return render(request, 'manager.html', {'man': q})
    return redirect(login)

# Login portal for salespersons
def login(request):
    return render(request, 'login.html')

def view(request):
    if request.method == 'POST':
        q = None
        view_type = request.POST.get('view_type')
        if view_type == 'product':
            q = Product.objects.all()
        elif view_type == 'salesperson':
            q = Salesperson.objects.all()
        elif view_type == 'customer':
            q = Customer.objects.all()
        elif view_type == 'sale':
            q = Sale.objects.all()
        elif view_type == 'discount':
            q = Discount.objects.all()
        return render(request, 'view.html', {'values': q, 'table_type': view_type, 'manager_id': request.POST.get('manager_id')})
    return redirect(request, 'manager.html')

def edit(request):
    if request.method == 'POST':
        q = None
        form_type = request.POST.get('edit_type')
        if form_type == 'product':
            q = Product.objects.all().filter(id=int(request.POST.get('edit_id'))).first()
        elif form_type == 'salesperson':
            q = Salesperson.objects.all().filter(id=int(request.POST.get('edit_id'))).first()
        elif form_type == 'customer':
            q = Customer.objects.all().filter(id=int(request.POST.get('edit_id'))).first()
        elif form_type == 'sale':
            q = Sale.objects.all().filter(id=int(request.POST.get('edit_id'))).first()
        elif form_type == 'discount':
            q = Discount.objects.all().filter(id=int(request.POST.get('edit_id'))).first()
        return render(request, 'edit.html', {'value' : q, 'form_type' : form_type, 'manager_id' : request.POST.get('manager_id')})
    return redirect(request, 'manager.html')

def result(request):
    if request.method == 'POST':
        if request.POST.get('edit_type') == 'product':
            nm = request.POST.get('name')
            man = request.POST.get('manufacturer')
            sty = request.POST.get('style')
            purchase = float(request.POST.get('purchase_price'))
            sale= float(request.POST.get('sale_price'))
            qty = int(request.POST.get('quantity_on_hand'))
            commission = float(request.POST.get('commission_percentage'))
            if Product.objects.all().filter(name=nm).first() is not None:
                return render(request, 'result.html', {'result': 'Failed. [Product Name Taken]'})  
            prod = Product.objects.get(id=int(request.POST.get('id')))    
            prod.name = nm
            prod.manufacturer = man
            prod.style = sty
            prod.purchase_price = purchase
            prod.sale_price = sale
            prod.quantity_on_hand = qty
            prod.commision_percentage = commission   
            prod.save() 
    return render(request, 'result.html', {'result': 'Success!'})

