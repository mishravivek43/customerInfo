"""firstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
#include is required for viewsets here(used to include other routes or urls)
from django import urls
from django.urls import path,include
from shopApp import views
"""
#to import routers to integrate viewsets in urls =>
from rest_framework.routers import DefaultRouter
#Creating Object of Default Router
router = DefaultRouter()
#Registering out View set in the object
router.register('students', views.StudentViewSet)

#Include auto creted urls in the url patterns =>
urlpatterns = [
    path('', include(router.urls)),

]
"""
#for Class based Views/mixins/generics
urlpatterns = [
    path('customers/',views.CustomerListView.as_view()),
    path('customers/<int:pk>',views.CustomerDetailView.as_view()),
    path('orders/',views.OrderListView.as_view()),
    path('orders/<int:pk>',views.OrderDetailView.as_view()),

]
