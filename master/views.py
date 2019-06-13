from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from django.views import generic
import barcode, os, shutil
from barcode.writer import ImageWriter
from django.conf import settings
# Create your views here.

EAN = barcode.get_barcode_class('ean13')



'''### Geographical ###'''

# Render Tabs------------------------------------------------------------------------

@login_required(login_url='account:login')
def index(request):
    return render(request, 'master/index.html')

@login_required(login_url='account:login')
def country(request):
    return render(request, 'master/pages/country.html')

@login_required(login_url='account:login')
def state(request):
    return render(request, 'master/pages/state.html')

@login_required(login_url='account:login')
def city(request):
    return render(request, 'master/pages/city.html')

@login_required(login_url='account:login')
def area(request):
    return render(request, 'master/pages/area.html')

# Add Geographical------------------------------------------------------------------------------------

@login_required(login_url='account:login')
def AddArea(request):
    if request.method == 'POST':
        form = AreaForm(request.POST, user=request.user)
        if form.is_valid():
            area = form.save(commit=False)
            area.user = request.user
            area.save()
            return redirect('master:area')
        else:
            return render(request, 'master/pages/add-area.html', {'form': form})
    else:
        form = AreaForm(None, user=request.user)
        return render(request, 'master/pages/add-area.html', {'form': form})

@login_required(login_url='account:login')
def AddCity(request):
    if request.method == 'POST':
        form = CityForm(request.POST, user=request.user)
        if form.is_valid():
            city = form.save(commit=False)
            city.user = request.user
            city.save()
            return redirect('master:city')
        else:
            return render(request, 'master/pages/add-city.html', {'form': form})
    else:
        form = CityForm(None, user=request.user)
        return render(request, 'master/pages/add-city.html', {'form': form})

@login_required(login_url='account:login')
def AddState(request):
    if request.method == 'POST':
        form = StateForm(request.POST, user=request.user)
        if form.is_valid():
            state = form.save(commit=False)
            state.user = request.user
            state.save()
            return redirect('master:state')
        else:
            return render(request, 'master/pages/add-state.html', {'form': form})
    else:
        form = StateForm(None, user=request.user)
        return render(request, 'master/pages/add-state.html', {'form': form})

@login_required(login_url='account:login')
def AddCountry(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            country = form.save(commit=False)
            country.user = request.user
            country.save()
            return redirect('master:country')
        else:
            return render(request, 'master/pages/add-country.html', {'form': form})
    else:
        form = CountryForm(None)
        return render(request, 'master/pages/add-country.html', {'form': form})

# Delete Geographical-----------------------------------------------------------------------------------

@login_required(login_url='account:login')
def DelArea(request, area_id):
    area = Area.objects.get(pk=area_id)
    area.delete()
    return redirect('master:area')

@login_required(login_url='account:login')
def DelCity(request, city_id):
    city = City.objects.get(pk=city_id)
    city.delete()
    return redirect('master:city')

@login_required(login_url='account:login')
def DelState(request, state_id):
    state = State.objects.get(pk=state_id)
    state.delete()
    return redirect('master:state')

@login_required(login_url='account:login')
def DelCountry(request, country_id):
    country = Country.objects.get(pk=country_id)
    country.delete()
    return redirect('master:country')

# Edit Geographical--------------------------------------------------------------------------------

@login_required(login_url='account:login')
def EditArea(request, area_id):
    data = {
        'name': Area.objects.get(pk=area_id),
        'pin_code': Area.objects.get(pk=area_id).pin_code,
        'country': Area.objects.get(pk=area_id).country,
        'state': Area.objects.get(pk=area_id).state,
        'city': Area.objects.get(pk=area_id).city,
    }
    if request.method == 'POST':
        area = Area.objects.get(pk=area_id)
        area.name = request.POST.get('name')
        area.pin_code = request.POST.get('pin_code')
        area.country = Country.objects.get(pk=request.POST.get('country'))
        area.state = State.objects.get(pk=request.POST.get('state'))
        area.city = City.objects.get(pk=request.POST.get('city'))
        area.save()
        return redirect('master:area')
    else:
        form = AreaForm(initial=data, user=request.user)
        return render(request, 'master/pages/add-area.html', {'form': form})

@login_required(login_url='account:login')
def EditCity(request, city_id):
    data = {
        'name': City.objects.get(pk=city_id),
        'std_code': City.objects.get(pk=city_id).std_code,
        'country': City.objects.get(pk=city_id).country,
        'state': City.objects.get(pk=city_id).state,
    }
    if request.method == 'POST':
        city = City.objects.get(pk=city_id)
        city.name = request.POST.get('name')
        city.std_code = request.POST.get('std_code')
        city.country = Country.objects.get(pk=request.POST.get('country'))
        city.state = State.objects.get(pk=request.POST.get('state'))
        city.save()
        return redirect('master:city')
    else:
        form = CityForm(initial=data, user=request.user)
        return render(request, 'master/pages/add-city.html', {'form': form})

@login_required(login_url='account:login')
def EditState(request, state_id):
    data = {
        'name': State.objects.get(pk=state_id),
        'state_code': State.objects.get(pk=state_id).state_code,
        'country': State.objects.get(pk=state_id).country,
    }
    if request.method == 'POST':
        state = State.objects.get(pk=state_id)
        state.name = request.POST.get('name')
        state.state_code = request.POST.get('state_code')
        state.country = Country.objects.get(pk=request.POST.get('country'))
        state.save()
        return redirect('master:state')
    else:
        form = StateForm(initial=data, user=request.user)
        return render(request, 'master/pages/add-state.html', {'form': form})

@login_required(login_url='account:login')
def EditCountry(request, country_id):
    if request.method == 'POST':
        country = Country.objects.get(pk=country_id)
        country.name = request.POST.get('name')
        country.save()
        return redirect('master:country')
    else:
        form = CountryForm(initial={'name': Country.objects.get(pk=country_id)})
        return render(request, 'master/pages/add-country.html', {'form': form})





'''---------------- Product Master ------------------'''

# Render Product --------------------------------------------------------------------------------

@login_required(login_url='account:login')
def category(request):
    return render(request, 'master/pages/category.html')

@login_required(login_url='account:login')
def design(request):
    return render(request, 'master/pages/design.html')

@login_required(login_url='account:login')
def quality(request):
    return render(request, 'master/pages/quality.html')

@login_required(login_url='account:login')
def unit(request):
    return render(request, 'master/pages/unit.html')

@login_required(login_url='account:login')
def shade(request):
    return render(request, 'master/pages/shade.html')

@login_required(login_url='account:login')
def manufacturer(request):
    return render(request, 'master/pages/manufacturer.html')

@login_required(login_url='account:login')
def item(request):
    return render(request, 'master/pages/item.html')

@login_required(login_url='account:login')
def barcode(request):
    if request.method == 'POST':
        query = request.POST['srh']
        if query:
            item = Item.objects.get(Q(name__icontains=query))
            image = item.barcode_img
            if image:
                return render(request, 'master/pages/barcode.html', {'image': image, 'item': item})
            else:
                return render(request, 'master/pages/barcode.html', {'massage': 'No data found'})
        else:
            return redirect('master:barcode')
    return render(request, 'master/pages/barcode.html')

# Add Product ------------------------------------------------------------------------------

@login_required(login_url='account:login')
def AddCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('master:category')
        else:
            return render(request, 'master/pages/add-category.html', {'form': form})
    else:
        form = CategoryForm(None)
        return render(request, 'master/pages/add-category.html', {'form': form})

@login_required(login_url='account:login')
def AddDesign(request):
    if request.method == 'POST':
        form = DesignForm(request.POST)
        if form.is_valid():
            design = form.save(commit=False)
            design.user = request.user
            design.save()
            return redirect('master:design')
        else:
            return render(request, 'master/pages/add-design.html', {'form': form})
    else:
        form = DesignForm(None)
        return render(request, 'master/pages/add-design.html', {'form': form})

@login_required(login_url='account:login')
def AddDesign(request):
    if request.method == 'POST':
        form = DesignForm(request.POST)
        if form.is_valid():
            design = form.save(commit=False)
            design.user = request.user
            design.save()
            return redirect('master:design')
        else:
            return render(request, 'master/pages/add-design.html', {'form': form})
    else:
        form = DesignForm(None)
        return render(request, 'master/pages/add-design.html', {'form': form})

@login_required(login_url='account:login')
def AddQuality(request):
    if request.method == 'POST':
        form = QualityForm(request.POST)
        if form.is_valid():
            quality = form.save(commit=False)
            quality.user = request.user
            quality.save()
            return redirect('master:quality')
        else:
            return render(request, 'master/pages/add-quality.html', {'form': form})
    else:
        form = QualityForm(None)
        return render(request, 'master/pages/add-quality.html', {'form': form})

@login_required(login_url='account:login')
def AddUnit(request):
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.user = request.user
            unit.save()
            return redirect('master:unit')
        else:
            return render(request, 'master/pages/add-unit.html', {'form': form})
    else:
        form = UnitForm(None)
        return render(request, 'master/pages/add-unit.html', {'form': form})

@login_required(login_url='account:login')
def AddShade(request):
    if request.method == 'POST':
        form = ShadeForm(request.POST)
        if form.is_valid():
            shade = form.save(commit=False)
            shade.user = request.user
            shade.save()
            return redirect('master:shade')
        else:
            return render(request, 'master/pages/add-shade.html', {'form': form})
    else:
        form = ShadeForm(None)
        return render(request, 'master/pages/add-shade.html', {'form': form})

@login_required(login_url='account:login')
def AddManufacturer(request):
    manufacturers = Manufacturer.objects.filter(user=request.user)
    codes = []
    for manufacturer in manufacturers:
        codes.append(manufacturer.code)

    if request.method == 'POST':
        form = ManufacturerForm(request.POST, user=request.user)
        if form.is_valid():
            manufacturer = form.save(commit=False)
            manufacturer.user = request.user
            manufacturer.save()
            return redirect('master:manufacturer')
        else:
            return render(request, 'master/pages/add-manufacturer.html', {'form': form, 'codes': codes})
    else:
        form = ManufacturerForm(None, user=request.user)
        return render(request, 'master/pages/add-manufacturer.html', {'form': form, 'codes': codes})

@login_required(login_url='account:login')
def AddItem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, user=request.user)

        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            code = form.cleaned_data['barcode']
            ean = EAN(code, writer=ImageWriter())
            item.barcode_img = ean.save(item.name)
            f = item.name + '.png'
            os.chdir(settings.BASE_DIR)
            shutil.move(f, settings.MEDIA_ROOT)
            item.save()
            return redirect('master:item')
        else:
            return render(request, 'master/pages/add-item.html', {'form': form})
    else:
        form = ItemForm(None, user=request.user)
        return render(request, 'master/pages/add-item.html', {'form': form})

# Product Details -------------------------------------------------------------------------------------------------

@login_required(login_url='account:login')
def CategoryDetail(request, category_id):
    category = Category.objects.get(pk=category_id, user=request.user)
    return render(request, 'master/pages/category-detail.html', {'category': category})

@login_required(login_url='account:login')
def DesignDetail(request, design_id):
    design = Design.objects.get(pk=design_id, user=request.user)
    return render(request, 'master/pages/design-detail.html', {'design': design})

@login_required(login_url='account:login')
def QualityDetail(request, quality_id):
    quality = Quality.objects.get(pk=quality_id, user=request.user)
    return render(request, 'master/pages/quality-detail.html', {'quality': quality})

@login_required(login_url='account:login')
def ShadeDetail(request, shade_id):
    shade = Shade.objects.get(pk=shade_id, user=request.user)
    return render(request, 'master/pages/shade-detail.html', {'shade': shade})

@login_required(login_url='account:login')
def ManufacturerDetail(request, manufacturer_id):
    manufacturer = Manufacturer.objects.get(pk=manufacturer_id, user=request.user)
    return render(request, 'master/pages/manufacturer-detail.html', {'manufacturer': manufacturer})

@login_required(login_url='account:login')
def ItemDetail(request, item_id):
    item = Item.objects.get(pk=item_id, user=request.user)
    return render(request, 'master/pages/item-detail.html', {'item': item})

# Edit Products ---------------------------------------------------------------------------------------------------

@login_required(login_url='account:login')
def EditCategory(request, category_id):
    data = {
        'name': Category.objects.get(pk=category_id),
        'code': Category.objects.get(pk=category_id).code,
        'image': Category.objects.get(pk=category_id).image,
    }
    if request.method == 'POST':
        category = Category.objects.get(pk=category_id)
        category.name = request.POST.get('name')
        category.code = request.POST.get('code')
        try:
            category.image = request.FILES['image']
        except:
            try:
                if request.POST['image-clear']:
                    category.image = None
            except:
                category.image = category.image
        category.save()
        return redirect('master:category')
    else:
        form = CategoryForm(initial=data)
        return render(request, 'master/pages/add-category.html', {'form': form})

@login_required(login_url='account:login')
def EditDesign(request, design_id):
    data = {
        'name': Design.objects.get(pk=design_id),
        'code': Design.objects.get(pk=design_id).code,
        'pattern': Design.objects.get(pk=design_id).pattern,
        'additional_tags': Design.objects.get(pk=design_id).additional_tags,
        'status': Design.objects.get(pk=design_id).status,
    }
    if request.method == 'POST':
        design = Design.objects.get(pk=design_id)
        design.name = request.POST.get('name')
        design.code = request.POST.get('code')
        design.pattern = request.POST.get('pattern')
        design.status = request.POST.get('status')
        design.save()
        return redirect('master:design')
    else:
        form = DesignForm(initial=data)
        return render(request, 'master/pages/add-design.html', {'form': form})

@login_required(login_url='account:login')
def EditQuality(request, quality_id):
    data = {
        'name': Quality.objects.get(pk=quality_id),
        'code': Quality.objects.get(pk=quality_id).code,
        'end_use': Quality.objects.get(pk=quality_id).end_use,
        'fabric_type': Quality.objects.get(pk=quality_id).fabric_type,
        'color_fastness': Quality.objects.get(pk=quality_id).color_fastness,
        'composition': Quality.objects.get(pk=quality_id).composition,
        'additional_tags': Quality.objects.get(pk=quality_id).additional_tags,
        'instruction': Quality.objects.get(pk=quality_id).instruction,
        'status': Quality.objects.get(pk=quality_id).status,
    }
    if request.method == 'POST':
        quality = Quality.objects.get(pk=quality_id)
        quality.name = request.POST.get('name')
        quality.code = request.POST.get('code')
        quality.end_use = request.POST.get('end_use')
        quality.fabric_type = request.POST.get('fabric_type')
        quality.color_fastness = request.POST.get('color_fastness')
        quality.composition = request.POST.get('composition')
        quality.additional_tags = request.POST.get('additional_tags')
        quality.instruction = request.POST.get('instruction')
        quality.status = request.POST.get('status')
        quality.save()
        return redirect('master:quality')
    else:
        form = QualityForm(initial=data)
        return render(request, 'master/pages/add-quality.html', {'form': form})

@login_required(login_url='account:login')
def EditUnit(request, unit_id):
    data = {
        'name': Unit.objects.get(pk=unit_id),
        'code': Unit.objects.get(pk=unit_id).code,
    }
    if request.method == 'POST':
        unit = Unit.objects.get(pk=unit_id)
        unit.name = request.POST['name']
        unit.code = request.POST['code']
        unit.save()
        return redirect('master:unit')
    else:
        form = UnitForm(initial=data)
        return render(request, 'master/pages/add-unit.html', {'form': form})

@login_required(login_url='account:login')
def EditShade(request, shade_id):
    data = {
        'name': Shade.objects.get(pk=shade_id),
        'code': Shade.objects.get(pk=shade_id).code,
        'color': Shade.objects.get(pk=shade_id).color,
        'additional_tags': Shade.objects.get(pk=shade_id).additional_tags,
        'status': Shade.objects.get(pk=shade_id).status,
    }
    if request.method == 'POST':
        shade = Shade.objects.get(pk=shade_id)
        shade.name = request.POST['name']
        shade.code = request.POST['code']
        shade.color = request.POST['color']
        shade.additional_tags = request.POST['additional_tags']
        shade.status = request.POST['status']
        shade.save()
        return redirect('master:shade')
    else:
        form = ShadeForm(initial=data)
        return render(request, 'master/pages/add-shade.html', {'form': form})

@login_required(login_url='account:login')
def EditManufacturer(request, manufacturer_id):
    data = {
        'name': Manufacturer.objects.get(pk=manufacturer_id),
        'code': Manufacturer.objects.get(pk=manufacturer_id).code,
        'state': Manufacturer.objects.get(pk=manufacturer_id).state,
        'city': Manufacturer.objects.get(pk=manufacturer_id).city,
        'pin_code': Manufacturer.objects.get(pk=manufacturer_id).pin_code,
        'address': Manufacturer.objects.get(pk=manufacturer_id).address,
        'mobile': Manufacturer.objects.get(pk=manufacturer_id).mobile,
        'phone': Manufacturer.objects.get(pk=manufacturer_id).phone,
        'email': Manufacturer.objects.get(pk=manufacturer_id).email,
        'gst_no': Manufacturer.objects.get(pk=manufacturer_id).gst_no,
    }
    if request.method == 'POST':
        manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
        manufacturer.name = request.POST.get('name')
        manufacturer.code = request.POST.get('code')
        manufacturer.state = State.objects.get(pk=request.POST.get('state'))
        manufacturer.city = City.objects.get(pk=request.POST.get('city'))
        manufacturer.pin_code = request.POST.get('pin_code')
        manufacturer.address = request.POST.get('address')
        manufacturer.mobile = request.POST['mobile']
        manufacturer.phone = request.POST['phone']
        manufacturer.email = request.POST.get('email')
        manufacturer.gst_no = request.POST.get('gst_no')
        manufacturer.save()
        return redirect('master:manufacturer')
    else:
        form = ManufacturerForm(initial=data, user=request.user)
        return render(request, 'master/pages/add-manufacturer.html', {'form': form})

@login_required(login_url='account:login')
def EditItem(request, item_id):
    data = {
        'name': Item.objects.get(pk=item_id),
        'category': Item.objects.get(pk=item_id).category,
        'design': Item.objects.get(pk=item_id).design,
        'shade': Item.objects.get(pk=item_id).shade,
        'unit': Item.objects.get(pk=item_id).unit,
        'unit_size': Item.objects.get(pk=item_id).unit_size,
        'product_type': Item.objects.get(pk=item_id).product_type,
        'manufacturer': Item.objects.get(pk=item_id).manufacturer,
        'sale_rate': Item.objects.get(pk=item_id).sale_rate,
        'barcode': Item.objects.get(pk=item_id).barcode,
        'discount': Item.objects.get(pk=item_id).discount,
        'image': Item.objects.get(pk=item_id).image,
        'status': Item.objects.get(pk=item_id).status,
        'deal': Item.objects.get(pk=item_id).deal,
    }
    if request.method == 'POST':
        item = Item.objects.get(pk=item_id)
        item.name = request.POST['name']
        item.category = Category.objects.get(pk=request.POST['category'])
        item.design = Design.objects.get(pk=request.POST['design'])
        if request.POST['shade'] == '':
            item.shade = None
        else:
            item.shade = Shade.objects.get(pk=request.POST['shade'])
        item.unit = Unit.objects.get(pk=request.POST['unit'])
        item.unit_size = request.POST['unit_size']
        item.product_type = request.POST['product_type']
        item.manufacturer = Manufacturer.objects.get(pk=request.POST['manufacturer'])
        item.sale_rate = request.POST['sale_rate']
        item.barcode = request.POST['barcode']
        if request.POST['discount'] == '':
            item.discount = None
        else:
            item.discount = request.POST['discount']
        try:
            item.image = request.FILES['image']
        except:
            try:
                if request.POST['image-clear']:
                    item.image = None
            except:
                item.image = item.image
        item.status = request.POST['status']
        item.deal = request.POST['deal']
        item.barcode_img.delete()
        ean = EAN(request.POST['barcode'], writer=ImageWriter())
        item.barcode_img = ean.save(request.POST['name'])
        f = request.POST['name'] + '.png'
        os.chdir(settings.BASE_DIR)
        shutil.move(f, settings.MEDIA_ROOT)
        item.save()
        return redirect('master:item')
    else:
        form = ItemForm(initial=data, user=request.user)
        return render(request, 'master/pages/add-item.html', {'form': form})

# Delete Products -----------------------------------------------------------------------------------------------

@login_required(login_url='account:login')
def DeleteCategory(request, category_id):
    category = Category.objects.get(pk=category_id)
    category.delete()
    return redirect('master:category')

@login_required(login_url='account:login')
def DeleteDesign(request, design_id):
    design = Design.objects.get(pk=design_id)
    design.delete()
    return redirect('master:design')

@login_required(login_url='account:login')
def DeleteQuality(request, quality_id):
    quality = Quality.objects.get(pk=quality_id)
    quality.delete()
    return redirect('master:quality')

@login_required(login_url='account:login')
def DeleteUnit(request, unit_id):
    unit = Unit.objects.get(pk=unit_id)
    unit.delete()
    return redirect('master:unit')

@login_required(login_url='account:login')
def DeleteShade(request, shade_id):
    shade = Shade.objects.get(pk=shade_id)
    shade.delete()
    return redirect('master:shade')

@login_required(login_url='account:login')
def DeleteManufacturer(request, manufacturer_id):
    manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
    manufacturer.delete()
    return redirect('master:manufacturer')

@login_required(login_url='account:login')
def DeleteItem(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.delete()
    return redirect('master:item')



'''------------------- Customer Master -----------------------'''

# Render Customer -------------------------------------------------------------------------

@login_required(login_url='account:login')
def CustomerMaster(request):
    return render(request, 'master/pages/customer.html')

# Add Customer ----------------------------------------------------------------------------

@login_required(login_url='account:login')
def AddCustomerMaster(request):
    customers = Customer.objects.filter(user=request.user)
    codes = []
    for customer in customers:
        codes.append(customer.code)

    if request.method == 'POST':
        form = CustommerForm(request.POST, request.FILES, user=request.user)

        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            return redirect('master:customer')

        return render(request, 'master/pages/add-customer.html', {'form': form, 'codes': codes})

    else:
        form = CustommerForm(None, user=request.user)
        return render(request, 'master/pages/add-customer.html', {'form': form, 'codes': codes})


