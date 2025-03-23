from django.urls import path
from app_ import views

urlpatterns = [
    path('',views.registration,name='registration'),
    path('login/',views.login_page,name='login_page'),
    
    
    path('home/',views.home_side,name='home_side'),
    path('contact/',views.contact_side,name='contact_side'),
    
    # path('sign/',views.signup_page,name='signup_page'),
    # path('check_values/',views.check_values,name='check_values'),
]