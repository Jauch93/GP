from Tkinter import *

class MainWindow:
	def __init__(self, growBox):
		self.growBox = growBox
		self.tf_sensor = growBox.getDHT11()
		self.licht = growBox.getLight()
		self.water = growBox.getWater()
		self.venti = growBox.getVentilation()
		self.grow = growBox.getGrow()

		self.buildGui()

	def buildGui(self):
		master = Tk()
		frame = Frame(master)

		self.button_TF = Button(frame, text = "TF_SENSOR")
		self.button_TF.pack(side = LEFT)

		self.button_grow = Button(frame,text = "GROW")
		self.button_grow.pack(side = LEFT)

		self.button_licht = Button(frame, text = "LICHT")
		self.button_licht.pack(side = LEFT)

		self.button_wasser = Button(frame, text = "WASSER")
		self.button_wasser.pack(side = LEFT)

		self.button_luft = Button (frame, text = "LUEFTUNG")
		self.button_luft.pack(side = LEFT)

		frame.pack()

		root.mainloop()
