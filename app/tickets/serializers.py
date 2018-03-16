# -*- coding: utf-8 -*-
from django.contrib.auth.models import User

from rest_framework import serializers

from .models import State
from .models import Ticket


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'last_login', 'is_superuser',
                  'first_name', 'last_name', 'email',
                  'is_staff', 'is_active', 'date_joined')
