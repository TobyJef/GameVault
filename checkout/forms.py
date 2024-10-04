from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('title', 'first_name', 'last_name', 'email', 'contact_number',
                  'street_address_1', 'street_address_2', 'town_or_city',
                  'post_zipcode' 'county_or_state', 'country')

def __init__(self, *args, **kwargs):
    """
    Add placeholders and classes, remove auto-generated
    labels and set autofocus on title field
    """
    super().__init__(*args, **kwargs)
    placeholders = {
        'title': 'Title',
        'first_name': 'First Name',
        'second_name': 'Second Name',
        'email': 'Email Address',
        'contact_number': 'Contact Number',
        'street_address_1': 'Street Address 1',
        'street_address_2': 'Street Address 2',
        'town_or_city': 'Town or City',
        'post_zipcode': 'Post Code/Zip Code',
        'county_or_state': 'County or State',
        'country': 'Country',
    }

    self.fields['title'].widget.attrs['autofocus'] = True
    for field in self.fields:
        if self.fields[field].required:
            placeholder = f'{placeholders[field]} *'
        else:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


