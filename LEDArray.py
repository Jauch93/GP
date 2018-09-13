from Actor import *
import time
import datetime
import thread

class LEDArray(Actor):

	def __init__(self, pinNr):
		super(LEDArray, self).__init__(pinNr)
		self.switchOnTime = 18
		self.duration = 18

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
			currTime = datetime.datetime.now().hour
			if(self.isOn): #Check if Lights need to be turned off
				if (currTime > self.calcSwitchOffTime()) and (currTime < self.switchOnTime):
					self.turnOff()
			else: #Check if lights need to be turned On
				if (currTime >= self.switchOnTime) or (currTime < self.calcSwitchOffTime()):
					self.turnOn()

			time.sleep(1)

	def calcSwitchOffTime(self):
		return ((self.switchOnTime + self.duration)%24)
