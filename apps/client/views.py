from django.db.models import Count, Sum
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, DetailView
from django.contrib.auth.models import User
from django.db.models import Q

from apps.message_core.tasks import generate_number
from apps.core.models import State, City, Neighborhood, Place, Address
from .forms import *
from .models import *
from datetime import datetime, timedelta


"""
USUARIO VIEW
"""
class UsuarioList(View):
    template_name = "usuario/list.html"

    def get(self, request):
        usuario = Usuario.objects.all()
        if request.user.is_authenticated:
            user = request.user.pk
            usuario_master = Usuario.objects.filter(user__pk=user, user__is_superuser=True, tipo_usuario='Master')
            usuario_gerente = Usuario.objects.filter(user__pk=user, tipo_usuario='Gerente')
            usuario_supervisor = Usuario.objects.filter(user__pk=user, tipo_usuario='Supervisor')
            usuario_operador = Usuario.objects.filter(user__pk=user, tipo_usuario='Operador')
            if usuario_master:
                usuario_master = Usuario.objects.get(user__pk=user, user__is_superuser=True, tipo_usuario='Master')
                context = {'usuario_master': usuario_master}
            elif usuario_gerente:
                usuario_gerente = Usuario.objects.get(user__pk=user, tipo_usuario='Gerente')
                context = {'usuario_gerente': usuario_gerente}
            elif usuario_supervisor:
                usuario_supervisor = Usuario.objects.get(user__pk=user, tipo_usuario='Supervisor')
                context = {'usuario_supervisor': usuario_supervisor}
            elif usuario_operador:
                usuario_operador = Usuario.objects.get(user__pk=user, tipo_usuario='Operador')
                context = {'usuario_operador': usuario_operador}
                return redirect(reverse("dashboard_operador"))
            else:
                user = user
                context = {'user': user}
            
        context.update({'usuario': usuario})
        return render(request, self.template_name, context)


class UsuarioCreate(View):
    template_name = "usuario/create.html"

    def get(self, request):
        form = UsuarioForm()
        if request.user.is_authenticated:
            user = request.user.pk
            usuario_master = Usuario.objects.filter(user__pk=user, user__is_superuser=True, tipo_usuario='Master')
            usuario_gerente = Usuario.objects.filter(user__pk=user, tipo_usuario='Gerente')
            usuario_supervisor = Usuario.objects.filter(user__pk=user, tipo_usuario='Supervisor')
            usuario_operador = Usuario.objects.filter(user__pk=user, tipo_usuario='Operador')
            if usuario_master:
                usuario_master = Usuario.objects.get(user__pk=user, user__is_superuser=True, tipo_usuario='Master')
                context = {'usuario_master': usuario_master}
            elif usuario_gerente:
                usuario_gerente = Usuario.objects.get(user__pk=user, tipo_usuario='Gerente')
                context = {'usuario_gerente': usuario_gerente}
            elif usuario_supervisor:
                usuario_supervisor = Usuario.objects.get(user__pk=user, tipo_usuario='Supervisor')
                context = {'usuario_supervisor': usuario_supervisor}
            elif usuario_operador:
                usuario_operador = Usuario.objects.get(user__pk=user, tipo_usuario='Operador')
                context = {'usuario_operador': usuario_operador}
                return redirect(reverse("dashboard_operador"))
            else:
                user = user
                context = {'user': user}

        context.update({'form': form})
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UsuarioForm(request.POST, request.FILES)

        if form.is_valid():
            usuario = form.save(commit=False)
            new_user = User.objects.create_user(username=usuario.email, email=usuario.email, password='rifa2019')
            new_user.is_active = True
            new_user.first_name = usuario.nome_completo
            new_user.save()

            usuario.user = new_user
            usuario.save()

            return redirect(reverse("usuario-edit", kwargs={'pk': usuario.pk}))

        context = {'form':form}
        return render(request, self.template_name, context)


class UsuarioEdit(View):
    template_name = "usuario/edit.html"

    def get(self, request, pk):
        usuario = Usuario.objects.get(pk=pk)
        form = UsuarioForm(instance=usuario)
        if request.user.is_authenticated:
            user = request.user.pk
            usuario_master = Usuario.objects.filter(user__pk=user, user__is_superuser=True, tipo_usuario='Master')
            usuario_gerente = Usuario.objects.filter(user__pk=user, tipo_usuario='Gerente')
            usuario_supervisor = Usuario.objects.filter(user__pk=user, tipo_usuario='Supervisor')
            usuario_operador = Usuario.objects.filter(user__pk=user, tipo_usuario='Operador')

            if usuario_master:
                usuario_master = Usuario.objects.get(user__pk=user, user__is_superuser=True, tipo_usuario='Master')
                context = {'usuario_master': usuario_master}
            elif usuario_gerente:
                usuario_gerente = Usuario.objects.get(user__pk=user, tipo_usuario='Gerente')
                context = {'usuario_gerente': usuario_gerente}
            elif usuario_supervisor:
                usuario_supervisor = Usuario.objects.get(user__pk=user, tipo_usuario='Supervisor')
                context = {'usuario_supervisor': usuario_supervisor}
            elif usuario_operador:
                usuario_operador = Usuario.objects.get(user__pk=user, tipo_usuario='Operador')
                context = {'usuario_operador': usuario_operador}
                return redirect(reverse("dashboard_operador"))
            else:
                user = user
                context = {'user': user}

        context.update({'form': form, 'usuario':usuario})
        return render(request, self.template_name, context)

    def post(self, request, pk):    
        usuario = Usuario.objects.get(pk=pk)
        form = UsuarioForm(request.POST, request.FILES, instance=usuario)

        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()
            
            return redirect(reverse("usuario-list"))

        context = {'form':form, 'usuario':usuario}
        return render(request, self.template_name, context)


class UsuarioDelete(View):
    def get(self, request, pk):
        Usuario.objects.get(pk=pk).delete()
        return redirect(reverse("usuario-list"))

