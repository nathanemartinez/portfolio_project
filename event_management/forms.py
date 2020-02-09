from django import forms
from .models import EventModel, GuestModel


class EventForm(forms.ModelForm):
	class Meta:
		model = EventModel
		fields = ['name', 'date']
		widgets = {
			'name': forms.TextInput(
				attrs={
					'placeholder': 'Event title',
					'class': 'form-control',
				}),
			'date': forms.DateInput(
				attrs={
					'class': 'form-control',
					'type': 'date',
				}),
			'description': forms.Textarea(
				attrs={
					'placeholder': 'Event description',
					'class': 'form-control',
				}),

		}


TRUE_FALSE_CHOICES = (
	(True, 'Yes'),
	(False, 'No'),
)


class GuestForm(forms.ModelForm):
	class Meta:
		model = GuestModel
		fields = ['will_attend']
		widgets = {
			'will_attend': forms.Select(
				attrs={
					'class': 'form-control',
					'type': 'date',
				},
			),
		}
