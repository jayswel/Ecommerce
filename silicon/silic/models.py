from django.db import models

class Registration(models.Model):
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Phone = models.CharField(max_length=12,default='')
    Password = models.CharField(max_length=200)
    State = models.CharField(max_length=200,default='')
    City = models.CharField(max_length=200,default='')
    Pincode = models.IntegerField(default=0)
    Address = models.TextField(default='')
    About = models.TextField(default='')
    Lock = models.CharField(max_length=200,default='')
    User_role = models.CharField(max_length=200,default='')

class Pre_order(models.Model):
    Category_name = models.CharField(max_length=200)
    Product_name = models.CharField(max_length=200)
    Price = models.FloatField()
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Phone = models.CharField(max_length=12)
    State = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    Pincode = models.BigIntegerField()
    Address = models.TextField()
    Quantity = models.IntegerField()
    Order_date = models.DateField(auto_now_add=True)
    Total_amount = models.FloatField()
    Order_status = models.CharField(max_length=200)

class Cust_cart(models.Model):
    Front_message = models.CharField(max_length=200)
    Back_message = models.CharField(max_length=200)
    Color = models.CharField(max_length=200)
    Fon_style = models.CharField(max_length=200)
    Ban_size = models.FloatField()
    Ban_style = models.CharField(max_length=200)
    Clippart_name = models.CharField(max_length=200)
    QQuantity = models.BigIntegerField()
    Pricce = models.FloatField(null=True)
    Total_amount = models.FloatField(null=True)
    Delivery_charge = models.FloatField(null=True)
    regg = models.ForeignKey(Registration, on_delete=models.CASCADE)

class Band_order(models.Model):
    Front_message = models.CharField(max_length=200)
    Back_message = models.CharField(max_length=200)
    Color = models.CharField(max_length=200)
    Fonts_style = models.CharField(max_length=200)
    Bandd_size = models.CharField(max_length=200)
    Bandd_style = models.CharField(max_length=200)
    Clipartt_name = models.CharField(max_length=200)
    Quantitty = models.BigIntegerField(default=0)
    Pricee = models.FloatField(default=0)
    Totall_amount = models.FloatField(default=0)
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Phone = models.CharField(max_length=12)
    State = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    Pincode = models.BigIntegerField(default=0)
    Address = models.TextField()
    Order_date = models.DateField(auto_now_add=True)
    Order_status = models.CharField(max_length=200)


class Faq(models.Model):
    Customer_name = models.CharField(max_length=200,null=True)
    Customer_email = models.EmailField(null=True)
    Question = models.TextField(null=True)
    Answer = models.TextField(null=True)
    Submission_date = models.DateField(auto_now_add=True,null=True)

class Quotation_cus(models.Model):
    Customer_name = models.CharField(max_length=200)
    Customer_email = models.EmailField()
    Category_name = models.CharField(max_length=200)
    Description = models.TextField()
    Quantity_selected = models.BigIntegerField()
    Quotation_date = models.DateField(auto_now_add=True)
    Status = models.CharField(max_length=200)

class Band_details(models.Model):
    Size_in_inch = models.FloatField(default=1)
    Style = models.CharField(max_length=200)
    Clipart_name = models.CharField(max_length=200)
    Clipart_image = models.ImageField(null=True)
    Font_name = models.CharField(max_length=200)
    Minimum_quantity = models.BigIntegerField(default=0)
    Maximum_quantity = models.BigIntegerField(default=0)
    Discount_percentage = models.FloatField(default=0)
    Unit_price = models.IntegerField(default=0)
    Status =  models.CharField(max_length=200)


class Conveyance_fees(models.Model):
    Delivery_charge_min_km = models.BigIntegerField(null=True)
    Delivery_charge_max_km = models.BigIntegerField(null=True)
    Delivery_fees = models.FloatField(null=True)
    Shipping_days = models.BigIntegerField(null=True)
    Shipping_description = models.TextField(null=True)
    Shipping_cost = models.FloatField(null=True)
    Status = models.CharField(max_length=200,null=True)

class Category_product(models.Model):
    Category_name = models.CharField(max_length=200,null=True)
    Product_name = models.CharField(max_length=200,null=True)
    Product_image = models.ImageField(null=True)
    Minimum_quantity = models.BigIntegerField(default=0,null=True)
    Maximum_quantity = models.BigIntegerField(default=0,null=True)
    Discount_percentage = models.FloatField(default=0,null=True)
    Unit_price = models.FloatField(default=0,null=True)
    Status = models.CharField(max_length=200,null=True)

class Quotation(models.Model):
    Category_name = models.CharField(max_length=200)
    Minimum_quantity = models.BigIntegerField()
    Maximum_quantity = models.BigIntegerField()
    Discount_percent = models.FloatField()
    Status = models.CharField(max_length=200)
    catt = models.ForeignKey(Category_product, on_delete=models.CASCADE,null=True)

class Feedback(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Category = models.CharField(max_length=200)
    Content = models.TextField()
    Submission_date = models.DateField(auto_now_add = True)





##################################
class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

#####################################

class category(models.Model):
    name = models.CharField(max_length=40,null=True)

    def __str__(self):
        return self.name


class fontstyle(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class size(models.Model):
        fontstyle = models.ForeignKey(fontstyle, on_delete=models.CASCADE,null=True)
        name = models.CharField(max_length=40)

        def __str__(self):
            return self.name


class price(models.Model):
    size = models.ForeignKey(size, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    category = models.ForeignKey(category, on_delete=models.SET_NULL, blank=True, null=True)
    fontstyle = models.ForeignKey(fontstyle, on_delete=models.SET_NULL, blank=True, null=True)
    size = models.ForeignKey(size, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.ForeignKey(price, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


