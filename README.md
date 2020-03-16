# indicators-api

[DEMO](https://indicators-api.herokuapp.com/api/v1/)
 
## Prerequisites
 
- [Docker](https://docs.docker.com/docker-for-mac/install/) 
 
## Initialize the project
 
Start the dev server for local development:
 
```bash
docker-compose up
```

After the dev server is started you can go to the [API Documentation](http://localhost:8001/) and the [Browsable API](http://localhost:8000/).
 
A [Visual Studio Code dev container](https://code.visualstudio.com/docs/remote/containers) configuration is also part of this project.
 
## Import data
 
This project can import data from the World Bank Indicators API.
 
 
To fetch and import data run this command:
```bash
docker-compose run --rm web python manage.py fetch_data
```
 
This imports the following indicators for the most populous countries (USA, Mexico, India, Nigeria, China):
 
Name              |Description       |
------------------|------------------|
SP.POP.TOTL       | Population, total
NY.GDP.MKTP.CD    | GDP, total
EN.ATM.CO2E.PC    | CO2 emissions
SP.DYN.LE00.IN    | Life Expectancy at Birth
TX.VAL.TECH.MF.ZS | High-technology exports (% of manufactured exports)
IP.PAT.NRES       | Patent Application, non-residents
IP.PAT.RESD       | Patent Application, residents

 
## Tests
 
```bash
docker-compose run --rm web pytest
```
