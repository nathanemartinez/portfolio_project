from django.urls import path
from .views import (
	EventDetailView, EventListView, EventCreateView, EventUpdateView, EventDeleteView,
	GuestListView, GuestCreateView, GuestUpdateView, GuestDetailView, GuestDeleteView,
	SendEmail, VerifyAttendance, success
)

app_name = 'event_management'
urlpatterns = [
	# EVENTS
	path('<username>/events/', EventListView.as_view(), name='event_management-events'),
	path('<username>/events/new/', EventCreateView.as_view(), name='event_management-create'),
	path('<username>/events/<int:pk>/', EventDetailView.as_view(), name='event_management-detail'),
	# Leave 'update' at the end - the user may have an event called 'update'
	path('<username>/events/<int:pk>/update/', EventUpdateView.as_view(), name='event_management-update'),
	path('<username>/events/<int:pk>/delete/', EventDeleteView.as_view(), name='event_management-delete'),

	# GUESTS
	path('<username>/<int:event_pk>/guests/', GuestListView.as_view(), name='guests'),
	path('<username>/<int:event_pk>/guests/new/', GuestCreateView.as_view(), name='guest-create'),
	path('<username>/<int:event_pk>/guest/<int:guest_pk>/', GuestDetailView.as_view(), name='guest-detail'),
	# Leave 'update' at the end - the user may have an event called 'update'
	path('<username>/<int:event_pk>/guest/<int:guest_pk>/update/', GuestUpdateView.as_view(), name='guest-update'),
	path('<username>/<int:event_pk>/guest/<int:guest_pk>/delete/', GuestDeleteView.as_view(), name='guest-delete'),

	# OTHER FUNCTIONALITY
	path('<username>/<int:event_pk>/guests/send-email', SendEmail.as_view(), name='guest-email'),
	path('event-verification/<int:guest_pk>/<str:token>/', VerifyAttendance.as_view(), name='guest-verify'),
	path('event-verification-success/<int:guest_pk>/', success, name='guest-verify-success'),

]
