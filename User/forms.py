from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django import forms
from .models import User

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username','user_type', 'email',  'cell_phone')


class UserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label=("Password"),
        help_text=(
            "Raw passwords are not stored, so there is no way to see this "
            "user's password, but you can change the password using "
            "<a href=\"../password_change/\">this form</a>."
        ),
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'cell_phone', 'address1', 'address2', 'city', 'state', 'zipcode')

rateservices = [
    ("Excellent", 'Excellent'),
    ("Good", 'Good'),
    ("Bad", 'Bad'),
]

recommend = [
    ("Yes", 'Yes'),
    ("No", 'No'),
]

class ContactForm(forms.Form):
    rate_services = forms.CharField(widget=forms.RadioSelect(choices=rateservices))
    likethebest = forms.CharField(
        widget=forms.Textarea
    )
    howcanweimprove = forms.CharField(
        widget=forms.Textarea
    )
    recommed_friends = forms.CharField(widget=forms.RadioSelect(choices=recommend))
    anything = forms.CharField(
        widget=forms.Textarea
    )


