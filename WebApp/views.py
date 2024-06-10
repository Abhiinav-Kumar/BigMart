from django.shortcuts import render,redirect
from Backend.models import ProductDB,CategoriesDB
from WebApp.models import ContactDB,UserDB,cartDB,BillingDB
from django.contrib import messages
import razorpay

# Create your views here.

def Home_page(request):
    cat = CategoriesDB.objects.all()
    return render(request,"Home.html",{'cat':cat})

def About_page(request):
    cat = CategoriesDB.objects.all()
    return render(request,"About.html",{'cat':cat})

def Contact_page(request):
    cat = CategoriesDB.objects.all()
    return render(request,"Contact.html",{'cat':cat})

def Product_web_page(request):
    pro = ProductDB.objects.all()
    cat = CategoriesDB.objects.all()
    return render(request,"Product_web.html",{'Products':pro,'cat':cat})

def Save_Contact(req):
    if req.method=="POST":
        NM = req.POST.get('NAME')
        EM = req.POST.get('EMAIL')
        PH = req.POST.get('PHONE')
        SUB = req.POST.get('SUBJECT')
        MES = req.POST.get('MESSAGES')
        obj = ContactDB(Name=NM,Email=EM,Phone=PH,Subject=SUB,Messages=MES)
        obj.save()
        messages.success(req,"Your message has been sent. We aim to respond within 7 business days.")
        return redirect(Contact_page)

def Filtered_products(req,cat_name):
    data = ProductDB.objects.filter(category_p=cat_name)
    cat = CategoriesDB.objects.all()
    return render(req,"Products_Filtered.html",{'data':data,'cat':cat})

def Single_Product_page(req,pro_id):
    data = ProductDB.objects.get(id=pro_id)
    cat = CategoriesDB.objects.all()
    return render(req,"Single_Product.html",{'data':data,'cat':cat})

def User_login_page(req):
    return render(req,"User_Login.html")

def User_Signup_page(req):
    return render(req,"User_Signup.html")

def Save_user(requset):
    if requset.method=="POST":
        UN = requset.POST.get('user')
        EM = requset.POST.get('email')
        PWD = requset.POST.get('pass')

        obj =UserDB(Username=UN,Email=EM,Pass=PWD)
        if UserDB.objects.filter(Username=UN).exists():
            messages.warning(requset,"Username Already Exists")
            return redirect(User_Signup_page)
        elif UserDB.objects.filter(Email=EM).exists():
            messages.warning(requset,"Email already Exists")
            return redirect(User_Signup_page)
        else:
            obj.save()
            messages.success(requset, "Account Created ")
        return redirect(User_login_page)

def User_loginn(request):
    if request.method == "POST":
        un = request.POST.get('sign_user')
        pwd = request.POST.get('sign_pass')
        if UserDB.objects.filter(Username=un,Pass=pwd).exists():
            request.session['Username'] = un
            request.session['Pass'] = pwd
            messages.success(request,"Succesfully Login")
            return redirect(Home_page)
        else:
            # messages.warning(request, "User Not Found")
            return redirect(User_login_page)

    else:
        # messages.warning(request, "User Not Found")
        return redirect(User_login_page)


def user_logout(request):
    del request.session['Username']
    del request.session['Pass']
    messages.success(request, "Succesfully Logout")
    return redirect(Home_page)


def CartPage(req):
    cat = CategoriesDB.objects.all()
    try:
        data = cartDB.objects.filter(Username=req.session['Username'])
        subtotal = 0
        shipping_charge = 0
        total = 0
        for x in data:
            subtotal += x.TotalPrice
            if subtotal >= 800:
                shipping_charge = 30
            elif subtotal >= 500:
                shipping_charge = 50
            else:
                shipping_charge = 80

            total = subtotal + shipping_charge
        return render(req,"Cart.html",{'cat':cat,'data':data,'subtotal':subtotal,'total':total,'shipping_charge':shipping_charge})
    except KeyError:
        return redirect(User_login_page)

def saveCart(req):
    if req.method == "POST":
        QN = req.POST.get('QUANTITY')
        TP = req.POST.get('TOTALPRICE')
        US = req.POST.get('USERNAME')
        PN = req.POST.get('PRODUCTNAME')

        obj = cartDB(Username=US,ProductName=PN,Quantity=QN,TotalPrice=TP)
        obj.save()
        messages.success(req,"Added to cart")
        return redirect(CartPage)

def Delete_cart_item(requset,p_id):
    x = cartDB.objects.filter(id=p_id)
    x.delete()
    messages.error(requset,"Item removed")
    return redirect(CartPage)

def Checkout_page(req):
    cat = CategoriesDB.objects.all()
    products = cartDB.objects.filter(Username=req.session['Username'])
    subtotal = 0
    shipping_charge = 0
    total = 0
    for x in products:
        subtotal += x.TotalPrice
        if subtotal >= 800:
            shipping_charge = 30
        elif subtotal >= 500:
            shipping_charge = 50
        else:
            shipping_charge = 80

        total = subtotal + shipping_charge
    return render(req,"Checkout.html",{'cat':cat,'products':products,'shipping_charge':shipping_charge,'subtotal':subtotal,'total':total})


def Save_billing(req):
    if req.method=="POST":
        na = req.POST.get('username')
        em = req.POST.get('email')
        add = req.POST.get('address')
        ph = req.POST.get('phone')
        mes = req.POST.get('message')
        tot = req.POST.get('totalprice')

        obj = BillingDB(Name=na,Email=em,Address=add,Phone=ph,Message=mes,TotalPrice=tot)
        obj.save()
        x = cartDB.objects.filter(Username=req.session['Username'])
        x.delete()
        return redirect(Payment_page)


def Payment_page(req):
    customer = BillingDB.objects.order_by('-id').first() #Retrive BillingDb object with specified ID
    pay = customer.TotalPrice #Get payment amount of the specified customer
    amount = int(pay*100) #Assuming Payment amount in ruppee  #Convert amount to paisa (Smallest Currency unit)
    pay_str = str(amount) #convert amount to string for print
    for i in pay_str:
        print(i)
    if req.method=="POST":
        order_currency = 'INR'
        client = razorpay.Client()
    return render(req,"Payment.html",{'customer':customer})