""" The art site views """
import random
from django.shortcuts import render
from django.views import View

from .models import ArtImage, Page, PageText, PageTitle

class Menu:
    """ Define the menu """
    def __init__(self, link, text):
        self.link = link
        self.text = text

def get_menu_list():
    """ get the menu list """
    all_pages = Page.objects.all()

    art_menu_list = list()
    for page in all_pages:
        menu = Menu(page.name.lower(), page.get_name_display())
        art_menu_list.append(menu)

    return art_menu_list

# Create your views here.

class IndexView(View):
    """ Define the index views """
    template_name = 'artfilters/index.html'

    def get(self, request):
        """ Get the data for the home page """
        home_page = Page.objects.get(name = "HOME")
        home_title = PageTitle.objects.get(page = home_page)
        home_text = PageText.objects.get(page = home_page)

        all_images = ArtImage.objects.all()
        index = random.randint(0, len(all_images) - 1)

        context = {
            'art_menu_list': get_menu_list(),
            'index_title': home_title.text,
            'index_intro': home_text.text,
            'index_image': all_images[index].file_name,
        }

        return render(request, 'artfilters/index.html', context)

class ManifestoView(View):
    """ Define the manifesto view """
    template_name = 'artfilters/manifesto.html'

    def get(self, request):
        """ Get the data for the manifesto page """
        manifesto_page = Page.objects.get(name = "MANIFESTO")
        manifesto_title = PageTitle.objects.get(page = manifesto_page)
        manifesto_text = PageText.objects.get(page = manifesto_page)

        context = {
            'art_menu_list': get_menu_list(),
            'manifesto_title': manifesto_title.text,
            'manifesto_intro': manifesto_text.text,
        }

        return render(request, 'artfilters/manifesto.html', context)

class ImagesView(View):
    """ Define the images view """
    template_name = 'artfilters/images.html'

    def get(self, request):
        """ Get the data for the images page """
        images_page = Page.objects.get(name = "IMAGES")
        images_title = PageTitle.objects.get(page = images_page)
        images_text = PageText.objects.get(page = images_page)

        context = {
            'art_menu_list': get_menu_list(),
            'images_title': images_title.text,
            'images_intro': images_text.text,
        }

        return render(request, 'artfilters/images.html', context)

class PrintView(View):
    """ Define the print view """
    template_name = 'artfilters/print.html'

    def get(self, request):
        """ Get the data for the print page """
        print_page = Page.objects.get(name = "PRINT")
        print_title = PageTitle.objects.get(page = print_page)
        print_text = PageText.objects.get(page = print_page)

        context = {
            'art_menu_list': get_menu_list(),
            'print_title': print_title.text,
            'print_intro': print_text.text,
        }

        return render(request, 'artfilters/print.html', context)

class BioView(View):
    """ Define the bio view """
    template_name = 'artfilters/bio.html'

    def get(self, request):
        """ Get the data for the bio page """
        bio_page = Page.objects.get(name = "BIO")
        bio_title = PageTitle.objects.get(page = bio_page)
        bio_text = PageText.objects.get(page = bio_page)

        context = {
            'art_menu_list': get_menu_list(),
            'bio_title': bio_title.text,
            'bio_intro': bio_text.text,
        }

        return render(request, 'artfilters/bio.html', context)

class ContactView(View):
    """ Define the the contact view """
    template_name = 'artfilters/contact.html'

    def get(self, request):
        """ Get the data for the contact page """
        contact_page = Page.objects.get(name = "CONTACT")
        contact_title = PageTitle.objects.get(page = contact_page)
        contact_text = PageText.objects.get(page = contact_page)

        context = {
            'art_menu_list': get_menu_list(),
            'contact_title': contact_title.text,
            'contact_intro': contact_text.text,
        }

        return render(request, 'artfilters/contact.html', context)

class BlogView(View):
    """ Define the blog view """
    template_name = 'artfilters/blog.html'

    def get(self, request):
        """ Get the data for the blog page """
        blog_page = Page.objects.get(name = "BLOG")
        blog_title = PageTitle.objects.get(page = blog_page)
        blog_text = PageText.objects.get(page = blog_page)

        context = {
            'art_menu_list': get_menu_list(),
            'blog_title': blog_title.text,
            'blog_intro': blog_text.text,
        }

        return render(request, 'artfilters/blog.html', context)
