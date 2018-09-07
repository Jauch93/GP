from Actor import *

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


