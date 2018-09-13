from Tkinter import *
from gui_actor import *

class WaterSettings(ActorGui):
	def __init__(self, actor):
		super(WaterSettings, self).__init__(actor)

	def buildGui(self):
		self.master = Tk(className = "WasserSteuerung")
		self.fullscreen()

		for i in range (0, 2):
			self.master.columnconfigure(i, weight = 1)
		for i in range(0, 3):
			self.master.rowconfigure(i, weight = 1)

		Label(self.master, text = "BewaesserungsZeit: ").grid(row = 0, column = 0)
		self.waterTime = Scale(self.master, from_ = 0, to = 23, orient = HORIZONTAL)
		self.waterTime.set(self.actor.getWateringTime())
		self.waterTime.grid(row = 0, column = 1)

		Label(self.master, text = "Menge [cl]: ").grid(row = 1, column = 0)
		self.amount = Scale(self.master, from_ = 0, to = 200, orient = HORIZONTAL)
		self.amount.set(self.actor.getAmount())
		self.amount.grid(row = 1, column = 1)

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
		self.actor.setWateringTime(self.waterTime.get())
		self.actor.setAmount(self.amount.get())
		self.swapButtonColors()

