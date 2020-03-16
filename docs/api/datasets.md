# DataSets
Supports viewing and updating indicator data.
 
## Update data value for year
 
**Request**:
 
`PUT/PATCH` `/display_data/:id/`
 
Parameters:
 
Name       | Type   | Description
-----------|--------|---
year       | string | The year for which the value should be changed.
value      | float  | The new value.
 
 
 
**Response**:
 
```json
Content-Type application/json
200 OK
 
{
   "id": 1,
   "country": "USA",
   "indicator": "SP.POP.TOTL",
   "data": {
       "1960": "180671000",
       "1961": "183691000",
       "1962": "186538000",
       "1963": "189242000"
   }
}
```
 
 
## List indicator data
 
**Request**:
 
`GET` `/display_data/`
 
**Query parameters**:
 
Name       | Type   | Description
-----------|--------|---
indicator  | string | Filters data by the specified indicator. Possible Values: `SP.POP.TOTL`, `NY.GDP.MKTP.CD`, `EN.ATM.CO2E.PC`, `SP.DYN.LE00.IN`, `TX.VAL.TECH.MF.ZS`, `IP.PAT.NRES`, `IP.PAT.RESD`
 
 
**Response**:
 
```json
Content-Type application/json
200 OK
 
[
   {
       "id": 1,
       "country": "USA",
       "indicator": "SP.POP.TOTL",
       "data": {
           "1960": "180671000",
           "1961": "183691000",
           "1962": "186538000",
           "1963": "189242000"
       }
   }
]
```
