import allsky
BASEPATH = list(allsky.__path__)[0][:-len('allsky')]

# ZWO
SDK_LIB_PATH = BASEPATH + 'data/libASICamera2.so'

# DHT Sensor
DHT_SENSOR_TYPE = 11
DHT_GPIO_PIN = 2

# HEATER
HEATER_PIN = 5

# SHELL SERVO
SERVO_PIN = 11
SHELL_LOG = BASEPATH + 'data/shellPos.log'

# Coordinates
CERECEDA_ALLSKY_LAT =  43.25916375853605 
CERECEDA_ALLSKE_LON = -6.603491884147439


