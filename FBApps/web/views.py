from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.hashers import check_password, make_password
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from functools import wraps

from FBApps.customers.models import Customers, CustomerProfile
from FBApps.web.models import Cakes, Categories, CustomizeCake, Cart,Order, OrderItem
from FBApps.master.helpers.UNIQUE.checkPassword import is_valid_password
from FBApps.master.helpers.UNIQUE.JWTToken import create_jwt_token, decode_jwt_token
from FBApps.master.helpers.UNIQUE.createOtp import generate_otp
from .emailHelpers import send_activation_email

import time
import jwt
import json




def login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Check if 'customer_id' is in session
        if 'customer_id' not in request.session:
            # Redirect to the login page if not authenticated
            messages.warning(request, "You need to login first.")
            return redirect('login_view')
        # Call the original view function if authenticated
        return view_func(request, *args, **kwargs)
    return wrapper

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        email_ = request.POST.get('email')
        mobile_ = request.POST.get('mobile')
        password_ = request.POST.get('password')
        confirm_password_ = request.POST.get('confirm_password')

        if  Customers.objects.filter(email=email_).exists():
            messages.info(request, "Email already exists")
            return redirect('register_view')
        else:
            if password_!= confirm_password_:
                messages.info(request, "Password and Confirm Password should match")
                return redirect('register_view')
            else:
                is_valid, validation_message = is_valid_password(password_)
                if not is_valid:
                    messages.info(request, validation_message)  # Show validation message if password is invalid
                    return redirect('register_view')
                else:
                    new_customer = Customers.objects.create(
                        email=email_,
                        mobile=mobile_,
                        password=password_

                    )
                    new_customer.save()
                    user = {
                        'customer_id':new_customer.customer_id,
                        'email': email_,
                        'verification_token':create_jwt_token(new_customer.customer_id)
                    }
                    send_activation_email(request, user)
                    messages.success(request, "Registration successful! Please check your email to activate your account.")
                    return redirect('register_view')
    return render(request, 'web/register.html')


def activate_account(request, customer_id, token):
    try:
        # Decode the token
        payload = decode_jwt_token(token)
        
        # Check if the customer ID in the payload matches the customer ID in the URL
        if payload['customer_id'] != customer_id:
            messages.error(request, "Invalid confirmation link.")
            return redirect('some_error_page')  # Redirect to an error page

        # Check if the token is expired
        if payload['exp'] < time.time():
            messages.error(request, "Confirmation link has expired.")
            return redirect('some_error_page')  # Redirect to an error page

        # Find the customer and activate the account
        customer = Customers.objects.get(customer_id=customer_id)
        customer.is_active = True  # Assuming you have an is_active field
        customer.save()

        messages.success(request, "Your account has been activated successfully.")
        return redirect('login_view')  # Redirect to the login page

    except jwt.ExpiredSignatureError:
        messages.error(request, "Confirmation link has expired.")
        return redirect('some_error_page')  # Redirect to an error page
    except jwt.InvalidTokenError:
        messages.error(request, "Invalid confirmation link.")
        return redirect('some_error_page')  # Redirect to an error page
    except Customers.DoesNotExist:
        messages.error(request, "Customer not found.")
        return redirect('some_error_page')  # Redirect to an error page

def some_error_page(request):
    return render(request, 'web/some_error_page.html')

def login_view(request):
    if request.method == 'POST':
        email_ = request.POST.get('email')
        password_ = request.POST.get('password')

        if Customers.objects.filter(email=email_).exists():
            customer = Customers.objects.get(email=email_)
            if customer.is_active:
                is_valid = check_password(password_, customer.password)
                if is_valid:
                    request.session['customer_id'] = customer.customer_id
                    return redirect('index_view')
                else:
                    messages.info(request, "Invalid password.")
                    return redirect('login_view')
            else:
                messages.info(request, "Account is not activated. Please activate your account first.")
                return redirect('login_view')
        else:
            messages.warning(request, "Email does not exist.")
            return redirect('login_view')
    return render(request, 'web/login.html')

def forgot_password_view(request):
    if request.method == 'POST':
        email_ = request.POST.get('email')
        if Customers.objects.filter(email=email_).exists():
            customer = Customers.objects.get(email=email_)
            otp_ =  generate_otp()
            customer.otp = otp_
            customer.save()

            message = f'Your one-time password is: {otp_}'

            send_mail(
            "Forgot your password | Frostybites",
            message,
            settings.EMAIL_HOST_USER, 
            [email_]
            )
            request.session['FB-email'] = email_
            messages.success(request, "We have sent a one-time password to your email. Please check your inbox.")
            return redirect('otp_verify_view')
        else:
            messages.warning(request, "Email does not exist.")
            return redirect('forgot_password_view')



    return render(request, 'web/forgot-password.html')

def otp_verify_view(request):
    if request.method == 'POST':
        email_ = request.session['FB-email']
        otp_ = request.POST.get('otp')
        new_password_ = request.POST['new_password']
        confirm_password_ = request.POST['confirm_password']

        if Customers.objects.filter(email=email_).exists():
            customer = Customers.objects.get(email=email_)
            if customer.otp == otp_:
                if new_password_!= confirm_password_:
                    messages.info(request, "Password and Confirm Password should match")
                    return redirect('otp_verify_view')
                else:
                    is_valid, validation_message = is_valid_password(new_password_)
                    if not is_valid:
                        messages.info(request, validation_message)  # Show validation message if password is invalid
                        return redirect('otp_verify_view')
                    else:
                        customer.password = make_password(new_password_)
                        customer.save()
                        del request.session['FB-email']
                        messages.success(request, "Password has been changed successfully.")
                        return redirect('login_view')
            else:
                messages.info(request, "Invalid OTP.")
                return redirect('otp_verify_view')
        else:
            messages.warning(request, "Email does not exits.")
            return redirect('otp_verify_view')
    return render(request, 'web/otp-verify.html')

@login_required
def logout(request):
    request.session.clear()
    messages.success(request, "You have been logged out successfully.")
    return redirect('login_view')



def index_view(request):
    categories = Categories.objects.all().order_by('name')
    context = {
        'categories': categories
    }
    return render(request, 'web/index.html', context)

def catagories_view(request):
    cakes = Cakes.objects.all()
    return render(request, 'web/catagories.html', {'cakes':cakes})

def latest_collection_view(request):
    return render(request, 'web/latest_collection.html')

def on_trand_view(request):
    return render(request, 'web/on_trand.html')

def custom_cake_view(request):
    if request.method == 'POST':
        image_ = request.FILES['image']
        content_ = request.POST['content']

        new_cake_request = CustomizeCake.objects.create(
            customer_id=request.session['customer_id'],
            image=image_,
            content=content_
        )

        new_cake_request.save()
        messages.success(request, "Your custom cake request has been submitted successfully. We will get back to you soon.")
        return redirect('custom_cake_view')


    cake_requests = CustomizeCake.objects.filter(customer_id=request.session['customer_id'])
    
    context = {
        'cake_requests':cake_requests,
        'request_length': len(cake_requests)
    }
    print(context)
    return render(request, 'web/custom_cake.html', context)


def removeCustomCake(request, cake_id):
    get_cake = CustomizeCake.objects.get(customize_cake_id=cake_id)
    get_cake.delete()
    messages.success(request, "Your custom cake request has been removed successfully.")
    return redirect('custom_cake_view')

@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(customer_id=request.session['customer_id'])
    context = {
        'cart_items': cart_items,
        'total_items': len(cart_items),
    }
    return render(request, 'web/cart.html', context)

@login_required
def add_to_cart(request, cake_id):
    get_cake = Cakes.objects.get(cake_id=cake_id)
    customer_id = request.session['customer_id']

    add_item = Cart.objects.create(
        customer_id=customer_id,
        cake_id = cake_id
    )
    add_item.save()
    messages.success(request, "Cake added to cart successfully.")
    return redirect('cart_view')
@login_required
@require_POST
def update_cart_quantity(request):
    try:
        data = json.loads(request.body)
        cart_id = data.get('cart_id')
        quantity = data.get('quantity')
        new_total = data.get('new_total')

        # Update the cart item quantity
        cart_item = Cart.objects.get(cart_id=cart_id)
        cart_item.quantity = quantity
        cart_item.subtotal = new_total
        cart_item.save()

        return JsonResponse({'success': True})
    except Cart.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Cart item not found'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@login_required
@csrf_exempt
def place_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cart_ids = data.get('cart_ids', [])
        

        if not cart_ids:
            return JsonResponse({'success': False, 'message': 'No cart items selected.'})
        
        grandTotal = 0
        for cart_id in cart_ids:
            get_cart_item = Cart.objects.get(cart_id=cart_id)
            grandTotal += get_cart_item.subtotal

        new_order = Order.objects.create(
            customer_id=request.session['customer_id'],
            grand_total=grandTotal
        )
        new_order.save()
            

        # Process the selected cart items and create an order
        # For example, you can save the order to the database
        # Here, just a simple response for demonstration
        # Replace this with your order processing logic
        # Example: Order.objects.create(cart_ids=cart_ids, ...)

        return JsonResponse({'success': True, 'message': 'Order placed successfully.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


@login_required
def profile_view(request):
    getCustomer = Customers.objects.get(customer_id=request.session['customer_id'])
    getCustomerProfile = CustomerProfile.objects.get(customer_id=request.session['customer_id'])

    return render(request, 'web/profile.html', {
        'customer': getCustomer,
        'customerProfile': getCustomerProfile
    })

@login_required
def edit_profile(request):
    if request.method == 'POST':
        first_name_ = request.POST['first_name']
        last_name_ = request.POST['last_name']
        mobile_ = request.POST['mobile']
        gender_ = request.POST['gender']
        date_ = request.POST['date_of_birth']

        getCustomer = Customers.objects.get(customer_id=request.session['customer_id'])
        getCustomer.mobile = mobile_
        getCustomer.save()

        getCustomerProfile = CustomerProfile.objects.get(customer_id=request.session['customer_id'])
        getCustomerProfile.first_name = first_name_
        getCustomerProfile.last_name = last_name_
        getCustomerProfile.gender = gender_
        getCustomerProfile.date_of_birth = date_
        getCustomerProfile.save()

        messages.success(request, "Profile data updated successfully.")
        return redirect('profile_view')
    
@login_required
def edit_profile_picture(request):
    if request.method == 'POST' and request.FILES.get('profile'):
        profile_picture_ = request.FILES['profile']
        print(profile_picture_)
        try:
            getCustomerProfile = CustomerProfile.objects.get(customer_id=request.session['customer_id'])
            getCustomerProfile.profile_picture = profile_picture_
            getCustomerProfile.save()
            messages.success(request, "Profile picture updated successfully.")
        except CustomerProfile.DoesNotExist:
            messages.error(request, "Profile not found.")
    else:
        messages.error(request, "No file uploaded.")

    return redirect('profile_view')