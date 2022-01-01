from django.urls import reverse
from django.db import models
from django.db.models.base import Model, ModelBase
from django.db.models.fields import BooleanField

# Create your models here.

class MainMenu(models.Model):
    """Model definition for MainMenu."""

    
    menuitem = models.CharField("Menu", max_length=50)
    mslug = models.SlugField("Slug")
    isvisible = models.BooleanField(default=False)
    
    
    class Meta:
        """Meta definition for MainMenu."""

        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        """Unicode representation of MainMenu."""
        return self.menuitem

    
    # TODO: ეს გასარკვევი მაქვს
    def get_absolute_url(self):
        """Return absolute url for MainMenu."""
        return reverse(self.mslug)

    # TODO: Define custom methods here
    
    
class Gallery(models.Model):
    """Model definition for Gallery."""
    ph_name = models.CharField("Name", max_length=50)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    style =  models.CharField("Style",max_length = 50)
    title = models.CharField(max_length = 255)
    content = models.TextField(blank=True)
    btitle = models.CharField(max_length = 150)
    bslug = models.SlugField(max_length = 50)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    
     
    # TODO: Define fields here

    class Meta:
        """Meta definition for Gallery."""

        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallerys'

    def __str__(self):
        """Unicode representation of Gallery."""
        return self.ph_name

    


    # TODO: Define custom methods here
    
class Category(models.Model):
    """Model definition for category."""

    # TODO: Define fields here
    name = models.CharField(max_length = 150,db_index=True)
    

    class Meta:
        """Meta definition for category."""

        verbose_name = 'category'
        verbose_name_plural = 'categorys'

    def __str__(self):
        """Unicode representation of category."""
        return self.name

    


    # TODO: Define custom methods here
