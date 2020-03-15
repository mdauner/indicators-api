from django.db import models
from django.contrib.postgres.fields import HStoreField


class DataSet(models.Model):
    class Country(models.TextChoices):
        MEX = "mex", "Mexico"
        USA = "usa", "USA"
        IND = "ind", "India"
        CHN = "chn", "China"
        NGA = "nga", "Nigeria"

    class Indicator(models.TextChoices):
        POPULATION_TOTAL = "SP.POP.TOTL", "Population, total"
        GDP_TOTAL = "NY.GDP.MKTP.CD", "GDP, total"
        CO2_EMISSIONS = "EN.ATM.CO2E.PC", "CO2 Emissions"
        LIFE_EXPECTANCY = "SP.DYN.LE00.IN", "Life Expectancy at Birth"
        HIGH_TECHNOLOGY_EXPORTS = (
            "TX.VAL.TECH.MF.ZS",
            "High-technology exports (% of manufactured exports)",
        )
        PATENT_APPLICATIONS_NRES = "IP.PAT.NRES", "Patent Application, non-residents"
        PATENT_APPLICATIONS_RES = "IP.PAT.RESD", "Patent Application, residents"

    country = models.CharField(max_length=3, choices=Country.choices)
    indicator = models.CharField(max_length=20, choices=Indicator.choices)
    data = HStoreField()

    def __str__(self):
        return f"{self.indicator} ({self.get_country_display()})"
