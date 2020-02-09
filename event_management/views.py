from django.shortcuts import render
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView, TemplateView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

from .models import EventModel, GuestModel
from .forms import GuestForm, EventForm

"""
***EVENT VIEWS***

"""
class EventListView(LoginRequiredMixin, ListView):
	model = EventModel
	template_name = 'event_management/event_list.html'
	# Default is 'object_list' - this is the context variable
	context_object_name = 'events'
	# Most recent events first
	ordering = ['-date_posted']

	def get_queryset(self):
		return EventModel.objects.filter(author=self.request.user)


class EventDetailView(LoginRequiredMixin, DetailView):
	model = EventModel
	template_name = 'event_management/event_detail.html'
	context_object_name = 'event'

	def get_context_data(self, **kwargs):
		# Primary key of event
		pk = self.kwargs['pk']
		# Overrides default get_context_data method?
		context = super(EventDetailView, self).get_context_data(**kwargs)
		# Gets all guest models and names the context 'guestmodel'
		context['guestmodel'] = GuestModel.objects.filter(event=pk)
		return context


# **ADD 'LoginRequiredMixin' TO THE FAR LEFT**
# This is like a login required decorator
class EventCreateView(LoginRequiredMixin, CreateView):
	model = EventModel
	template_name = 'event_management/event_create.html'
	fields = ['name', 'date', 'description']

	# Overrides the form valid method
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


# **ADD 'LoginRequiredMixin' TO THE FAR LEFT**
class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = EventModel
	template_name = 'event_management/event_update.html'
	fields = ['name', 'date', 'description']
	context_object_name = 'events'

	# Overrides the form valid method
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		# Gets the current event (model object)
		event = self.get_object()
		# Is the current user equal to the author (user that made it)?
		if self.request.user == event.author:
			return True
		return False


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = EventModel
	template_name = 'event_management/event_delete.html'

	def get_success_url(self):
		return reverse('event_management:event_management-events', kwargs={'username': self.request.user})

	def test_func(self):
		# Gets the current event (model object)
		event = self.get_object()
		# Is the current user equal to the author (user that made it)?
		if self.request.user == event.author:
			return True
		return False


"""
***GUEST VIEWS***

"""
class GuestListView(LoginRequiredMixin, ListView):
	model = GuestModel
	template_name = 'event_management/guests/guest_list.html'
	# Default is 'object_list' - this is the context variable
	context_object_name = 'guests'
	# Most recent events first
	ordering = ['-date_created']

	def get_queryset(self):
		# All events associated with user
		return GuestModel.objects.filter(event=self.kwargs['event_pk'])

	def get_context_data(self, **kwargs):
		context = super(GuestListView, self).get_context_data(**kwargs)
		event_pk = self.kwargs['event_pk']
		context['event_pk'] = event_pk
		return context


class GuestDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
	model = GuestModel
	template_name = 'event_management/guests/guest_detail.html'
	context_object_name = 'guest'
	pk_url_kwarg = 'guest_pk'

	def test_func(self):
		event = EventModel.objects.get(pk=self.kwargs['event_pk'])
		# Is the current user equal to the author (user that made it)?
		if self.request.user == event.author:
			return True
		return False


# **ADD 'LoginRequiredMixin' TO THE FAR LEFT**
# This is like a login required decorator
class GuestCreateView(LoginRequiredMixin, CreateView):
	model = GuestModel
	template_name = 'event_management/guests/guest_create.html'
	fields = ['first_name', 'last_name', 'email', 'notes']
	context_object_name = 'guest'

	def form_valid(self, form):
		self.object = form.save(commit=False)
		event = EventModel.objects.get(pk=self.kwargs['event_pk'])
		self.object.event = event
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		event_pk = self.kwargs['event_pk']
		return reverse('event_management:guest-create', kwargs={'username': self.request.user, 'event_pk': event_pk})


# **ADD 'LoginRequiredMixin' TO THE FAR LEFT**
class GuestUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = GuestModel
	template_name = 'event_management/guests/guest_update.html'
	fields = ['first_name', 'last_name', 'email', 'notes']
	context_object_name = 'guest'
	# The view looks for 'pk' for the guest model by default
	pk_url_kwarg = 'guest_pk'

	def form_valid(self, form):
		self.object = form.save(commit=False)
		event = EventModel.objects.get(pk=self.kwargs['event_pk'])
		self.object.event = event
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		event_pk = self.kwargs['event_pk']
		guest_pk = self.kwargs['guest_pk']
		return reverse('event_management:guest-detail', kwargs={'username': self.request.user, 'event_pk': event_pk, 'guest_pk': guest_pk})

	def test_func(self):
		event = EventModel.objects.get(pk=self.kwargs['event_pk'])
		if self.request.user == event.author:
			return True
		return False


class GuestDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = GuestModel
	template_name = 'event_management/guests/guest_delete.html'
	context_object_name = 'guest'
	pk_url_kwarg = 'guest_pk'

	def get_success_url(self):
		event_pk = self.kwargs['event_pk']
		return reverse('event_management:guests', kwargs={'username': self.request.user, 'event_pk': event_pk})

	def test_func(self):
		event = EventModel.objects.get(pk=self.kwargs['event_pk'])
		if self.request.user == event.author:
			return True
		return False


class SendEmail(TemplateView):
	def get(self, request, *args, **kwargs):
		# Event primary key
		event_pk = self.kwargs['event_pk']
		# Get guests with that pk
		guest_objects = GuestModel.objects.filter(event=event_pk, will_attend=True)
		# Get the guest emails
		# [[email, token, pk], [email, token, pk]]
		guests = [[guest.email, guest.token, guest.pk, guest.first_name] for guest in guest_objects]
		# The event
		event = EventModel.objects.get(pk=event_pk)

		# send_email params
		for guest in guests:
			subject = f'{guest[3]}, you are invited'
			token_url = reverse('event_management:guest-verify', kwargs={'guest_pk': guest[2], 'token': guest[1]})
			token_url = str(get_current_site(request=request)) + token_url
			message = f'You are invited to {event}.\nTo verify your attendance, ' \
					  f'click the link: {token_url}'
			from_email = settings.EMAIL_HOST_USER
			recipient_list = [guest[0]]
			auth_user = settings.EMAIL_HOST_USER
			auth_password = settings.EMAIL_HOST_PASSWORD
			datatuple = (subject, message, from_email, recipient_list)
			send_mass_mail(
				datatuple=(datatuple,), fail_silently=True, auth_user=auth_user, auth_password=auth_password,
			)

		context = {
			'guests': guest_objects,
			'event': event,
		}

		return render(request, 'event_management/functionality/send_email.html', context)


class VerifyAttendance(UpdateView):
	model = GuestModel
	template_name = 'event_management/functionality/attend_event.html'
	fields = ['will_attend']
	context_object_name = 'guest'
	pk_url_kwarg = 'guest_pk'

	def get_success_url(self):
		return reverse('event_management:guest-verify-success', kwargs={'guest_pk': self.kwargs['guest_pk']})


def success(request, guest_pk):
	template_name = 'event_management/functionality/attend_event_success.html'
	context = {

	}

	return render(request, template_name, context)
