# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import IndexedTimeStampedModel


class Category(IndexedTimeStampedModel):
    name = models.CharField(
        verbose_name=_('Category'),
        max_length=150,
        db_index=True
    )
    slug = models.SlugField(
        verbose_name=_('Slug'),
        max_length=150,
        unique=True,
        db_index=True
    )

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = (
            'name',
        )

    def __str__(self):
        return self.name
