from django.contrib import admin

from .models import *

admin.site.register(Usuario)
admin.site.register(CartaoReal)
admin.site.register(CartaoVigente)
admin.site.register(Transacao)