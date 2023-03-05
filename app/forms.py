from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={
            'type': 'text',
            'id': 'name',
            'placeholder': 'Укажите здесь ваше имя',
    }),
    'email' : forms.EmailInput(attrs={
            'type': 'email',
            'id': 'email',
            'placeholder': 'Ваша электронная почта',
    }),
    'address' : forms.TextInput(attrs={
            'type': 'address',
            'id': 'subject',
            'placeholder': 'Адресс куда доставить еду',
    }),
    'phone' : forms.TextInput(attrs={
            'type': 'tel',
            'id': 'contact',
            'placeholder': 'Ваш контактный номер',
    }),
    'text' : forms.Textarea(attrs={
            'type': 'text',
            'id': 'subject',
            'placeholder': 'Опишите ваш заказ здесь',
            'rows': 3
    })
        }