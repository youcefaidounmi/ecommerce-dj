from django.db import models
from django.utils.translation import gettext_lazy as _
from category.models import Category

# Create your models here.
class Product(models.Model):
    title = models.CharField(_('title'), max_length=200, unique=True)
    slug = models.SlugField(_('slug'), max_length=200, unique=True)
    description = models.TextField(_('description'), max_length=600, blank=True)
    price = models.IntegerField(_('price'))
    image = models.ImageField(_('image'), upload_to='images/products')
    stock = models.IntegerField(_('stock'))
    is_available = models.BooleanField(_('is available'), default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories', verbose_name='category')
    created_date = models.DateTimeField(_('created date'), auto_now_add=True)
    modified_date = models.DateTimeField(_('modified date'), auto_now=True)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ('-modified_date',)
        

    def __str__(self):
        return self.title
