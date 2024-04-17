from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['name', 'tel_num', 'description', 'time', 'address']

    def __init__(self, *args, **kwargs):
        super(OrdersForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Отправить'))

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['category', 'title', 'description', 'price', 'image_url']

class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['category', 'title', 'description', 'image_url']

class VacanciesForm(forms.ModelForm):
    class Meta:
        model = Vacancies
        fields = ['category', 'title', 'description']