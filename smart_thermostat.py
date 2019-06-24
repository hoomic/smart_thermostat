from enum import Enum

import RPi.GPIO as GPIO
import Adafruit_DHT as DHT

GPIO.setmode(GPIO.BCM)

pin_list = [2, 3, 4, 17]

for i in pin_list:
  GPIO.setup(i, GPIO.OUT)
  GPIO.output(i, GPIO.HIGH)

class State(Enum):
  OFF = 1
  COOL = 2
  HEAT = 3
  AUXHEAT = 4
  FAN = 5

class Thermostat():
  def __init__(self, tolerance=0.5, use_aux_heat=False, aux_heat_tolerance=5.0):
    self.state = State.OFF
    self.tolerance = tolerance
    self.use_aux_heat = use_aux_heat
    self.aux_heat_tolerance = aux_heat_tolerance
    self.get_humidity_and_temperature()
    self.temperature_setting = round(self.temperature, 1)

  def turn_off(self):
    for i in pin_list:
      GPIO.output(i, GPIO.HIGH)
    self.state = State.OFF

  def cool_on(self):
    self.turn_off()
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)
    self.state = State.COOL

  def heat_on(self):
    self.turn_off()
    GPIO.output(2, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    self. state = State.HEAT

  def aux_heat_on(self):
    self.turn_off()
    GPIO.output(2, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    self.state = State.AUXHEAT

  def fan_on(self):
    self.turn_off()
    GPIO.output(2, GPIO.LOW)
    self.state = State.FAN

  def get_humidity_and_temperature(self):
    self.humidity, self.temperature = DHT.read_retry(DHT.DHT22, 27)
    
  def set_temperature(self, temperature):
    self.temperature_setting = temperature

  def determine_state(self):
    self.get_humidity_and_temperature()
    if self.temperature > self.temperature_setting + self.tolerance:
      if self.state != State.COOL:
        print("Setting state to COOL. temperature={0:.2f}, temp_setting={1:.2f}, tolerace={2:.2f}".format(
          self.temperature
          , self.temperature_setting
          , self.tolerance)
        )
        self.cool_on()
    elif self.use_aux_heat and self.temperature < self.temperature_setting - self.aux_heat_tolerance:
      if self.state != State.AUXHEAT:
        print("Setting state to AUXHEAT. temperature={0:.2f}, temp_setting={1:.2f}, tolerace={2:.2f}".format(
          self.temperature
          , self.temperature_setting
          , self.tolerance)
        )
        self.aux_heat_on()
    elif self.temperature < self.temperature_setting - self.tolerance:
      if self.state != State.HEAT:
        print("Setting state to HEAT. temperature={0:.2f}, temp_setting={1:.2f}, tolerace={2:.2f}".format(
          self.temperature
          , self.temperature_setting
          , self.tolerance)
        )
        self.heat_on()
    elif self.state != State.OFF:
      print("Setting state to OFF. temperature={0:.2f}, temp_setting={1:.2f}, tolerace={2:.2f}".format(
        self.temperature
        , self.temperature_setting
        , self.tolerance)
      )
      self.turn_off()