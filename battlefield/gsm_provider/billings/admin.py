from django.contrib import admin
from billings.models import Call, ShortMessageService


class CallAdmin(admin.ModelAdmin):
    list_display = ('call_date', 'duration', 'caller', 'callee')
    list_select_related = ('caller', 'callee')


class ShortMessageServiceAdmin(admin.ModelAdmin):
    list_display = ('content', 'send_date', 'sending_party_id', 'sent_party_id')
    list_select_related = ('sending_party_id', 'sent_party_id')

admin.site.register(Call, CallAdmin)
admin.site.register(ShortMessageService, ShortMessageServiceAdmin)
