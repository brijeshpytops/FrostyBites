from django.urls import path
from FBAPIS.customer_requests.views import *

urlpatterns = [
    path('requests/', CustomerRequestsListAPI, name='CustomerRequestsListAPI'),
    path('specific-customer-requests/', specificCustomerRequestsListAPI, name='specificCustomerRequestsListAPI'),
    path('request/<str:request_id>', CustomerRequestsDetailAPI, name='CustomerRequestsDetailAPI')
]