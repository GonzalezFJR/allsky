'''
 Class to get current time and coordinates for the observatory, sunset, sunrise and other space-time features

'''


import time, datetime
import astroplan
import astropy.units as u
from astropy.time import Time

from allsky.config import CERECEDA_ALLSKY_LAT, CERECEDA_ALLSKE_LON

class obscoor:
  def __init__(self, latitude=CERECEDA_ALLSKY_LAT, longitude=CERECEDA_ALLSKE_LON):
    self.latitude = latitude
    self.longitude = longitude
    self.t0 = time.time()
    self.obs = astroplan.Observer(longitude=longitude*u.deg, latitude=latitude*u.deg, elevation=700*u.m, name='Cereceda', timezone='Europe/Madrid')

  def GetAstroTimeNow(self):
    time = Time(datetime.datetime.now())
    return time

  def GetTimeNow(self, format="%d/%m/%Y %H:%M:%S"):
    now = datetime.datetime.now()
    s = now.strftime(format)
    return s

  def GetToday(self, format="%d/%m/%Y"):
    today = datetime.date.today()
    s = today.strftime(format)
    return s

  def GetDeltaTime(self):
    return time.time() - self.t0

#o = obscoor()
#t = o.GetAstroTimeNow()
#print(o.obs.is_night(t))
