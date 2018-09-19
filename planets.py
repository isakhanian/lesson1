import datetime
import ephem


mars = ephem.Mars(datetime.datetime.now())
jupiter = ephem.Jupiter(datetime.datetime.now())
mercury = ephem.Mercury(datetime.datetime.now())
venus = ephem.Venus(datetime.datetime.now())
saturn = ephem.Saturn(datetime.datetime.now())
uranus = ephem.Uranus(datetime.datetime.now())
neptune = ephem.Neptune(datetime.datetime.now())