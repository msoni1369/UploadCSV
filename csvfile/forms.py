from django import forms
from . models import Profile
from dal import autocomplete
class LeaseProfileForm(forms.Form):
    tenant = forms.ModelChoiceField(queryset=Profile.objects.all(),widget=autocomplete.ModelSelect2(url='tenant-autocomplete'))
    class Meta:
        model = Profile
        #exclude = ['lease']