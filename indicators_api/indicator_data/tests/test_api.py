from django.urls import reverse
import pytest

from .factories import DataSetFactory
from ..models import DataSet


@pytest.mark.django_db
def test_lists_datasets(api_client):
    dataset_1 = DataSetFactory()
    dataset_2 = DataSetFactory()

    url = reverse("dataset-list")
    response = api_client.get(url)

    dataset_ids = [dataset["id"] for dataset in response.data]

    assert response.status_code == 200
    assert len(response.data) == 2
    assert dataset_1.id in dataset_ids
    assert dataset_2.id in dataset_ids


@pytest.mark.django_db
def test_filters_datasets_by_indicator(api_client):
    indicator_1 = DataSet.Indicator.choices[0][0]
    indicator_2 = DataSet.Indicator.choices[1][0]
    dataset_1 = DataSetFactory(indicator=indicator_1)
    dataset_2 = DataSetFactory(indicator=indicator_1)
    DataSetFactory(indicator=indicator_2)

    url = reverse("dataset-list")
    response = api_client.get(url, data={"indicator": indicator_1})

    dataset_ids = [dataset["id"] for dataset in response.data]

    assert response.status_code == 200
    assert len(response.data) == 2
    assert dataset_1.id in dataset_ids
    assert dataset_2.id in dataset_ids


@pytest.mark.django_db
def test_returns_all_dataset_fields(api_client):
    dataset = DataSetFactory()

    url = reverse("dataset-detail", kwargs={"pk": dataset.id})
    response = api_client.get(url)

    assert response.status_code == 200
    assert list(response.data.keys()) == ["id", "country", "indicator", "data"]

