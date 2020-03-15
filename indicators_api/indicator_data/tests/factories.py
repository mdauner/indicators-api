import factory
from factory.fuzzy import FuzzyChoice

from ..models import DataSet


class DataSetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DataSet

    country = FuzzyChoice(DataSet.Country)
    indicator = FuzzyChoice(DataSet.Indicator)
    data = {"1980": "123.0", "1981": "130.4", "1982": "150.9"}
