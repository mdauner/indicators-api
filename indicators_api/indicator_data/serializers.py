from rest_framework import serializers
import re

from .models import DataSet


class DataSetSerializer(serializers.ModelSerializer):
    country = serializers.CharField(read_only=True, source="get_country_display")
    year = serializers.CharField(write_only=True)
    value = serializers.FloatField(write_only=True)

    class Meta:
        model = DataSet
        fields = ["id", "country", "indicator", "data", "year", "value"]
        read_only_fields = ["indicator", "data"]

    def validate_year(self, year):
        match = re.match(r"^\d{4}$", year)
        if match:
            return year
        raise serializers.ValidationError("A valid year is required.")

    def update(self, instance, validated_data):
        year = validated_data.get("year")
        value = validated_data.get("value")

        if not year:
            raise serializers.ValidationError({"year": "This field is required."})

        if not value:
            raise serializers.ValidationError({"value": "This field is required."})

        instance.data[year] = value
        instance.save()
        return instance
