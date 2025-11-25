from django.contrib import admin
from cars.models import Car,Brand




class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class  CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand','factor_year','model_year','value')
    search_fields = ('model',)



admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)