# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .category import Category


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name=_('Category'),
        related_name='products',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=100,
        db_index=True
    )
    slug = models.SlugField(
        verbose_name=_('Slug'),
        max_length=100,
        db_index=True
    )
    description = models.TextField(
        verbose_name=_('Description'),
        blank=True
    )
    price = models.DecimalField(
        verbose_name=_('Price'),
        max_digits=10,
        decimal_places=2
    )
    available = models.BooleanField(
        verbose_name=_('Available'),
        default=True
    )
    stock = models.PositiveIntegerField(
        verbose_name=_('Stock')
    )
    image = models.ImageField(
        verbose_name=_('Image'),
        upload_to='products/%Y/%m/%d',
        blank=True
    )

    class Meta:
        index_together = (('id', 'slug'),)
        ordering = (
            'name',
        )

    def __str__(self):
        return self.name
