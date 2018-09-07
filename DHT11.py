from Sensor import Sensor
import RPi.GPIO as GPIO
import time

def bin2dec(string_num):
	return str(int(string_num, 2))

class DHT11(Sensor):
	def __init__(self, pinNr):
		super(DHT11, self).__init__(pinNr)
		self.Temperature = 0
		self.Humidity = 0

	def getHumidity(self):
		while(not self. __getData()):
			pass
		return self.Humidity

	def getTemperature(self):
		while(not self.__getData()):
			pass
		return self.Temperature

	def __getData(self):	#Private Methode
		GPIO.setup(self.pinNr, GPIO.OUT)
		GPIO.output(self.pinNr, GPIO.HIGH)
		time.sleep(0.025)
		GPIO.output(self.pinNr, GPIO.LOW)
		time.sleep(0.018)

		GPIO.setup(self.pinNr, GPIO.IN, pull_up_down=GPIO.PUD_UP)

		data = []

		for i in range(0,1000):
			data.append(GPIO.input(self.pinNr))

		ones = 0
		bitStream = ""

		for i in range (0,len(data)): #Interpreting received Data
			if data[i] == 0:
				if ones > 10:
					bitStream = bitStream + "1"
				elif ones > 2:
					bitStream = bitStream + "0"
				ones = 0
			if data[i] == 1:
				ones += 1

		HumidityByte = bitStream[1:9]
		TemperatureByte = bitStream[17:25]
		crcByte = bitStream[33:41]

		try:
			H = bin2dec(HumidityByte)
			T = bin2dec(TemperatureByte)
			CRC = bin2dec(crcByte)
		except:
			return False
		if int(H) + int(T) - int(CRC) == 0:
			self.Humidity = H
			self.Temperature = T

			return True
		else:
			return False
