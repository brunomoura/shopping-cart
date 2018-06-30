from model_utils.fields import AutoCreatedField, AutoLastModifiedField

from django.db import models
from django.utils.translation import ugettext_lazy as _


class IndexedTimeStampedModel(models.Model):
    created = AutoCreatedField(
        _('created'),
        db_index=True
    )
    modified = AutoLastModifiedField(
        _('modified'),
        db_index=True
    )

    class Meta:
        abstract = True
