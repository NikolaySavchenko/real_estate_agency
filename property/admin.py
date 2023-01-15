from django.contrib import admin

from .models import *

class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ('created_at',)
    list_display = ('id', 'address', 'price', 'new_building',
                    'construction_year', 'town')
    inlines = [OwnerInline]
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('liked_by',)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat',)

class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('full_name',)
    list_display = ('full_name', )
    raw_id_fields = ('flats',)



admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
