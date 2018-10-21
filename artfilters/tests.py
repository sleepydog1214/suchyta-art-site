""" The artfilters tests """
from django.test import TestCase
from django.urls import reverse

from .models import ArtImage, Page, PageText, PageTitle

# Create your tests here.
class ArtImageModelTests(TestCase):
    """ ArtImage Model tests """

    def test_artimage_has_filename(self):
        """ Test that each image has a file name """
        image_list = ArtImage.objects.all()
        for image in image_list:
            self.assertIsNotNone(image.file_name)

class BioViewTests(TestCase):
    """ Index View tests """

    def create_bio_page(self):
        """ Create the Bio page """
        bio = Page.objects.create(name='BIO');
        PageTitle.objects.create(name='Bio', text='Thomas Suchyta Art', page=bio)
        PageText.objects.create(name='Bio', text='Bio page text.', page=bio)
        return bio

    def test_bio_has_menu(self):
        """ Test that the index page has a menu """
        bio = self.create_bio_page()
        self.assertIsNotNone(bio)

        response = self.client.get(reverse('artfilters:bio'))
        self.assertEqual(response.status_code, 200)

        menu = response.context['art_menu_list']
        self.assertGreater(len(menu), 0)