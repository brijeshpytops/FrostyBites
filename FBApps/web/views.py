from django.shortcuts import render

from FBApps.customers.models import Customers

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        email_ = request.POST.get('email')
        mobile_ = request.POST.get('mobile')
        password_ = request.POST.get('password')
        confirm_password_ = request.POST.get('confirm_password')

        if password_!= confirm_password_:
            print("Password and Confirm Password should match")
            return render(request, 'web/register.html')
        else:
            new_customer = Customers.objects.create(
                email=email_,
                mobile=mobile_,
                password=password_

            )
            new_customer.save()
            return render(request, 'web/register.html')

    return render(request, 'web/register.html')

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