# -*- coding: utf-8 -*-

from app import models
from app import serializers
from rest_framework import permissions
from app.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(operator=self.request.user)
