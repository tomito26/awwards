from django import forms
from django.db.models import fields
from .models import Review,RATE_CHOICES

class RateForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))
    rate = forms.ChoiceField(choices=RATE_CHOICES,widget=forms.Select())
    
    class Meta:
        model = Review
        fields = ('text','rate')