import datetime

class Grow:

	def __init__(self, sortName):
		self.isActive = True
		self.sortName = sortName
		self.growDay = 1
		self.flowerDay = 0
		self.Ertrag = 0
		self.consumedEnergy = 0
		thread.start_new_thread(self.__countDays, ())

	def getGrowDay(self):
		return self.growDay

	def __countDays(self):
		while self.isActive:
			self.growDay += 1
			sleep(24*3600)

	def endGrow(self):
		self.isActive = False

	def startFlowerPhase(self):
		if self.flowerDay == 0:
			self.flowerDay = self.growDay
