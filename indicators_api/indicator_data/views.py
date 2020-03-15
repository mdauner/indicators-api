from rest_framework import viewsets, mixins
from django_filters import rest_framework as filters
from .models import DataSet

from .serializers import DataSetSerializer


class DataSetViewSet(
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("indicator",)
