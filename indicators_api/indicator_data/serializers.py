from rest_framework import serializers

from .models import DataSet


class DataSetSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source="get_country_display")

    class Meta:
        model = DataSet
        fields = ["id", "country", "indicator", "data"]
