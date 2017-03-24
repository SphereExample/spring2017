from django import forms
from maps.models import Country


class CountryForm(forms.ModelForm):

    class Meta:
        fields = ('name', 'population')
        model = Country
