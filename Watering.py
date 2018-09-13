from Actor import *
import thread
import time

class Watering(Actor):
	def __init__(self, pinNr):
		super(Watering, self).__init__(pinNr)
		self.amount = 1 #Amount of Water in Liters
		self.propK = 60 #Amount of Seconds to get the amount of 1 Liter
		self.wateringTime = 9

	def startWaterCycle(self):
		self.turnOn()
		time.sleep(self.amount * self.propK)
		self.turnOff()

	def startAuto(self):
		self.isAuto = True
		thread.start_new_thread(self.__automatic, ())

	def __automatic(self):
		while self.isAuto:
			currTime = datetime.datetime.now()
			if currTime.hour == self.wateringTime:
				self.startWaterCycle()
				time.sleep(3600)

	def setAmount(self, amount):
		self.amount = amount

	def getAmount(self):
		return self.amount

	def setWateringTime(self, t):
		self.wateringTime = t

	def getWateringTime(self):
		return self.wateringTime
