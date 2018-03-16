# -*- coding: utf-8 -*-

from django_filters.rest_framework import FilterSet

from .models import Ticket


class TicketFilter(FilterSet):
    class Meta:
        model = Ticket
        fields = {
            'created_at': ['lte', 'gte'],
            'title': ['exact'],
            'state': ['exact']
        }
