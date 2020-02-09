from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from uuid import uuid4

CHOICES = (
	('Hourly', 'HOURLY'),
	('Daily', 'DAILY'),
	('Weekly', 'WEEKLY'),
)
# ADMIN = User.objects.filter(is_superuser=True, username='brickspy').first().pk


class Checker(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	site = models.URLField(max_length=200, blank=False, null=False)
	scan = models.CharField(max_length=6, blank=False, null=False, choices=CHOICES)
	email = models.EmailField(blank=True, null=True)
	date_created = models.DateTimeField(default=timezone.now)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
	notes = models.TextField(max_length=200, null=True, blank=True, default='')

	def __str__(self):
		return self.site

	def date_published(self):
		return self.date_created.strftime('%m/%d/%Y')

	def get_absolute_url(self):
		return reverse('site_down:checker-detail', kwargs={'pk': self.pk})

	class Meta:
		verbose_name = 'Site'
		verbose_name_plural = "Sites"
