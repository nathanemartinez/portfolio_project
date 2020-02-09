from django import forms
from .models import Checker


class BrokenLinkCheckerModelForm(forms.ModelForm):
	class Meta:
		model = Checker
		fields = ['site']
		widgets = {
			'site': forms.URLInput(
				attrs={
					'placeholder': 'http://example.com',
					'class': 'form-control',
				})
		}
