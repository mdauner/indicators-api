from rest_framework import viewsets, mixins
from .models import DataSet

from .serializers import DataSetSerializer


class DataSetViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
):
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer
