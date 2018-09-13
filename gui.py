from Tkinter import *

class MainWindow:
	def __init__(self, growBox):
		self.growBox = growBox
		self.tf_sensor = growBox.getDHT11()
		self.light = growBox.getLight()
		self.water = growBox.getWater()
		self.venti = growBox.getVentilation()
		self.grow = growBox.getGrow()

		self.buildGui()

	def buildGui(self):
		master = Tk(className = "GrowBox")

		self.button_TF = Button(master, text = "TF_SENSOR")
		self.button_TF.grid(row = 0, column = 0)

		self.button_grow = Button(master, text = "GROW")
		self.button_grow.grid(row = 0, column = 1)

		self.button_light = Button(master, text = "LICHT")
		self.button_light.bind("<Button-1>", self.startLightSettings)
		self.button_light.grid(row = 0, column = 2)

		self.button_wasser = Button(master, text = "WASSER")
		self.button_wasser.grid(row = 1, column = 2)

		self.button_luft = Button (master, text = "LUEFTUNG")
		self.button_luft.grid(row = 2, column = 2)

		master.mainloop()

	def startLightSettings(self, *args):
		LS = LightSettings(self.light)

class LightSettings:
	def __init__(self, light):
		self.light = light
		self.buildGui()

	def buildGui(self):
		self.master = Tk(className = "LichtSteuerung")

		Label(self.master, text = "StartZeit: ").grid(row = 0, column = 0)
		self.startTime = Scale(self.master, from_ = 0, to = 23, orient = HORIZONTAL)
		self.startTime.set(self.light.getSwitchOnTime())
		self.startTime.grid(row = 0, column = 1)

		Label(self.master, text = "BrennDauer: ").grid(row = 1, column = 0)
		self.duration = Scale(self.master, from_ = 0, to = 23, orient = HORIZONTAL)
		self.duration.set(self.light.getDuration())
		self.duration.grid(row = 1, column = 1)

		Label(self.master, text = "AusschaltZeit: ").grid(row = 2, column = 0)
		self.switchOffTime = Label(self.master, text = self.light.calcSwitchOffTime())
		self.switchOffTime.grid(row = 2, column = 1)

		self.applyButton = Button(self.master, text = "Apply")
		self.applyButton.bind("<Button-1>", self.applyValues)
		self.applyButton.grid(row = 3, column = 0)

		self.applyCloseButton = Button(self.master, text = "Apply/Close")
		self.applyCloseButton.bind("<Button-1>", self.applyClose)
		self.applyCloseButton.grid(row = 3, column = 1)

		master.mainloop()

	def applyClose(self, *args):
		self.applyValues()
		self.master.destroy()

	def applyValues(self, *args):
		self.light.setSwitchOnTime(self.startTime.get())
		self.light.setDuration(self.duration.get())
		self.switchOffTime.config(text = self.light.calcSwitchOffTime())
