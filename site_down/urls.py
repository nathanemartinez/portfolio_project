from django.urls import path
from .views import (
	CheckerCreateView, CheckerDetailView, CheckerListView, CheckerUpdateView, CheckerDeleteView
)

app_name = 'site_down'
urlpatterns = [
	# EVENTS
	path('checkers/', CheckerListView.as_view(), name='checker-list'),
	path('checkers/new/', CheckerCreateView.as_view(), name='checker-create'),
	path('checkers/<int:pk>/', CheckerDetailView.as_view(), name='checker-detail'),
	# Leave 'update' at the end - the user may have an event called 'update'
	path('checkers/<int:pk>/update/', CheckerUpdateView.as_view(), name='checker-update'),
	path('checkers/<int:pk>/delete/', CheckerDeleteView.as_view(), name='checker-delete'),

]
