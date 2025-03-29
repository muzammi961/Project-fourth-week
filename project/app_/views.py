from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Registration_class,MenuItem,Category
from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import redirect
from django.contrib import messages


def registration(request):
    if request.method == 'POST':
        name_registr = request.POST.get('name_registr')
        phone_number_registr = request.POST.get('phone_number_registr')
        gmail_person_registr = request.POST.get('gmail_person_registr')
        password_registr = request.POST.get('password_registr')
        mk_password = make_password(password_registr)
        if Registration_class.objects.filter(gmail_person_registr=gmail_person_registr).exists():  
            messages.error(request, "This email is already registered. Please log in.")
            print('you allready register in this gmail')
            return redirect('registration')
        try:
            obj1 = Registration_class(name_registr=name_registr,phone_number_registr=phone_number_registr,gmail_person_registr=gmail_person_registr,password_registr=mk_password)
            obj1.save()
    
            print('you register this ')
            return redirect('login_page')
        except Exception as e:
            print('you got a erorr register')
            return redirect('registration')
    return render(request, 'html_/index.html')
 
def login_page(request):
    if request.method=='POST':
        gmail_person_login=request.POST.get('gmail_person_login')
        password_login=request.POST.get('password_login')
        try:
            user2=Registration_class.objects.get(gmail_person_registr=gmail_person_login)
            print('it is checking the try ')
            if check_password(password_login, user2.password_registr):
               print("login")
               return redirect('home_side')
            else:
                print('could not found password')
        except Registration_class.DoesNotExist:
                 print('could not found email')
    return render(request,'html_/login.html')


def admin_html(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        price = request.POST.get('price')
        offer_price = request.POST.get('offer_price')
        item_photo = request.FILES.get('item_photo')
        category_id = request.POST.get('category')
        if category_id:
            catagory= Category.objects.get(id=category_id)
            obj1 = MenuItem(item_name=item_name,price=price,offer_price=offer_price,item_photo=item_photo,category=catagory)
            obj1.save()
            return redirect('admin_menu_data')

    return render(request, 'admin_side_html/admin_html.html', {'categories': categories})

def admin_menu_data(request):
    menu_all_things = MenuItem.objects.all()
    return render(request, 'admin_side_html/admin_menu_data.html', {'menu_all_things': menu_all_things})

def product_create(request):
    categories = Category.objects.all()

    # if request.method == "POST":
    #     name = request.POST.get('name')
    #     category_id = request.POST.get('category')
    #     price = request.POST.get('price')

    #     if category_id and name and price:
    #         category = Category.objects.get(id=category_id)
    #         MenuItem.objects.create(create_name=name, category=category, price=price)
    #         return redirect('product_list')

    return render(request, 'product_form.html', {'categories': categories})
def menu_side(request):
    menu_all_things = MenuItem.objects.all()
    print(list(menu_all_things))
    return render(request, 'html2/menu_side_html.html', {'menu_all_things': menu_all_things})

def home_side(request):
    return render(request,'html2/home_side_html.html')
def contact_side(request):
    return render(request,'html2/contact_side_html.html')



# def update_items(request, id):
#     item = get_object_or_404(MenuItem, id=id)
    
#     if request.method == 'POST':
#         item_name = request.POST.get('item_name')
#         price = request.POST.get('price')
#         offer_price = request.POST.get('offer_price',0)



#         item.item_name = item_name
#         item.price = price
#         item.offer_price = offer_price  if offer_price else 0
        
#         item.save()
#         return redirect('admin_menu_data')

#     return render(request, 'admin_side_html/update_html.html', {'item': item})





def update_items(request, id):
    item = get_object_or_404(MenuItem, id=id)

    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        price = request.POST.get('price')
        offer_price = request.POST.get('offer_price')  

        if not item_name:
            return render(request, 'admin_side_html/update_html.html', {'item': item, 'error': 'Item name is required'})

        if not price or not price.isdigit():
            return render(request, 'admin_side_html/update_html.html', {'item': item, 'error': 'Valid price is required'})

        item.item_name = item_name
        item.price =price
        item.offer_price =offer_price
        item.save()

        return redirect('admin_menu_data')

    return render(request, 'admin_side_html/update_html.html', {'item': item})


def menu_delete(request,id):
    if request.method=='POST': 
     obj = get_object_or_404(MenuItem,id=id)
     obj.delete()
     return redirect('admin_menu_data') 
    return redirect('admin_menu_data')