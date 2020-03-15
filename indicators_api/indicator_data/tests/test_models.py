import pytest

from .factories import DataSetFactory


@pytest.mark.django_db
def test_str():
    data_point = DataSetFactory()

    assert (
        str(data_point)
        == f"{data_point.indicator} ({data_point.get_country_display()})"
    )
