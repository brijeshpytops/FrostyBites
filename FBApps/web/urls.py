from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('activate/<str:customer_id>/<str:token>/', activate_account, name='activate_account'),
    path('change-password/', forgot_password_view, name='forgot_password_view'),
    path('otp-verify/', otp_verify_view, name='otp_verify_view'),
    path('index/', index_view, name='index_view'),
    path('catagories/', catagories_view, name='catagories_view'),
    path('latest-collection/', latest_collection_view, name='latest_collection_view'),
    path('on-trand/', on_trand_view, name='on_trand_view'),
    path('custom-cake/', custom_cake_view, name='custom_cake_view'),
    path('profile/', profile_view, name='profile_view'),
    path('some-error/', some_error_page, name='some_error_page'),
]