# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import State
from .models import Ticket
from .serializers import StateSerializer
from .serializers import TicketSerializer
from .serializers import UserSerializer
from .filters import TicketFilter
from .permissions import IsStaffOrReadOnly


class StateList(generics.ListCreateAPIView):
    """
    get:
        Retorna lista de Estados.
    post:
        Crea Estado.
    """

    queryset = State.objects.all()
    permission_classes = (IsAuthenticated, IsStaffOrReadOnly)
    serializer_class = StateSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'id')


class StateDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
        Retorna Estado.
    put:
        Modifica Estado.
    delete:
        Elimina Estado.
    """

    queryset = State.objects.all()
    permission_classes = (IsAuthenticated, IsStaffOrReadOnly)
    serializer_class = StateSerializer


class TicketList(generics.ListCreateAPIView):
    """
    get:
        Retorna lista de Tickets.
    post:
        Crea Ticket.
    """

    queryset = Ticket.objects.all()
    permission_classes = (IsAuthenticated, IsStaffOrReadOnly)
    serializer_class = TicketSerializer
    filter_class = TicketFilter
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('title', 'description', 'state__name')
    ordering_fields = ('title', 'id', 'created_at',)


class TicketDetail(generics.RetrieveUpdateAPIView):
    """
    get:
        Retorna Ticket.
    put:
        Modifica Ticket.
    """

    queryset = Ticket.objects.all()
    permission_classes = (IsAuthenticated, IsStaffOrReadOnly)
    serializer_class = TicketSerializer


class Logout(APIView):
    """
    get:
        Elimina token(si existe)
    """

    def get(self, request, format=None):
        if(hasattr(request.user, 'auth_token')):
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CheckToken(APIView):
    """
    get:
        Retorna usuario actual
    """
    serializer_class = UserSerializer

    def get(self, request, format=None):
        user = request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data)
