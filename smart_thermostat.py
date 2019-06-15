import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pin_list = [2, 3, 4, 17]

for i in pin_list:
  GPIO.setup(i, GPIO.OUT)
  GPIO.output(i, GPIO.HIGH)


class Thermostat():
  def __init__(self):
    pass

  def reset(self):
    for i in pin_list:
      GPIO.output(i, GPIO.HIGH)

  def cool_on(self):
    self.reset()
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)

  def heat_on(self):
    self.reset()
    GPIO.output(2, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)

  def aux_heat_on(self):
    self.reset()
    GPIO.output(2, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)

  def fan_on(self):
    self.reset()
    GPIO.output(2, GPIO.LOW)
