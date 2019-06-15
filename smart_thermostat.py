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
  def __init__(self):
    self.state = State.OFF
    self.get_humidity_and_temperature()

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


  
