from FBAPIS.customer_requests.models import CustomerRequests

from rest_framework import serializers

class CustomerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerRequests
        fields = "__all__"