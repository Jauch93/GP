from Tkinter import *

class GrowSettings(object):
	def __init__(self, grow):
		self.grow = grow
		self.buildGui()

	def buildGui(self):
		self.master = Tk(className = "GrowInformationen")
		self.fullscreen()

		for i in range (0, 3):
			self.master.columnconfigure(i, weight = 1)
		for i in range(0, 4):
			self.master.rowconfigure(i, weight = 1)

		Label(self.master, text = "GrowPhase: ").grid(row = 0, column = 0)
		Label(self.master, text = self.grow.getGrowPhase()).grid(row = 0, column = 1)

		Label(self.master, text = "GrowBeginn: ").grid(row = 1, column = 0)
		Label(self.master, text = str(self.grow.getGrowStartDate())).grid(row = 1, column = 1)

		Label(self.master, text = "BlueteBeginn: ").grid(row = 2, column = 0)
		Label(self.master, text = str(self.grow.getFlowerStartDate())).grid(row = 2, column = 1)

		Label(self.master, text = "EndDatum: ").grid(row = 3, column = 0)
		Label(self.master, text = str(self.grow.getGrowEnd())).grid(row = 3, column = 1)

		Label(self.master, text = "Sorte: ").grid(row = 0, column = 2)
		Label(self.master, text = self.grow.getSort()).grid(row = 0, column = 3)

		Label(self.master, text = "GrowTag: ").grid(row = 1, column = 2)
		Label(self.master, text = self.grow.getGrowDay()).grid(row = 1, column = 3)

		Label(self.master, text = "BlueteTag: ").grid(row = 2, column = 2)
		Label(self.master, text = self.grow.getFlowerDay()).grid(row = 2, column = 3)

		self.startFlowerPhaseButton = Button(self.master, text = "Bluete Starten")
		self.startFlowerPhaseButton.bind("<Button-1>", self.startFlowerPhase)
		self.startFlowerPhaseButton.grid(row = 3, column = 3)

		self.endGrowButton = Button(self.master, text = "End Grow")
		self.endGrowButton.bind("<Button-1>", self.endGrow)
		self.endGrowButton.grid(row = 4, column = 3)

		self.applyCloseButton = Button(self.master, text = "CLOSE")
		self.applyCloseButton.bind("<Button-1>", self.applyClose)
		self.applyCloseButton.grid(row = 4, column = 0)

		self.master.mainloop()

	def startFlowerPhase(self, *args):
		self.grow.startFlowerPhase()

	def endGrow(self, *args):
		self.grow.endGrow()

	def fullscreen(self):
		w,h = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
		self.master.geometry("%dx%d+0+0" % (w,h))
		self.master.attributes('-zoomed', True)

	def applyClose(self, *args):
		self.applyValues()
		self.master.destroy()

	def applyValues(self, *args):
                pass


