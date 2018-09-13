from Tkinter import *
from gui_actor import *

class VentilationSettings(ActorGui):
	def __init__(self, actor):
		super(VentilationSettings, self).__init__(actor)

	def buildGui(self):
		self.master = Tk(className = "LueftungsSteuerung")
		self.fullscreen()

		for i in range (0, 2):
			self.master.columnconfigure(i, weight = 1)
		for i in range(0, 3):
			self.master.rowconfigure(i, weight = 1)

		Label(self.master, text = "Kritische Temperatur: ").grid(row = 0, column = 0)
		self.critTemp = Scale(self.master, from_ = 10, to = 30, orient = HORIZONTAL)
		self.critTemp.set(self.actor.getCriticTemperature())
		self.critTemp.grid(row = 0, column = 1)

		Label(self.master, text = "Kritische RHE: ").grid(row = 1, column = 0)
		self.critHumidity = Scale(self.master, from_ = 0, to = 100, orient = HORIZONTAL)
		self.critHumidity.set(self.actor.getCriticHumidity())
		self.critHumidity.grid(row = 1, column = 1)


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
		self.actor.setCriticTemperature(self.critTemp.get())
		self.actor.setCriticHumidity(self.critHumidity.get())
		self.swapButtonColors()


