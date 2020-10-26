from django import forms
from django.db.models import fields
from .models import Review,RATE_CHOICES

class RateForm(forms.ModelForm):
    rate_usability = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(),required=True)
    rate_content = forms.ChoiceField(choices=RATE_CHOICES,widget=forms.Select(),required=True)
    rate_design = forms.ChoiceField(choices=RATE_CHOICES,widget=forms.Select(),required=True)

    class Meta:
        model = Review
        fields = ('rate_content','rate_usability','rate_design')