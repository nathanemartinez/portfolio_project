from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
#
# from .models import Profile
#
#
# class UserRegisterForm(UserCreationForm):
# 	# Adding additional fields
# 	email = forms.EmailField(required=False)
# 	User._meta.get_field('email')._unique = True
#
# 	class Meta:
# 		# Whenever the form validates it creates a new user
# 		model = User
# 		fields = ['username', 'email', 'password1', 'password2']
#
#
# # To update username and email
# class UserUpdateForm(forms.ModelForm):
# 	# Adding additional fields
# 	email = forms.EmailField(required=False)
# 	User._meta.get_field('email')._unique = True
#
# 	class Meta:
# 		# Whenever the form validates it creates a new user
# 		model = User
# 		fields = ['username', 'email']
#
#
# # To update the image
# class ProfileUpdateForm(forms.ModelForm):
# 	class Meta:
# 		model = Profile
# 		fields = ['image']
