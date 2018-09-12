from Actor import *
from DHT11 import *
import thread

class Ventilation(Actor):
	def __init__(self, pinNr, tf_sensor):
		super(self, Ventilation).__init__(pinNr)
		self.tf_sensor = tf_sensor
		self.criticHumidty = 60
		self.criticTemp = 23

	def __automatic(self):
		while self.isAuto:
			if (tf_sensor.getHumidity() > self.criticHumidity) or (tf_sensor.getTemperature() > self.criticTemp):
				self.turnOn()
			else:
				self.turnOff()

	def startAuto(self):
		self.isAuto = True
		thread.start_new_thread(self.__automatic, ())
