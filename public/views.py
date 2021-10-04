""" Views module

"""

from rest_framework import viewsets, permissions

from . import models, serializers


class NewsViewSet(viewsets.ModelViewSet):

    queryset = models.News.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.NewsSerializer


class LegalsViewSet(viewsets.ModelViewSet):

    queryset = models.Legals.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.LegalsSerializer
