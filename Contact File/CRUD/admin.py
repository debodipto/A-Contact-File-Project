from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')  # Fields to display in the admin list view
    search_fields = ('name', 'phone', 'email')  # Adds a search box to the admin
    list_filter = ('email',)  # Adds a filter sidebar by the specified field(s)
