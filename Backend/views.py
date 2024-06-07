from django.shortcuts import render,redirect
from Backend.models import CategoriesDB,ProductDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import ContactDB
from django.contrib import messages
# Create your views here.

def Index_page(req):
    return render(req,"index.html")

def Category_page(req):
    return render(req,"Category.html")

def Save_Category(req):
    if req.method == "POST":
        CT = req.POST.get('CATEGORY')
        CDES = req.POST.get('DESCRIPTION')
        CIMG = req.FILES['CIMAGES']

        obj = CategoriesDB(title_category=CT,Des_category=CDES,Img_category=CIMG)
        obj.save()
        messages.success(req,"Category Saved Successfully.")
        return redirect(Category_page)

def Display_Category(req):
    data = CategoriesDB.objects.all()
    return render(req,"Display_category.html",{"data":data})

def Update_Category_page(req,ctid):
    data = CategoriesDB.objects.get(id=ctid)
    return render(req,"Update_Category.html",{"data":data})

def Update_Category(req,ctid):
    if req.method == "POST":
        CT = req.POST.get('CATEGORY')
        CDES = req.POST.get('DESCRIPTION')

        try:
            img = req.FILES['CIMAGES']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file =CategoriesDB.objects.get(id=ctid).Img_category

        CategoriesDB.objects.filter(id=ctid).update(title_category=CT,Des_category=CDES,Img_category=file)
        messages.success(req,"Updated Successfuly.")
        return redirect(Display_Category)

def Delete_category(req,ctid):
    CT = CategoriesDB.objects.filter(id=ctid)
    CT.delete()
    messages.error(req,"Successfully Deleted.")
    return redirect(Display_Category)

def Login_page(req):
    return render(req,"Login.html")

def admin_login(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pwd = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username'] =un
                request.session['password'] =pwd
                messages.success(request,"Welcome !")
                return redirect(Index_page)
            else:
                messages.error(request,"Invalid Password")
                return redirect(Login_page)
        else:
            messages.warning(request,"User Not Found")
            return redirect(Login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"Logout Successfully")
    return redirect(Login_page)

def Product_page(req):
    cat = CategoriesDB.objects.all()
    return render(req,"Product.html",{"cat":cat})

def Save_product(req):
    if req.method=="POST":
        CT = req.POST.get('CATEGORY')
        PN = req.POST.get('PRODUCT')
        MRP = req.POST.get('PRICE')
        DES = req.POST.get('DESCRIPTION')
        PIMG = req.FILES['PIMAGES']

        obj =ProductDB(category_p=CT,product=PN,price=MRP,Des_product=DES,Img_product=PIMG)
        obj.save()
        messages.success(req,"Product saved Successfully")
        return redirect(Product_page)

def Display_product(req):
    data = ProductDB.objects.all()
    return render(req,"Display_product.html",{"data":data})

def Update_product_page(req,pid):
    data=ProductDB.objects.get(id=pid)
    cat = CategoriesDB.objects.all()
    return render(req,"Update_product.html",{"data": data,"cat":cat})

def Update_product(req,pid):
    if req.method=="POST":
        CT = req.POST.get('CATEGORY')
        PN = req.POST.get('PRODUCT')
        MRP = req.POST.get('PRICE')
        DES = req.POST.get('DESCRIPTION')
        try:
            PIMG = req.FILES['PIMAGES']
            fs =FileSystemStorage()
            file =fs.save(PIMG.name,PIMG)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=pid).Img_product

        ProductDB.objects.filter(id=pid).update(category_p=CT,product=PN,price=MRP,Des_product=DES,Img_product=file)
        messages.success(req,'Updated Successfully')
        return redirect(Display_product)

def Delete_product(req,pid):
    x = ProductDB.objects.filter(id=pid)
    x.delete()
    messages.error(req,"Successfully Deleted")
    return redirect(Display_product)

def Contact_details(req):
    data = ContactDB.objects.all()
    return render(req,"ContactData.html",{'data':data})

def Delete_contact(req,cid):
    cs = ContactDB.objects.filter(id=cid)
    cs.delete()
    messages.error(req,"Successfully Deleted")
    return redirect(Contact_details)