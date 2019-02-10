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
        context = {'usuario': usuario}
        return render(request, self.template_name, context)


class UsuarioCreate(View):
    template_name = "usuario/create.html"

    def get(self, request):
        form = UsuarioForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UsuarioForm(request.POST, request.FILES)

        if form.is_valid():
            usuario = form.save(commit=False)
            new_user = User.objects.create_user(username=usuario.email, email=usuario.email, password='apenasum2019')
            new_user.is_active = True
            new_user.first_name = usuario.nome_completo
            new_user.save()

            usuario.user = new_user
            usuario.save()

            return redirect(reverse("usuario-list"))

        context = {'form':form}
        return render(request, self.template_name, context)


class UsuarioEdit(View):
    template_name = "usuario/edit.html"

    def get(self, request, pk):
        usuario = Usuario.objects.get(pk=pk)
        form = UsuarioForm(instance=usuario)
        context = {'form': form, 'usuario':usuario}
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


"""
TRANSAÇÃO VIEW
"""
class TransacaoList(View):
    template_name = "transacao/list.html"

    def get(self, request):
        transacao = Transacao.objects.all()
        context = {'transacao': transacao}
        return render(request, self.template_name, context)


class TransacaoCreate(View):
    template_name = "transacao/create.html"

    def get(self, request):
        form = TransacaoForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = TransacaoForm(request.POST, request.FILES)

        if form.is_valid():
            transacao = form.save(commit=False)
            transacao.save()

            return redirect(reverse("transacao-list"))

        context = {'form':form}
        return render(request, self.template_name, context)


class TransacaoEdit(View):
    template_name = "transacao/edit.html"

    def get(self, request, pk):
        transacao = Transacao.objects.get(pk=pk)
        form = TransacaoForm(instance=transacao)
        context = {'form': form, 'transacao':transacao}
        return render(request, self.template_name, context)

    def post(self, request, pk):    
        transacao = Transacao.objects.get(pk=pk)
        form = TransacaoForm(request.POST, request.FILES, instance=transacao)

        if form.is_valid():
            transacao = form.save(commit=False)
            transacao.save()
            
            return redirect(reverse("transacao-list"))

        context = {'form':form, 'transacao':transacao}
        return render(request, self.template_name, context)


class TransacaoDelete(View):
    def get(self, request, pk):
        Transacao.objects.get(pk=pk).delete()
        return redirect(reverse("transacao-list"))
