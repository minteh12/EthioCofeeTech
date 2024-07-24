from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import FarmerData
from .models import TourismSpot



# Create your views here.

def home(request):

    return render(request, 'home.html')
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']

        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('service')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    return render(request, 'login.html')


def registration(request):

    if request.method == "POST":
        fullname = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['pass']
        confirmPass = request.POST['confirmPass']

        myuser = User.objects.create_user(username,email,password)
        myuser.full_name = fullname

        myuser.save()

        messages.success(request, "Your account has been successfuly created")

        return redirect('login')

    return render(request, 'registration.html') 

def portal(request):
   
    data = FarmerData.objects.all().order_by('address')
    print(data)
    return render(request, 'portal.html', {'data': data})

def search(request):
    query = request.GET.get('address')
    results = None
    if query:
        results = FarmerData.objects.filter(address__icontains=query)
    return render(request, 'search.html', {'results': results})

def tourism(request):
    tourism_spots = TourismSpot.objects.all()
    return render(request, 'tourism.html', {'tourism_spots': tourism_spots})

def service(request):

    return render(request, 'service.html')

def about(request):

    return render(request, 'about.html')