from django.urls import reverse
from django.db import models
from django.db.models.base import Model, ModelBase
from django.db.models.fields import BooleanField


class MainMenu(models.Model):
    """Model definition for MainMenu."""

    
    menu_item = models.CharField("Menu", max_length=50)
    memu_slug = models.SlugField("Slug")
    menu_visible = models.BooleanField(default=False)
    
    
    class Meta:
        """Meta definition for MainMenu."""

        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        """Unicode representation of MainMenu."""
        return self.menu_item

    
    # TODO: ეს გასარკვევი მაქვს
    def get_absolute_url(self):
        """Return absolute url for MainMenu."""
        return reverse(self.menu_slug)

    # TODO: Define custom methods here
    
 