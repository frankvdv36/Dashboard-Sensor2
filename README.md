# Dashboard-Sensor2
Dit is een voortvloeing van de eerste versie Dashboard-sensor.
Het probleem van het scherm updaten is opgelost door gebruik van de bib 'Pygame'

## Beschrijving
Het project zal via externe sensoren temperatuur, luchtvochtigheid, luchtdruk en CO2 meten en deze zichtbaar maken.
Het zichtbaar maken gebeurt grafisch, een 4-tal wijzers geven de de waarden weer.
In het midden wordt de tijd en datum ook zichtbaar gemaakt

## Bronnen
https://github.com/wahajmurtaza/Pygame_Percent_Gauge/blob/main/percentage_gauge.py
https://www.pygame.org/docs/ref/gfxdraw.html
https://www.w3schools.com/colors/default.asp 
https://github.com/adafruit/Adafruit_CircuitPython_BME680
/usr/local/lib/python3/ is het pad waar de Modules te vinden zijn

## Hardware
Voor dit project gebruiken we een BME680 (temperatuur, vochtigheid en luchtdruk) van Bosch en de SCD30 een CO2 meter met temperatur en vochtigheid. 
Beide worden via de I2C-bus uitgelezen.
 
## Software
De BME680 en de SCD30 sensoren worden via de I2C-bus aangesloten.
https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas/python-circuitpython en
https://pypi.org/project/adafruit-circuitpython-scd30/
Beide sensoren worden iedere x-seconden uitgelezen en de data wordt opgeslagen om later in het programma zichtbaar te maken. 
Voor dit project worden wijzers gebruikt om de huidige waarden zichbaar te maken.
We gebruiken 'Pygame' die een snelle toegang geeft tot het (deel)scherm. Ook een snelle en onzichtbare update is mogelijk, wat het doel was.  
Een combinatie van 4 wijzers worden gebruikt om de volgende gegevens zichtbaar te maken: temperatuur, vochtigheid, luchtdruk en CO2 aangevuld mùet de tijd en datum in tekstvorm. Een voorbeeld is te vinden op https://github.com/wahajmurtaza/Pygame_Percent_Gauge. Van hieruit heb ik de aanpassingen gemaakt naar het eindresultaat.

### Eigen scripts en programma's
Zie in bijlage.
