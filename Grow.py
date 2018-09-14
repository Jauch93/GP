import datetime

class Grow:

	def __init__(self):
		self.isActive = True
		self.sortName = "NONE"
		self.growStart = datetime.datetime.now()
		self.flowerStart = 0
		self.growEnd = 0
		self.Ertrag = 0
		self.consumedEnergy = 0

	def getSort(self):
		return self.sortName

	def getGrowPhase(self):
		if self.isActive:
			if self.flowerStart == 0:
				return "Veggetations-Phase"
			else:
				return "Bluete-Phase"
		else:
			return "Beendet"

	def getGrowStartDate(self):
		return self.growStart

	def getFlowerStartDate(self):
		return self.flowerStart

	def getGrowEnd(self):
		return self.growEnd

	def getGrowDay(self):
		if self.growEnd == 0:
			return (datetime.datetime.now().day - self.growStart.day)
		else:
			return (self.growEnd.day - self.growStart.day)

	def endGrow(self):
		self.growEnd = datetime.datetime.now()
		self.isActive = False

	def startFlowerPhase(self):
		if self.flowerStart == 0:
			self.flowerStart = datetime.datetime.now()

	def getFlowerDay(self):
		if self.flowerStart == 0:
			return 0
		else:
			return  (datetime.datetime.now().day - self.flowerStart.day)

