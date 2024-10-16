from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

def __init__(self, *args, **kwargs):
    """
    Add placeholders and classes, remove auto-generated
    labels and set autofocus on title field
    """
    super().__init__(*args, **kwargs)
    placeholders = {
        'default_contact_number': 'Contact Number',
        'default_street_address_1': 'Street Address 1',
        'default_street_address_2': 'Street Address 2',
        'default_town_or_city': 'Town or City',
        'default_post_zipcode': 'Post Code/Zip Code',
        'default_county_or_state': 'County or State',
    }

    self.fields['default_contact_number'].widget.attrs['autofocus'] = True
    for field in self.fields:
        if field != 'default_country':
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
        self.fields[field].label = False


