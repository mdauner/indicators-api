from django.core.management.base import BaseCommand
import requests
import logging

from ...models import DataSet

logger = logging.getLogger("django")

BASE_URL = "http://api.worldbank.org/v2/"


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        logger.info("Emptying table ...")
        DataSet.objects.all().delete()

        for indicator in DataSet.Indicator.choices:
            for country in DataSet.Country.choices:
                logger.info(
                    f"Importing data for indicator '{indicator[1]}' ({country[1]}) ..."
                )
                url = f"{BASE_URL}country/{country[0]}/indicator/{indicator[0]}"

                data = requests.get(
                    url,
                    params={"format": "json", "date": "1960:2018", "per_page": "100"},
                ).json()[1]

                DataSet.objects.create(
                    country=country[0],
                    indicator=indicator[0],
                    data={point["date"]: point["value"] for point in data},
                )

        logger.info(
            f"Fetched data for {len(DataSet.Indicator.choices)} indicators in {len(DataSet.Country.choices)} countries"
        )
