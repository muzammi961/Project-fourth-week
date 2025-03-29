from django.urls import path
from app_ import views

urlpatterns = [
    path('',views.registration,name='registration'),
    path('login/',views.login_page,name='login_page'),
    
    
    path('men/',views.menu_side,name='menu_side'),
    path('home/',views.home_side,name='home_side'),
    path('cont/',views.contact_side,name='contact_side'),
    
    
    path('admin_/',views.admin_html,name='admin_html'),
    path('admin_menu_data/',views.admin_menu_data,name='admin_menu_data'),
    
    path('product/create/',views.product_create, name='product_create'),
    path('delete/<int:id>/',views.menu_delete,name='delete_menu'),
    path('update/<int:id>/',views.update_items,name='update_things') 

    
    
    # path('sign/',views.signup_page,name='signup_page'),
    # path('check_values/',views.check_values,name='check_values'),
]