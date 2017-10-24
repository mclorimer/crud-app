from django import forms
from django.forms import ModelForm

from .models import Event

class EventCreationForm(forms.ModelForm):

	class Meta:
		model = Event
		fields = ('title', 'content', 'location', 'date', 'creator')
		widgets = {
			"creator": forms.HiddenInput(),
			"date": forms.DateTimeInput(attrs=dict(type='datetime'))
		}