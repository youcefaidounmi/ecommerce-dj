from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    title = models.CharField(_('title'),max_length=50, unique=True)
    slug =  models.SlugField(_('slug'),max_length=100, unique=True)
    description = models.TextField(_('description'),max_length=200, blank=True)
    image = models.ImageField(_('image'),upload_to='images/categories', blank=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ('title',)

    def get_url(self):
        return reverse('store_by_category', args=[self.slug])

    def __str__(self):
        return self.title
