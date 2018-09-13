from Tkinter import *

class ActorGui(object):
	def __init__(self, actor):
		self.actor = actor
		self.buildGui()

	def buildGui(self):
		pass

	def swapButtonColors(self):
		if self.actor.isOn:
			self.onButton.configure(bg = "green")
			self.offButton.configure(bg = "black")
		else:
			self.onButton.configure(bg = "black")
			self.offButton.configure(bg = "red")

		if self.actor.isAuto:
			self.autoButton.configure(bg = "green")
		else:
			self.autoButton.configure(bg = "red")

	def auto(self, *args):
		if self.actor.isAuto:
			self.actor.stopAuto()
		else:
			self.actor.startAuto()
		self.swapButtonColors()

	def turnOff(self, *args):
		self.actor.stopAuto()
		self.actor.turnOff()
		self.swapButtonColors()

	def turnOn(self, *args):
		self.actor.stopAuto()
		self.actor.turnOn()
		self.swapButtonColors()

	def applyClose(self, *args):
		self.applyValues()
		self.master.destroy()

	def applyValues(self, *args):
                pass

