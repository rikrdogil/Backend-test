from django.contrib import admin

# Register your models here.
from api.models import Produto,Categoria

admin.site.register(Produto)
admin.site.register(Categoria)
