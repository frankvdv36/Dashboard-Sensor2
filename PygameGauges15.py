# https://github.com/wahajmurtaza/Pygame_Percent_Gauge/blob/main/percentage_gauge.py
# https://www.pygame.org/docs/ref/gfxdraw.html
# https://www.w3schools.com/colors/default.asp 
# https://github.com/adafruit/Adafruit_CircuitPython_BME680
# /usr/local/lib/python3/ is het pad waar de Modules te vinden zijn 
# i2cdetect -y 1        # Scan I2C in terminal

import pygame
import pygame.gfxdraw
import math
import time
from time import gmtime, strftime

import board
import adafruit_bme680
import adafruit_scd30                   # pip3 install adafruit-circuitpython-scd30

circle_c = (150, 150, 150)              # background color circle
bg_c = (70, 70, 70)                  # background color
width, height = (1680, 990)            # window afmetingen 1680x990 vol

lavender= (255, 240, 245)
darkblue= ( 0, 0, 139)
sladegray= (112, 128, 144)
palegreen= (152, 251, 152)
Tomato= (255, 99, 71)
lightblue= (173, 216, 230)
navajowhite= (255, 222, 173)

titel= 'Dashboard'                    # txt bovenrand          
#txtcenter = 'Dashboard'               # txt center beeld, staat bij Linksboven
txt = [255, 222, 173]                   # Txt midden voor tijd en datum
x1 =  600       # X positie txt midden was 660 zonder GMT
y1 =  475       # y positie txt midden

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25       # correctie huidige luchtdruk
temperature_offset = -1                   # correctie op de sensor in °C

# Declair variablen
now =0      # tijd en datum in 1 getal
temp = 20    # BME680
hum = 50
air =0 
press = 1013
co2 = 825      # SCD30
temp2 = 22
hum2 = 45
ts = time.gmtime()

#-----------------------------------------------------------------------

# Deze functie leest 2 sensoren uit. BME680 (0x77) en SCD30 (0x62). 

def readSensor():
    
    global mylist    
    global temp
    global hum 
    global press
    global temp2
    global hum2 
    global co2
    global ts
    
    i2c = board.I2C()               # uses board.SCL and board.SDA
    scd = adafruit_scd30.SCD30(i2c) # address is 0x62 Zie 'sudo i2cdetect -y'
    if scd.data_available:
        scdData = [round(scd.CO2), round(scd.temperature,1), round(scd.relative_humidity,1)]
        co2 = scdData[0]; temp2 = scdData[1]; hum2 = scdData[2]
        temp2 = temp2 -1.5          # correctie op de temperatuur
        #print('CO2: ',co2); print('temp2: ',temp2); print('hum2: ',hum2)
     
  
    ts = time.gmtime()
    #now = time.localtime()           # Bevat juiste tijd maar we kunnen het niet zichtbaar maken in eigen structuur
    #print ("now= ",now)
    #print ("time.localtime() : %s" % time.localtime())
    
    temp = bme680.temperature       # 
    hum = bme680.relative_humidity  # address is 0x77 Zie 'sudo i2cdetect -y'   
    press = bme680.pressure          # "Alle 4 zijn is een float"
    air = bme680.gas
    temp = round (temp,1); hum = round (hum,1); press = round (press); 
    #air = round (air); #now = round(now)
    mylist = [temp, hum, press, air, co2, temp2, hum2]    
    print (mylist)
    return
 
#-----------------------------------------------------------------------

class Gauge:
    def __init__(self, screen, FONT, x_cord, y_cord, thickness, radius, circle_colour, glow=True):
        self.screen = screen
        self.Font = FONT
        self.font = pygame.font.SysFont('Arial', 50) # extra text boog
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.thickness = thickness
        self.radius = radius
        self.circle_colour = circle_colour
        self.glow = glow
                
#-----------------------------------------------------------------------
# Links boven

    def draw1(self, percent): 
            
        acc1 = [250,250,0]    # kleur boog indien geen voorwaarden waarbij kleuren veranderen
        ac1 = [255,255,0] # kleur txt center boog 
        txt1 = [255,255,255] # kleur txt 
                                    
        fill_angle = int((temp2+20)*270/80)       # hoek 270° per %
        if fill_angle >= 270:
            fill_angle = 280                     # boog 100% opvullen
        if fill_angle <=10:                             
            fill_angle =10                        # boog 2.7% opvullen
        '''    
        if fill_angle >=0 and fill_angle <=68:    # tussen -20 en 0 Blauw (regel van drie met 270°)
            acc1 = [173, 216, 230]
        if fill_angle >= 68 and fill_angle <155: # tussen 0 en 25 groen
            acc1 = [0,250,0]  
        if fill_angle >= 155 and fill_angle <= 280:# boven 25 Rood             
            acc1 = [255,0,0]                       # kleur boog    
        '''    
        pertext = self.Font.render(str(temp2) + "°C", True, ac1)  # °C of % of hpa                                    # Temperatuur in °C
        pertext_rect = pertext.get_rect(center=(int(self.x_cord), int(self.y_cord)))
        #self.screen.blit(self.Font.render(txtcenter, True, txt), (x1,y1))                                               # Txt midden in beeld
        self.screen.blit(self.Font.render(time.strftime("%H:%M GMT %d-%m", ts), True, txt), (x1,y1))                     # Txt midden in beeld
        #self.screen.blit(self.Font.render(strftime("%H:%M   %d-%m", ts), True, txt), (x1,y1))                          # Txt midden in beeld
        self.screen.blit(self.font.render('Temperatuur', True, txt1), (int(self.x_cord/1.5), int(self.y_cord*1.7)))     # TEXT bij boog = OK
        self.screen.blit(self.font.render('-20', True, acc1), (int(self.x_cord*0.7), int(self.y_cord*1.4)))              # cijfer begin boog
        self.screen.blit(self.font.render('60', True, acc1), (int(self.x_cord*1.15), int(self.y_cord*1.4)))              # cijfer einde boog
        self.screen.blit(pertext, pertext_rect) # laat text zijn binnen boog (zonder deze lijn zien we enkel de boog)
        
        for i in range(0, self.thickness):  # dikte van de boog wordt meegegeven
            pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, 270 - 225, self.circle_colour) # teken een boog maar lege achtergrond
        #    if percent >4:      # boog begint boven de 4
            pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, fill_angle - 225-8, acc1) # kleurt de boog volgens value
        #if percent < 4:         # teken geen boog onder de 4
        #    return
#-----------------------------------------------------------------------
# Rechts boven

    def draw2(self, percent):
        
        acc2 = [0,255,250]    # kleur boog 
        ac2 = [0,255,255] # kleur txt center boog 
        txt2= [255,255,255] # kleur txt 
            
        fill_angle = int((press-970)*270/80)       # hoek 270° per %
        if fill_angle >= 270:    #
            fill_angle = 280
        if fill_angle <=10:
            fill_angle=10
      
        pertext = self.Font.render(str(press) + "hpa", True, ac2)  # °C of % of hpa
        pertext_rect = pertext.get_rect(center=(int(self.x_cord), int(self.y_cord)))
        self.screen.blit(self.font.render('Luchtdruk', True, txt2), (int(self.x_cord/1.1), int(self.y_cord*1.7)))       # TEXT bij boog = OK
        self.screen.blit(self.font.render('970', True, ac2), (int(self.x_cord*0.9), int(self.y_cord*1.4)))              # cijfer begin boog
        self.screen.blit(self.font.render('1050', True, ac2), (int(self.x_cord*1.01), int(self.y_cord*1.4)))              # cijfer einde boog
        self.screen.blit(pertext, pertext_rect) # laat text zijn binnen boog (zonder deze lijn zien we enkel de boog)

        for i in range(0, self.thickness):  # dikte van de boog wordt meegegeven
            pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, 270 - 225, self.circle_colour) # teken een boog maar lege achtergrond
        #    if percent >4:      # boog begint boven de 4
            pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, fill_angle - 225-8, acc2) # kleurt de boog volgens value
        #if percent < 4:         # teken geen boog onder de 4
        #    return
#-----------------------------------------------------------------------
# Links onder

    def draw3(self, percent):
            
        acc3 = [255, 99, 71]    # kleur boog 
        ac3 = [255, 99, 71] # kleur txt center boog 
        txt3 = [255,255,255] # kleur txt     
        
        fill_angle = int(hum2*270/100)       # hoek per %
        if fill_angle >= 270:
            fill_angle = 280                     # boog 100% opvullen
        if fill_angle <=10:                             
            fill_angle=10                        # boog 2.7% opvullen
        
        pertext = self.Font.render(str(hum2) + "%", True, ac3)
        pertext_rect = pertext.get_rect(center=(int(self.x_cord), int(self.y_cord)))
        self.screen.blit(self.font.render('Vochtigheid', True, txt3), (int(self.x_cord/1.5), int(self.y_cord*1.22)))       # TEXT bij boog = OK
        self.screen.blit(self.font.render('0', True, ac3), (int(self.x_cord*0.7), int(self.y_cord*1.14)))              # cijfer begin boog
        self.screen.blit(self.font.render('100', True, ac3), (int(self.x_cord*1.1), int(self.y_cord*1.14)))              # cijfer einde boog
        self.screen.blit(pertext, pertext_rect) # laat text zijn binnen boog (zonder deze lijn zien we enkel de boog)

        for i in range(0, self.thickness):  # dikte van de boog wordt meegegeven
            pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, 270 - 225, self.circle_colour) # teken een boog maar lege achtergrond
        #    if percent >4:      # boog begint boven de 4
            pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, fill_angle - 225-8, acc3) # kleurt de boog volgens value
        #if percent < 4:         # teken geen boog onder de 4
        #    return
#-----------------------------------------------------------------------
# Rechts onder

    def draw4(self, percent):
            
        acc4 = [152, 251, 152]    # kleur boog 
        ac4 = [152, 251, 152] # kleur txt center boog 
        txt4 = [255,255,255] # kleur txt wit   
         
        fill_angle = int((co2-500)*270/1000)       # hoek per %  vb 1000/270 * 800
        
        if fill_angle >= 270:
            fill_angle = 280                     # boog 100% opvullen
        if fill_angle <=10:                             
            fill_angle=10                        # boog 2.7% opvullen       if percent >= 100:
        if fill_angle >=0 and fill_angle <=135:    # tussen -20 en 0 Blauw (regel van drie met 270°)
            acc4 = [152, 251, 152]
        if fill_angle > 135 and fill_angle <=280: # tussen 0 en 25 groen
            acc4 = [255,0,0]  
            
        pertext = self.Font.render(str(co2) + "ppm", True, ac4)  # °C of % of hpa
        pertext_rect = pertext.get_rect(center=(int(self.x_cord), int(self.y_cord)))
        self.screen.blit(self.font.render('CO2', True, txt4), (int(self.x_cord/1.05), int(self.y_cord*1.22)))       # TEXT bij boog = OK
        self.screen.blit(self.font.render('500', True, ac4), (int(self.x_cord*0.9), int(self.y_cord*1.14)))              # cijfer begin boog
        self.screen.blit(self.font.render('1500', True, ac4), (int(self.x_cord*1.01), int(self.y_cord*1.14)))              # cijfer einde boog
        self.screen.blit(pertext, pertext_rect) # laat text zijn binnen boog (zonder deze lijn zien we enkel de boog)

        for i in range(0, self.thickness):  # dikte van de boog wordt meegegeven
            pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, 270 - 225, self.circle_colour) # teken een boog met lege achtergrond
        #    if percent >4:      # boog begint boven de 4
            pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, fill_angle - 225-8, acc4) # kleurt de boog volgens value
        #if percent < 4:         # teken geen boog onder de 4
        #    return                        
########################################################################

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(titel) # Tekst boven

    fps = 0.2    # snelheid refresh screen nu op 5s
    FONT = pygame.font.SysFont('Franklin Gothic Heavy', 100) # size tekens value
#-----------------------------------------------------------------------
    my_gauge1 = Gauge(       # Links boven
        screen=screen,
        FONT=FONT,
        x_cord=width / 4,   # plaats gauges x
        y_cord=height / 4,  # plaats gauges y
        thickness= 40,   # dikte boog was 50
        radius=225, # straal boog
        circle_colour=circle_c,
        glow=False)
#-----------------------------------------------------------------------
    my_gauge2 = Gauge(          # Rechts boven
        screen=screen,
        FONT=FONT,
        x_cord=width / 1.3,   # plaats gauges x
        y_cord=height / 4,  # plaats gauges y
        thickness= 40,   # dikte boog
        radius=225, # straal boog
        circle_colour=circle_c,
        glow=False)
#-----------------------------------------------------------------------
    my_gauge3 = Gauge(          # Links onder 
        screen=screen,
        FONT=FONT,
        x_cord=width / 4,   # plaats gauges x
        y_cord=height / 1.3,  # plaats gauges y
        thickness= 40,   # dikte boog
        radius=225, # straal boog
        circle_colour=circle_c,
        glow=False)
#-----------------------------------------------------------------------
    my_gauge4 = Gauge(          # Rechts onder
        screen=screen,
        FONT=FONT,
        x_cord=width / 1.3,   # plaats gauges x
        y_cord=height / 1.3,  # plaats gauges y
        thickness= 40,   # dikte boog
        radius=225, # straal boog
        circle_colour=circle_c,
        glow=False)
#-----------------------------------------------------------------------

    percentage = 5      # groter dan 4 is boog opvullen, dus gebeurt nu direct
    time.sleep(3)
    while True:
        #time.sleep(5)
        #percentage+=1
        screen.fill(bg_c)                   # zonder deze lijn wordt steeds overelkaar geprojecteerd
        my_gauge1.draw1(percent=percentage)   # toont beeld
        my_gauge2.draw2(percent=percentage)   # toont beeld
        my_gauge3.draw3(percent=percentage)   # toont beeld
        my_gauge4.draw4(percent=percentage)   # toont beeld
        pygame.display.update()             # toont beeld
        clock.tick(fps)
        readSensor()                        # data sensoren ophalen
        time.sleep(5)
        print (mylist)
        '''
        obj = time.localtime()
        t = time.asctime(obj)
        print('time',t)
        '''        
'''
https://www.tutorialspoint.com/python/time_localtime.htm

#!/usr/bin/python
import time

print "time.localtime() : %s" % time.localtime()
When we run above program, it produces following result −

time.localtime() : (2009, 2, 17, 17, 3, 38, 1, 48, 0)

'''
