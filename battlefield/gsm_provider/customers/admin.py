from django.contrib import admin
from customers.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'username')


admin.site.register(Customer, CustomerAdmin)
