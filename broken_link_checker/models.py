from django.db import models


class BrokenLinkCheckerModel(models.Model):
	site_name = models.URLField(max_length=200)

	def __str__(self):
		return self.site_name

	class Meta:
		verbose_name = 'Link'
		verbose_name_plural = "Links"
