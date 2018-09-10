from Actor import *
import time
import datetime
import thread

class LEDArray(Actor):

	def __init__(self, switchOnTime, duration, pinNr):
		super(LEDArray, self).__init__(pinNr)
		self.switchOnTime = switchOnTime
		self.duration = duration

	def getSwitchOnTime(self):
		return self.switchOnTime

	def getDuration(self):
		return self.duration

	def setSwitchOnTime(self, switchOnTime):
		self.switchOnTime = switchOnTime

	def setDuration(self, duration):
		self.duration = duration

	def startAuto(self):
		self.isAuto = True
		thread.start_new_thread(self.__automatic, ())

	def __automatic(self):
		while self.isAuto:
			currTime = datetime.datetime.now()
			if(self.isOn): #Check if Lights need to be turned off
				if currTime.hour >= ((self.switchOnTime + self.duration) % 24):
					self.turnOff()
			else: #Check if lights need to be turned On
				if currTime.hour >= self.switchOnTime:
					self.turnOn()
