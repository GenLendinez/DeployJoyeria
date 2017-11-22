from django.contrib import admin
from .models import Reloj

# Register your models here.

#admin.site.register(Watch)

class WatchAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca','precio')
admin.site.register(Reloj, WatchAdmin)
