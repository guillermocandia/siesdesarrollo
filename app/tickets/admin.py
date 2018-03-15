# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import State
from .models import Ticket


class StateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'state']
    list_editable = ['state']
    list_filter = ['state']
    fields = ['title', 'description', 'state', 'created_at']
    readonly_fields = ['created_at']
    search_fields = ['title', 'description']


admin.site.register(State, StateAdmin)
admin.site.register(Ticket, TicketAdmin)
