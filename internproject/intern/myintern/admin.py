from django.contrib import admin
from .models import Report 
# Register your models here.
# admin.site.register(Report)

@admin.register(Report)
class ReportModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'location', 'date']