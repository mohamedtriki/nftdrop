from django.contrib import admin
from .models import case,Profile


# Register your models here.
admin.site.register(case)
admin.site.register(Profile)
# @admin.register(case)
# class vehicleadmin(admin.ModelAdmin):
#     list_display=('case_title','case_price')