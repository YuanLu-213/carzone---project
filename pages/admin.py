from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class Teamadmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.photos.url))

    thumbnail.short_description = 'photo'
    list_display = ('first_name', 'thumbnail', 'designation', 'created_data')
    list_display_links = ('first_name', 'thumbnail')
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation', )

admin.site.register(Team, Teamadmin)