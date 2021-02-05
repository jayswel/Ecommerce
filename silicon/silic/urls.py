from django.urls import path
import silic.views

urlpatterns =[
    path('',silic.views.HI, name='HI'),
    path('login',silic.views.login,name='login'),
    path('register',silic.views.register,name='register'),
    path('LoginAction',silic.views.LoginAction,name='LoginAction'),
    path('loginbcak',silic.views.loginbcak,name='loginbcak'),
    path('adminRegister',silic.views.adminRegister,name='adminRegister'),
    path('customerRegister',silic.views.customerRegister,name='customerRegister'),
    path('customerRegisterAction',silic.views.customerRegisterAction,name='customerRegisterAction'),
    path('AdminRegisterAction',silic.views.AdminRegisterAction,name='AdminRegisterAction'),
    path('insertfonts',silic.views.insertfonts,name='insertfonts'),
    path('viewfonts',silic.views.viewfonts,name='viewfonts'),
    path('insertfontaction',silic.views.insertfontaction,name='insertfontaction'),
    path('adminhome',silic.views.adminhome,name='adminhome'),
    path('about',silic.views.about,name='about'),
    path('contact',silic.views.contact,name='contact'),
    path('insertbandsize',silic.views.insertbandsize,name='insertbandsize'),
    path('viewbandsize',silic.views.viewbandsize,name='viewbandsize'),
    path('insertbandsizeaction',silic.views.insertbandsizeaction,name='insertbandsizeaction'),
    path('messagesubmitaction',silic.views.messagesubmitaction,name='messagesubmitaction'),
    path('viewmessage',silic.views.viewmessage,name='viewmessage'),
    path('updateprofile',silic.views.updateprofile,name='updateprofile'),
    path('updateAdminProfileAction', silic.views.updateAdminProfileAction, name='updateAdminProfileAction'),
    path('addcategory', silic.views.addcategory, name='addcategory'),
    path('addcategoryaction', silic.views.addcategoryaction, name='addcategoryaction'),
    path('addproductprice', silic.views.addproductprice, name='addproductprice'),
    path('addproductpriceaction', silic.views.addproductpriceaction, name='addproductpriceaction'),
    path('viewcategory', silic.views.viewcategory, name='viewcategory'),
    path('viewprice', silic.views.viewprice, name='viewprice'),
    path('addimage', silic.views.addimage, name='addimage'),
    path('insertiamgeaction', silic.views.insertiamgeaction, name='insertiamgeaction'),
    path('viewimage', silic.views.viewimage, name='viewimage'),

    path('temperory', silic.views.temperory, name='temperory'),
    path('insertfonts2', silic.views.insertfonts2, name='insertfonts2'),
    path('insertfontaction2', silic.views.insertfontaction2, name='insertfontaction2'),
    path('insertcategory2', silic.views.insertcategory2, name='insertcategory2'),
    path('insertcategoryaction2', silic.views.insertcategoryaction2, name='insertcategoryaction2'),
    path('insertsize2', silic.views.insertsize2, name='insertsize2'),
    path('insertprice2', silic.views.insertprice2, name='insertprice2'),
    path('insertsizeaction', silic.views.insertsizeaction, name='insertsizeaction'),
    path('insertpriceacton2', silic.views.insertpriceacton2, name='insertpriceacton2'),

    path('getfontstyle', silic.views.getfontstyle, name='getfontstyle'),
    path('submit', silic.views.submit, name='submit'),

    path('Product_name', silic.views.Product_name, name='Product_name'),
    path('Product_image', silic.views.Product_image, name='Product_image'),
    path('Minimum_quantity', silic.views.Minimum_quantity, name='Minimum_quantity'),
    path('Maximum_quantity', silic.views.Maximum_quantity, name='Maximum_quantity'),
    path('Discount_percentage', silic.views.Discount_percentage, name='Discount_percentage'),
    path('Unit_price', silic.views.Unit_price, name='Unit_price'),
    path('Status', silic.views.Status, name='Status'),

    path('insertproductname', silic.views.insertproductname, name='insertproductname'),
    path('insertproductimage', silic.views.insertproductimage, name='insertproductimage'),
    path('insertminimumquant', silic.views.insertminimumquant, name='insertminimumquant'),
    path('insertmaximumquantity', silic.views.insertmaximumquantity, name='insertmaximumquantity'),
    path('insertpercentage', silic.views.insertpercentage, name='insertpercentage'),
    path('insertunitprice', silic.views.insertunitprice, name='insertunitprice'),
    path('insertstatus', silic.views.insertstatus, name='insertstatus'),

    path('viewProduct_name', silic.views.viewProduct_name, name='viewProduct_name'),
    path('viewProduct_image', silic.views.viewProduct_image, name='viewProduct_image'),
    path('viewMinimum_quantity', silic.views.viewMinimum_quantity, name='viewMinimum_quantity'),
    path('viewMaximum_quantity', silic.views.viewMaximum_quantity, name='viewMaximum_quantity'),
    path('viewDiscount_percentage', silic.views.viewDiscount_percentage, name='viewDiscount_percentage'),
    path('viewUnit_price', silic.views.viewUnit_price, name='viewUnit_price'),
    path('viewStatus', silic.views.viewStatus, name='viewStatus'),
    path('home', silic.views.home, name='home'),

    path('Delivery_charge_min_km', silic.views.Delivery_charge_min_km, name='Delivery_charge_min_km'),
    path('Delivery_charge_max_km', silic.views.Delivery_charge_max_km, name='Delivery_charge_max_km'),
    path('Delivery_fees', silic.views.Delivery_fees, name='Delivery_fees'),
    path('Shipping_days', silic.views.Shipping_days, name='Shipping_days'),
    path('Shipping_description', silic.views.Shipping_description, name='Shipping_description'),
    path('Shipping_cost', silic.views.Shipping_cost, name='Shipping_cost'),
    path('convayenceStatus', silic.views.convayenceStatus, name='convayenceStatus'),

    path('Delivery_charge_min_km_action', silic.views.Delivery_charge_min_km_action, name='Delivery_charge_min_km_action'),
    path('Delivery_charge_max_km_action', silic.views.Delivery_charge_max_km_action, name='Delivery_charge_max_km_action'),
    path('insertdeliveryfees', silic.views.insertdeliveryfees, name='insertdeliveryfees'),
    path('insertshippingdays', silic.views.insertshippingdays, name='insertshippingdays'),
    path('insertshippingdesc', silic.views.insertshippingdesc, name='insertshippingdesc'),
    path('insertshippingcost', silic.views.insertshippingcost, name='insertshippingcost'),
    path('insertconayenceststus', silic.views.insertconayenceststus, name='insertconayenceststus'),

    path('viewDelivery_charge_min_km', silic.views.viewDelivery_charge_min_km, name='viewDelivery_charge_min_km'),
    path('viewDelivery_charge_max_km', silic.views.viewDelivery_charge_max_km, name='viewDelivery_charge_max_km'),
    path('viewDelivery_fees', silic.views.viewDelivery_fees, name='viewDelivery_fees'),
    path('viewShipping_days', silic.views.viewShipping_days, name='viewShipping_days'),
    path('viewShipping_description', silic.views.viewShipping_description, name='viewShipping_description'),
    path('viewShipping_cost', silic.views.viewShipping_cost, name='viewShipping_cost'),
    path('viewconvayenceStatus', silic.views.viewconvayenceStatus, name='viewconvayenceStatus'),

    path('cusselectcategory', silic.views.cusselectcategory, name='cusselectcategory'),
    path('cus_selectcategory', silic.views.cus_selectcategory, name='cus_selectcategory'),
    path('cus_selectproduct', silic.views.cus_selectproduct, name='cus_selectproduct'),
    path('addproduct', silic.views.addproduct, name='addproduct'),
    path('admin_addproduct', silic.views.admin_addproduct, name='admin_addproduct'),
    path('convayencefees', silic.views.convayencefees, name='convayencefees'),
    path('addbanddetail', silic.views.addbanddetail, name='addbanddetail'),

    path('inserstyle', silic.views.inserstyle, name='inserstyle'),
    path('viewstyle', silic.views.viewstyle, name='viewstyle'),
    path('inseclipname', silic.views.inseclipname, name='inseclipname'),
    path('viewbandname', silic.views.viewbandname, name='viewbandname'),
    path('bandimage', silic.views.bandimage, name='bandimage'),
    path('viewbandimage', silic.views.viewbandimage, name='viewbandimage'),
    path('bandminquan', silic.views.bandminquan, name='bandminquan'),
    path('viewbandminquan', silic.views.viewbandminquan, name='viewbandminquan'),
    path('bandmaxquant', silic.views.bandmaxquant, name='bandmaxquant'),
    path('viewbandmaxquant', silic.views.viewbandmaxquant, name='viewbandmaxquant'),
    path('banddiscount', silic.views.banddiscount, name='banddiscount'),
    path('viewbanddiscount', silic.views.viewbanddiscount, name='viewbanddiscount'),
    path('bandunitprice', silic.views.bandunitprice, name='bandunitprice'),
    path('viewbandunitprice', silic.views.viewbandunitprice, name='viewbandunitprice'),
    path('bandstatus', silic.views.bandstatus, name='bandstatus'),
    path('viewbandstatus', silic.views.viewbandstatus, name='viewbandstatus'),

    path('addbandstyleaction', silic.views.addbandstyleaction, name='addbandstyleaction'),
    path('addcbandclipart', silic.views.addcbandclipart, name='addcbandclipart'),
    path('insertbandimage', silic.views.insertbandimage, name='insertbandimage'),
    path('bandminquant', silic.views.bandminquant, name='bandminquant'),
    path('bandmmaxnquant', silic.views.bandmmaxnquant, name='bandmmaxnquant'),
    path('banddiscount2', silic.views.banddiscount2, name='banddiscount2'),
    path('bandunit', silic.views.bandunit, name='bandunit'),
    path('bandstatus2', silic.views.bandstatus2, name='bandstatus2'),
    path('addanewband', silic.views.addanewband, name='addanewband'),
    path('addanewbandaction', silic.views.addanewbandaction, name='addanewbandaction'),
    path('selectbandsizeaction', silic.views.selectbandsizeaction, name='selectbandsizeaction'),
    path('customizedband2', silic.views.customizedband2, name='customizedband2'),
    path('cus_customizebandaction', silic.views.cus_customizebandaction, name='cus_customizebandaction'),
    path('cusfaq', silic.views.cusfaq, name='cusfaq'),
    path('cusfaqaction', silic.views.cusfaqaction, name='cusfaqaction'),
    path('adminfaq', silic.views.adminfaq, name='adminfaq'),
    path('adminprovideanswer/<int:id>', silic.views.adminprovideanswer, name='adminprovideanswer'),
    path('cusviewfaq', silic.views.cusviewfaq, name='cusviewfaq'),
    path('cusfeedback', silic.views.cusfeedback, name='cusfeedback'),
    path('cussendfeedback', silic.views.cussendfeedback, name='cussendfeedback'),
    path('adminviewfeedback', silic.views.adminviewfeedback, name='adminviewfeedback'),
    path('adminviewquatation', silic.views.adminviewquatation, name='adminviewquatation'),
    path('adminaddquatation', silic.views.adminaddquatation, name='adminaddquatation'),
    path('adminsendquotation', silic.views.adminsendquotation, name='adminsendquotation'),

    path('cussendquotataion', silic.views.cussendquotataion, name='cussendquotataion'),
    path('cusviewquotataion', silic.views.cusviewquotataion, name='cusviewquotataion'),
    path('cussendquottation', silic.views.cussendquottation, name='cussendquottation'),

    path('dependency', silic.views.dependency, name='dependency'),
    path('viewcart', silic.views.viewcart, name='viewcart'),
    path('backtoconfigure', silic.views.backtoconfigure, name='backtoconfigure'),
    path('delete_cart/<int:id>', silic.views.delete_cart, name='delete_cart'),
    path('ckeckout', silic.views.ckeckout, name='ckeckout'),
    path('paybutton', silic.views.paybutton, name='paybutton'),


    ######################FASHION#####################
    path('fashion', silic.views.fashion, name='fashion'),
    path('checkboxaction', silic.views.checkboxaction, name='checkboxaction'),
    path('backtofashome', silic.views.backtofashome, name='backtofashome'),
    path('Registration_teacher_action', silic.views.Registration_teacher_action, name='Registration_teacher_action'),
    path('view_prdct_cus/<id>/<idg>', silic.views.view_prdct_cus, name='view_prdct_cus'),
    path('ord_product', silic.views.ord_product, name='ord_product'),
    path('Remove_order/<id>/<idm>/<idt>', silic.views.Remove_order, name='Remove_order'),
    path('ch_out', silic.views.ch_out, name='ch_out'),
    path('ch_out1', silic.views.ch_out1, name='ch_out1'),
    path('new_delivery', silic.views.new_delivery, name='new_delivery'),
    path('view_delivery', silic.views.view_delivery, name='view_delivery'),
    path('admin_home', silic.views.admin_home, name='admin_home'),
    path('edit_delivery/<id>', silic.views.edit_delivery, name='edit_delivery'),
    path('delete_delivery/<id>', silic.views.delete_delivery, name='delete_delivery'),
    path('new_ship', silic.views.new_ship, name='new_ship'),
    path('view_ship', silic.views.view_ship, name='view_ship'),
    path('edit_ship/<id>', silic.views.edit_ship, name='edit_ship'),
    path('delete_ship/<id>', silic.views.delete_ship, name='delete_ship'),
    path('pre_orders', silic.views.pre_orders, name='pre_orders'),
    path('delete_pre_orders', silic.views.delete_pre_orders, name='delete_pre_orders'),
    path('delete_pre_orderss/<id>', silic.views.delete_pre_orderss, name='delete_pre_orderss'),
    path('band_cust_orders', silic.views.band_cust_orders, name='band_cust_orders'),
    path('delete_band_cust_orders', silic.views.delete_band_cust_orders, name='delete_band_cust_orders'),
    path('delete_cust_band_orders/<id>', silic.views.delete_cust_band_orders, name='delete_cust_band_orders'),
    path('quott_req', silic.views.quott_req, name='quott_req'),
    path('del_quot', silic.views.del_quot, name='del_quot'),
    path('del_qtt/<id>', silic.views.del_qtt, name='del_qtt'),
    path('quott_disc/<id>', silic.views.quott_disc, name='quott_disc'),
    path('customers', silic.views.customers, name='customers'),
    path('block_cust/<id>', silic.views.block_cust, name='block_cust'),
    path('open_cust/<id>', silic.views.open_cust, name='open_cust'),
    path('g_m', silic.views.g_m, name='g_m'),
    path('delete_g_msg/<id>', silic.views.delete_g_msg, name='delete_g_msg'),
    path('abb', silic.views.abb, name='abb'),
    path('logout', silic.views.logout, name='logout'),
    path('quott_disc/<id>', silic.views.quott_disc, name='quott_disc'),
    path('delete_quot/<id>', silic.views.delete_quot, name='delete_quot'),
    path('delete_quotm/<id>', silic.views.delete_quotm, name='delete_quotm'),
    path('customer_home', silic.views.customer_home, name='customer_home'),
    path('view_cus_band_orders', silic.views.view_cus_band_orders, name='view_cus_band_orders'),
    path('view_quotations_cust', silic.views.view_quotations_cust, name='view_quotations_cust'),
    path('view_pre_cus_ord/<id>', silic.views.view_pre_cus_ord, name='view_pre_cus_ord'),
    path('my_prof', silic.views.my_prof, name='my_prof'),
    path('quott', silic.views.quott, name='quott'),
    path('price_chart', silic.views.price_chart, name='price_chart'),
    path('view_all_products', silic.views.view_all_products, name='view_all_products'),
    path('quott1', silic.views.quott1, name='quott1'),
    path('logout', silic.views.logout, name='logout'),
    path('contact', silic.views.contact, name='contact'),
    path('about', silic.views.about, name='about'),
    path('home', silic.views.home, name='home'),
    path('cushome', silic.views.cushome, name='cushome'),
    path('edit_category/<id>', silic.views.edit_category, name='edit_category'),
    path('delete_category/<id>', silic.views.delete_category, name='delete_category'),
    path('nfs', silic.views.nfs, name='nfs'),
    path('view_font_style', silic.views.view_font_style, name='view_font_style'),
    path('new_band_size', silic.views.new_band_size, name='new_band_size'),
    path('view_band_size', silic.views.view_band_size, name='view_band_size'),
    path('edit_band_size/<id>', silic.views.edit_band_size, name='edit_band_size'),
    path('delete_band_size/<id>', silic.views.delete_band_size, name='delete_band_size'),
    path('new_clipart', silic.views.new_clipart, name='new_clipart'),
    path('view_clipart', silic.views.view_clipart, name='view_clipart'),
    path('delete_clipart/<id>', silic.views.delete_clipart, name='delete_clipart'),
    path('nbs', silic.views.nbs, name='nbs'),
    path('view_band_style', silic.views.view_band_style, name='view_band_style'),
    path('edit_band_style/<id>', silic.views.edit_band_style, name='edit_band_style'),
    path('delete_band_style/<id>', silic.views.delete_band_style, name='delete_band_style'),

    path('new_price', silic.views.new_price, name='new_price'),
    path('view_price', silic.views.view_price, name='view_price'),
    path('edit_band_price/<id>', silic.views.edit_band_price, name='edit_band_price'),
    path('delete_band_price/<id>', silic.views.delete_band_price, name='delete_band_price'),

    path('add_product/<id>', silic.views.add_product, name='add_product'),
    path('view_product/<id>', silic.views.view_product, name='view_product'),
    path('edit_product/<id>', silic.views.edit_product, name='edit_product'),
    path('delete_product/<id>', silic.views.delete_product, name='delete_product'),

    path('del_faq', silic.views.del_faq, name='del_faq'),
    path('delete_faq/<id>', silic.views.delete_faq, name='delete_faq'),
    path('feedbak', silic.views.feedbak, name='feedbak'),
    path('faqs', silic.views.faqs, name='faqs'),
    path('edit_font_style/<id>', silic.views.edit_font_style, name='edit_font_style'),
    path('delete_font_style/<id>', silic.views.delete_font_style, name='delete_font_style'),
    path('faq', silic.views.faq, name='faq'),
    path('feedbak', silic.views.feedbak, name='feedbak'),
    path('feedback', silic.views.feedback, name='feedback'),
    path('delete_feedback/<id>', silic.views.delete_feedback, name='delete_feedback'),

































    #path('viewproof', silic.views.viewproof, name='viewproof'),
   # path('deleteorder', silic.views.deleteorder, name='deleteorder'),








































































































]