""" The art site models """
from django.db import models

# Create your models here.

IMAGE_TYPES = (
    ('JPG', 'Joint Photographic Experts Group'),
    ('PNG', 'Portable Network Graphics'),
    ('SVG', 'Scalable Vector Graphics')
)


class ArtImage(models.Model):
    """ The art image model """
    imgPath = '/mnt/d/development/python3_env/suchyta-art-site/artfilters/static/artfilters/images'

    file_name = models.CharField(max_length=160)
    path = models.FilePathField(path=imgPath, max_length=255)
    file_size = models.IntegerField(default=0)
    type = models.CharField(max_length=10, choices=IMAGE_TYPES)
    description = models.TextField()
    height = models.SmallIntegerField()
    width = models.SmallIntegerField()
    date_created = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)

class ArtImageFilter(models.Model):
    """ The art image filter model """
    name = models.CharField(max_length=80)
    type = models.CharField(max_length=10, choices=IMAGE_TYPES)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)

class Page(models.Model):
    """ The art site page model """
    PAGE_NAMES = (
        ('HOME', 'Home'),
        ('MANIFESTO', 'Manifesto'),
        ('IMAGES', 'Available Images'),
        ('PRINT', 'Printer Links'),
        ('BIO', 'Bio'),
        ('CONTACT', 'Contact'),
        ('BLOG', 'Blog')
    )
    name = models.CharField(max_length=25, choices=PAGE_NAMES)
    date_created = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)

class PageText(models.Model):
    """ The art site page text model """
    name = models.CharField(max_length=80)
    text = models.TextField()
    page = models.ForeignKey(Page, on_delete = models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)

class PageTitle(models.Model):
    """ The art site page title model """
    name = models.CharField(max_length=80)
    text = models.TextField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)
