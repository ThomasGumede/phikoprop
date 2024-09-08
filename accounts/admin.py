from django.contrib import admin
from accounts.models import Account, RelativeModel

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(RelativeModel)
class RelativeModelAdmin(admin.ModelAdmin):
    pass
