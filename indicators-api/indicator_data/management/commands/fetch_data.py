from django.core.management.base import BaseCommand
import requests


COUNTRIES = ["usa", "mex", "ind", "chn", "nga"]
INDICATORS = [
    "SP.POP.TOTL",
    "NY.GDP.MKTP.CD",
    "EN.ATM.CO2E.PC",
    "SP.DYN.LE00.IN",
    "TX.VAL.TECH.MF.ZS",
    "IP.PAT.NRES",
    "IP.PAT.RESD",
]
BASE_URL = "http://api.worldbank.org/v2/"


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for indicator in INDICATORS:
            for country in COUNTRIES:
                url = f"{BASE_URL}country/{country}/indicator/{indicator}"
                data = requests.get(
                    url, params={"format": "json", "date": "1960:2018"},
                ).json()[1]

                print(data)
