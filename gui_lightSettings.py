from Tkinter import *
from gui_actor import *

class LightSettings(ActorGui):
	def __init__(self, actor):
		super(LightSettings, self).__init__(actor)

	def buildGui(self):
		self.master = Tk(className = "LichtSteuerung")
		self.fullscreen()

		for i in range (0, 2):
			self.master.columnconfigure(i, weight = 1)
		for i in range(0, 3):
			self.master.rowconfigure(i, weight = 1)

		Label(self.master, text = "StartZeit: ").grid(row = 0, column = 0)
		self.startTime = Scale(self.master, from_ = 0, to = 23, orient = HORIZONTAL)
		self.startTime.set(self.actor.getSwitchOnTime())
		self.startTime.grid(row = 0, column = 1)

		Label(self.master, text = "BrennDauer: ").grid(row = 1, column = 0)
		self.duration = Scale(self.master, from_ = 1, to = 24, orient = HORIZONTAL)
		self.duration.set(self.actor.getDuration())
		self.duration.grid(row = 1, column = 1)

		Label(self.master, text = "AusschaltZeit: ").grid(row = 2, column = 0)
		self.switchOffTime = Label(self.master, text = self.actor.calcSwitchOffTime())
		self.switchOffTime.grid(row = 2, column = 1)

		self.applyButton = Button(self.master, text = "Apply")
		self.applyButton.bind("<Button-1>", self.applyValues)
		self.applyButton.grid(row = 3, column = 0)

		self.applyCloseButton = Button(self.master, text = "Apply/Close")
		self.applyCloseButton.bind("<Button-1>", self.applyClose)
		self.applyCloseButton.grid(row = 3, column = 1)

		self.onButton = Button(self.master, text = "ON")
		self.onButton.bind("<Button-1>", self.turnOn)
		self.onButton.grid(row = 0, column = 2)

		self.offButton = Button(self.master, text = "OFF")
		self.offButton.bind("<Button-1>", self.turnOff)
		self.offButton.grid(row = 1, column = 2)

		self.autoButton = Button(self.master, text = "AUTO")
		self.autoButton.bind("<Button-1>", self.auto)
		self.autoButton.grid(row = 2, column = 2)

		self.swapButtonColors()

		self.master.mainloop()

	def applyValues(self, *args):
		self.actor.setSwitchOnTime(self.startTime.get())
		self.actor.setDuration(self.duration.get())
		self.swapButtonColors()
		self.switchOffTime.config(text = self.actor.calcSwitchOffTime())

