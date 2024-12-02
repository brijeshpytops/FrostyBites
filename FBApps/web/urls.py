from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('activate/<str:customer_id>/<str:token>/', activate_account, name='activate_account'),
    path('change-password/', forgot_password_view, name='forgot_password_view'),
    path('otp-verify/', otp_verify_view, name='otp_verify_view'),
    path('logout/', logout, name='logout'),
    path('index/', index_view, name='index_view'),
    path('catagories/', catagories_view, name='catagories_view'),
    path('latest-collection/', latest_collection_view, name='latest_collection_view'),
    path('on-trand/', on_trand_view, name='on_trand_view'),
    path('custom-cake/', custom_cake_view, name='custom_cake_view'),
    path('remove-Custom-Cake/<str:cake_id>', removeCustomCake, name='removeCustomCake'),
    path('customer-support/', customer_support_view, name='customer_support_view'),
    path('delete_cutomer_request/<str:request_id>', delete_cutomer_request, name='delete_cutomer_request'),
    path('carts/', cart_view, name='cart_view'),
    path('place-order/', place_order, name='place_order'),
    path('add_to_cart/<str:cake_id>',add_to_cart, name='add_to_cart'),
    path('update-cart-quantity/', update_cart_quantity, name='update_cart_quantity'),
    path('profile/', profile_view, name='profile_view'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('edit-profile-picture/', edit_profile_picture, name='edit_profile_picture'),
    path('some-error/', some_error_page, name='some_error_page'),
]