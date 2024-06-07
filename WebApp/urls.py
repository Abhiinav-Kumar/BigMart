from django.urls import path
from WebApp import views
urlpatterns = [
    path('',views.Home_page,name="Home"),
    path('About/',views.About_page,name="About"),
    path('Contact/',views.Contact_page,name="Contact"),
    path('Save_Contact/',views.Save_Contact,name="Save_Contact"),

    path('Product_web_page/',views.Product_web_page,name="Product_web_page"),
    path('Filtered_products/<cat_name>',views.Filtered_products,name="Filtered_products"),
    path('Single_Product_page/<int:pro_id>/',views.Single_Product_page,name="Single_Product_page"),

    path('User_login_page/',views.User_login_page,name="User_login_page"),
    path('Save_user/',views.Save_user,name="Save_user"),
    path('User_loginn/',views.User_loginn,name="User_loginn"),
    path('User_Signup_page/',views.User_Signup_page,name="User_Signup_page"),
    path('user_logout/',views.user_logout,name="user_logout"),

    path('CartPage/',views.CartPage,name="CartPage"),
    path('saveCart/',views.saveCart,name="saveCart"),
    path('Delete_cart_item/<int:p_id>',views.Delete_cart_item,name="Delete_cart_item"),
    path('Checkout_page/',views.Checkout_page,name="Checkout_page"),

]