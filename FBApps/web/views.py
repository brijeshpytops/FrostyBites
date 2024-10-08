from django.shortcuts import render, redirect
from django.contrib import messages

from FBApps.customers.models import Customers
from FBApps.master.helpers.UNIQUE.checkPassword import is_valid_password
from FBApps.master.helpers.UNIQUE.JWTToken import create_jwt_token, decode_jwt_token
from .emailHelpers import send_activation_email

import time
import jwt

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
        return redirect('login')  # Redirect to the login page

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
    return render(request, 'web/login.html')

def forgot_password_view(request):
    return render(request, 'web/forgot-password.html')

def otp_verify_view(request):
    return render(request, 'web/otp-verify.html')

def index_view(request):
    return render(request, 'web/index.html')

def catagories_view(request):
    return render(request, 'web/catagories.html')

def latest_collection_view(request):
    return render(request, 'web/latest_collection.html')

def on_trand_view(request):
    return render(request, 'web/on_trand.html')

def custom_cake_view(request):
    return render(request, 'web/custom_cake.html')

def profile_view(request):
    return render(request, 'web/profile.html')