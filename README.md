# Dashboard-Sensor2
Dit is een voortvloeing van de eerste versie Dashboard-sensor.
Het probleem van het scherm updaten is opgelost door gebruik van de bib 'Pygame'

## Beschrijving
Het project zal via externe sensoren temperatuur, luchtvochtigheid, luchtdruk en CO2 meten en deze zichtbaar maken.
Het zichtbaar maken gebeurt grafisch, een 4-tal wijzers geven de de waarden weer.
In het midden wordt de tijd en datum ook zichtbaar gemaakt

## Bronnen

.

## Hardware
Voor dit project gebruiken we een BME680 (temperatuur, vochtigheid en luchtdruk) van Bosch en de SCD30 een CO2 meter met temperatur en vochtigheid. 
Beide worden via de I2C-bus uitgelezen.
 
## Software
De BME680 en de SCD30 sensoren worden via de I2C-bus aangesloten.
https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas/python-circuitpython en
https://pypi.org/project/adafruit-circuitpython-scd30/
Beide sensoren worden iedere x-seconden uitgelezen en de data wordt opgeslagen om later in het programma zichtbaar te maken. 
Voor dit project worden wijzers gebruikt om de huidige waarden zichbaar te maken.
We gebruiken 'Pygame' die een snelle toegang geeft tot het (deel)scherm. Ook een snelle en onzichtbare update is mogelijk, wat het doel is.  
Een combinatie van 4 wijzers worden gebruikt om de volgende gegevens zichtbaar te maken: temperatuur, vochtigheid, luchtdruk en CO2.
Daarvoor was een voorbeeld te vinden op https://github.com/wahajmurtaza/Pygame_Percent_Gauge

### Eigen scripts en programma's
Zie in bijlage.
