from django.shortcuts import render
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView, TemplateView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

from .models import Checker


class CheckerListView(LoginRequiredMixin, ListView):
	model = Checker
	template_name = 'site_down/checker_list.html'
	context_object_name = 'checkers'
	ordering = ['-date_created']

	def get_queryset(self):
		return Checker.objects.filter(user=self.request.user)


class CheckerDetailView(LoginRequiredMixin, DetailView):
	model = Checker
	template_name = 'site_down/checker_detail.html'
	context_object_name = 'checker'


# Create your views here.
class CheckerCreateView(LoginRequiredMixin, CreateView):
	model = Checker
	template_name = 'site_down/checker_create.html'
	fields = ['name', 'site', 'scan']
	context_object_name = 'checker'


class CheckerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Checker
	template_name = 'site_down/checker_update.html'
	fields = ['name', 'site', 'scan']
	context_object_name = 'checker'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		checker = self.get_object()
		return self.request.user == checker.user


class CheckerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Checker
	template_name = 'site_down/checker_delete.html'

	def get_success_url(self):
		return reverse('site_down:checker-list')

	def test_func(self):
		checker = self.get_object()
		return self.request.user == checker.user


def send_email(request):
	checker = Checker.objects.filter(user=request.user).first()
	subject = f'{request.user}, testing site down'
	message = f'Is this your name: {request.user}, testing site down app.'
	from_email = settings.EMAIL_HOST_USER
	recipient_list = [checker.email]
	auth_user = settings.EMAIL_HOST_USER
	auth_password = settings.EMAIL_HOST_PASSWORD
	send_mail(
		subject=subject, message=message, from_email=from_email, recipient_list=recipient_list,
		fail_silently=False, auth_user=auth_user, auth_password=auth_password,
	)

	context = {
		'site': checker.site,
		'email': checker.email
	}

	return render(request=request, template_name='site_down/send_email.html', context=context)


