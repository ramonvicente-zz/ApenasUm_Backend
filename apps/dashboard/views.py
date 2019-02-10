from django.shortcuts import render
from django.views.generic import View
from apps.client.models import *


class Dashboard(View):
    template_name = "dashboard.html"        

    def get(self, request):
        if request.user.is_authenticated:
            user = request.user.pk
            usuario_master = Usuario.objects.filter(user__pk=user, tipo_usuario='Master', user__is_superuser=True)
            usuario_gerente = Usuario.objects.filter(user__pk=user, tipo_usuario='Gerente')
            usuario_supervisor = Usuario.objects.filter(user__pk=user, tipo_usuario='Supervisor')
            usuario_operador = Usuario.objects.filter(user__pk=user, tipo_usuario='Operador')
            
            if usuario_master:
                usuario_master = Usuario.objects.get(user__pk=user, user__is_superuser=True, tipo_usuario='Master')
                context = {'usuario_master': usuario_master}
            elif usuario_gerente:
                usuario_gerente = Usuario.objects.get(user__pk=user, tipo_usuario='Gerente')
                context = {'usuario_gerente': usuario_gerente}
                return redirect(reverse("dashboard_gerente"))
            elif usuario_supervisor:
                usuario_supervisor = Usuario.objects.get(user__pk=user, tipo_usuario='Supervisor')
                context = {'usuario_supervisor': usuario_supervisor}
                return redirect(reverse("dashboard_supervisor"))
            elif usuario_operador:
                usuario_operador = Usuario.objects.get(user__pk=user, tipo_usuario='Operador')
                context = {'usuario_operador': usuario_operador}
                return redirect(reverse("dashboard_operador"))
            else:
                user = user
                context = {'user': user}
            
        context.update({})
        return render(request, self.template_name, context)
