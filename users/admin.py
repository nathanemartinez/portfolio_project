from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
# RENAMES ADMIN PAGE TITLE
admin.site.site_header = 'Administration'
