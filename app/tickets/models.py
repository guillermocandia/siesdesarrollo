# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class State(models.Model):
    """
    State
    """

    name = models.CharField(
       verbose_name='Name',
       max_length=64,
       blank=False,
       null=False,
       unique=True
    )

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.name


class Ticket(models.Model):
    """
    Ticket
    """

    title = models.CharField(
       verbose_name='Titulo',
       max_length=64,
       blank=False,
       null=False
    )

    description = models.CharField(
       verbose_name='Descripción',
       max_length=256,
       blank=True,
       null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    state = models.ForeignKey(
        State,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'

    def __str__(self):
        return self.title
