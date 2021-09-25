from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


class ModalFormAdmin(admin.ModelAdmin):
    list_display = ['name','email','created']
    list_filter = ['created']

class BiharPropertyAdmin(admin.ModelAdmin):
    list_display = ['name','email','created']

admin.site.register(EnquiryForm)
admin.site.register(ContactForm)
admin.site.register(BiharPropertyContactForm,BiharPropertyAdmin)
admin.site.register(ModalForm,ModalFormAdmin)
admin.site.register(PatnaPropertyContactForm)
admin.site.register(CareerForm)

#unregistered models
# admin.site.unregister(Group)