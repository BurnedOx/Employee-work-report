from django.db import models
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

#Geographical Master ---------------------------
class Country(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class State(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    state_code = models.IntegerField()

    def __str__(self):
        return self.name

class City(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    std_code = models.IntegerField()

    def __str__(self):
        return self.name

class Area(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    pin_code = models.IntegerField()

    def __str__(self):
        return self.name


# Product Master ------------------------

product_status_choices = (
        ('active', 'active'),
        ('inactive', 'inactive'),
    )

product_type_choices = (
        ('Finish', 'Finish'),
        ('Raw', 'Raw'),
        ('Scrap', 'Scrap'),
        ('Semi-finish', 'Semi-finish')
    )

deal_choises = (
    ('both', 'both'),
    ('sale', 'sale'),
    ('purchase', 'purchase')
)

class Category(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

class Design(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    pattern = models.CharField(max_length=200, blank=True, null=True)
    additional_tags = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=10, choices=product_status_choices)

    def __str__(self):
        return self.name

class Quality(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    end_use = models.CharField(max_length=200, blank=True, null=True)
    fabric_type = models.CharField(max_length=200, blank=True, null=True)
    color_fastness = models.CharField(max_length=200, blank=True, null=True)
    composition = models.CharField(max_length=200, blank=True, null=True)
    additional_tags = models.CharField(max_length=200, blank=True, null=True)
    instruction = models.TextField(max_length=1000, blank=True, null=True)
    status = models.CharField(choices=product_status_choices, max_length=100)

    def __str__(self):
        return self.name

class Unit(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Shade(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    color = models.CharField(max_length=200, blank=True, null=True)
    additional_tags = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(choices=product_status_choices, max_length=100)

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=50, unique=True)
    state = models.ForeignKey(State, on_delete=None)
    city = models.ForeignKey(City, on_delete=None)
    pin_code = models.IntegerField()
    address = models.TextField(max_length=1000)
    mobile = models.CharField(blank=True, null=True, max_length=10)
    phone = models.CharField(blank=True, null=True, max_length=20)
    email = models.CharField(max_length=200)
    gst_no = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    design = models.ForeignKey(Design, on_delete=models.CASCADE)
    shade = models.ForeignKey(Shade, blank=True, null=True, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    unit_size = models.CharField(blank=True, null=True, max_length=500)
    product_type = models.CharField(choices=product_type_choices, max_length=100, blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    sale_rate = models.CharField(max_length=50, blank=True, null=True)
    barcode = models.CharField(blank=True, null=True, max_length=100)
    barcode_img = models.ImageField(blank=True, null=True, upload_to='media')
    discount = models.FloatField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='media')
    status = models.CharField(choices=product_status_choices, max_length=100)
    deal = models.CharField(choices=deal_choises, max_length=100)

    def __str__(self):
        return self.name


'''--------BANK-------------'''

class Bank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=20)

    def __str__(self):
        return self.bank_name



''' Customer Master ------------------------------------------------------'''

customer_type_choices = (
    ('Enquiry', 'Enquiry'),
    ('Propect', 'Prospect'),
    ('Customer', 'Customer'),
)

agent_choices = (
    ('Executive', 'Executive'),
    ('Collaborative', 'Collaborative'),
    ('Contributory', 'Contributory'),
    ('Communicative', 'Communicative'),
    ('Service', 'Service'),
)

broker_choises = (
    ('amd', 'amd'),
    ('BrokerTest', 'BrokerTest'),
    ('KLM', 'KLM'),
    ('Test', 'Test'),
)

registration_type_choices = (
    ('Regular', 'Regular'),
    ('Composition', 'Composition'),
    ('Consumer', 'Consumer'),
    ('Unregistered', 'Unregistered'),
    ('Unknown', 'Unknown'),
)

tax_type_choices = (
    ('Local', 'Local'),
    ('Out-Station', 'Out-Station'),
)

party_type_choices = (
    ('Not Applicable', 'Not Applicable'),
    ('Deemed Export', 'Deemed Export'),
    ('Govt. Entry', 'Govt. Entry'),
    ('SEZ', 'SEZ'),
)

customer_status_choices = (
    ('Proprietary', 'Proprietary'),
    ('Partnership', 'Partnership'),
    ('Pvt. Ltd. Company', 'Pvt. Ltd. Company'),
    ('Public Ltd', 'Public Ltd'),
)

investment_choices = (
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
)



class Customer(models.Model):

    # Personal Details ------------

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, unique=True)
    type = models.CharField(choices=customer_type_choices, max_length=10)
    company = models.CharField(max_length=200)
    print_name = models.CharField(max_length=200)
    address = models.TextField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    agent = models.CharField(max_length=20, choices=agent_choices, blank=True, null=True)
    broker = models.CharField(max_length=20, choices=broker_choises, blank=True, null=True)
    registration_type = models.CharField(max_length=20, choices=registration_type_choices, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    tax_type = models.CharField(max_length=20, choices=tax_type_choices)
    vendor_code = models.CharField(max_length=100, blank=True, null=True)
    party_type = models.CharField(max_length=10, choices=party_type_choices, blank=True, null=True)

    # Tax Doc Details ----------------------------------

    gstin_no = models.CharField(max_length=15, blank=True, null=True)
    aadhar_no = models.CharField(max_length=15, blank=True, null=True)
    pan_no = models.CharField(max_length=15, blank=True, null=True)
    dl_no = models.CharField(max_length=15, blank=True, null=True)
    other = models.CharField(max_length=15, blank=True, null=True)
    gstin_doc = models.FileField(blank=True, null=True)
    aadhar_doc = models.FileField(blank=True, null=True)
    pan_doc = models.FileField(blank=True, null=True)
    dl_doc = models.FileField(blank=True, null=True)
    other_doc = models.FileField(blank=True, null=True)

    # Other Details ----------------------------------------

    status = models.CharField(max_length=15, blank=True, null=True, choices=customer_status_choices)
    investment = models.CharField(max_length=15, blank=True, null=True, choices=investment_choices)
    establishment_year = models.IntegerField(blank=True, null=True)
    certification = models.TextField(max_length=500, blank=True, null=True)
    credit_days = models.IntegerField(blank=True, null=True)
    credit_limit = models.CharField(max_length=20, blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    contact_person = models.CharField(max_length=50, blank=True, null=True)
    page_no = models.IntegerField(blank=True, null=True)
    remark = models.TextField(max_length=300, blank=True, null=True)

    # Bank Details ------------------------------------------

    bank = models.ForeignKey(Bank, blank=True, null=True, on_delete=models.CASCADE)
    brunch = models.CharField(max_length=30, blank=True, null=True)
    account_no = models.CharField(max_length=18, blank=True, null=True)
    isfc = models.CharField(max_length=10, blank=True, null=True)
    bank_address = models.TextField(max_length=200, blank=True, null=True)

    # E-Docket ------------------------------------------

    document_heading = models.CharField(max_length=20, blank=True, null=True)
    docket_category = models.CharField(max_length=20, blank=True, null=True)
    docket_description = models.TextField(max_length=200, blank=True, null=True)
    docket_file = models.FileField(blank=True, null=True)

    # Delivery Address ---------------------------------

    delivery_contact = models.CharField(max_length=30, blank=True, null=True)
    delivery_location = models.CharField(max_length=50, blank=True, null=True)
    delivery_address = models.TextField(max_length=500, blank=True, null=True)
    delivery_mobile = models.CharField(max_length=30, blank=True, null=True)
    delivery_email = models.EmailField(blank=True, null=True)

    # Contact Person ---------------------------------

    person_name = models.CharField(max_length=30, blank=True, null=True)
    person_department = models.CharField(max_length=30, blank=True, null=True)
    person_mobile = models.CharField(max_length=30, blank=True, null=True)
    person_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.company


class RateMaster(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=None)
    date = models.DateField(auto_created=True)
    rate = models.CharField(max_length=20)
    product = models.ForeignKey(Item, on_delete=None)
    discount = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.rate

