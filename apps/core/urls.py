# -*- coding: utf-8 -*-
from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required

from allauth.account import views as authViews
from .views import SignUp, ConfirmSms, ChangePhone, ReSendSms, ExtraInfo
from . import views


'''
	DJANGO URLS
'''

allauth_urls = [
    # ACCOUNT
    path('accounts/login/', authViews.login, name="account_login"),
    path('accounts/logout/', authViews.logout, name="account_logout"),
    path('accounts/inactive/', authViews.account_inactive, name="account_inactive"),
    # PASSWORD CHANGE
    path('accounts/password/change/', authViews.password_change, name="account_change_password"),
    path('accounts/password/set/', authViews.password_set, name="account_set_password"),
    # EMAIL CONFIRMATION
    path('accounts/confirm-email/', authViews.email_verification_sent,name="account_email_verification_sent"),
    re_path(r'^accounts/confirm-email/(?P<key>[-:\w]+)/$', authViews.confirm_email, name="account_confirm_email"),
    # PASSWORD RESET
    path('accounts/password/reset/', authViews.password_reset, name="account_reset_password"),
    path('accounts/password/reset/done/', authViews.password_reset_done, name="account_reset_password_done"),
    re_path(r'^accounts/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$', authViews.password_reset_from_key, name="account_reset_password_from_key"),
    path('accounts/password/reset/key/done/', authViews.password_reset_from_key_done, name="account_reset_password_from_key_done"),
]

urlpatterns = [
    # CUSTOM AUTH
    path('accounts/signup/', SignUp.as_view(), name='account_signup'),
    re_path(r'^accounts/confirm-sms/(?P<pk>\d+)/$', ConfirmSms.as_view(), name='account_confirm_sms'),
    re_path(r'^accounts/resend-sms/(?P<pk>\d+)/$', ReSendSms.as_view(), name='account_resend_sms'),
    re_path(r'^accounts/change-phone/(?P<pk>\d+)/$', ChangePhone.as_view(), name='account_change_phone'),
    re_path(r'^accounts/extra-info/(?P<pk>\d+)/$', ExtraInfo.as_view(), name='account_extra_info'),
    
] + allauth_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
