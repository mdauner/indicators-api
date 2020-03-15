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


@pytest.mark.django_db
def test_creates_new_dataset_value(api_client):
    dataset = DataSetFactory()
    year = "2020"
    value = "123.5"

    assert year not in dataset.data

    url = reverse("dataset-detail", kwargs={"pk": dataset.id})
    response = api_client.patch(url, data={"year": year, "value": value})

    dataset.refresh_from_db()

    assert dataset.data[year] == value
    assert response.status_code == 200
    assert response.data["id"] == dataset.id


@pytest.mark.django_db
def test_updates_existing_dataset_value(api_client):
    dataset = DataSetFactory()
    year = list(dataset.data.keys())[0]
    value = "123.5"

    url = reverse("dataset-detail", kwargs={"pk": dataset.id})
    response = api_client.patch(url, data={"year": year, "value": value})

    dataset.refresh_from_db()

    assert dataset.data[year] == value
    assert response.status_code == 200
    assert response.data["id"] == dataset.id


@pytest.mark.django_db
def test_throws_error_when_no_year_is_passed(api_client):
    dataset = DataSetFactory()
    value = "123.5"

    url = reverse("dataset-detail", kwargs={"pk": dataset.id})
    response = api_client.patch(url, data={"value": value})

    assert response.status_code == 400
    assert response.data["year"] == "This field is required."


@pytest.mark.django_db
def test_throws_error_when_no_value_is_passed(api_client):
    dataset = DataSetFactory()
    year = list(dataset.data.keys())[0]

    url = reverse("dataset-detail", kwargs={"pk": dataset.id})
    response = api_client.patch(url, data={"year": year})

    assert response.status_code == 400
    assert response.data["value"] == "This field is required."


@pytest.mark.django_db
def test_throws_error_when_year_is_not_valid(api_client):
    dataset = DataSetFactory()
    year = "abc"
    value = "123.5"

    url = reverse("dataset-detail", kwargs={"pk": dataset.id})
    response = api_client.patch(url, data={"year": year, "value": value})

    assert response.status_code == 400
    assert response.data["year"][0] == "A valid year is required."


@pytest.mark.django_db
def test_throws_error_when_value_is_not_a_number(api_client):
    dataset = DataSetFactory()
    year = list(dataset.data.keys())[0]
    value = "abc"

    url = reverse("dataset-detail", kwargs={"pk": dataset.id})
    response = api_client.patch(url, data={"year": year, "value": value})

    assert response.status_code == 400
    assert response.data["value"][0] == "A valid number is required."
