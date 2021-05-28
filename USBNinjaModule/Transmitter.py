from bluepy import btle
import time
import re

class TX:
	def __init__(self, BTADDR):
		self.BTADDR = BTADDR

	def Initialconnection(self):
		try:
			p = btle.Peripheral(self.BTADDR, btle.ADDR_TYPE_PUBLIC, 0)
			if(p == None):
				print("Device not Found")
				return False
			else:
				return True
		except:
			print("Device not Found")
			return False


	def bintohex (self, binaryhexstring):
		hexstring = re.sub("b|x|'","",str(binaryhexstring))
		hexstring = re.sub("[^0-9|a-f]"," ",hexstring)
		return hexstring[1: ]

	def deviceinforamtion (self):
		try:
			p = btle.Peripheral(self.BTADDR, btle.ADDR_TYPE_PUBLIC, 0)
			print("Device name:", end = '\t\t\t')
			print(p.readCharacteristic(int("0x03",16)).decode("utf-8"))
			#print("Device appearance:", end = '')
			#print(self.bintohex(p.readCharacteristic(int("0x05",16))))
			#print("Pheripheral preffered connection parameters:", end = '')
			#print(self.bintohex(p.readCharacteristic(int("0x07",16))))
			#print("Central address resolution:", end = '')
			#print(self.bintohex(p.readCharacteristic(int("0x09",16))))
			print("Model number string:", end = '\t\t')
			print(p.readCharacteristic(int("0x12",16)).decode("utf-8"))
			print("Serial number string:", end = '\t\t')
			print(p.readCharacteristic(int("0x14",16)).decode("utf-8"))
			print("Hardware revision string:", end = '\t')
			print(p.readCharacteristic(int("0x16",16)).decode("utf-8"))
			print("Firmware revision string:", end = '\t')
			print(p.readCharacteristic(int("0x18",16)).decode("utf-8"))
			print("Software revision string:", end = '\t')
			print(p.readCharacteristic(int("0x1a",16)).decode("utf-8"))
			print("System id:", end = '\t\t\t')
			print(self.bintohex(p.readCharacteristic(int("0x1c",16)))[1: ])
			print("PnP id:", end = '\t\t\t\t')
			print(self.bintohex(p.readCharacteristic(int("0x1e",16))))
			p.disconnect()
			return True
		except:
			print("Device got disconnected")
			return False

	def Button(self, Button):
		try:
			p = btle.Peripheral(self.BTADDR, btle.ADDR_TYPE_PUBLIC, 0)
			#p.writeCharacteristic(int("0x22",16) , b'\x01\x00')
			#time.sleep(1)
			p.writeCharacteristic(int("0x25",16) , b'\x38\x38\x38\x38')
			time.sleep(1)

			if(Button == True):
				p.writeCharacteristic(int("0x25",16) , b'\x41\x3d\x4c\x0d\x0a')
			else:
				p.writeCharacteristic(int("0x25",16) , b'\x42\x3d\x4c\x0d\x0a')
			p.disconnect()
			return True
		except:
			print("Device not Found")
			return False
