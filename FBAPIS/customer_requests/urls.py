from django.urls import path
from FBAPIS.customer_requests.views import *

urlpatterns = [
    path('requests/', CustomerRequestsListAPI, name='CustomerRequestsListAPI'),
    path('specific-customer-requests/<str:customer_id>', specificCustomerRequestsListAPI, name='specificCustomerRequestsListAPI'),
    path('request/<str:request_id>', CustomerRequestsDetailAPI, name='CustomerRequestsDetailAPI')
]