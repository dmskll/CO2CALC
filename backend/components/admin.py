from django.contrib import admin

from .models import Component, ComponentUsage, ComponentList



class ComponentAdmin (admin.ModelAdmin):
    list_display = ('name', 'owner_name')
    search_fields = ['name', 'owner_name']
    list_filter = ['system_component']
    def owner_name(self, obj):
        return obj.owner.username

admin.site.register(Component, ComponentAdmin)
# admin.site.register(CustomComponent, ComponentAdmin)
admin.site.register(ComponentUsage)
admin.site.register(ComponentList)