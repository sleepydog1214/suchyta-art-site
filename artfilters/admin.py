""" Art filters admin """
from django.contrib import admin

from .models import ArtImage, ArtImageFilter, Page, PageText, PageTitle

class ArtImageAdmin(admin.ModelAdmin):
    """ Art image admin class """
    fieldsets = [
        ('File information', {'fields': ['file_name', 'path', 'file_size', 'type']}),
        ('Image details', {'fields': ['description', 'height', 'width']}),
    ]

    list_display = ('path', 'description', 'file_size')

# Register your models here.
admin.site.register(ArtImage, ArtImageAdmin)
admin.site.register(ArtImageFilter)
admin.site.register(Page)
admin.site.register(PageText)
admin.site.register(PageTitle)
