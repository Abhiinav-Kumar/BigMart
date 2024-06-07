from django.urls import path
from Backend import views

urlpatterns = [
    path('Index_page/',views.Index_page,name="Index_page"),

    path('Category_page/',views.Category_page,name="Category_page"),
    path('Save_Category/',views.Save_Category,name="Save_Category"),
    path('Display_Category/',views.Display_Category,name="Display_Category"),
    path('Update_Category_page/<int:ctid>/',views.Update_Category_page,name="Update_Category_page"),
    path('Update_Category/<int:ctid>/',views.Update_Category,name="Update_Category"),
    path('Delete_category/<int:ctid>/',views.Delete_category,name="Delete_category"),

    path('Login_page/',views.Login_page,name="Login_page"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),

    path('Product_page/',views.Product_page,name="Product_page"),
    path('Save_product/',views.Save_product,name="Save_product"),
    path('Display_product/',views.Display_product,name="Display_product"),
    path('Update_product_page/<int:pid>/',views.Update_product_page,name="Update_product_page"),
    path('Update_product/<int:pid>/',views.Update_product,name="Update_product"),
    path('Delete_product/<int:pid>/',views.Delete_product,name="Delete_product"),

    path('Contact_details/',views.Contact_details,name="Contact_details"),
    path('Delete_contact/<int:cid>/',views.Delete_contact,name="Delete_contact")
]