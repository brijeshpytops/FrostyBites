from django.shortcuts import render

# Create your views here.
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