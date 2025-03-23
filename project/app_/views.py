from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration_class
from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import redirect
from django.contrib import messages

# def registration(request):
#     return render(request,'html/registration_.html')

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
            messages.success(request, "Registration successful! Please log in.")
            print('you register this ')
            return redirect('login_page')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            print('you got a erorr register')
            return redirect('registration')
    return render(request, 'html_/registration.html')
 
def login_page(request):
    if request.method=='POST':
        gmail_person_login=request.POST.get('gmail_person_login')
        password_login=request.POST.get('password_login')
        try:
        
            user2=Registration_class.objects.get(gmail_person_registr=gmail_person_login)
            print('it is checking the try ')
            if check_password(password_login, user2.password_registr):
               print("login")
               return redirect('project_main')
            else:
                print('could not found password')
        except Registration_class.DoesNotExist:
                 print('could not found email')
    return render(request,'html_/login.html')




def home_side(request):
    return render(request,'html2/home_side_html.html')
def contact_side(request):
    return render(request,'html2/contact_side_html.html')

# def signup_page(request):
#     return render(request,'html_/signup_page.html')

