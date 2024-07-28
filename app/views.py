from django.shortcuts import render, HttpResponse, redirect
from app.models import Manager, Product, Salesperson, Sale, Discount, Customer
from datetime import datetime, date


# Login Portal : Used to login to manager portal
def login(request):
    return render(request, 'login.html')

# Manager Portal : Displays the many options the manager needs
def manager(request):
    # Manager should be accessed using post request, otherwise go to login
    if request.method == 'POST':
        # Signing in is used on initial login. 
        # Logged in is used to simulate a session
        if request.POST.get('status') == 'signing_in':
            # Check if input is a valid manager login
            q = Manager.objects.all()
            q = q.filter(username=request.POST.get('username')).first()
            if q.password == request.POST.get('password'):
                return render(request, 'manager.html', {'man': q})
        elif request.POST.get('status') == 'logged_in':
            q = Manager.objects.all().filter(id=int(request.POST.get('manager_id'))).first()
            return render(request, 'manager.html', {'man': q})
    return redirect(login)

# View page : Used to display data to the screen
def view(request):
    if request.method == 'POST':
        q = None
        # Uses 'view_type' to determine which database should be displayed
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

# Edit page : Used to change/add items in the database
def edit(request):
    if request.method == 'POST':
        q = None
        # Uses 'view_type' to determine which database should be displayed
        form_type = request.POST.get('edit_type')
        edit_id = request.POST.get('edit_id')
        if edit_id != 'new':
            if form_type == 'product':
                q = Product.objects.all().filter(id=int(edit_id)).first()
            elif form_type == 'salesperson':
                q = Salesperson.objects.all().filter(id=int(edit_id)).first()
            elif form_type == 'customer':
                q = Customer.objects.all().filter(id=int(edit_id)).first()
            elif form_type == 'sale':
                q = Sale.objects.all().filter(id=int(edit_id)).first()
            elif form_type == 'discount':
                q = Discount.objects.all().filter(id=int(edit_id)).first()
        return render(request, 'edit.html', {'value' : q, 'form_type' : form_type, 'manager_id' : request.POST.get('manager_id')})
    return redirect(request, 'manager.html')

# Result page : Used to display if a change/add was successful. 
def result(request):
    if request.method == 'POST':
        
        # Manager chose to change/add a product
        if request.POST.get('edit_type') == 'product':
            nm = request.POST.get('name')
            prod = Product.objects.all().filter(name=nm).first()
            # Ensures duplicate products are not added
            if prod is not None and prod.name != nm:
                return render(request, 'result.html', {'result': 'Failed. [Product Name Taken]'})  
            # Determines if the manager is adding or changing
            if request.POST.get('change_type') == 'change':
                prod = Product.objects.get(id=int(request.POST.get('id'))) 
            else:
                prod = Product()
            # Updates variables of product
            prod.name = nm
            prod.manufacturer = request.POST.get('manufacturer')
            prod.style = request.POST.get('style')
            prod.purchase_price = float(request.POST.get('purchase_price'))
            prod.sale_price = float(request.POST.get('sale_price'))
            prod.quantity_on_hand = int(request.POST.get('quantity_on_hand'))
            prod.commision_percentage = float(request.POST.get('commission_percentage'))  
            prod.save() 
            
        # Manager chose to change/add a salesperson
        elif request.POST.get('edit_type') == 'salesperson':
            # Ensures duplicate salespersons are not added
            person = Salesperson.objects.all().filter(first_name=request.POST.get('first_name')).filter(last_name=request.POST.get('last_name')).first()
            if person is not None and person.first_name != request.POST.get('first_name') and person.second_name != request.POST.get('second_name'):
                return render(request, 'result.html', {'result': 'Failed. [Salesperson Name Taken]'}) 
            # Determines if the manager is adding or changing            
            if request.POST.get('change_type') == 'change':
                person = Salesperson.objects.get(id=int(request.POST.get('id'))) 
            else:
                person = Salesperson()
            # Updates variables of salesperson
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
            
        # Manager chose to change/add a customer
        elif request.POST.get('edit_type') == 'customer':
            # Determines if the manager is adding or changing
            if request.POST.get('change_type') == 'change':
                customer = Customer.objects.get(id=int(request.POST.get('id'))) 
            else:
                customer = Customer()
            # Updates variables of customer
            customer.first_name = request.POST.get('first_name')
            customer.last_name = request.POST.get('last_name')
            customer.address = request.POST.get('address')
            customer.phone = request.POST.get('phone')
            customer.start_date = datetime.strptime(request.POST.get('start_date'), '%m/%d/%y').date()
            customer.save() 
            
        # Manager chose to change/add a sale                        
        elif request.POST.get('edit_type') == 'sale':
            # Determines if the manager is adding or changing
            if request.POST.get('change_type') == 'change':
                sale = Sale.objects.get(id=int(request.POST.get('id'))) 
            else:
                sale = Sale() 
            # Updates variables of sale
            sale.product = int(request.POST.get('product'))
            sale.salesperson = int(request.POST.get('salesperson'))
            sale.customer = int(request.POST.get('customer'))
            sale.sale_date = datetime.strptime(request.POST.get('sale_date'), '%m/%d/%y').date()
            sale.save() 
            
        # Manager chose to change/add a discount
        elif request.POST.get('edit_type') == 'discount':
            # Determines if the manager is adding or changing
            if request.POST.get('change_type') == 'change':
                discount = Discount.objects.get(id=int(request.POST.get('id'))) 
            else:
                discount = Discount()  
            # Updates variables of discount
            discount.product = int(request.POST.get('product'))
            discount.begin_date = datetime.strptime(request.POST.get('begin_date'), '%m/%d/%y').date()
            discount.end_date = datetime.strptime(request.POST.get('end_date'), '%m/%d/%y').date()
            discount.discount_percentage = float(request.POST.get('discount_percentage'))
            discount.save() 
    return render(request, 'result.html', {'result': 'Success!'})

# report page
def report(request):
    if request.method == 'POST':
        quarter = request.POST.get('quarter')
        start_date = None
        end_date = None
        # Filters date based on chosen quarter
        if quarter == 'Q1':
            start_date = date(2023, 10, 1)
            end_date = date(2023, 12, 31)
        elif quarter == 'Q2':
            start_date = date(2024, 1, 1)
            end_date = date(2024, 3, 31)
        elif quarter == 'Q3':
            start_date = date(2024, 4, 1)
            end_date = date(2024, 6, 30)
        elif quarter == 'Q4':
            start_date = date(2024, 7, 1)
            end_date = date(2024, 9, 30)
        # Query data and dicts needed to build commission report
        sales = Sale.objects.filter(sale_date__range=(start_date, end_date))
        salespeople = Salesperson.objects.all()
        nameDict = {}
        totalDict = {}
        commissionDict = {}
        # Iterate through every person and create an instance in each dict
        for person in salespeople:
            nameDict.update({person.id : person.first_name + ' ' + person.last_name})
            totalDict.update({person.id : 0})
            commissionDict.update({person.id : 0})
        # Iterate through all sales and determine who made each sale
        for sale in sales:
            seller = sale.salesperson
            productID = sale.product
            price = Product.objects.get(id=productID).sale_price
            # Check for valid discounts for sold product
            discounts = Discount.objects.all().filter(product=productID).filter(end_date__gte=sale.sale_date).filter(begin_date__lte=sale.sale_date)
            discount = None
            for disc in discounts:
                discount = disc.discount_percentage
            if discount is not None:
                price -= price * (discount/100)
            # Generate comission based on sell price and any valid discount
            commission =  price * (Product.objects.get(id=productID).commision_percentage/100)
            totalDict[seller] += price
            commissionDict[seller] += commission
            # Build list for display
            data = []
            for person_id in nameDict:
                data.append({
                'key' : person_id,
                'name' : nameDict[person_id],
                'total' : totalDict[person_id],
                'commission' : commissionDict[person_id]
            })
    return render(request, 'report.html', {'manager_id' : request.POST.get('manager_id'), 'data' : data})


