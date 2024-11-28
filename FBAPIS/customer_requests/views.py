from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from FBAPIS.customer_requests.models import CustomerRequests
from FBAPIS.customer_requests.serializers import CustomerRequestSerializer

@api_view(['GET', 'POST'])
def CustomerRequestsListAPI(request):

    if request.method == 'POST':
        serializer = CustomerRequestSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        querySet = CustomerRequests.objects.all()
        serializer = CustomerRequestSerializer(querySet, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def specificCustomerRequestsListAPI(request, customer_id):
    try:
        # Fetch customer requests for the specific customer_id
        customer_requests = CustomerRequests.objects.filter(customer_id=customer_id).values(
            'request_id', 'customer_id', 'messages', 'created_at', 'updated_at'
        )
        
        # Convert queryset to list of dictionaries
        customer_requests_list = list(customer_requests)

        if customer_requests_list:
            return JsonResponse({
                "status": "success",
                "customer_id": customer_id,
                "requests": customer_requests_list
            }, status=200)
        else:
            return JsonResponse({
                "status": "error",
                "message": "No requests found for this customer."
            }, status=404)

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def CustomerRequestsDetailAPI(request, request_id):
    try:
        querySet = CustomerRequests.objects.get(request_id=request_id)
    except CustomerRequests.DoesNotExist:
        return Response({'message':f"{request_id} - Data not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CustomerRequestSerializer(querySet)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = CustomerRequestSerializer(querySet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        serializer = CustomerRequestSerializer(querySet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        querySet.delete()
        return Response({'message': f"{request_id} - Data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)