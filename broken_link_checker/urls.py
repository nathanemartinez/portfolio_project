from django.urls import path
from .views import broken_link_checker

app_name = 'broken_link_checker'
urlpatterns = [
	path('broken-link-checker/', broken_link_checker, name='broken-link-checker'),

]
