from django.shortcuts import render, HttpResponse, redirect
from app.models import Manager, Product, Salesperson, Sale, Discount, Customer
from datetime import datetime


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
            if Product.objects.all().filter(name=nm).first() is not None:
                return render(request, 'result.html', {'result': 'Failed. [Product Name Taken]'})  
            prod = Product.objects.get(id=int(request.POST.get('id')))    
            prod.name = nm
            prod.manufacturer = request.POST.get('manufacturer')
            prod.style = request.POST.get('style')
            prod.purchase_price = float(request.POST.get('purchase_price'))
            prod.sale_price = float(request.POST.get('sale_price'))
            prod.quantity_on_hand = int(request.POST.get('quantity_on_hand'))
            prod.commision_percentage = float(request.POST.get('commission_percentage'))  
            prod.save() 
            
        elif request.POST.get('edit_type') == 'salesperson':
            if Salesperson.objects.all().filter(first_name=request.POST.get('first_name')).filter(last_name=request.POST.get('last_name')).first() is not None:
                return render(request, 'result.html', {'result': 'Failed. [Salesperson Name Taken]'})  
            person = Salesperson.objects.get(id=int(request.POST.get('id')))    
            person.first_name = request.POST.get('first_name')
            person.last_name = request.POST.get('last_name')
            person.address = request.POST.get('address')
            person.phone = request.POST.get('phone')
            person.start_date = datetime.strptime(request.POST.get('start_date'), '%m/%d/%y').date()
            termination_date = request.POST.get('termination_date')
            if termination_date not in [None, '', 'None']:
                person.termination_date = datetime.strptime(request.POST.get('termination_date'), '%m/%d/%y').date()
            person.manager_id = int(request.POST.get('manager_id'))
            person.save() 
            
        elif request.POST.get('edit_type') == 'customer':
            if Customer.objects.all().filter(first_name=request.POST.get('first_name')).filter(last_name=request.POST.get('last_name')).first() is not None:
                return render(request, 'result.html', {'result': 'Failed. [Salesperson Name Taken]'})  
            customer = Customer.objects.get(id=int(request.POST.get('id')))    
            customer.first_name = request.POST.get('first_name')
            customer.last_name = request.POST.get('last_name')
            customer.address = request.POST.get('address')
            customer.phone = request.POST.get('phone')
            customer.start_date = datetime.strptime(request.POST.get('start_date'), '%m/%d/%y').date()
            customer.save() 
            
        elif request.POST.get('edit_type') == 'sale':
            sale = Sale.objects.get(id=int(request.POST.get('id')))    
            sale.product = int(request.POST.get('product'))
            sale.salesperson = int(request.POST.get('salesperson'))
            sale.customer = int(request.POST.get('customer'))
            sale.sale_date = datetime.strptime(request.POST.get('sale_date'), '%m/%d/%y').date()
            sale.save() 
            
        elif request.POST.get('edit_type') == 'discount':
            discount = Discount.objects.get(id=int(request.POST.get('id')))    
            discount.product = int(request.POST.get('product'))
            discount.begin_date = datetime.strptime(request.POST.get('begin_date'), '%m/%d/%y').date()
            discount.end_date = datetime.strptime(request.POST.get('end_date'), '%m/%d/%y').date()
            discount.discount_percentage = float(request.POST.get('discount_percentage'))
            discount.save() 
    return render(request, 'result.html', {'result': 'Success!'})

