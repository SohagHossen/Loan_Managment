from django.contrib import admin
from  customer.models import customer_data

# Register your models h

class customeradmin(admin.ModelAdmin):
    list_display =("id","first_name","last_name","email")

admin.site.register(customer_data,customeradmin)


