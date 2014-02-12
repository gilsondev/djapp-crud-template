# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

class {{ app_name|title }}(models.Model):
    slug = models.SlugField(_(u"Slug"), max_length=255, unique=True)

    class Meta:
        db_table = "{{ app_name }}"

    def __unicode__(self):
        pass
