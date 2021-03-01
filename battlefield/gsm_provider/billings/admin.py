from django.contrib import admin
from billings.models import Call, ShortMessageService


class CallAdmin(admin.ModelAdmin):
    list_display = ('call_date', 'duration', 'customer_display')
    list_select_related = ('customer',)

    def customer_display(self, obj):
        return f'({obj.customer.id}) {obj.customer.username}'


class ShortMessageServiceAdmin(admin.ModelAdmin):
    list_display = ('content', 'send_date', 'customer_display')
    list_select_related = ('customer',)

    def customer_display(self, obj):
        return f'({obj.customer.id}) {obj.customer.username}'


admin.site.register(Call, CallAdmin)
admin.site.register(ShortMessageService, ShortMessageServiceAdmin)
