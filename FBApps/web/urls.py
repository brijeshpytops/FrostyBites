from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index_view'),
    path('catagories/', catagories_view, name='catagories_view'),
    path('latest-collection/', latest_collection_view, name='latest_collection_view'),
    path('on-trand/', on_trand_view, name='on_trand_view'),
    path('custom-cake/', custom_cake_view, name='custom_cake_view'),
    path('profile/', profile_view, name='profile_view'),
]