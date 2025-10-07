from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  

    if filter_type == "all":
        products_list = Product.objects.all()
    else:
        products_list = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'class': 'PBP B',
        'products_list': products_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html",context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        products_entry = form.save(commit = False)
        products_entry.user = request.user
        products_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    products_list = Product.objects.all()
    xml_data = serializers.serialize("xml", products_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    products_list = Product.objects.all()
    data = [
            {
                'id': str(product.id),
                'name': product.name,
                'description': product.description,
                'category': product.category,
                'thumbnail': product.thumbnail,
                'product_views': product.product_views,
                'created_at': product.created_at.isoformat() if product.created_at else None,
                'is_featured': product.is_featured,
                'user_id': product.user_id,
            }
            for product in products_list
        ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try : 
        products_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", products_item)
        return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
            product = Product.objects.select_related('user').get(pk=product_id)
            data = {
                'id': str(product.id),
                'name': product.name,
                'description': product.description,
                'category': product.category,
                'thumbnail': product.thumbnail,
                'product_views': product.product_views,
                'created_at': product.created_at.isoformat() if product.created_at else None,
                'is_featured': product.is_featured,
                'user_id': product.user_id,
                'user_username': product.user.username if product.user_id else None,
            }
            return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

@csrf_exempt
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                "status": "success",
                "message": "Your account has been successfully created!"
            })
        else:
            errors = {field: [str(e) for e in errs] for field, errs in form.errors.items()}
            return JsonResponse({
                "status": "error",
                "errors": errors
            })
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = JsonResponse({
                'status': 'success',
                'message': 'Login successful!',
                'redirect_url': '/main/'
            })
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            errors = form.errors.get_json_data()
            return JsonResponse({'status': 'error', 'errors': errors})
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@csrf_exempt
def logout_user(request):
    if request.method == "POST":
        logout(request)
        response = JsonResponse({'status': 'success', 'message': 'You have been logged out.'})
        response.delete_cookie('last_login')
        return response
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'}, status=400)

@csrf_exempt
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({
                "status": "success",
                "message": "Product updated successfully!",
                "product_id": str(product.id)
            })
        else:
            errors = {field: [str(e) for e in errs] for field, errs in form.errors.items()}
            return JsonResponse({
                "status": "error",
                "errors": errors
            })
    product_data = {
        "id": str(product.id),
        "name": product.name,
        "price": str(product.price),
        "description": product.description,
        "category": product.category,
        "thumbnail": product.thumbnail,
        "is_featured": product.is_featured,
        "stock": product.stock
    }
    return JsonResponse({
        "status": "ok",
        "product": product_data
    })

@require_POST
@csrf_exempt
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success', 'message': 'Product deleted successfully'})
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'
    stock = request.POST.get("stock")  # checkbox handling
    user = request.user

    new_product = Product(
        name = name, 
        price = price,
        description = description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        stock = stock,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)