#-*- coding: utf-8 -*-

from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.views.generic import View
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
	path('usuario/list/', login_required(views.UsuarioList.as_view()), name='usuario-list'),
    path('usuario/create/', login_required(views.UsuarioCreate.as_view()), name='usuario-create'),
    path('usuario/edit/<int:pk>/', login_required(views.UsuarioEdit.as_view()), name='usuario-edit'),
    path('usuario/delete/<int:pk>/', login_required(views.UsuarioDelete.as_view()), name='usuario-delete'),

    path('transacao/list/', login_required(views.TransacaoList.as_view()), name='transacao-list'),
    path('transacao/create/', login_required(views.TransacaoCreate.as_view()), name='transacao-create'),
    path('transacao/edit/<int:pk>/', login_required(views.TransacaoEdit.as_view()), name='transacao-edit'),
    path('transacao/delete/<int:pk>/', login_required(views.TransacaoDelete.as_view()), name='transacao-delete'),
]