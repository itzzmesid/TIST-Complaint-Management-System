from django.contrib import admin
from .models import Complaint

class ComplaintDisplay(admin.ModelAdmin):
    list_display = ('user', 'Title', 'Time')
    readonly_fields = ('id', 'Time')

admin.site.register(Complaint, ComplaintDisplay)