from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.
from . models import *
from django.http import HttpResponse, HttpResponseRedirect

from django.core.files.storage import FileSystemStorage
from django.db.models import Sum


def HI(request):
    return render(request, 'HOME.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'selectregistration.html')


def adminRegister(request):
    return render(request, 'admin reg.page.html')


def customerRegister(request):
    return render(request, 'customerregi.page.html')


def loginbcak(request):
    return render(request, 'login.html')


def customerRegisterAction(request):
    if request.method == "POST":
        First_name = request.POST.get('fnn')
        Last_name=request.POST.get('fn2')
        Email=request.POST.get('Email_Id'),
        Phone=request.POST.get('mobile')
        Password=request.POST.get('txtpswd')
        State=request.POST.get('fnc')
        City=request.POST.get('cty')
        Pincode=request.POST.get('pin')
        Address=request.POST.get('txtadddr')
        data = Registration()
        data.First_name = First_name
        data.Last_name = Last_name
        data.Email = Email
        data.Phone = Phone
        data.Password = Password
        data.State = State
        data.City = City
        data.Pincode = Pincode
        data.Address = Address
        data.About = ''
        data.Lock = ''
        data.User_role = 'customer'
        data.save()
    return render(request, 'registrationsuccsess.html')


def AdminRegisterAction(request):
    if request.method == "POST":
        First_name=request.POST.get('Adminfirstn'),
        Last_name=request.POST.get('Adfn2'),
        Email=request.POST.get('email'),
        Password=request.POST.get('adtxtpswd'),
        data = Registration()
        data.First_name = First_name
        data.Last_name = Last_name
        data.Email = Email
        data.Password = Password
        data.Phone = ''
        data.State = ''
        data.Style = ''
        data.City = ''
        data.Address = ''
        data.About = ''
        data.Lock = ''
        data.User_role ='admin'
        data.save()
    return render(request, 'registrationsuccsess.html')



def LoginAction(request):
   if request.method == "POST":
        data=Registration.objects.filter(Email=request.POST.get('email'),Password=request.POST.get('pwd'))
        if data.count()>0:
            if data[0].User_role == 'customer':
                request.session['user_id'] = data[0].id

                dd = Category_product.objects.all()
                idd = []
                ds = []
                for i in dd:
                    if i.Category_name not in ds:
                        ds.append(i.Category_name)
                        idd.append(i.id)
                d = zip(idd, ds)
                k = zip(idd, ds)
                return render(request, 'customerHOME.html', {'d': d, 'k': k})

            elif data[0].User_role == 'admin':
                request.session['user_id'] = data[0].id

                dd = Category_product.objects.all()
                idd = []
                ds = []
                for i in dd:
                    if i.Category_name not in ds:
                        ds.append(i.Category_name)
                        idd.append(i.id)
                d = zip(idd, ds)
                k = zip(idd, ds)
                zx = zip(idd, ds)
                kf = zip(idd, ds)
                return render(request, 'ADMIN_HOME.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf})

        else:
            return render(request,'login.html',{'msg':'Email or password entered is incorrect !!'})





def adminhome(request):
    return render(request, 'adminHOME.html')

def contact(request):
    return render(request, 'contact.html')




def messagesubmitaction(request):
    if request.method == "POST":
        message = request.POST.get('messages')
        data = Band_order(Front_message = message,Back_message='',Color='',Fonts_style='',Bandd_size='',Bandd_style='',Clipartt_name='',First_name='',Last_name='',Email='',Phone='',State='',City='',Address='',Order_status='',)
        data.save()
        return render(request, 'succsess.html')



def viewmessage(request):
    obj = Band_order.objects.all()
    return render(request, 'view_cus_message.html', {'details': obj})

def updateprofile(request):
    data=Registration.objects.filter(id=request.session['user_id'])
    return render(request, 'updateprofile.html', {'details': data})

def updateAdminProfileAction(request):
    if request.method == "POST":
        data = Registration.objects.filter(id=request.session['user_id']).update(First_name=request.POST.get('Adminfirstn'),Last_name=request.POST.get('Adfn2'),Email=request.POST.get('email'),Password=request.POST.get('adtxtpswd'))
        return render(request,'succsess.html')
    else:
        return render(request,'error.html')

def addcategory(request):
    return render(request, 'add_category.html')



def addcategoryaction(request):
    if request.method == "POST":
        catname = request.POST.get('catname')
        gh = Category_product.objects.all()
        for i in gh:
            if i.Category_name == catname:
                return render(request, 'add_category.html', {'msg': 'category already exist !!'})
        data = Category_product(Product_name='', Product_image='', Status='', Category_name=catname)
        data.save()
        return render(request, 'ADMIN_HOME.html',{'msg':'category added sucessfully !!'})



def addproductprice(request):
        return render(request, 'ADMIN_HOME.html')

def addproductpriceaction(request):
    if request.method == "POST":
        price = request.POST.get('price')
        data = Band_details(Font_name='', Style='', Clipart_name='', Clipart_image='', Status='', Unit_price=price)
        data.save()
        return render(request, 'succsess.html')

def viewcategory(request):
    obj = Category_product.objects.all()
    sds = []
    for t in obj:
        print(t.Category_name)
        if t.Category_name not in sds:
            sds.append(t.Category_name)
    print(sds)
    return render(request, 'viewcategory.html', {'details': sds})

def viewprice(request):
    obj = Band_details.objects.all()
    return render(request, 'viewproduct_price.html', {'details': obj})

def addimage(request):
    return render(request, 'add_image.html')

def insertiamgeaction(request):
    if request.method == "POST":
        img = request.FILES.get('image')
        data = Band_details(Font_name='', Style='', Clipart_name='', Clipart_image=img, Status='')
        data.save()
        return render(request, 'succsess.html')


def viewimage(request):
    obj = Band_details.objects.all()
    return render(request, 'view_image.html', {'details': obj})








#########################################

def temperory(request):
    return render(request, 'temperory.html')


def insertfonts2(request):
    return render(request, 'insertfont2.html')

def insertfontaction2(request):
    if request.method == "POST":
        Fontname = request.POST.get('font2')
        data = fontstyle(name=Fontname)
        data.save()
        return render(request, 'succsess.html')

def insertcategory2(request):
    return render(request, 'insertcategory.html')

def insertcategoryaction2(request):
    if request.method == "POST":
        categor = request.POST.get('category')
        data = category(name=categor)
        data.save()
        return render(request, 'succsess.html')

def insertsize2(request):
        return render(request, 'insertsize2.html')

def insertsizeaction(request):
    if request.method == "POST":
        insize = request.POST.get('insize')
        data = size(name=insize)
        data.save()
        return render(request, 'succsess.html')


def insertprice2(request):
    return render(request, 'insertprice2.html')

def insertpriceacton2(request):
    if request.method == "POST":
        inprize = request.POST.get('inprize')
        data = category(name=inprize)
        data.save()
        return render(request, 'succsess.html')

################################################




def getfontstyle(request):
    category = request.GET.get('cat')
    objfont = fontstyle.objects.filter(name=category,)
    return render(request, "getfontstyle.html", {'Subjects': objfont})


def submit(request):
    if len(request.FILES) != 0:
        category = request.POST['allfont']
        print('category', category)
        if (category == 'No_category'):
            return render(request, 'dependency_drop.html')
        else:
            objfont = fontstyle.objects.get(id=request.POST['allfont'])
            print('cat', objfont)
            print('category', request.POST['category'])
            return render(request, 'dependency_drop.html')


########################################################3


def Product_name(request):
    return render(request, 'Product_name.html')

def Product_image(request):
    return render(request, 'Product_image.html')

def Minimum_quantity(request):
    return render(request, 'Minimum_quantity.html')

def Maximum_quantity(request):
    return render(request, 'Maximum_quantity.html')

def Discount_percentage(request):
    return render(request, 'Discount_percentage.html')

def Unit_price(request):
    return render(request, 'Unit_price.html')

def Status(request):
    return render(request, 'Status.html')


def insertproductname(request):
    if request.method == "POST":
        inproduct = request.POST.get('inproduct')
        gh = Category_product.objects.all()
        for i in gh:
            if i.Product_name == inproduct:
                return render(request, 'Product_name.html', {'msg': 'product already exist !!'})
        data = Category_product(Category_name='', Product_image='', Status='', Product_name=inproduct)
        data.save()
        return render(request, 'ADMIN_HOME.html',{'msg':'product added sucessfully !!'})

def insertproductimage(request):
    if request.method == "POST":
        image = request.FILES['image']
        fs = FileSystemStorage()
        fs.save(image.name, image)
        data = Category_product(Product_image=image)
        data.save()
        return render(request, 'succsess.html')


def insertminimumquant(request):
    if request.method == "POST":
        minimum = request.POST.get('minimum')
        gh = Category_product.objects.all()
        for i in gh:
            if i.Minimum_quantity == minimum:
                return render(request, 'Minimum_quantity.html', {'msg': 'minimum quantity already exist !!'})
        data = Category_product(Category_name='', Product_image='', Status='', Product_name='',Minimum_quantity=minimum)
        data.save()
        return render(request, 'ADMIN_HOME.html',{'msg':'minimum quantity added sucessfully !!'})


def insertmaximumquantity(request):
    if request.method == "POST":
        max = request.POST.get('max')
        gh = Category_product.objects.all()
        for i in gh:
            if i.Maximum_quantity == max:
                return render(request, 'Maximum_quantity.html', {'msg': 'maximum quantity already exist !!'})
        data = Category_product(Category_name='', Product_image='', Status='', Product_name='',Maximum_quantity=max)
        data.save()
        return render(request, 'ADMIN_HOME.html',{'msg':'maximum quantity added sucessfully !!'})


def insertpercentage(request):
    if request.method == "POST":
        yes = request.POST.get('per')
        gh = Category_product.objects.all()
        for i in gh:
            if i.Discount_percentage == yes:
                return render(request, 'Discount_percentage.html', {'msg': 'discount already exist !!'})
        data = Category_product(Category_name='', Product_image='', Status='', Product_name='',Discount_percentage=yes)
        data.save()
        return render(request, 'ADMIN_HOME.html',{'msg':'discount added sucessfully !!'})


def insertunitprice(request):
    if request.method == "POST":
        unitpri = request.POST.get('unitpri')
        gh = Category_product.objects.all()
        for i in gh:
            if i.Unit_price == unitpri:
                return render(request, 'Unit_price.html', {'msg': 'unit price already exist !!'})
        data = Category_product(Category_name='', Product_image='', Status='', Product_name='',Unit_price=unitpri)
        data.save()
        return render(request, 'ADMIN_HOME.html',{'msg':'unitprice added sucessfully !!'})

def insertstatus(request):
    if request.method == "POST":
        Status = request.POST.get('Status')
        gh = Category_product.objects.all()
        for i in gh:
            if i.Status == Status:
                return render(request, 'Status.html', {'msg': 'status already exist !!'})
        data = Category_product(Product_name='', Product_image='', Category_name='', Status=Status)
        data.save()
        return render(request, 'ADMIN_HOME.html',{'msg':'status added sucessfully !!'})


def viewProduct_name (request):
    obj = Category_product.objects.all()
    sds = []
    for t in obj:
        print(t.Product_name)
        if t.Product_name not in sds and t.Product_name != '':
            sds.append(t.Product_name)
    print(sds)
    return render(request, 'viewProduct_name.html', {'details': sds})

def viewProduct_image (request):
    obj=Category_product.objects.all()
    sds = []
    for t in obj:
        if t.Product_image != '':
            sds.append(t)
    return render(request,'viewProduct_image.html',{'details':sds})

def viewMinimum_quantity (request):
    obj = Category_product.objects.all()
    sds = []
    for t in obj:
        print(t.Minimum_quantity)
        if (t.Minimum_quantity not in sds) and (t.Minimum_quantity != 0):
            sds.append(t.Minimum_quantity)
    print(sds)
    return render(request, 'viewMinimum_quantity.html', {'details': sds})

def viewMaximum_quantity (request):
    obj = Category_product.objects.all()
    sds = []
    for t in obj :
        print(t.Maximum_quantity)
        if (t.Maximum_quantity not in sds) and (t.Maximum_quantity != 0):
            sds.append(t.Maximum_quantity)
    print(sds)
    return render(request, 'viewMinimum_quantity.html', {'details': sds})

def viewDiscount_percentage (request):
    obj = Category_product.objects.all()
    sds = []
    for t in obj:
        print(t.Discount_percentage)
        if (t.Discount_percentage not in sds) and (t.Discount_percentage != 0):
            sds.append(t.Discount_percentage)
    print(sds)
    return render(request, 'viewDiscount_percentage.html', {'details': sds})

def viewUnit_price (request):
    obj = Category_product.objects.all()
    sds = []
    for t in obj:
        print(t.Unit_price)
        if (t.Unit_price not in sds) and (t.Unit_price != 0):
            sds.append(t.Unit_price)
    print(sds)
    return render(request, 'viewUnit_price.html', {'details': sds})

def viewStatus (request):
    obj = Category_product.objects.all()
    sds = []
    for t in obj:
        print(t.Status)
        if t.Status not in sds and t.Status != '':
            sds.append(t.Status)
    print(sds)
    return render(request, 'viewStatus.html', {'details': sds})



####################################################CONVAYENCE FEES###################################

def Delivery_charge_min_km(request):
    return render(request, 'insertDelivery_charge_min_km.html')
def Delivery_charge_max_km(request):
    return render(request, 'insertDelivery_charge_max_km.html')
def Delivery_fees(request):
    return render(request, 'insertDelivery_fees.html')
def Shipping_days(request):
    return render(request, 'insertShipping_days.html')
def Shipping_description(request):
    return render(request, 'insertShipping_description.html')
def Shipping_cost(request):
    return render(request, 'insertShipping_cost.html')
def convayenceStatus(request):
    return render(request, 'insertconvayenceStatus.html')




def Delivery_charge_min_km_action(request):
    if request.method == "POST":
        dcmin = request.POST.get('dcmin')
        data = Conveyance_fees(Delivery_charge_min_km=dcmin)
        data.save()
        return render(request, 'succsess.html')



def Delivery_charge_max_km_action(request):
    if request.method == "POST":
        dcmax = request.POST.get('dcmax')
        data = Conveyance_fees(Delivery_charge_max_km=dcmax)
        data.save()
        return render(request, 'succsess.html')

def insertdeliveryfees(request):
    if request.method == "POST":
        insdlfees = request.POST.get('insdlfees')
        data = Conveyance_fees(Delivery_fees=insdlfees)
        data.save()
        return render(request, 'succsess.html')


def insertshippingdays(request):
    if request.method == "POST":
        insshdays = request.POST.get('insshdays')
        data = Conveyance_fees(Shipping_days=insshdays)
        data.save()
        return render(request, 'succsess.html')


def insertshippingdesc(request):
    if request.method == "POST":
        insshdesc = request.POST.get('insshdesc')
        data = Conveyance_fees(Shipping_description=insshdesc)
        data.save()
        return render(request, 'succsess.html')


def insertshippingcost(request):
    if request.method == "POST":
        insshcost = request.POST.get('insshcost')
        data = Conveyance_fees(Shipping_cost=insshcost)
        data.save()
        return render(request, 'succsess.html')


def insertconayenceststus(request):
    if request.method == "POST":
        inscovstst = request.POST.get('inscovstst')
        data = Conveyance_fees(Status=inscovstst)
        data.save()
        return render(request, 'succsess.html')


def viewDelivery_charge_min_km (request):
    obj=Conveyance_fees.objects.all()
    return render(request,'viewDelivery_charge_min_km.html',{'details':obj})

def viewDelivery_charge_max_km (request):
    obj=Conveyance_fees.objects.all()
    return render(request,'viewDelivery_charge_max_km',{'details':obj})

def viewDelivery_fees (request):
    obj=Conveyance_fees.objects.all()
    return render(request,'viewDelivery_fees.html',{'details':obj})

def viewShipping_days (request):
    obj=Conveyance_fees.objects.all()
    return render(request,'viewShipping_days.html',{'details':obj})

def viewShipping_description (request):
    obj=Conveyance_fees.objects.all()
    return render(request,'viewShipping_description.html',{'details':obj})

def viewShipping_cost (request):
    obj=Conveyance_fees.objects.all()
    return render(request,'viewShipping_cost.html',{'details':obj})

def viewconvayenceStatus (request):
    obj=Conveyance_fees.objects.all()
    return render(request,'viewconvayenceStatus.html',{'details':obj})





#############################   CUSTOMER      ###############################
def cusselectcategory(request):
    obj = Category_product.objects.all()
    sds = []
    for t in obj:
        print(t.Category_name)
        if t.Category_name not in sds:
            sds.append(t.Category_name)
    print(sds)
    return render(request, 'customerHOME.html', {'details': sds})


def cus_selectcategory(request):

    return render(request, 'cus_viewproduct.html')




def cus_selectproduct(request):
    obj = Category_product.objects.all()
    sds = []
    for t in obj:
        print(t.Product_name)
        if t.Product_name:
            sds.append(t.Product_name)
    print(sds)
    return render(request, 'cus_viewproduct.html', {'details': sds})



def addproduct (request):
    obj = Category_product.objects.all()
    sds = []
    for t in obj:
        print(t.Category_name)
        if t.Category_name:
            sds.append(t.Category_name)
    print(sds)
    return render(request, 'addproduct.html', {'details': sds})



def admin_addproduct(request):
    if request.method == "POST":
        cat = request.POST.get('source')
        product = request.POST.get('pro')
        image = request.FILES['image']
        fs = FileSystemStorage()
        fs.save(image.name, image)
        min = request.POST.get('min')
        max = request.POST.get('max')
        discount = request.POST.get('dp')
        unitpri = request.POST.get('up')
        status = request.POST.get('sts')
        data = Category_product()
        data.Category_name = cat
        data.Product_name = product
        data.Product_image = image
        data.Minimum_quantity = min
        data.Maximum_quantity = max
        data.Discount_percentage = discount
        data.Unit_price = unitpri
        data.Status = status
        data.save()
        return render(request, 'succsess.html')

def convayencefees(request):
    return render(request, 'CONVAYENCE.html')


###########################################BAND_DETAILS################

def addbanddetail(request):
    return render(request, 'ADD_BAND_DETAILS.html')

def cushome(request):
    return render(request, 'ADMIN_HOME.html')




def insertfonts(request):
    return render(request, 'insertfont.html')

def insertfontaction(request):
        if request.method == "POST":
            catname = request.POST.get('font')
            gh = Band_details.objects.all()
            for i in gh:
                if i.Font_name == catname:
                    return render(request, 'insertfont.html', {'msg': 'font already exist !!'})
            data = Band_details(Font_name = catname,Style='',Clipart_name='',Clipart_image='',Status='')
            data.save()
            return render(request, 'ADMIN_HOME.html', {'msg': 'font added sucessfully !!'})

def viewfonts (request):
    obj = Band_details.objects.all()
    sds = []
    for t in obj:
        print(t.Font_name)
        if t.Font_name not in sds and t.Font_name != '':
            sds.append(t.Font_name)
    print(sds)
    return render(request, 'viewfonts.html', {'details': sds})

#####################

def insertbandsize(request):
    return render(request, 'insert_band_size.html')

def insertbandsizeaction(request):
    if request.method == "POST":
        band = request.POST.get('bandsize')
        gh = Band_details.objects.all()
        for i in gh:
            if i.Size_in_inch == band:
                return render(request, 'insert_band_size.html', {'msg': 'Band size already exist !!'})
        data = Band_details(Font_name='', Style='', Clipart_name='', Clipart_image='', Status='',Size_in_inch=band)
        data.save()
        return render(request, 'ADMIN_HOME.html',{'msg':'Band size added sucessfully !!'})

def viewbandsize(request):
    obj = Band_details.objects.all()
    sds = []
    for t in obj:
        print(t.Size_in_inch)
        if (t.Size_in_inch not in sds) and (t.Size_in_inch != 0):
            sds.append(t.Size_in_inch)
    print(sds)
    return render(request, 'view_band_size.html', {'details': sds})





def inserstyle(request):
    return render(request, 'band_style.html')

def addbandstyleaction(request):
    if request.method == "POST":
        band = request.POST.get('catname')
        gh = Band_details.objects.all()
        for i in gh:
            if i.Style == band:
                return render(request, 'band_style.html', {'msg': 'Band style already exist !!'})
        data = Band_details(Font_name='', Clipart_name='', Clipart_image='', Status='', Style=band)
        data.save()
        return render(request, 'ADD_BAND_DETAILS.html',{'msg':'Band style added sucessfully !!'})

def viewstyle(request):
    obj = Band_details.objects.all()
    sds = []
    for t in obj:
        print(t.Style)
        if t.Style not in sds and t.Style != '':
            sds.append(t.Style)
    print(sds)
    return render(request, 'view_bandstyle.html', {'details': sds})


########

def inseclipname(request):
    return render(request, 'insertbandclipart.html')

def addcbandclipart(request):
    if request.method == "POST":
        band = request.POST.get('catname')
        gh = Band_details.objects.all()
        for i in gh:
            if i.Clipart_name  == band:
                return render(request, 'insertbandclipart.html', {'msg': 'clipartname already exist !!'})
        data = Band_details(Font_name='', Clipart_image='', Status='', Style='', Clipart_name=band)
        data.save()
        return render(request, 'ADD_BAND_DETAILS.html',{'msg':'clipart name added sucessfully !!'})

def viewbandname(request):
    obj = Band_details.objects.all()
    sds = []
    for t in obj:
        print(t.Clipart_name )
        if t.Clipart_name not in sds and t.Clipart_name != '':
            sds.append(t.Clipart_name )
    print(sds)
    return render(request, 'viewclipartname.html', {'details': sds})

###########


def bandimage(request):
    return render(request, 'insertbandimage.html')

def insertbandimage(request):
    if request.method == "POST":
        image = request.FILES['image']
        fs = FileSystemStorage()
        fs.save(image.name, image)
        data = Band_details(Clipart_image =image)
        data.save()
    return render(request, 'ADD_BAND_DETAILS.html', {'msg': 'image added sucsessfully exist !!'})


def viewbandimage(request):
    obj=Band_details.objects.all()
    sds = []
    for t in obj:
        if t.Clipart_image  != '':
            sds.append(t)
    return render(request,'viewbandimage.html',{'details':sds})

################


def bandminquan(request):
    return render(request, 'bandminimumquant.html')

def bandminquant(request):
    if request.method == "POST":
        band = request.POST.get('catname')
        gh = Band_details.objects.all()
        for i in gh:
            if i.Minimum_quantity  == band:
                return render(request, 'bandminimumquant.html', {'msg': 'Band min.quantity already exist !!'})
        data = Band_details(Font_name='', Clipart_name='', Clipart_image='', Status='', Style='',Minimum_quantity =band)
        data.save()
        return render(request, 'ADD_BAND_DETAILS.html',{'msg':'Band min.quantity added sucessfully !!'})

def viewbandminquan(request):
    obj = Band_details.objects.all()
    sds = []
    for t in obj:
        print(t.Minimum_quantity )
        if (t.Minimum_quantity not in sds) and (t.Minimum_quantity != 0):
            sds.append(t.Minimum_quantity )
    print(sds)
    return render(request, 'viewbandminquan.html', {'details': sds})

######################


def bandmaxquant(request):
    return render(request, 'bandmaxquant.html')

def bandmmaxnquant(request):
    if request.method == "POST":
        band = request.POST.get('catname')
        gh = Band_details.objects.all()
        for i in gh:
            if i.Maximum_quantity  == band:
                return render(request, 'bandmaxquant.html', {'msg': ' already exist !!'})
        data = Band_details(Font_name='', Style='', Clipart_name='', Clipart_image='', Status='',Maximum_quantity=band)
        data.save()
        return render(request, 'ADD_BAND_DETAILS.html',{'msg':'maxquantity added sucessfully !!'})

def viewbandmaxquant(request):
    obj = Band_details.objects.all()
    sds = []
    for t in obj:
        print(t.Maximum_quantity)
        if (t.Maximum_quantity not in sds) and (t.Maximum_quantity != 0):
            sds.append(t.Maximum_quantity)
    print(sds)
    return render(request, 'viewbandmaxquant.html', {'details': sds})


################


def banddiscount(request):
    return render(request, 'banddiscount.html')

def banddiscount2(request):
    if request.method == "POST":
        band = request.POST.get('catname')
        gh = Band_details.objects.all()
        for i in gh:
            if i.Discount_percentage  == band:
                return render(request, 'banddiscount.html', {'msg': ' already exist !!'})
        data = Band_details(Font_name='', Clipart_name='', Clipart_image='', Status='', Style='',Discount_percentage=band)
        data.save()
        return render(request, 'ADD_BAND_DETAILS.html',{'msg':'Band Discount percentage added sucessfully !!'})

def viewbanddiscount(request):
    obj = Band_details.objects.all()
    sds = []
    for t in obj:
        print(t.Discount_percentage)
        if (t.Discount_percentage not in sds) and (t.Discount_percentage != 0):
            sds.append(t.Discount_percentage)
    print(sds)
    return render(request, 'viewbanddiscount.html', {'details': sds})


########################


def bandunitprice(request):
    return render(request, 'bandunitprice.html')

def bandunit(request):
    if request.method == "POST":
        band = request.POST.get('catname')
        gh = Band_details.objects.all()
        for i in gh:
            if i.Unit_price  == band:
                return render(request, 'bandunitprice.html', {'msg': 'already exist !!'})
        data = Band_details(Font_name='', Clipart_name='', Clipart_image='', Status='', Style='',Unit_price=band)
        data.save()
        return render(request, 'ADD_BAND_DETAILS.html',{'msg':'Band unitprice added sucessfully !!'})

def viewbandunitprice(request):
    obj = Band_details.objects.all()
    sds = []
    for t in obj:
        print(t.Unit_price)
        if (t.Unit_price not in sds) and (t.Unit_price != 0):
            sds.append(t.Unit_price)
    print(sds)
    return render(request, 'viewbandunitprice.html', {'details': sds})



###########################


def bandstatus(request):
    return render(request, 'bandstatus.html')

def bandstatus2(request):
    if request.method == "POST":
        band = request.POST.get('catname')
        gh = Band_details.objects.all()
        for i in gh:
            if i.Status  == band:
                return render(request, 'bandstatus.html', {'msg': 'Band status already exist !!'})
        data = Band_details(Font_name='', Clipart_name='', Clipart_image='', Style='', Status=band)
        data.save()
        return render(request, 'ADD_BAND_DETAILS.html',{'msg':'Band status added sucessfully !!'})

def viewbandstatus(request):
    obj = Band_details.objects.all()
    sds = []
    for t in obj:
        print(t.Status )
        if t.Status not in sds and t.Status != '':
            sds.append(t.Status )
    print(sds)
    return render(request, 'viewbandstatus.html', {'details': sds})

def addanewband (request):
    obj = Band_details.objects.all()
    sds = []
    for t in obj:
        print(t.Font_name)
        if t.Font_name:
            sds.append(t.Font_name)
    print(sds)
    return render(request, 'addanewband.html', {'details': sds})



def addanewbandaction(request):
    if request.method == "POST":
        font = request.POST.get('source')
        bandsize = request.POST.get('pro')
        style = request.POST.get('style')
        clipname = request.POST.get('clipname')
        image = request.FILES['image']
        fs = FileSystemStorage()
        fs.save(image.name, image)
        min = request.POST.get('min')
        max = request.POST.get('max')
        discount = request.POST.get('dp')
        unitpri = request.POST.get('up')
        status = request.POST.get('sts')
        data = Band_details()
        data.Clipart_image = image
        data.Font_name = font
        data.Size_in_inch = bandsize
        data.Style = style
        data.Clipart_name = clipname
        data.Minimum_quantity = min
        data.Maximum_quantity = max
        data.Discount_percentage = discount
        data.Unit_price = unitpri
        data.Status = status
        data.save()
        return render(request, 'succsess.html')

###################################################

def selectbandsizeaction(request):
    if request.method == 'POST' :
        size_sel = request.POST.get('source')
        ob = Band_details.objects.filter(Size_in_inch = size_sel ).values('Style').distinct()

        print('======================================================',ob)

    return render(request, 'cus_selectfont_style.html',{'style':ob})

##################################################################



def customizedband2(request):
    obj = Band_details.objects.all()

    obj2 = Band_details.objects.all()
    sds = []
    for t in obj2:
        print(t.Style)
        if t.Style not in sds and t.Style != '':
            sds.append(t.Style)


    obj3 = Band_details.objects.all()
    sds3 = []
    for t in obj3:
        print(t.Size_in_inch)
        if (t.Size_in_inch not in sds3) and (t.Size_in_inch != 0):
            sds3.append(t.Size_in_inch)


    obj4 = Band_details.objects.all()
    sds4 = []
    for t in obj4:
        print(t.Font_name)
        if t.Font_name not in sds4 and t.Font_name != '':
            sds4.append(t.Font_name)


    obj5 = Band_details.objects.all()
    sds5 = []
    for t in obj5:
        print(t.Clipart_name)
        if t.Clipart_name not in sds5 and t.Clipart_name != '':
            sds5.append(t.Clipart_name)


    return render(request, 'customizedband2.html', {'details':obj,'details2':sds,'details3':sds3,'details4':sds4,'details5':sds5})



def cus_customizebandaction(request):
    if request.method == "POST":
        data = Band_details.objects.filter(Size_in_inch=request.POST.get('bansiz'), Style=request.POST.get('source3'), Clipart_name=request.POST.get('source5'))
        if data.count() > 0:
            fmess = request.POST.get('catname1')
            bkmess = request.POST.get('catname2')
            color = request.POST.get('catname3')
            fontsty = request.POST.get('source2')
            bndsize = request.POST.get('bansiz')
            bndstyle = request.POST.get('source3')
            clipname = request.POST.get('source5')
            quantity = request.POST.get('source4')

            nm = Band_details.objects.get(Style = bndstyle,Size_in_inch = bndsize,Clipart_name = clipname)
            unit_price = nm.Unit_price
            total = int(unit_price) * int(quantity)

            b = Registration.objects.get(id = request.session['user_id'])
            data = Cust_cart(regg=b, Front_message=fmess, Back_message=bkmess, Color=color, Fon_style=fontsty, Ban_size=bndsize,
                             Ban_style=bndstyle, Clippart_name=clipname, QQuantity=quantity, Pricce = unit_price, Total_amount = total)


            data.save()

            obj = Band_details.objects.all()
            obj2 = Band_details.objects.all()
            sds = []
            for t in obj2:
                print(t.Style)
                if t.Style not in sds:
                    sds.append(t.Style)

            obj3 = Band_details.objects.all()
            sds3 = []
            for t in obj3:
                print(t.Size_in_inch)
                if t.Size_in_inch not in sds3:
                    sds3.append(t.Size_in_inch)

            obj4 = Band_details.objects.all()
            sds4 = []
            for t in obj4:
                print(t.Font_name)
                if t.Font_name not in sds4:
                    sds4.append(t.Font_name)

            obj5 = Band_details.objects.all()
            sds5 = []
            for t in obj5:
                print(t.Clipart_name)
                if t.Clipart_name not in sds5:
                    sds5.append(t.Clipart_name)

            return render(request, 'customizedband2.html',
                          {'details': obj, 'details2': sds, 'details3': sds3, 'details4': sds4, 'details5': sds5,
                           'msg': 'item added to cart sucessfully !!'})


        else:

            obj = Band_details.objects.all()
            obj2 = Band_details.objects.all()
            sds = []
            for t in obj2:
                print(t.Style)
                if t.Style not in sds:
                    sds.append(t.Style)


            obj3 = Band_details.objects.all()
            sds3 = []
            for t in obj3:
                print(t.Size_in_inch)
                if t.Size_in_inch not in sds3:
                    sds3.append(t.Size_in_inch)


            obj4 = Band_details.objects.all()
            sds4 = []
            for t in obj4:
                print(t.Font_name)
                if t.Font_name not in sds4:
                    sds4.append(t.Font_name)

            obj5 = Band_details.objects.all()
            sds5 = []
            for t in obj5:
                print(t.Clipart_name)
                if t.Clipart_name not in sds5:
                    sds5.append(t.Clipart_name)

            return render(request, 'customizedband2.html',
                          {'details': obj, 'details2': sds, 'details3': sds3, 'details4': sds4, 'details5': sds5,'msg':'sorry this configuration is not available right now !!'})



####################################################################
def cusfaq(request):
    data=Registration.objects.filter(id=request.session['user_id'])
    return render(request, 'cusfaq.html', {'details': data})

def cusfaqaction(request):
    if request.method == "POST":
        cusfaq = request.POST.get('cusfaq')
        wert = request.POST.get('wert')
        trew = request.POST.get('trew')
        data = Faq(Customer_name=wert,Customer_email=trew,Question=cusfaq,Answer='to be expected soon !!!')
        data.save()
    return render(request, 'customerHOME.html',
                  {'msg': 'Success please wait for  replay !!'})

##def cusviewfaq(request):
   # obj = Faq.objects.all()
    #sds = []
    #for t in obj:
        #if t.Question and t.Answer not in sds:
           # sds.append(t.Question,t.Answer)

    #return render(request, 'cusviewfaq.html', {'details': sds})


def cusviewfaq(request):
    se = Faq.objects.all()
    dd = Registration.objects.get(id = request.session['user_id'])
    if request.method == 'POST':
        text_feed = request.POST.get('text_feed')
        ss = Faq()
        a = str(dd.First_name)
        b = str(dd.Last_name)
        ss.Customer_name = a+' '+b
        ss.Customer_email = dd.Email
        ss.Question = text_feed
        ss.Answer = "To be expected soon"
        ss.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        return render(request, 'customer_home.html', {'d': d, 'k': k})
    return render(request, 'faq.html', {'se': se})


def adminfaq(request):
    obj = Faq.objects.filter(Answer='to be expected soon !!!')
    return render(request, 'adminviewfaq.html', {'details': obj})






def adminprovideanswer(request,id):
    if request.method == "POST":
        answer = request.POST.get('ans')
        Faq.objects.filter(id=id).update(Answer=answer)
    obj = Faq.objects.filter(Answer__isnull=True)
    return render(request, 'adminviewfaq.html',{'details': obj,'msg':'answer added sucessfully !!'})


############################################FEEDBACK#############################


def cusfeedback(request):
    data=Registration.objects.filter(id=request.session['user_id'])
    obj = Category_product.objects.all()
    sds = []
    for t in obj:
        print(t.Category_name)
        if t.Category_name not in sds and t.Category_name != '':
            sds.append(t.Category_name)
    print(sds)
    return render(request, 'cusfeedback.html', {'details': data,'key': sds})


def cussendfeedback(request):
    if request.method == "POST":
        ab = request.POST.get('wert')
        cd = request.POST.get('trew')
        ef = request.POST.get('source')
        gh = request.POST.get('cusfaq')
        data = Feedback(Name=ab, Email=cd, Category=ef, Content=gh)
        data.save()
        return render(request, 'customerHOME.html',{'msg':'feed backsend !!'})

def adminviewfeedback(request):
    obj = Feedback.objects.all()
    return render(request, 'adminviewfeedback.html', {'details': obj})


#######################################ADMIN QUOTATION##############################


def adminsendquotation(request):
    obj = Category_product.objects.all()
    return render(request, 'adminsendquotation.html', {'details': obj})


def adminaddquatation(request):
    if request.method == "POST":
        minq = request.POST.get('wert')
        maxq = request.POST.get('trew')
        disc = request.POST.get('disc')
        sts = request.POST.get('sta')
        source = request.POST.get('source')
        data = Quotation(Category_name=source, Minimum_quantity=minq, Maximum_quantity=maxq, Discount_percent=disc, Status=sts)
        data.save()
        return render(request, 'adminsendquotation.html',{'msg':'quotataion send !!'})

def adminviewquatation(request):
    obj = Quotation.objects.all()
    return render(request, 'adminviewquatation.html', {'details': obj})

######################

def cussendquotataion(request):
    data=Registration.objects.filter(id=request.session['user_id'])
    obj = Category_product.objects.all()
    return render(request, 'cussendquotataion.html', {'details': data,'key': obj})


def cussendquottation(request):
    if request.method == "POST":
        name = request.POST.get('wert')
        email = request.POST.get('trew')
        cat = request.POST.get('source')
        desc = request.POST.get('des')
        quans = request.POST.get('quant')
        status = request.POST.get('sts')
        data = Quotation_cus(Customer_name=name, Customer_email=email, Category_name=cat, Description=desc, Quantity_selected=quans, Status=status)
        data.save()
        return render(request, 'cussendquotataion.html',{'msg':'quotataion send !!'})



def cusviewquotataion(request):
    obj = Quotation_cus.objects.all()
    return render(request, 'cusviewquotataion.html', {'details': obj})

############################## DEPENDENCY DROP ####################################3

def dependency(request):
    obj2 = Band_details.objects.all()
    sds = []
    for t in obj2:
        print(t.Maximum_quantity)
        if t.Maximum_quantity  not in sds:
            sds.append(t.Maximum_quantity)
    print(sds)
    return render(request, 'dependency.html', {'details': sds})



############################ CART  ###########################


def viewcart(request):
    obj = Cust_cart.objects.all()
    return render(request, 'cart.html', {'details': obj})

def backtoconfigure(request):
    obj = Band_details.objects.all()

    obj2 = Band_details.objects.all()
    sds = []
    for t in obj2:
        print(t.Style)
        if t.Style  not in sds:
            sds.append(t.Style)
    print(sds)

    obj3 = Band_details.objects.all()
    sds3 = []
    for t in obj3:
        print(t.Size_in_inch)
        if t.Size_in_inch  not in sds3:
            sds3.append(t.Size_in_inch)
    print(sds3)

    obj4 = Band_details.objects.all()
    sds4 = []
    for t in obj4:
        print(t.Font_name)
        if t.Font_name  not in sds4:
            sds4.append(t.Font_name)
    print(sds4)

    obj5 = Band_details.objects.all()
    sds5 = []
    for t in obj5:
        print(t.Clipart_name)
        if t.Clipart_name  not in sds5:
            sds5.append(t.Clipart_name)
    print(sds5)

    return render(request, 'customizedband2.html', {'details':obj,'details2':sds,'details3':sds3,'details4':sds4,'details5':sds5})




def viewcart(request):
    b = Cust_cart.objects.filter(regg = request.session['user_id'])
    g = Band_details.objects.all()
    for t in b:
        for y in g:
            if t.Clippart_name == y.Clipart_name and y.Clipart_image != '':
                print("hello")
                print (y.Clipart_name)

    gt ='20px'
    return render(request,'cart.html',{'b':b,'g':g,'gt':gt})



def delete_cart(request,id):
    Cust_cart.objects.get(id=id).delete()
    b = Cust_cart.objects.filter(regg=request.session['user_id'])
    g = Band_details.objects.all()
    gt = '20px'
    return render(request, 'cart.html', {'b': b, 'g': g, 'gt': gt})


def ckeckout(request):
    total = list(Cust_cart.objects.aggregate(Sum('Total_amount')).values())[0]
    data = Registration.objects.filter(id=request.session['user_id'])
    print(type(total))
    print(total)
    a=int(total)
    print(a)
    return render(request, 'checkout2.html', {'total': a, 'details': data})




def paybutton(request):
    total = list(Cust_cart.objects.aggregate(Sum('Total_amount')).values())[0]
    enterd = request.POST.get('pay')
    data = Registration.objects.filter(id=request.session['user_id'])
    a = int(total)
    try:
        b = int(enterd)
    except:
        return render(request, 'checkout2.html',{'total': total, 'details': data, 'msg': 'please enter amount'})


    if a < b:
        return render(request, 'checkout2.html',{'total': total, 'details': data, 'msg': 'we are sorry this is more than you have to pay'})
    elif a > b:
        return render(request, 'checkout2.html',{'total': total, 'details': data, 'msg': 'we are sorry this is lesser than you have to pay'})
    else:
        if request.method == "POST":
            a = request.POST.get('Adminfirstn')
            b = request.POST.get('Adfn2')
            z = request.POST.get('email')
            d = request.POST.get('aaa')
            e = request.POST.get('bbb')
            f = request.POST.get('ccc')
            g = request.POST.get('ddd')
            h = request.POST.get('eee')
            # data = Band_order(First_name=a, Last_name=b, Email=c,  Phone=d, State=e,  City=f ,Pincode=g,  Address=h)
            # data.save()

            all_items = Cust_cart.objects.filter(regg=request.session['user_id'])
            for c in all_items:
                li = Band_order(
                    Front_message=c.Front_message,
                    Back_message=c.Back_message,
                    Color=c.Color,
                    Fonts_style=c.Fon_style,
                    Bandd_size = c.Ban_size,
                    Bandd_style = c.Ban_style,
                    Clipartt_name = c.Clippart_name,
                    Quantitty = c.QQuantity,
                    Pricee=c.Pricce,
                    Totall_amount=c.Total_amount,First_name=a, Last_name=b, Email=z,  Phone=d, State=e,  City=f ,Pincode=g,  Address=h,
                    Order_status = 'billed'
                )
                li.save()
            Cust_cart.objects.filter(regg=request.session['user_id']).delete()
        return render(request, 'customerHOME.html',{'msg':'Order placed sucessfully !!'})



#############################################  FASHION  ############################################################################################################

def fashion(request):
    products = Category_product.objects.filter(Category_name='Fashion')
    return render(request, 'fashionHOME.html', {'details': products})

def checkboxaction(request):
    if request.method == "POST":
        quant = request.POST.get('source4')
        data = []
        abcd = request.POST.getlist('chk[]')
        for v in abcd:
            data1 = Category_product.objects.get(id=v)
            data.append(data1)
    return render(request, 'fashionCART.html', {'data': data,'quantity':quant})


def backtofashome(request):
    return render(request, 'customerHOME.html')

def Registration_teacher_action(request):
    return render(request, 'customerHOME.html')


################################################### FROM SAMPLE ####################################

def view_prdct_cus(request, id, idg):
    idg = str(idg)
    request.session["cataa_name"] = idg
    id = int(id)
    request.session["catt_id"] = id
    z = Category_product.objects.filter(Category_name = idg).exclude(Product_name = '')
    zz = str()
    for p in z:
        zz += p.Category_name
        zz = str(zz)
        zz = zz.upper()
        request.session["cata_name"] = zz
        break
    try:
        n = Category_product.objects.filter(Category_name = idg).exclude(Product_name = '')
        return render(request, 'view_prdct_cus.html', {'n': n,'zz':zz})
    except:
        return render(request, 'view_prdct_cus.html')

def ord_product(request):
    zz = request.session["cata_name"]
    idg = request.session["cataa_name"]
    request.session['cart_product'] = cart = request.POST.getlist('cart')
    try:
        request.session['quantity'] = qqn = request.POST.getlist('quantity')
    except:
        try:
            n = Category_product.objects.filter(Category_name = idg).exclude(Product_name = '',Unit_price = 0)
            return render(request, 'view_prdct_cus.html', {'n': n,'zz':zz,'msg':'Please enter quantity required !!'})
        except:
            return render(request, 'view_prdct_cus.html')

    while ("" in qqn):
        qqn.remove("")
    request.session['quantity'] = qqn
    qse = len(cart)
    qvs = len(qqn)
    if int(qse) < int(qvs):
        try:
            n = Category_product.objects.filter(Category_name = idg).exclude(Product_name = '',Unit_price = 0)
            return render(request, 'view_prdct_cus.html', {'n': n,'zz':zz,'msg':'Please enter selected item to cart !!'})
        except:
            return render(request, 'view_prdct_cus.html')

    if int(qse) != int(qvs):
        try:
            n = Category_product.objects.filter(Category_name = idg).exclude(Product_name = '',Unit_price = 0)
            return render(request, 'view_prdct_cus.html', {'n': n,'zz':zz,'msg':'Please enter quantity required !!'})
        except:
            return render(request, 'view_prdct_cus.html')
    Idd = []
    Image_namme = []
    Product_namme = []
    Pprice = []
    quantity = []
    for i in cart:
        i = int(i)
        vb = Category_product.objects.get(id = i)
        Idd.append(vb.id)
        Image_namme.append(vb.Product_image)
        Product_namme.append(vb.Product_name)
        Pprice.append(vb.Unit_price)
    for u in qqn:
        quantity.append(u)
    request.session['checkouts'] = Idd
    bm = zip(Idd, Image_namme, Product_namme, Pprice, quantity)
    bt = zip(Pprice, quantity)
    mz = 0
    mzm = []
    for i,j in bt:
        bp = int(i) * int(j)
        mz = mz + (int(i) * int(j))
        mzm.append(bp)
    request.session["indivi_price"] = mzm
    request.session["tot_price"] = mz
    return render(request,'checkout.html',{'bm':bm})



def Remove_order(request, id, idm, idt):
    cart = request.session['cart_product']
    qqn = request.session['quantity']
    th = request.session["tot_price"]
    idr = float(idm) * float(idt)
    thh = float(th) - float(idr)
    request.session["tot_price"] = thh
    cart.remove(id)
    qqn.remove(idm)
    Idd = []
    Image_namme = []
    Product_namme = []
    Pprice = []
    quantity = []
    for i in cart:
        vb = Category_product.objects.get(id=i)
        Idd.append(vb.id)
        Image_namme.append(vb.Product_image)
        Product_namme.append(vb.Product_name)
        Pprice.append(vb.Unit_price)
    for u in qqn:
        quantity.append(u)
    request.session['checkouts'] = Idd
    request.session['quantity'] = qqn
    bm = zip(Idd, Image_namme, Product_namme, Pprice, quantity)
    return render(request, 'checkout.html', {'bm': bm})


def ch_out(request):
    tot_pri = request.session["tot_price"]
    return render(request,'delivery_addr_product.html',{'tot_pri':tot_pri})


def ch_out1(request):
    tot_pri = request.session["tot_price"]
    amt = request.POST.get('amt')
    tot = request.session["tot_price"]


    a = int(tot)
    try:
        b = int(amt)
    except:
        return render(request, 'delivery_addr_product.html', {'total': tot, 'details': tot, 'msg': 'please enter amount'})

    if a < b:
        return render(request, 'delivery_addr_product.html',
                      {'total': tot, 'details': tot, 'msg': 'we are sorry this is more than you have to pay'})
    elif a > b:
        return render(request, 'delivery_addr_product.html',
                      {'total': tot, 'details': tot, 'msg': 'we are sorry this is lesser than you have to pay'})
    else:
        if float(amt) < float(tot):
            return render(request, 'delivery_addr_product.html',{'tot_pri':tot_pri,'msg':'Please pay in full !!'})
        qq = request.session['quantity']
        q = request.session['checkouts']
        nbn = zip(q,qq)
        for i,j in nbn:
            i = int(i)
            mb = Category_product.objects.get(id = i)
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            state = request.POST.get('state')
            city = request.POST.get('city')
            pincode = request.POST.get('pincode')
            address = request.POST.get('address')
            Category_name = mb.Category_name
            product_name = mb.Product_name
            pricc = mb.Unit_price
            s = Pre_order()
            s.First_name = first_name
            s.Last_name = last_name
            s.Email = email
            s.Phone = phone
            s.State = state
            s.City = city
            s.Pincode = pincode
            s.Address = address
            s.Category_name = Category_name
            s.Product_name = product_name
            s.Price = pricc


            if int(j) >= int(mb.Minimum_quantity) and int(j) <= int(mb.Maximum_quantity):
                print("hellow")
                bgb = float(j)
                bc = float(mb.Unit_price)
                km = bc * bgb
                kmm = (float(mb.Discount_percentage)/100.0) * float(km)
                kdf = km - kmm
                kdd = round(kdf,2)
                s.Total_amount = kdd
                s.Quantity = bgb
                s.Order_status = "To be expected"
                s.save()
            else:
                print("hiiii")
                bgb = float(j)
                bc = float(mb.Unit_price)
                km = bc * bgb
                km = float(km)
                kdd = round(km, 2)
                s.Total_amount = kdd
                s.Quantity = bgb
                s.Order_status = "To be expected"
                s.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds and i.Category_name != '':
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        return render(request, 'customerHOME.html', {'d': d, 'k': k,'msg':'Order has been placed successfully'})



def new_delivery(request):
    if request.method == 'POST':
        Minimum_kilometer = request.POST.get('Minimum_kilometer')
        Maximum_kilometer = request.POST.get('Maximum_kilometer')
        huh = Conveyance_fees.objects.all()
        for i in huh:
            if i.Delivery_charge_min_km == int(Minimum_kilometer) and i.Delivery_charge_max_km == int(Maximum_kilometer):
                return render(request, 'new_delivery.html',{'msg':'Kilometer range already exists'})
        price = request.POST.get('price')
        actt = request.POST.get('actt')
        a = Conveyance_fees()
        a.Shipping_days = 0
        a.Shipping_description = ''
        a.Shipping_cost = 0
        a.Delivery_charge_min_km = Minimum_kilometer
        a.Delivery_charge_max_km = Maximum_kilometer
        a.Delivery_fees = price
        a.Status = actt
        a.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        return render(request, 'ADMIN_HOME.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf,'msg':'New delivery details added'})
    return render(request, 'new_delivery.html')

def view_delivery(request):
        b = Conveyance_fees.objects.all()
        return render(request, 'view_delivery.html', {'b': b})


def admin_home(request):
    dd = Category_product.objects.all()
    idd = []
    ds = []
    for i in dd:
        if i.Category_name not in ds:
            ds.append(i.Category_name)
            idd.append(i.id)
    d = zip(idd, ds)
    k = zip(idd, ds)
    zx = zip(idd, ds)
    kf = zip(idd, ds)
    return render(request, 'ADMIN_HOME.html', {'d': d, 'k': k,'zx':zx,'kf':kf})

def edit_delivery(request, id):
    b = Conveyance_fees.objects.get(id=id)
    if request.method == 'POST':
        Minimum_kilometer = request.POST.get('Minimum_kilometer')
        Maximum_kilometer = request.POST.get('Maximum_kilometer')
        huh = Conveyance_fees.objects.exclude(id = id)
        for i in huh:
            if i.Delivery_charge_min_km == int(Minimum_kilometer) and i.Delivery_charge_max_km == int(Maximum_kilometer):
                try:
                    b = Conveyance_fees.objects.all()
                    return render(request, 'view_delivery.html', {'b': b,'msg':'Kilometer range already exists'})
                except:
                    return render(request, 'view_delivery.html',{'msg':'Kilometer range already exists'})

        price = request.POST.get('price')
        actt = request.POST.get('actt')
        b.Delivery_charge_min_km = Minimum_kilometer
        b.Delivery_charge_max_km = Maximum_kilometer
        b.Delivery_fees = price
        b.Status = actt
        b.save()

        b = Conveyance_fees.objects.all()
        return render(request, 'view_delivery.html', {'b': b,'msg':'Delivery details edited'})
    return render(request, 'edit_delivery.html', {'b': b})


def delete_delivery(request, id):
    Conveyance_fees.objects.get(id=id).delete()
    b = Conveyance_fees.objects.all()
    return render(request, 'view_delivery.html', {'b': b})


def new_ship(request):
    if request.method == 'POST':
        day = request.POST.get('day')
        desc = request.POST.get('desc')
        cost = request.POST.get('cost')
        actt = request.POST.get('actt')
        cv = Conveyance_fees.objects.all()
        for i in cv:
            k = float(i.Shipping_cost)
            if k == float(cost):
                return render(request, 'new_ship.html',{'msg':'Shipping cost already exists'})
        a = Conveyance_fees()
        a.Delivery_charge_min_km = 0
        a.Delivery_charge_max_km = 0
        a.Delivery_fees = 0
        a.Shipping_days = day
        a.Shipping_description = desc
        a.Shipping_cost = cost
        a.Status = actt
        a.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        return render(request, 'ADMIN_HOME.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf,'msg':'New shipping details added'})
    return render(request, 'new_ship.html')

def view_ship(request):
    try:
        b = Conveyance_fees.objects.all()
        return render(request, 'view_ship.html', {'b': b})
    except:
        return render(request, 'view_ship.html')


def edit_ship(request, id):
    id = int(id)
    b = Conveyance_fees.objects.get(id=id)
    if request.method == 'POST':
        Shipping_days = request.POST.get('Shipping_days')
        desc = request.POST.get('desc')
        Cost = request.POST.get('Cost')
        actt = request.POST.get('actt')
        b.Shipping_days = Shipping_days
        b.Shipping_description = desc
        b.Shipping_cost = Cost
        b.Status = actt
        b.save()

        try:
            b = Conveyance_fees.objects.all()
            return render(request, 'view_ship.html', {'b': b,'msg':'Shipping details edited'})
        except:
            return render(request, 'view_ship.html')
    return render(request, 'edit_ship.html', {'b': b,'msg':'Shipping details edited'})

def delete_ship(request, id):
    id = int(id)
    kj = Conveyance_fees.objects.get(id=id)
    kj.Shipping_days = 0
    kj.Shipping_description = ''
    kj.Shipping_cost = 0
    kj.save()

    try:
        b = Conveyance_fees.objects.all()
        return render(request, 'view_ship.html', {'b': b})
    except:
        return render(request, 'view_ship.html')



def pre_orders(request):
    if request.method == 'POST':
        status = request.POST.getlist('status')
        idd = request.POST.getlist('idd')
        idm = []
        for i in idd:
            n = int(i)
            idm.append(n)
        st_id = zip(idd,status)
        for k,j in st_id:
            try:
                f = Pre_order.objects.get(id = k)
                f.Order_status = j
                f.save()
            except:
                try:
                    b = Pre_order.objects.all()
                    return render(request, 'view_pre_order.html', {'b': b})
                except:
                    return render(request, 'view_pre_order.html')

    try:
        b = Pre_order.objects.all()
        return render(request, 'view_pre_order.html', {'b': b})
    except:
        return render(request, 'view_pre_order.html')


def delete_pre_orders(request):
    prr = Pre_order.objects.all()
    return render(request,'delete_pre_orders.html',{'prr':prr})

def delete_pre_orderss(request, id):
    Pre_order.objects.get(id=id).delete()
    prr = Pre_order.objects.all()
    return render(request, 'delete_pre_orders.html', {'prr':prr})



def band_cust_orders(request):
    if request.method == 'POST':
        status = request.POST.getlist('status')
        idd = request.POST.getlist('idd')
        idm = []
        for i in idd:
            n = int(i)
            idm.append(n)
        st_id = zip(idm,status)
        for k,j in st_id:
            try:
                f = Band_order.objects.get(id = k)
                f.Order_status = j
                f.save()
            except:
                try:
                    b = Band_order.objects.all()
                    return render(request, 'view_band_order.html', {'b': b})
                except:
                    return render(request, 'view_band_order.html')

    try:
        b = Band_order.objects.all()
        mm = Band_details.objects.all()
        return render(request, 'view_band_order.html', {'b': b,'mm':mm})
    except:
        return render(request, 'view_band_order.html')


def delete_band_cust_orders(request):
    prr = Band_order.objects.all()
    mm = Band_details.objects.all()
    return render(request, 'delete_band_cust_orders.html', {'prr': prr,'mm':mm})

def delete_cust_band_orders(request, id):
    Band_order.objects.get(id=id).delete()
    prr = Band_order.objects.all()
    mm = Band_details.objects.all()
    return render(request, 'delete_band_cust_orders.html', {'prr':prr,'mm':mm})



def quott_req(request):
    if request.method == 'POST':
        status = request.POST.getlist('status')
        idd = request.POST.getlist('idd')
        idm = []
        for i in idd:
            n = int(i)
            idm.append(n)
        st_id = zip(idm,status)
        for k,j in st_id:
            try:
                f = Quotation_cus.objects.get(id = k)
                f.Status = j
                f.save()
            except:
                try:
                    b = Quotation_cus.objects.all()
                    return render(request,'quott_req.html',{'b':b})
                except:
                    return render(request,'quott_req.html')

    try:
        b = Quotation_cus.objects.all()
        return render(request, 'quott_req.html', {'b': b})
    except:
        return render(request, 'quott_req.html')


def del_quot(request):
    wr = Quotation_cus.objects.all()
    return render(request,'del_quot.html',{'wr':wr})


def del_qtt(request, id):
    Quotation_cus.objects.get(id = id).delete()
    wr = Quotation_cus.objects.all()
    return render(request, 'del_quot.html', {'wr': wr})


def quott_disc(request, id):
    id = int(id)
    g = Category_product.objects.get(id=id)
    if request.method == 'POST':
        min_q = request.POST.get('min_q')
        max_q = request.POST.get('max_q')
        dis_p = request.POST.get('dis_p')
        actt = request.POST.get('actt')
        try:
            m = Quotation.objects.get(catt=g)
            m.Category_name = g.Category_name
            m.Minimum_quantity = min_q
            m.Maximum_quantity = max_q
            m.Discount_percent = dis_p
            m.Status = actt
            m.catt = g
            m.save()
            dd = Category_product.objects.all()
            idd = []
            ds = []
            for i in dd:
                if i.Category_name not in ds:
                    ds.append(i.Category_name)
                    idd.append(i.id)
            d = zip(idd, ds)
            k = zip(idd, ds)
            zx = zip(idd, ds)
            kf = zip(idd, ds)
            return render(request, 'ADMIN_HOME.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf,'msg':'Quotation discount edited'})
        except:
            m = Quotation()
            m.Category_name = g.Category_name
            m.Minimum_quantity = min_q
            m.Maximum_quantity = max_q
            m.Discount_percent = dis_p
            m.Status = actt
            m.catt = g
            m.save()
            dd = Category_product.objects.all()
            idd = []
            ds = []
            for i in dd:
                if i.Category_name not in ds:
                    ds.append(i.Category_name)
                    idd.append(i.id)
            d = zip(idd, ds)
            k = zip(idd, ds)
            zx = zip(idd, ds)
            kf = zip(idd, ds)
            return render(request, 'ADMIN_HOME.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf,'msg':'Quotation discount added'})
    return render(request,'quott_disc.html',{'g':g})


def customers(request):
    rt = Registration.objects.exclude(Email = 'jaysweljay@gmail.com')
    return render(request,'customers.html',{'rt':rt})

def block_cust(request, id):
    rt = Registration.objects.get(id=id)
    rt.Lock = 'blocked'
    rt.save()
    rt = Registration.objects.exclude(Email = 'jaysweljay@gmail.com')
    return render(request, 'customers.html', {'rt': rt})

def open_cust(request, id):
    rt = Registration.objects.get(id=id)
    rt.Lock = 'opened'
    rt.save()
    rt = Registration.objects.exclude(Email = 'jaysweljay@gmail.com')
    return render(request, 'customers.html', {'rt': rt})

def g_m(request):
    bb = Feedback.objects.all()
    return render(request,'guest_message.html',{'bb':bb})

def delete_g_msg(request,id):
    Feedback.objects.get(id=id).delete()
    bb = Feedback.objects.all()
    return render(request, 'guest_message.html',{'bb':bb,'msg':'Message deleted'})



def abb(request):
    amm = Registration.objects.get(Email = 'jaysweljay@gmail.com')
    if request.method == 'POST':
        abbt = request.POST.get('abbt')
        idd = request.POST.get('idd')
        try:
            adc = Registration.objects.get(id = idd)
            adc.About = abbt
            adc.save()

            dd = Category_product.objects.all()
            idd = []
            ds = []
            for i in dd:
                if i.Category_name not in ds:
                    ds.append(i.Category_name)
                    idd.append(i.id)
            d = zip(idd, ds)
            k = zip(idd, ds)
            zx = zip(idd, ds)
            kf = zip(idd, ds)
            return render(request, 'ADMIN_HOME.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf,'msg':'Content added'})
        except:
            adc = About()
            adc.About = abbt
            adc.save()
            dd = Category_product.objects.all()
            idd = []
            ds = []
            for i in dd:
                if i.Category_name not in ds:
                    ds.append(i.Category_name)
                    idd.append(i.id)
            d = zip(idd, ds)
            k = zip(idd, ds)
            zx = zip(idd, ds)
            kf = zip(idd, ds)
            return render(request, 'ADMIN_HOME.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf,'msg':'Content added'})
    return render(request,'about_content.html',{'amm':amm})


def logout(request):
    if 'user_id' in request.session:
        del request.session["user_id"]
        return render(request,'HOME.html')
    return render(request, 'HOME.html')


def delete_quot(request, id):
    id = int(id)
    g = Category_product.objects.get(id=id)
    try:
        m = Quotation.objects.get(catt = g)
    except:

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        return render(request, 'ADMIN_HOME.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf,'msg':'No quotation discount added for the specified category'})
    return render(request, 'delete_quot.html', {'g': g,'m':m})



def delete_quotm(request, id):
    Quotation.objects.get(id = id).delete()
    dd = Category_product.objects.all()
    idd = []
    ds = []
    for i in dd:
        if i.Category_name not in ds:
            ds.append(i.Category_name)
            idd.append(i.id)
    d = zip(idd, ds)
    k = zip(idd, ds)
    zx = zip(idd, ds)
    kf = zip(idd, ds)
    return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf,'msg':'Discount given for the category has been removed'})



def faq(request):
    se = Faq.objects.all()
    dd = Registration.objects.get(id = request.session['user_id'])
    if request.method == 'POST':
        text_feed = request.POST.get('text_feed')
        ss = Faq()
        a = str(dd.First_name)
        b = str(dd.Last_name)
        ss.Customer_name = a+' '+b
        ss.Customer_email = dd.Email
        ss.Question = text_feed
        ss.Answer = "To be expected soon"
        ss.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        return render(request, 'customerHOME.html', {'d': d, 'k': k,'msg':'Please wait for reply'})
    return render(request, 'faq.html', {'se': se})











def customer_home(request):
    dd = Category_product.objects.all()
    idd = []
    ds = []
    for i in dd:
        if i.Category_name not in ds:
            ds.append(i.Category_name)
            idd.append(i.id)
    d = zip(idd,ds)
    k = zip(idd, ds)
    return render(request, 'customerHOME.html', {'d': d,'k':k})

def view_cus_band_orders(request):
    n = Registration.objects.get(id = request.session["user_id"])
    b = Band_order.objects.filter(Email = n.Email)
    mm = Band_details.objects.all()
    return render(request,'view_cus_band_orders.html',{'b':b,'mm':mm})

def view_quotations_cust(request):
    n = Registration.objects.get(id=request.session["user_id"])
    b = Quotation_cus.objects.filter(Customer_email = n.Email)
    return render(request, 'view_quotations_cust.html',{'b':b})


def view_pre_cus_ord(request, id):
    id = str(id)
    n = Registration.objects.get(id = request.session["user_id"])
    try:
        b = Pre_order.objects.filter(Email = n.Email, Category_name = id)
        gf = str()
        for i in b:
            gf = i.Category_name
            break
        return render(request, 'view_pre_cus_ord.html', {'b': b,'gf':gf})
    except:
        return render(request, 'view_pre_cus_ord.html')


def my_prof(request):
    rt = Registration.objects.get(id = request.session['user_id'])
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')
        psw = request.POST.get('psw')
        Lok = request.POST.get('lok')
        rt.First_name = first_name
        rt.Last_name = last_name
        rt.Email = email
        rt.Password = psw
        rt.State = state
        rt.City = city
        rt.Pincode = pincode
        rt.Address = address
        rt.Phone = phone
        rt.Lock = Lok
        rt.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        return render(request, 'customerHOME.html', {'d': d, 'k': k,'msg':'Updated profile'})
    return render(request, 'my_prof.html', {'rt': rt})


def quott(request):
    b_det = Band_details.objects.all()
    b_st = []
    act = []
    b_s = []
    act1 = []
    f_nam = []
    act2 = []
    ght = zip(f_nam, act2)
    clip = []
    clip_img = []
    cll = zip(clip, clip_img)
    pricd = []

    for g in b_det:
        if (g.Style not in b_st) and (g.Style != ''):
            b_st.append(g.Style)
            act.append(g.Status)
        if (g.Size_in_inch not in b_s) and (g.Size_in_inch != 0):
            b_s.append(g.Size_in_inch)
            act1.append(g.Status)
        if (g.Font_name not in f_nam) and (g.Font_name != ''):
            f_nam.append(g.Font_name)
            act2.append(g.Status)
        if (g.Clipart_name not in clip) and (g.Clipart_name != ''):
            clip.append(g.Clipart_name)
        if (g.Clipart_image not in clip) and (g.Clipart_image != ''):
            clip_img.append(g.Clipart_image)
        if (g.Unit_price not in pricd) and (g.Unit_price != 0):
            pricd.append(g.Unit_price)
    bb_det = zip(b_s, b_st, pricd)
    jkj = Quotation.objects.all()

    deli = Conveyance_fees.objects.all()
    dd = Registration.objects.get(id = request.session["user_id"])
    if request.method == 'POST':
        catgo = request.POST.get('catgo')
        descript = request.POST.get('descript')
        qty = request.POST.get('qty')
        a = str(dd.First_name)
        c = str(dd.Last_name)
        b = Quotation_cus()
        b.Customer_name = a + ' ' + c
        b.Customer_email = dd.Email
        b.Category_name = catgo
        b.Description = descript
        b.Quantity_selected = qty
        b.Status = "To be expected"
        b.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        return render(request, 'customerHOME.html', {'d': d, 'k': k,'msg':'Quotation sent'})
    else:
        return render(request, 'quott.html', {'ght':ght,'bb_det':bb_det,'cll':cll,'b_s': b_s, 'b_st': b_st,'clip': clip, 'deli': deli,'jkj':jkj})


def price_chart(request):
    band_pr = Band_details.objects.all()
    quo_pr = Quotation.objects.filter(Status = 'Active')
    Categories = Category_product.objects.filter(Status = 'Active')
    Del_ch = Conveyance_fees.objects.filter(Status = 'Active')
    ship_cost = Conveyance_fees.objects.filter(Status = 'Active')
    return render(request,'price_chart.html',{'band_pr':band_pr,'quo_pr':quo_pr,'Categories':Categories,'Del_ch':Del_ch,'ship_cost':ship_cost})


def view_all_products(request):
    kr = Category_product.objects.all()
    gr = []
    idd = []
    st = []
    for t in kr:
        if t.Category_name not in gr:
            gr.append(t.Category_name)
            idd.append(t.id)
            st.append(t.Status)
    rr = zip(idd,gr,st)
    return render(request,'view_all_products.html',{'rr':rr})

def quott1(request):
    catg = request.POST.get('catg')
    pro = Category_product.objects.filter(Category_name = catg)
    return render(request,'quott1.html',{'pro':pro})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        t_a = request.POST.get('t_a')
        g = Feedback()
        g.Name = name
        g.Email = email
        g.Content = t_a
        g.Category = 'Guest'
        g.save()
        return render(request,'HOME.html',{'msg':'Message sent'})
    return render(request,'contact.html')

def about(request):
    df = Registration.objects.get(Email = 'jaysweljay@gmail.com')
    bn = Category_product.objects.all()
    return render(request,'about.html',{'df':df,'bn':bn})

def home(request):
    return render(request, 'HOME.html')


def addcategory(request):
    if request.method == 'POST':
        cat = request.POST.get('cat')
        actt = request.POST.get('actt')
        a = Category_product()
        a.Product_name = ''
        a.Product_image = ''
        a.Minimum_quantity = 0
        a.Maximum_quantity = 0
        a.Discount_percentage = 0
        a.Unit_price = 0
        a.Category_name = cat
        a.Status = actt
        a.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        return render(request, 'ADMIN_HOME.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf,'msg':'New category added'})
    return render(request, 'new_category.html')

def viewcategory(request):

    try:
        bb = Category_product.objects.all()
        idd = []
        c_n = []
        st = []
        for w in bb:
            if (w.Category_name not in c_n):
                idd.append(w.id)
                c_n.append(w.Category_name)
                st.append(w.Status)
        b = zip(idd,c_n,st)
        return render(request,'view_category.html',{'b':b})
    except:
        return render(request,'view_category.html')



def edit_category(request, id):
    id = int(id)
    b = Category_product.objects.get(id=id)
    if request.method == 'POST':
        cat = request.POST.get('cat')
        huh = Category_product.objects.exclude(id=id)
        for i in huh:
            if i.Category_name == cat:
                try:
                    bb = Category_product.objects.all()
                    idd = []
                    c_n = []
                    st = []
                    for w in bb:
                        if (w.Category_name not in c_n):
                            idd.append(w.id)
                            c_n.append(w.Category_name)
                            st.append(w.Status)
                    b = zip(idd, c_n, st)
                    return render(request, 'view_category.html', {'b': b,'msg':'Category already exists'})
                except:
                    return render(request, 'view_category.html', {'msg':'Category already exists'})
        actt = request.POST.get('actt')
        b.Category_name = cat
        b.Product_name = ''
        b.Product_image = ''
        b.Unit_price = 0
        b.Status = actt
        b.save()

        try:
            bb = Category_product.objects.all()
            idd = []
            c_n = []
            st = []
            for w in bb:
                if (w.Category_name not in c_n):
                    idd.append(w.id)
                    c_n.append(w.Category_name)
                    st.append(w.Status)
            b = zip(idd, c_n, st)
            return render(request, 'view_category.html', {'b': b,'msg':'Category edited'})
        except:
            return render(request, 'view_category.html')
    return render(request, 'edit_category.html', {'b': b})


def delete_category(request, id):
    Category_product.objects.get(id=id).delete()
    try:
        bb = Category_product.objects.all()
        idd = []
        c_n = []
        st = []
        for w in bb:
            if (w.Category_name not in c_n):
                idd.append(w.id)
                c_n.append(w.Category_name)
                st.append(w.Status)
        b = zip(idd,c_n,st)
        return render(request, 'view_category.html', {'b': b,'msg':'Category removed'})
    except:
        return render(request, 'view_category.html')


def nfs(request):
    if request.method == 'POST':
        font = request.POST.get('font')
        actt = request.POST.get('actt')
        cv = Band_details.objects.all()
        for i in cv:
            k = str(i.Font_name)
            if k == str(font):
                return render(request, "new_font_style.html", {'msg':'Font style already exists'})
        a = Band_details()
        a.Size_in_inch = 0.0
        a.Style = ''
        a.Clipart_name = ''
        a.Clip_image = ''
        a.Font_name = font
        a.Minimum_quantity = 0
        a.Maximum_quantity = 0
        a.Discount_percentage = 0.0
        a.Unit_price = 0
        a.Status = actt
        a.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf, 'msg':'New font style added'})
    return render(request, 'new_font_style.html')



def view_font_style(request):
    try:
        bb = Band_details.objects.all()
        idd = []
        sii = []
        st = []
        for w in bb:
            if (w.Font_name not in sii) and (w.Font_name != ''):
                idd.append(w.id)
                sii.append(w.Font_name)
                st.append(w.Status)
        b = zip(idd, sii, st)
        return render(request, 'view_font_style.html', {'b': b})
    except:
        return render(request, 'view_font_style.html')


def new_band_size(request):
    if request.method == 'POST':
        band_size = request.POST.get('band_size')
        actt = request.POST.get('actt')
        cv = Band_details.objects.all()
        for i in cv:
            k = float(i.Size_in_inch)
            if k == float(band_size):
                return render(request, "new_band_size.html", {'msg':'Band size already exists'})
        a = Band_details()
        a.Size_in_inch = band_size
        a.Style = ''
        a.Clipart_name = ''
        a.Clip_image = ''
        a.Font_name = ''
        a.Minimum_quantity = 0
        a.Maximum_quantity = 0
        a.Discount_percentage = 0.0
        a.Unit_price = 0
        a.Status = actt
        a.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf, 'msg':'New font style added'})
    return render(request, 'new_band_size.html')


def view_band_size(request):
    try:
        bb = Band_details.objects.all()
        idd = []
        sii = []
        st = []
        for w in bb:
            if (w.Size_in_inch not in sii) and (w.Size_in_inch != 0):
                idd.append(w.id)
                sii.append(w.Size_in_inch)
                st.append(w.Status)
        b = zip(idd,sii,st)
        return render(request, 'view_band_size.html',{'b':b})
    except:
        return render(request, 'view_band_size.html')



def delete_font_style(request, id):
    id = int(id)
    kj = Band_details.objects.get(id=id)
    kj.Font_name = ''
    kj.save()

    try:
        bb = Band_details.objects.all()
        idd = []
        sii = []
        st = []
        for w in bb:
            if (w.Font_name not in sii) and (w.Font_name != ''):
                idd.append(w.id)
                sii.append(w.Font_name)
                st.append(w.Status)
        b = zip(idd, sii, st)
        return render(request, 'view_font_style.html', {'b': b, 'msg':'Font style deleted'})
    except:
        return render(request, 'view_font_style.html')




def edit_font_style(request, id):
    id = int(id)
    b = Band_details.objects.get(id = id)
    if request.method == 'POST':
        font = request.POST.get('font')
        huh = Band_details.objects.exclude(id=id)
        for i in huh:
            if i.Font_name == font:
                try:
                    bb = Band_details.objects.all()
                    idd = []
                    sii = []
                    st = []
                    for w in bb:
                        if (w.Font_name not in sii) and (w.Font_name != ''):
                            idd.append(w.id)
                            sii.append(w.Font_name)
                            st.append(w.Status)
                    b = zip(idd, sii, st)
                    return render(request, 'view_font_style.html', {'b': b, 'msg':'Font style deleted'})
                except:
                    return render(request, 'view_font_style.html', {'msg':'Font style deleted'})
        actt = request.POST.get('actt')
        b.Font_name = font
        b.Status = actt
        b.save()

        try:
            bb = Band_details.objects.all()
            idd = []
            sii = []
            st = []
            for w in bb:
                if (w.Font_name not in sii) and (w.Font_name != ''):
                    idd.append(w.id)
                    sii.append(w.Font_name)
                    st.append(w.Status)
            b = zip(idd, sii, st)
            return render(request, 'view_font_style.html', {'b': b, 'msg':'Font style deleted'})
        except:
            return render(request, 'view_font_style.html', {'msg':'Font style deleted'})
    return render(request, 'edit_font_style.html', {'b': b})


def nbs(request):
    if request.method == 'POST':
        band_style = request.POST.get('band_style')
        actt = request.POST.get('actt')
        cv = Band_details.objects.all()
        for i in cv:
            k = str(i.Style)
            if k == str(band_style):
                return render(request, "new_band_style.html", {'msg':'New font style added'})
        a = Band_details()
        a.Size_in_inch = 0
        a.Style = band_style
        a.Clipart_name = ''
        a.Clip_image = ''
        a.Font_name = ''
        a.Minimum_quantity = 0
        a.Maximum_quantity = 0
        a.Discount_percentage = 0.0
        a.Unit_price = 0
        a.Status = actt
        a.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf,'msg':'New font style added'})
    return render(request,'new_band_style.html')


def view_band_style(request):

    try:
        bb = Band_details.objects.all()
        idd = []
        sii = []
        st = []
        for w in bb:
            if (w.Style not in sii) and (w.Style != ''):
                idd.append(w.id)
                sii.append(w.Style)
                st.append(w.Status)
        b = zip(idd,sii,st)
        return render(request, 'view_band_style.html',{'b':b})
    except:
        return render(request, 'view_band_style.html')

def new_clipart(request):
    if request.method == 'POST':
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        fs.save(photo.name, photo)
        clippart = request.POST.get('clippart')
        actt = request.POST.get('actt')

        cv = Band_details.objects.all()
        for i in cv:
            k = str(i.Clipart_name)
            if k == str(clippart):
                return render(request, "new_clipart.html",{'msg':'New font style added'})

        a = Band_details()
        a.Size_in_inch = 0
        a.Style = ''
        a.Clipart_name = clippart
        a.Clipart_image = photo
        a.Font_name = ''
        a.Minimum_quantity = 0
        a.Maximum_quantity = 0
        a.Discount_percentage = 0.0
        a.Unit_price = 0
        a.Status = actt
        a.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf,'msg':'New clipart added'})
    return render(request, 'new_clipart.html')

def view_clipart(request):

    try:
        bb = Band_details.objects.all()
        idd = []
        sii = []
        st = []
        for w in bb:
            if (w.Clipart_name not in sii) and (w.Clipart_name != ''):
                idd.append(w.id)
                sii.append(w.Clipart_name)
                st.append(w.Clipart_image)
        b = zip(idd,sii,st)
        return render(request, 'view_clipart.html',{'b':b})
    except:
        return render(request, 'view_clipart.html')


def delete_clipart(request, id):
    id = int(id)
    kj = Band_details.objects.get(id=id)
    kj.Clipart_name = ''
    kj.Clipart_image = ''
    kj.save()


    try:
        bb = Band_details.objects.all()
        idd = []
        sii = []
        st = []
        for w in bb:
            if (w.Clipart_name not in sii) and (w.Clipart_name != ''):
                idd.append(w.id)
                sii.append(w.Clipart_name)
                st.append(w.Clipart_image)
        b = zip(idd,sii,st)
        return render(request, 'view_clipart.html',{'b':b,'msg':'New clipart added'})
    except:
        return render(request, 'view_clipart.html')

def edit_band_size(request, id):
    id = int(id)
    b = Band_details.objects.get(id=id)
    if request.method == 'POST':
        bandd_size = request.POST.get('bandd_size')
        actt = request.POST.get('actt')
        b.Size_in_inch = bandd_size
        b.Status = actt
        b.save()

        try:
            bb = Band_details.objects.all()
            idd = []
            sii = []
            st = []
            for w in bb:
                if (w.Size_in_inch not in sii) and (w.Size_in_inch != 0):
                    idd.append(w.id)
                    sii.append(w.Size_in_inch)
                    st.append(w.Status)
            b = zip(idd, sii, st)
            return render(request, 'view_band_size.html', {'b': b,'msg':'Band size edited'})
        except:
            return render(request, 'view_band_size.html')
    return render(request, 'edit_band_size.html', {'b': b})


def delete_band_size(request, id):
    id = int(id)
    jk = Band_details.objects.get(id=id)
    jk.Size_in_inch = 0
    jk.save()
    try:
        bb = Band_details.objects.all()
        idd = []
        sii = []
        st = []
        for w in bb:
            if (w.Size_in_inch not in sii) and (w.Size_in_inch != 0):
                idd.append(w.id)
                sii.append(w.Size_in_inch)
                st.append(w.Status)
        b = zip(idd,sii,st)
        return render(request, 'view_band_size.html',{'b':b,'msg':'Band size edited'})
    except:
        return render(request, 'view_band_size.html')


def nbs(request):
    if request.method == 'POST':
        band_style = request.POST.get('band_style')
        actt = request.POST.get('actt')
        cv = Band_details.objects.all()
        for i in cv:
            k = str(i.Style)
            if k == str(band_style):
                return render(request, "new_band_style.html",{'msg':'Band size edited'})
        a = Band_details()
        a.Size_in_inch = 0
        a.Style = band_style
        a.Clipart_name = ''
        a.Clip_image = ''
        a.Font_name = ''
        a.Minimum_quantity = 0
        a.Maximum_quantity = 0
        a.Discount_percentage = 0.0
        a.Unit_price = 0
        a.Status = actt
        a.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf,'msg':'Band style added'})
    return render(request,'new_band_style.html')



def edit_band_style(request, id):
    id = int(id)
    b = Band_details.objects.get(id=id)
    if request.method == 'POST':
        bandd_style = request.POST.get('bandd_style')
        actt = request.POST.get('actt')
        b.Style = bandd_style
        b.Status = actt
        b.save()

        try:
            bb = Band_details.objects.all()
            idd = []
            sii = []
            st = []
            for w in bb:
                if (w.Style not in sii) and (w.Style != ''):
                    idd.append(w.id)
                    sii.append(w.Style)
                    st.append(w.Status)
            b = zip(idd, sii, st)
            return render(request, 'view_band_style.html', {'b': b,'msg':'Band style added'})
        except:
            return render(request, 'view_band_style.html')
    return render(request, 'edit_band_style.html', {'b': b})



def delete_band_style(request, id):

    id = int(id)
    kj = Band_details.objects.get(id=id)
    kj.Style = ''
    kj.save()

    try:
        bb = Band_details.objects.all()
        idd = []
        sii = []
        st = []
        for w in bb:
            if (w.Style not in sii) and (w.Style != ''):
                idd.append(w.id)
                sii.append(w.Style)
                st.append(w.Status)
        b = zip(idd,sii,st)
        return render(request, 'view_band_style.html',{'b':b,'msg':'Band style added'})
    except:
        return render(request, 'view_band_style.html')



def new_price(request):
    bsi = Band_details.objects.all()
    b_s = []
    b_st = []
    for y in bsi:
        if (y.Size_in_inch not in b_s) and (y.Size_in_inch != 0):
            b_s.append(y.Size_in_inch)
        if (y.Style not in b_st) and (y.Style != ''):
            b_st.append(y.Style)

    if request.method == 'POST':
        bd_s = request.POST.get('bd_s')
        bd_st = request.POST.get('bd_st')
        mi_qq = request.POST.get('mi_q')
        ma_qq = request.POST.get('ma_q')
        pricee = request.POST.get('price')
        discc = request.POST.get('disc')
        acttt = request.POST.get('actt')
        a = Band_details()
        a.Style = bd_st
        a.Size_in_inch = bd_s
        a.Clipart_name = ''
        a.Clipart_image = ''
        a.Font_name = ''
        a.Maximum_quantity = ma_qq
        a.Minimum_quantity = mi_qq
        a.Discount_percentage = discc
        a.Unit_price = pricee
        a.Status = acttt
        a.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf,'msg':'Band style added'})
    return render(request, 'new_price.html',{'b_s':b_s,'b_st':b_st})


def view_price(request):
    try:
        bb = Band_details.objects.all()
        idd = []
        stt = []
        sii = []
        maxx = []
        minn = []
        pricc = []
        disc = []
        st = []
        for w in bb:
            if (w.Style != '') and (w.Unit_price != 0):
                idd.append(w.id)
                stt.append(w.Style)
                sii.append(w.Size_in_inch)
                maxx.append(w.Maximum_quantity)
                minn.append(w.Minimum_quantity)
                pricc.append(w.Unit_price)
                disc.append(w.Discount_percentage)
                st.append(w.Status)
        b = zip(idd, stt, sii, minn, maxx, pricc, disc)
        return render(request, 'view_band_price.html', {'b': b})
    except:
        return render(request, 'view_band_price.html')


def edit_band_price(request, id):
    id = int(id)
    b = Band_details.objects.get(id = id)
    if request.method == 'POST':
        bs = request.POST.get('bs')
        bst = request.POST.get('bst')
        Maximum_quantity = request.POST.get('Maximum_quantity')
        Minimum_quantity = request.POST.get('Minimum_quantity')
        price = request.POST.get('price')
        disc = request.POST.get('disc')
        actt = request.POST.get('actt')
        b.Size_in_inch = bs
        b.Style = bst
        b.Minimum_quantity = Minimum_quantity
        b.Maximum_quantity = Maximum_quantity
        b.Unit_price = price
        b.Discount_percentage = disc
        b.Status = actt
        b.save()
        try:
            bb = Band_details.objects.all()
            idd = []
            stt = []
            sii = []
            maxx = []
            minn = []
            pricc = []
            disc = []
            st = []
            for w in bb:
                if (w.Style != '') and (w.Unit_price != 0):
                    idd.append(w.id)
                    stt.append(w.Style)
                    sii.append(w.Size_in_inch)
                    maxx.append(w.Maximum_quantity)
                    minn.append(w.Minimum_quantity)
                    pricc.append(w.Unit_price)
                    disc.append(w.Discount_percentage)
                    st.append(w.Status)
            b = zip(idd, stt, sii, minn, maxx, pricc, disc)
            return render(request, 'view_band_price.html', {'b': b,'msg':'Band style added'})
        except:
            return render(request, 'view_band_price.html')
    return render(request, 'edit_band_price.html',{'b':b,'msg':'Band style added'})



def delete_band_price(request, id):
    id = int(id)
    kj = Band_details.objects.get(id=id)
    kj.Minimum_quantity = 0
    kj.Maximum_quantity = 0
    kj.Discount_percentage = 0
    kj.Unit_price = 0
    kj.save()
    try:
        bb = Band_details.objects.all()
        idd = []
        stt = []
        sii = []
        maxx = []
        minn = []
        pricc = []
        disc = []
        st = []
        for w in bb:
            if (w.Style != '') and (w.Unit_price != 0):
                idd.append(w.id)
                stt.append(w.Style)
                sii.append(w.Size_in_inch)
                maxx.append(w.Maximum_quantity)
                minn.append(w.Minimum_quantity)
                pricc.append(w.Unit_price)
                disc.append(w.Discount_percentage)
                st.append(w.Status)
        b = zip(idd, stt, sii, minn, maxx, pricc, disc)
        return render(request, 'view_band_price.html', {'b': b})
    except:
        return render(request, 'view_band_price.html')




def add_product(request, id):
    id = int(id)
    c = Category_product.objects.get(id = id)
    if request.method == 'POST':
        nam = request.POST.get('nam')
        cv = Category_product.objects.all()
        for i in cv:
            k = str(i.Product_name)
            if k == str(nam):
                return render(request, 'add_product.html',{'c':c,'msg':'Band style added'})
        min_q = request.POST.get('min_q')
        max_q = request.POST.get('max_q')
        disc = request.POST.get('disc')
        price = request.POST.get('price')
        actt = request.POST.get('actt')
        photo1 = request.FILES['photo1']
        fs = FileSystemStorage()
        fs.save(photo1.name, photo1)
        b = Category_product()
        b.Category_name = c.Category_name
        b.Product_image = photo1
        b.Product_name = nam
        b.Minimum_quantity = min_q
        b.Maximum_quantity = max_q
        b.Discount_percentage = disc
        b.Unit_price = price
        b.Status = actt
        b.save()

        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf,'msg':'Band style added'})
    return render(request, 'add_product.html',{'c':c})



def view_product(request, id):
    id = str(id)
    request.session["cat_id"] = id
    z = Category_product.objects.filter(Category_name=request.session["cat_id"]).exclude(Product_name='')
    zz = str()
    for p in z:
        zz += p.Category_name
        zz = str(zz)
        zz = zz.upper()
        request.session["ctt_name"] = zz
        break
    try:
        n = Category_product.objects.filter(Category_name = request.session["cat_id"]).exclude(Product_name = '')
        return render(request, 'view_product.html',{'n':n,'zz':zz})
    except:
        return render(request, 'view_product.html')



def edit_product(request, id):
    zz = request.session["ctt_name"]
    b = Category_product.objects.get(id=id)
    if request.method == 'POST':
        pro_n = request.POST.get('pro_n')
        pro_p = request.POST.get('pro_p')
        min_q = request.POST.get('min_q')
        max_q = request.POST.get('max_q')
        disc = request.POST.get('disc')
        huh = Category_product.objects.exclude(id=id)
        for i in huh:
            if i.Product_name == pro_n:
                z = Category_product.objects.filter(Category_name=request.session["cat_id"]).exclude(Product_name='')
                zz = str()
                for p in z:
                    zz += p.Category_name
                    zz = str(zz)
                    zz = zz.upper()
                    request.session["ctt_name"] = zz
                    break
                try:
                    n = Category_product.objects.filter(Category_name=request.session["cat_id"]).exclude(Product_name='')
                    return render(request, 'view_product.html', {'n': n, 'zz': zz,'msg':'Band style added'})
                except:
                    return render(request, 'view_product.html',{'msg':'Band style added'})
        b.Product_name = pro_n
        b.Unit_price = pro_p
        b.Minimum_quantity = min_q
        b.Maximum_quantity = max_q
        b.Discount_percentage = disc
        b.save()
        try:
            n = Category_product.objects.filter(Category_name = request.session["cat_id"]).exclude(Product_name = '')
            return render(request, 'view_product.html', {'n': n,'zz':zz,'msg':'Band style added'})
        except:
            return render(request, 'view_product.html')
    return render(request, 'edit_product.html', {'b': b,'zz':zz})



def delete_product(request, id):
    zz = request.session["ctt_name"]
    Category_product.objects.get(id = id).delete()
    try:
        n = Category_product.objects.filter(Category_name = request.session["cat_id"]).exclude(Product_name = '')
        return render(request, 'view_product.html', {'n': n,'zz':zz})
    except:
        return render(request, 'view_product.html')



def del_faq(request):
    v = Faq.objects.all()
    return render(request,'del_faq.html',{'v':v})

def delete_faq(request, id):
    Faq.objects.get(id = id).delete()
    v = Faq.objects.all()
    return render(request, 'del_faq.html', {'v': v})

def feedbak(request):
    se = Feedback.objects.all()
    return render(request,'feedbak.html',{'se':se})

def delete_feedback(request, id):
    Feedback.objects.get(id=id).delete()
    se = Feedback.objects.all()
    return render(request, 'feedbak.html', {'se': se})

def faqs(request):
    se = Faq.objects.all()
    if request.method == 'POST':
        text_ques = request.POST.getlist('text_ques')
        text_answ = request.POST.getlist('text_answ')
        cus_name = request.POST.getlist('cus_name')
        Customer_email = request.POST.getlist('Customer_email')
        ss = Faq.objects.all()
        ft = []
        for y in ss:
            if y.id not in ft:
                ft.append(y.id)
        fb = zip(ft,cus_name, Customer_email, text_ques, text_answ)
        for m,p,i,j,k in fb:
            for e in ss:
                ty = e.id
                ty = int(ty)
                if int(m) == ty:
                    e.Customer_name = p
                    e.Customer_email = i
                    e.Question = j
                    e.Answer = k
                    e.save()
        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        zx = zip(idd, ds)
        kf = zip(idd, ds)
        return render(request, 'admin_home.html', {'d': d, 'k': k, 'zx': zx, 'kf': kf,'msg':'Band style added'})
    return render(request, 'faqs.html', {'se': se})

def del_faq(request):
    v = Faq.objects.all()
    return render(request,'del_faq.html',{'v':v})

def delete_faq(request, id):
    Faq.objects.get(id = id).delete()
    v = Faq.objects.all()
    return render(request, 'del_faq.html', {'v': v})


def feedback(request):
    dd = Registration.objects.get(id = request.session['user_id'])
    if request.method == 'POST':
        text_feed = request.POST.get('text_feed')
        qw = Feedback()
        a = str(dd.First_name)
        b = str(dd.Last_name)
        qw.Name =  a+' '+b
        qw.Email = dd.Email
        qw.Content = text_feed
        qw.Category = 'Customer'
        qw.save()
        dd = Category_product.objects.all()
        idd = []
        ds = []
        for i in dd:
            if i.Category_name not in ds:
                ds.append(i.Category_name)
                idd.append(i.id)
        d = zip(idd, ds)
        k = zip(idd, ds)
        return render(request, 'customerHOME.html', {'d': d, 'k': k,'msg':'Thank you for your valuable feedback'})
    return render(request,'feedback.html',{'dd':dd})










