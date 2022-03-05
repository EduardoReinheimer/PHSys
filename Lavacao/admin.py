from django.contrib import admin
from .models import Etapa, Marca, Veiculo
# Register your models here.
admin.sites.site.register(Etapa)
admin.sites.site.register(Marca)
admin.sites.site.register(Veiculo)