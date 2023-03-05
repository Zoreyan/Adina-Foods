from django.urls import path
from .views import home, form, success


urlpatterns = [
    path('', home, name='home'),
    path('order-form/', form, name='form'),
    path('success/', success, name='success')
]