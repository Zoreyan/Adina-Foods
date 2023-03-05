from django.urls import path
from .views import home, form


urlpatterns = [
    path('', home, name='home'),
    path('order-form/', form, name='form')
]