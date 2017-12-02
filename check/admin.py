from django.contrib import admin
from .models import Check, Client, Bank, Store, Account

admin.site.register(Client)
admin.site.register(Store)
admin.site.register(Account)
admin.site.register(Bank)
admin.site.register(Check)