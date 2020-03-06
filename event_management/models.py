from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from uuid import uuid4
import datetime

# ADMIN = User.objects.filter(is_superuser=True, username='brickspy').first().pk
BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))


class EventModel(models.Model):
	name = models.CharField(max_length=200, unique=True, null=False, blank=False)
	# If the user gets deleted - remove the events
	author = models.ForeignKey(
		User, on_delete=models.CASCADE, null=False
	)
	date_posted = models.DateTimeField(default=timezone.now)
	date = models.DateTimeField(null=True, blank=True)
	description = models.TextField(max_length=200, null=False, blank=False, default='')

	def __str__(self):
		return self.name

	def date_published(self):
		return self.date.strftime('%m/%d/%Y')

	def get_absolute_url(self):
		return reverse('event_management:event_management-detail', kwargs={'username': self.author, 'pk': self.pk})

	class Meta:
		verbose_name = 'Event'
		verbose_name_plural = 'Events'


class GuestModel(models.Model):
	first_name = models.CharField(max_length=200, null=False, blank=False)
	last_name = models.CharField(max_length=200, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	# They click yes after clicking the secret email link
	will_attend = models.BooleanField(blank=True, null=True, default=True, choices=BOOL_CHOICES)
	# , choices = ATTENDANCE_CHOICES
	notes = models.TextField(blank=True, null=True)
	event = models.ForeignKey(EventModel, on_delete=models.CASCADE)
	date_created = models.DateTimeField(default=timezone.now)
	token = models.UUIDField(blank=True, null=True, max_length=100, unique=True)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

	def get_absolute_url(self):
		return reverse('event_management:guest-detail', kwargs={'username': User.username, 'pk': self.pk, 'event_pk': self.event.primary_key})

	def save(self, *args, **kwargs):
		self.token = uuid4().hex
		super().save(*args, **kwargs)

	class Meta:
		verbose_name = 'Guest'
		verbose_name_plural = "Guests"


