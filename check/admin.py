from django.contrib import admin
from .models import Check, Client, Bank, Store, Account, User

admin.site.register(Client)
admin.site.register(Store)
admin.site.register(User)
admin.site.register(Account)
admin.site.register(Bank)
admin.site.register(Check)