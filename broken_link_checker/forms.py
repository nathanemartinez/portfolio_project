from django import forms
from .models import BrokenLinkCheckerModel


class BrokenLinkCheckerModelForm(forms.ModelForm):
	class Meta:
		model = BrokenLinkCheckerModel
		fields = ['site_name']
		widgets = {
			'site_name': forms.URLInput(
				attrs={
					'placeholder': 'http://example.com',
					'class': 'form-control',
				})
		}
