from django.contrib import admin

from .models import ArtImage, ArtImageFilter, Page, PageText, PageTitle

# Register your models here.
admin.site.register(ArtImage)
admin.site.register(ArtImageFilter)
admin.site.register(Page)
admin.site.register(PageText)
admin.site.register(PageTitle)
