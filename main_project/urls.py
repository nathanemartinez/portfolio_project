"""main_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import handler400, handler403, handler404, handler500
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # 'BASIC' PAGES
    path('', views.index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('projects/', views.projects, name='projects'),
    path('about/', views.about, name='about'),
    path('', include('users.urls')),


    # TEST ERROR PAGES
    path('400/', views.error_400, name='400'),
    path('403/', views.error_403, name='403'),
    path('404/', views.error_404, name='404'),
    path('500/', views.error_500, name='500'),


    # TESTER PAGES
    path('tester1/', views.tester1, name='tester1'),
    # path('tester2/', views.tester2, name='tester2'),


    # INCLUDING APP URLS
    path('', include('broken_link_checker.urls')),
    path('', include('quizlet_study_tool.urls')),
    path('', include('event_management.urls')),
    path('', include('site_down.urls')),


    # RESET PASSWORD - names must be exact
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]

# Overwrites the default error pages
handler400 = 'main_project.views.error_400'
handler403 = 'main_project.views.error_403'
handler404 = 'main_project.views.error_404'
handler500 = 'main_project.views.error_500'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
