from django.contrib import admin
from .models import Contact


class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'listing')
    list_per_page = 25


admin.site.register(Contact, ClassAdmin)
