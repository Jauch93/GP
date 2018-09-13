from Actor import *
from DHT11 import *
import thread
import time

class Ventilation(Actor):
	def __init__(self, pinNr, tf_sensor):
		super(Ventilation, self).__init__(pinNr)
		self.tf_sensor = tf_sensor
		self.criticHumidity = 60
		self.criticTemp = 23

	def __automatic(self):
		while self.isAuto:
			if (self.tf_sensor.getHumidity() > self.criticHumidity) or (self.tf_sensor.getTemperature() > self.criticTemp):
				self.turnOn()
			else:
				self.turnOff()
		time.sleep(5)

	def startAuto(self):
		self.isAuto = True
		thread.start_new_thread(self.__automatic, ())

	def getCriticTemperature(self):
                return self.criticTemp

        def getCriticHumidity(self):
                return self.criticHumidity

        def setCriticTemperature(self, T):
                self.criticTemp = T

        def setCriticHumidity(self, H):
                self.criticHumidity = H
