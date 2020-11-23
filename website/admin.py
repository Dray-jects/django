from django.contrib import admin
from .models import gallery ,buy,contact,aboutus
from  clerk.models import stock
admin.site.register(gallery)
admin.site.register(buy)

admin.site.register(aboutus)

class contactAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(contact,contactAdmin)



