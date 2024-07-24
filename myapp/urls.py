
from django.contrib import admin
from django.urls import include, path
from myapp import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('admin', views.home, name='home'),
    path('login', views.user_login, name='login'),
    path('registration', views.registration, name='registration'), 
    path('portal', views.portal, name='portal'),   
    path('search', views.search, name='search'),
    path('tourism', views.tourism, name='tourism'),
    path('service', views.service, name='service'),
    path('about', views.about, name='about'),
]

