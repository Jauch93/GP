from Tkinter import *
from gui_actor import *
from gui_lightSettings import *

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
		self.master = Tk(className = "GrowBox")

		self.button_TF = Button(self.master, text = "TF_SENSOR")
		self.button_TF.grid(row = 0, column = 0)

		self.button_grow = Button(self.master, text = "GROW")
		self.button_grow.grid(row = 0, column = 1)

		self.button_light = Button(self.master, text = "LICHT")
		self.button_light.bind("<Button-1>", self.startLightSettings)
		self.button_light.grid(row = 0, column = 2)

		self.button_wasser = Button(self.master, text = "WASSER")
		self.button_wasser.grid(row = 1, column = 2)

		self.button_luft = Button (self.master, text = "LUEFTUNG")
		self.button_luft.grid(row = 2, column = 2)

		self.button_allAuto = Button(self.master, text = "All Auto")
		self.button_allAuto.grid(row = 3, column = 2)

		self.button_allOff = Button(self.master, text = "ALL OFF")
		self.button_allOff.grid(row = 4, column = 2)

		self.master.mainloop()

	def startLightSettings(self, *args):
		LS = LightSettings(self.light)

