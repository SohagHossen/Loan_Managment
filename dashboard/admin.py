from django.contrib import admin
from dashboard.models import Desh_inf
# Register your models here.
class DeshInfAdmin(admin.ModelAdmin):
    list_display = ('desh_name','desh_age')
admin.site.register(Desh_inf,DeshInfAdmin)