from django import forms
from .models import *

# Geographical Master ---------------
class AreaForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Area Name'}))
    pin_code = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'fieldSelectorId', 'class': 'form-control', 'placeholder': 'PIN Code', 'minlength': '6'}))

    class Meta:
        model = Area
        fields = ['country', 'state', 'city', 'name', 'pin_code']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(AreaForm, self).__init__(*args, **kwargs)
        self.fields['country'] = forms.ModelChoiceField(queryset=Country.objects.filter(user=user).order_by('name'),
                                                        widget=forms.Select(attrs={'class': "selectpicker", 'data-live-search': 'true', 'tabindex': '-98'}))
        self.fields['state'] = forms.ModelChoiceField(queryset=State.objects.filter(user=user).order_by('name'),
                                       widget=forms.Select(attrs={'class': "selectpicker", 'data-live-search': 'true', 'tabindex': '-98'}))
        self.fields['city'] = forms.ModelChoiceField(queryset=City.objects.filter(user=user).order_by('name'),
                                      widget=forms.Select(attrs={'class': "selectpicker", 'data-live-search': 'true', 'tabindex': '-98'}))



class CityForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City Name'}))
    std_code = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'STD Code'}))

    class Meta:
        model = City
        fields = ['country', 'state', 'name', 'std_code']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CityForm, self).__init__(*args, **kwargs)
        self.fields['country'] = forms.ModelChoiceField(queryset=Country.objects.filter(user=user).order_by('name'),
                                                        widget=forms.Select(attrs={'class': "selectpicker", 'data-live-search': 'true', 'tabindex': '-98'}))
        self.fields['state'] = forms.ModelChoiceField(queryset=State.objects.filter(user=user).order_by('name'),
                                       widget=forms.Select(attrs={'class': "selectpicker", 'data-live-search': 'true', 'tabindex': '-98'}))



class StateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State Name'}))
    state_code = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'State Code'}))

    class Meta:
        model = State
        fields = ['country', 'name', 'state_code']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(StateForm, self).__init__(*args, **kwargs)
        self.fields['country'] = forms.ModelChoiceField(queryset=Country.objects.filter(user=user).order_by('name'),
                                                        widget=forms.Select(attrs={'class': "selectpicker", 'data-live-search': 'true', 'tabindex': '-98'}))



class CountryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country Name'}))

    class Meta:
        model = Country
        fields = ['name']


# Product Master ------------------------------------------------------------


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'code', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Code'}),
        }


class DesignForm(forms.ModelForm):
    status = forms.CharField(widget=forms.Select(choices=product_status_choices, attrs={'class': 'form-control-sm'}))

    class Meta:
        model = Design
        fields = ['name', 'code', 'pattern', 'additional_tags', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Design Name'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Design Code'}),
            'pattern': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Design Pattern'}),
            'additional_tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Additional Tags'}),
        }


class QualityForm(forms.ModelForm):
    status = forms.CharField(widget=forms.Select(choices=product_status_choices, attrs={'class': 'form-control-sm'}))

    class Meta:
        model = Quality
        fields = ['name', 'code', 'end_use', 'fabric_type', 'color_fastness', 'composition', 'additional_tags', 'instruction', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code'}),
            'end_use': forms.TextInput(attrs={'class': 'form-control'}),
            'fabric_type': forms.TextInput(attrs={'class': 'form-control'}),
            'color_fastness': forms.TextInput(attrs={'class': 'form-control'}),
            'composition': forms.TextInput(attrs={'class': 'form-control'}),
            'additional_tags': forms.TextInput(attrs={'class': 'form-control'}),
            'instruction': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UnitForm(forms.ModelForm):

    class Meta:
        model = Unit
        fields = ['name', 'code']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code'}),
        }

class ShadeForm(forms.ModelForm):

    class Meta:
        model = Shade
        fields = ['name', 'code', 'color', 'additional_tags', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Color'}),
            'additional_tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Additional Tags'}),
            'status': forms.Select(choices=product_status_choices, attrs={'class': 'form-control-sm'}),
        }

class ManufacturerForm(forms.ModelForm):

    class Meta:
        model = Manufacturer
        fields = ['name', 'code', 'state', 'city', 'pin_code', 'address', 'mobile', 'phone', 'email', 'gst_no']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'code': forms.TextInput(attrs={'id': 'code', 'class': 'form-control', 'placeholder': 'Code'}),
            'pin_code': forms.NumberInput(attrs={'id': 'pin_code', 'class': 'form-control', 'placeholder': 'PIN Code', 'minlength': '6'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'mobile': forms.NumberInput(attrs={'id': 'mobile_no', 'class': 'form-control', 'minlength': '10', 'placeholder': 'Mobile'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'gst_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GST No.'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ManufacturerForm, self).__init__(*args, **kwargs)
        self.fields['state'] = forms.ModelChoiceField(queryset=State.objects.filter(user=user).order_by('name'),
                                                        widget=forms.Select(
                                                            attrs={'class': "selectpicker", 'data-live-search': 'true',
                                                                   'tabindex': '-98'}))
        self.fields['city'] = forms.ModelChoiceField(queryset=City.objects.filter(user=user).order_by('name'),
                                                      widget=forms.Select(
                                                          attrs={'class': "selectpicker", 'data-live-search': 'true',
                                                                 'tabindex': '-98'}))

    def clean_pin_code(self):
        pin_code = self.cleaned_data['pin_code']

        if not Area.objects.filter(pin_code__iexact=pin_code):
            raise forms.ValidationError("Area for the PIN Code doesn't exist")
        return pin_code

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['name', 'category', 'design', 'shade', 'unit', 'unit_size', 'product_type', 'manufacturer', 'sale_rate', 'barcode', 'discount', 'image', 'status', 'deal']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'unit_size': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'product_type': forms.Select(choices=product_type_choices, attrs={'class': 'form-control-sm'}),
            'sale_rate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rate'}),
            'barcode': forms.NumberInput(attrs={'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'status': forms.Select(choices=product_status_choices, attrs={'class': 'form-control-sm'}),
            'deal': forms.Select(choices=deal_choises, attrs={'class': 'form-control-sm'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ItemForm, self).__init__(*args, **kwargs)

        self.fields['category'] = forms.ModelChoiceField(queryset=Category.objects.filter(user=user).order_by('name'),
                                                     widget=forms.Select(
                                                         attrs={'class': "selectpicker", 'data-live-search': 'true', 'tabindex': '-98'}
                                                     ))
        self.fields['design'] = forms.ModelChoiceField(queryset=Design.objects.filter(user=user, status='active').order_by('name'),
                                                       widget=forms.Select(
                                                           attrs={'class': "selectpicker", 'data-live-search': 'true', 'tabindex': '-98'}
                                                       ))
        self.fields['shade'] = forms.ModelChoiceField(queryset=Shade.objects.filter(user=user).order_by('name'),
                                                            widget=forms.Select(
                                                                attrs={'class': "selectpicker", 'data-live-search': 'true', 'tabindex': '-98'}),
                                                      required=False)
        self.fields['unit'] = forms.ModelChoiceField(queryset=Unit.objects.filter(user=user).order_by('name'),
                                                     widget=forms.Select(
                                                         attrs={'class': "selectpicker", 'data-live-search': 'true', 'tabindex': '-98'}
                                                     ))
        self.fields['manufacturer'] = forms.ModelChoiceField(queryset=Manufacturer.objects.filter(user=user).order_by('name'),
                                                     widget=forms.Select(
                                                         attrs={'class': "selectpicker", 'data-live-search': 'true',
                                                                'tabindex': '-98'}
                                                     ))

# Custommer Master -------------------------------------------------

class CustommerForm(forms.ModelForm):
    bank = forms.ModelChoiceField(queryset=Bank.objects.all().order_by('bank_name'),
                                                     widget=forms.Select(
                                                         attrs={'class': "selectpicker", 'data-live-search': 'true', 'tabindex': '-98'}
                                                     ))

    class Meta:
        model = Customer
        fields = ['code', 'type', 'company', 'print_name', 'address', 'country', 'state', 'city', 'area', 'agent', 'broker', 'registration_type', 'phone', 'mobile', 'email', 'website', 'tax_type', 'vendor_code', 'party_type',
                  'gstin_no', 'aadhar_no', 'pan_no', 'dl_no', 'other', 'gstin_doc', 'aadhar_doc', 'pan_doc', 'dl_doc', 'other_doc',
                  'status', 'investment', 'establishment_year', 'certification', 'credit_days', 'credit_limit', 'discount', 'contact_person', 'page_no', 'remark',
                  'bank', 'brunch', 'account_no', 'isfc', 'bank_address',
                  'document_heading', 'docket_category', 'docket_description', 'docket_file',
                  'delivery_contact', 'delivery_location', 'delivery_address', 'delivery_mobile', 'delivery_email',
                  'person_name', 'person_department', 'person_mobile', 'person_email']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code', 'id': 'code'}),
            'type': forms.Select(choices=customer_type_choices, attrs={'class': 'form-control-sm'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'print_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Print Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'agent': forms.Select(choices=agent_choices, attrs={'class': 'form-control'}),
            'broker': forms.Select(choices=broker_choises, attrs={'class': 'form-control'}),
            'registration_type': forms.Select(choices=registration_type_choices, attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'mobile': forms.NumberInput(attrs={'id': 'mobile_no', 'class': 'form-control', 'minlength': '10', 'placeholder': 'Mobile Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Website URL'}),
            'tax_type': forms.Select(choices=tax_type_choices, attrs={'class': 'form-control'}),
            'vendor_code': forms.TextInput(attrs={'class': 'form-control col-xl-5', 'placeholder': 'Vendor Code'}),
            'party_type': forms.Select(choices=party_type_choices, attrs={'class': 'form-control'}),
            'gstin_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GSTIN Number'}),
            'aadhar_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adhar Number'}),
            'pan_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PAN number'}),
            'dl_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DL Number'}),
            'other': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Other'}),
            'status': forms.Select(choices=customer_status_choices, attrs={'class': 'form-control'}),
            'investment': forms.Select(choices=investment_choices, attrs={'class': 'form-control'}),
            'establishment_year': forms.NumberInput(attrs={'class': 'form-control-sm', 'placeholder': 'Year', 'maxlength': '4'}),
            'certification': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Certification'}),
            'credit_days': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Credit Days'}),
            'credit_limit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Credit Limit'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            'contact_person': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Person'}),
            'page_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Page Number'}),
            'remark': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Remark'}),
            'brunch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brunch'}),
            'account_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Account Number'}),
            'isfc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISF Code'}),
            'bank_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bank Address'}),
            'document_heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Heading'}),
            'docket_category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'docket_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'delivery_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact'}),
            'delivery_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'delivery_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'delivery_mobile': forms.NumberInput(attrs={'id': 'mobile_no', 'class': 'form-control', 'minlength': '10', 'placeholder': 'Mobile Number'}),
            'delivery_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'person_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'person_department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}),
            'person_mobile': forms.NumberInput(attrs={'id': 'mobile_no', 'class': 'form-control', 'minlength': '10', 'placeholder': 'Mobile Number'}),
            'person_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CustommerForm, self).__init__(*args, **kwargs)

        self.fields['country'] = forms.ModelChoiceField(queryset=Country.objects.filter(user=user).order_by('name'),
                                                        widget=forms.Select(
                                                            attrs={'class': "selectpicker", 'data-live-search': 'true', 'tabindex': '-98'}
                                                        ))
        self.fields['state'] = forms.ModelChoiceField(queryset=State.objects.filter(user=user).order_by('name'),
                                                      widget=forms.Select(
                                                          attrs={'class': "selectpicker", 'data-live-search': 'true', 'tabindex': '-98'}
                                                      ))
        self.fields['city'] = forms.ModelChoiceField(queryset=City.objects.filter(user=user).order_by('name'),
                                                     widget=forms.Select(
                                                         attrs={'class': "selectpicker", 'data-live-search': 'true', 'tabindex': '-98'}
                                                     ))
        self.fields['area'] = forms.ModelChoiceField(queryset=Area.objects.filter(user=user).order_by('name'),
                                                     widget=forms.Select(
                                                         attrs={'class': "selectpicker", 'data-live-search': 'true', 'tabindex': '-98'}
                                                     ))

    def clean_gstin_doc(self):
        gstin_no = self.cleaned_data['gstin_no']
        gstin_doc = self.cleaned_data['gstin_doc']

        if (gstin_no is not None) and (gstin_doc is None):
            raise forms.ValidationError('You have to provide Document for the GSTIN Number')
        return gstin_doc

    def clean_aadhar_doc(self):
        aadhar_no = self.cleaned_data['aadhar_no']
        aadhar_doc = self.cleaned_data['aadhar_doc']

        if (aadhar_no is not None) and (aadhar_doc is None):
            raise forms.ValidationError('You have to provide Document for the Aadhar Number')
        return aadhar_doc

    def clean_pan_doc(self):
        pan_no = self.cleaned_data['pan_no']
        pan_doc = self.cleaned_data['pan_doc']

        if (pan_no is not None) and (pan_doc is None):
            raise forms.ValidationError('You have to provide Document for the PAN Number')
        return pan_doc

    def clean_dl_doc(self):
        dl_no = self.cleaned_data['dl_no']
        dl_doc = self.cleaned_data['dl_doc']

        if (dl_no is not None) and (dl_doc is None):
            raise forms.ValidationError('You have to provide Document for the DL Number')
        return dl_doc

    def clean_other_doc(self):
        other = self.cleaned_data['other']
        other_doc = self.cleaned_data['other_doc']

        if (other is not None) and (other_doc is None):
            raise forms.ValidationError('You have to provide Document for the service you have chosen')
        return other_doc



class RateMasterForm(forms.ModelForm):

    class Meta:
        model = RateMaster
        fields = '__all__'

        widgets = {
            'rate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rate'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(RateMasterForm, self).__init__(*args, **kwargs)
        user = kwargs.pop('user')

        self.fields['customer'] = forms.ModelChoiceField(queryset=Customer.objects.filter(user=user).orderby('company'),
                                                         widget=forms.Select(
                                                             attrs={'class': "selectpicker", 'data-live-search': 'true',
                                                                    'tabindex': '-98'}
                                                         ))
        self.fields['product'] = forms.ModelChoiceField(queryset=Item.objects.filter(user=user).orderby('name'),
                                                         widget=forms.Select(
                                                             attrs={'class': "selectpicker", 'data-live-search': 'true',
                                                                    'tabindex': '-98'}
                                                         ))
