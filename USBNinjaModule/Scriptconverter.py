import re, os

# infile 2 for 2nd payload
# atttack execution mode

class Converter:
	def __init__(self, ifile, ofile):

		self.ofile = open(ofile, "w")
		self.defaultdelay = 500
		self.tab = 0
		self.adddicts()
		self.convert(ifile)

		self.ofile.close()

	def adddicts(self):

		self.singlekey = {
			"A":"KEY_A",
			"B":"KEY_B",
			"C":"KEY_C",
			"D":"KEY_D",
			"E":"KEY_E",
			"F":"KEY_F",
			"G":"KEY_G",
			"H":"KEY_H",
			"I":"KEY_I",
			"J":"KEY_J",
			"K":"KEY_K",
			"L":"KEY_L",
			"M":"KEY_M",
			"N":"KEY_N",
			"O":"KEY_O",
			"P":"KEY_P",
			"Q":"KEY_Q",
			"R":"KEY_R",
			"S":"KEY_S",
			"T":"KEY_T",
			"U":"KEY_U",
			"V":"KEY_V",
			"W":"KEY_W",
			"X":"KEY_X",
			"Y":"KEY_Y",
			"Z":"KEY_Z"
		}

		self.fkeys = {
			"F1" :"KEY_F1",
			"F2" :"KEY_F2",
			"F3" :"KEY_F3",
			"F4" :"KEY_F4",
			"F5" :"KEY_F5",
			"F6" :"KEY_F6",
			"F7" :"KEY_F7",
			"F8" :"KEY_F8",
			"F9" :"KEY_F9",
			"F10":"KEY_F10",
			"F11":"KEY_F11",
			"F12":"KEY_F12"
		}

		self.arrows = {
			"UP"          :"KEY_ARROW_UP",
			"UPARROW"     :"KEY_ARROW_UP",
			"DOWN"        :"KEY_ARROW_DOWN",
			"DOWNARROW"  :"KEY_ARROW_DOWN",
			"LEFT"       :"KEY_ARROW_LEFT",
			"LEFTARROW"  :"KEY_ARROW_LEFT",
			"RIGHT"       :"KEY_ARROW_RIGHT",
			"RIGHTARROW" :"KEY_ARROW_RIGHT"
		}

		self.shiftaddons = {
			"DELETE"      :"KEY_DELETE",
			"HOME"        :"KEY_HOME",
			"INSERT"      :"KEY_INSERT",
			"PAGEUP"      :"KEY_PAGE_UP",
			"PAGEDOWN"    :"KEY_PAGE_DOWN",
			"WINDOWS"     :"MOD_GUI_LEFT",
			"GUI"         :"MOD_GUI_LEFT",
			"TAB"        :"KEY_TAB",
		}

		self.altaddons = {
			"END"        :"KEY_END",
			"ESC"        :"KEY_ESC",
			"ESCAPE"     :"KEY_ESC",
			"SPACE"      :"KEY_SPACE",
			"TAB"        :"KEY_TAB"
		}

		self.ctrladdons = {
			"BREAK"      :"PAUSE",
			"PAUSE"      :"KEY_SPACE",
			"ESC"        :"KEY_ESC",
			"ESCAPE"     :"KEY_ESC"
		}

		self.lang = {
			"US"        :"#define LAYOUT_US_ENGLISH",
			"CA_FR"     :"#define LAYOUT_CANADIAN_FRENCH",
			"CA"        :"#define LAYOUT_CANADIAN_MULTILINGUAL",
			"DK"        :"#define LAYOUT_DANISH",
			"FI"        :"#define LAYOUT_FINNISH",
			"FR"        :"#define LAYOUT_FRENCH",
			"FR_BE"     :"#define LAYOUT_FRENCH_BELGIAN",
			"FR_CH"     :"#define LAYOUT_FRENCH_SWISS",
			"DE"        :"#define LAYOUT_GERMAN",
			"DE_MAC"    :"#define LAYOUT_GERMAN_MAC",
			"DE_CH"     :"#define LAYOUT_GERMAN_SWISS",
			"ICLD"      :"#define LAYOUT_ICELANDIC",
			"IE"        :"#define LAYOUT_IRISH",
			"IT"        :"#define LAYOUT_ITALIAN",
			"NOR"       :"#define LAYOUT_NORWEGIAN",
			"POR"       :"#define LAYOUT_PORTUGUESE",
			"POR_BRA"   :"#define LAYOUT_PORTUGUESE_BRAZILIAN",
			"SPA"       :"#define LAYOUT_SPANISH",
			"SPA_LAT"   :"#define LAYOUT_SPANISH_LATIN_AMERICA",
			"SE"        :"#define LAYOUT_SWEDISH",
			"TUR"       :"#define LAYOUT_TURKISH",
			"UK"        :"#define LAYOUT_UNITED_KINGDOM",
			"US_INT"    :"#define LAYOUT_US_INTERNATIONAL",
		}

	def convert(self, ifile):

		print()
		self.cnt = 0
		filelist = []

		file = open(ifile, "r")
		for line in file:
			filelist.append(line)
		file.close()

		linesum = len(filelist)

		for line in filelist:
			
			self.cnt += 1
			
			if((self.cnt) < linesum):
				if("REPEAT" in filelist[self.cnt]):
					tempstring = filelist[self.cnt][(len("REPEAT")+1):-1]
					string = re.sub(' ', "", tempstring)
					try:
						cyles  = int(string)
						self.ofile.write('for (i = 0; i <' + str(cyles) + '; i++) {\n')
						self.tab = (self.tab + 1)
					except:
						self.errorlog(tempstring)

			while(line.startswith(" ") or line.startswith("\t")):
				line = line[1:]

			if(line.startswith("REM")):
				self.rem(line[(len("REM")+1):-1])

			elif(line.startswith("DEFAULT_DELAY")):
				self.default_delay(line[(len("DEFAULT_DELAY")+1):-1])
			elif(line.startswith("DEFAULTDELAY")):
				self.default_delay(line[(len("DEFAULTDELAY")+1):-1])
			
			elif(line.startswith("DELAY")):
				self.delay(line[(len("DELAY")+1):-1])

			elif(line.startswith("STRING")):
				self.string(line[(len("STRING")+1):-1])

			elif(line.startswith("GUI")):
				self.gui(line[(len("GUI")+1):-1])
			elif(line.startswith("WINDOWS")):
				self.gui(line[(len("WINDOWS")+1):-1])

			elif(line.startswith("APP") or line.startswith("MENU")):
				self.menu()

			elif(line.startswith("SHIFT")):
				self.shift(line[(len("SHIFT")+1):-1])

			elif(line.startswith("ALT")):
				self.alt(line[(len("ALT")+1):-1])

			elif(line.startswith("CTRL")):
				self.ctrl(line[(len("CTRL")+1):-1])
			elif(line.startswith("CONTROL")):
				self.ctrl(line[(len("CONTROL")+1):-1])

			elif(line.startswith("UP") or line.startswith("UPARROW") or line.startswith("DOWN") or line.startswith("DOWNARROW ") or line.startswith("LEFT") or line.startswith("LEFTARROW ") or line.startswith("RIGHT") or line.startswith("RIGHTARROW ")):
				self.arrow(line)

			elif(line.startswith("BREAK") or line.startswith("PAUSE")):
				self.pause()

			elif(line.startswith("CAPSLOCK")):
				self.caps()

			elif(line.startswith("DELETE")):
				self.delete()

			elif(line.startswith("END")):
				self.end()

			elif(line.startswith("ESC") or line.startswith("ESCAPE")):
				self.esc()

			elif(line.startswith("HOME")):
				self.home()

			elif(line.startswith("INSERT")):
				self.insert()

			elif(line.startswith("NUMLOCK")):
				self.numlock()

			elif(line.startswith("PAGEUP")):
				self.pageup()

			elif(line.startswith("PAGEDOWN")):
				self.pagedown()

			elif(line.startswith("PRINTSCREEN")):
				self.printscreen()

			elif(line.startswith("SCROLLLOCK")):
				self.scrolllock()

			elif(line.startswith("SPACE")):
				self.space()

			elif(line.startswith("TAB")):
				self.tab()

			elif(line.startswith("ENTER")):
				self.enter()

			elif(line.startswith("REPEAT")):

				self.tab = (self.tab - 1)	
				self.ofile.write('}\n')

			else:
				self.errorlog(line[:-1])

			
			if(line.startswith("REPEAT") == False and line.startswith("DEFAULTDELAY") == False and line.startswith("DEFAULT_DELAY") == False and line.startswith("DELAY") == False):
				if((self.cnt) < linesum):
					if("REPEAT" in filelist[self.cnt]):
						[self.ofile.write("\t") for tabs in range(self.tab)]
						self.ofile.write('NinjaKeyboard.delay('+ str(self.defaultdelay) +');\n')
					elif("DELAY" in filelist[self.cnt]):
						continue
					else:
						[self.ofile.write("\t") for tabs in range(self.tab)]	
						self.ofile.write('NinjaKeyboard.delay('+ str(self.defaultdelay) +');\n\n')						
				else:
	
					self.ofile.write('NinjaKeyboard.delay('+ str(self.defaultdelay) +');\n\n')
			else:
				self.ofile.write('\n')
		return

	def errorlog(self, string):
		print("\033[31m[Error at line " + str(self.cnt) + "]:\033[97m " + string)

	def rem(self, string):
		[self.ofile.write("\t") for tabs in range(self.tab)]		
		self.ofile.write("// " + string + "\n")
		return True

	def default_delay(self, string):
		tempstring = string
		string = re.sub(' ', "", string)
		try:
			string = int(string)
			self.defaultdelay = string
			return True
		except:
			self.errorlog("DEFAULT_DELAY " + tempstring)
			return False

	def delay(self, string):
		tempstring = string
		string = re.sub(' ', "", string)
		try:
			string = int(string)
			[self.ofile.write("\t") for tabs in range(self.tab)]
			self.ofile.write("NinjaKeyboard.delay(" + str(string) + ");\n")
			return True
		except:
			self.errorlog("DELAY " + tempstring)
			return False

	def string(self, string):
		try:
			string = re.sub("\\\\", "\ ", string)
			string = re.sub('"', "'", string)
			[self.ofile.write("\t") for tabs in range(self.tab)]
			self.ofile.write('NinjaKeyboard.println(F("' + string + '"));\n')
			return True
		except:
			self.errorlog("STRING " + string)
			return False

	def gui(self, string):
		tempstring = string
		string = re.sub(' ', "", string)
		if(len(string) == 1):
			[self.ofile.write("\t") for tabs in range(self.tab)]
			self.ofile.write('NinjaKeyboard.sendKeyStroke(' + self.singlekey[string.upper()] + ', MOD_GUI_LEFT);\n')
		elif(len(string) == 0):
			[self.ofile.write("\t") for tabs in range(self.tab)]
			self.ofile.write('NinjaKeyboard.sendKeyStroke(MOD_GUI_LEFT);\n')
		else:
			self.errorlog("GUI " + tempstring)
		return 

	def menu(self):
		[self.ofile.write("\t") for tabs in range(self.tab)]
		self.ofile.write('NinjaKeyboard.sendKeyStroke(KEY_MENU);\n')
		return True

	def shift(self, string):
		tempstring = string
		string = re.sub(' ', "", string)
		try:		
			for key in self.shiftaddons:
				if str(key) in string:
					[self.ofile.write("\t") for tabs in range(self.tab)]
					self.ofile.write('NinjaKeyboard.sendKeyStroke(' + self.shiftaddons[key] + ', MOD_SHIFT_LEFT);\n')
					return True

			for arrow in self.arrows:
				if str(arrow) in string:
					[self.ofile.write("\t") for tabs in range(self.tab)]
					self.ofile.write('NinjaKeyboard.sendKeyStroke(' + self.arrows[arrow] + ', MOD_SHIFT_LEFT);\n')
					return True
			raise Exception
		except:
			self.errorlog("SHIFT " + tempstring)
			return False

	def alt(self, string):
		tempstring = string
		string = re.sub(' ', "", string)
		try:
			if(len(string) == 1):
				[self.ofile.write("\t") for tabs in range(self.tab)]
				self.ofile.write('NinjaKeyboard.sendKeyStroke(' + self.singlekey[string.upper()] + ', MOD_ALT_LEFT);\n')
				return True

			for key in self.altaddons:
				if str(key) in string:
					[self.ofile.write("\t") for tabs in range(self.tab)]
					self.ofile.write('NinjaKeyboard.sendKeyStroke(' + self.altaddons[key] + ', MOD_ALT_LEFT);\n')
					return True

			for key in self.fkeys:
				if str(key) in string:
					[self.ofile.write("\t") for tabs in range(self.tab)]
					self.ofile.write('NinjaKeyboard.sendKeyStroke(' + self.fkeys[key] + ', MOD_ALT_LEFT);\n')
					return True
			raise Exception
		except:
			print("[Error at line " + str(self.cnt) + "]: ALT " + tempstring)
			return False

	def ctrl(self, string):
		tempstring = string
		string = re.sub(' ', "", string)
		try:
			if(len(string) == 1):
				[self.ofile.write("\t") for tabs in range(self.tab)]
				self.ofile.write('NinjaKeyboard.sendKeyStroke(' + self.singlekey[string.upper()] + ', MOD_GUI_LEFT);\n')
				return True			

			for key in self.ctrladdons:
				if str(key) in string:
					[self.ofile.write("\t") for tabs in range(self.tab)]
					self.ofile.write('NinjaKeyboard.sendKeyStroke(' + self.ctrladdons[key] + ', MOD_GUI_LEFT);\n')
					return True

			for key in self.fkeys:
				if str(key) in string:
					[self.ofile.write("\t") for tabs in range(self.tab)]
					self.ofile.write('NinjaKeyboard.sendKeyStroke(' + self.fkeys[key] + ', MOD_GUI_LEFT);\n')
					return True		
			raise Exception
		except:
			print("[Error at line " + str(self.cnt) + "]: CRTL " + tempstring)
			return False

	def arrow(self, string):
		for arrow in self.arrows:
			if str(arrow) in string:
				[self.ofile.write("\t") for tabs in range(self.tab)]
				self.ofile.write('NinjaKeyboard.sendKeyStroke(' + self.arrows[arrow] + ');\n')
				return True

		self.errorlog(string)
		return False

	def pause(self):
		[self.ofile.write("\t") for tabs in range(self.tab)]
		self.ofile.write('NinjaKeyboard.sendKeyStroke(KEY_PAUSE);\n')
		return True

	def caps(self):
		[self.ofile.write("\t") for tabs in range(self.tab)]
		self.ofile.write('NinjaKeyboard.sendKeyStroke(KEY_CAPS_LOCK);\n')
		return True

	def delete(self):
		[self.ofile.write("\t") for tabs in range(self.tab)]
		self.ofile.write('NinjaKeyboard.sendKeyStroke(KEY_DELETE);\n')
		return True

	def end(self):
		[self.ofile.write("\t") for tabs in range(self.tab)]
		self.ofile.write('NinjaKeyboard.sendKeyStroke(KEY_END);\n')
		return True

	def esc(self):
		[self.ofile.write("\t") for tabs in range(self.tab)]
		self.ofile.write('NinjaKeyboard.sendKeyStroke(KEY_ESC);\n')
		return True

	def home(self):
		[self.ofile.write("\t") for tabs in range(self.tab)]
		self.ofile.write('NinjaKeyboard.sendKeyStroke(KEY_HOME);\n')
		return True

	def insert(self):
		[self.ofile.write("\t") for tabs in range(self.tab)]
		self.ofile.write('NinjaKeyboard.sendKeyStroke(KEY_INSERT);\n')
		return True

	def numlock(self):
		[self.ofile.write("\t") for tabs in range(self.tab)]
		self.ofile.write('NinjaKeyboard.sendKeyStroke(KEY_NUM_LOCK);\n')
		return True

	def pageup(self):
		[self.ofile.write("\t") for tabs in range(self.tab)]
		self.ofile.write('NinjaKeyboard.sendKeyStroke(KEY_PAGE_UP);\n')
		return True

	def pagedown(self):
		[self.ofile.write("\t") for tabs in range(self.tab)]
		self.ofile.write('NinjaKeyboard.sendKeyStroke(KEY_PAGE_DOWN);\n')
		return True

	def printscreen(self):
		[self.ofile.write("\t") for tabs in range(self.tab)]
		self.ofile.write('NinjaKeyboard.sendKeyStroke(KEY_PRINT_SCREEN);\n')
		return True

	def scrolllock(self):
		[self.ofile.write("\t") for tabs in range(self.tab)]
		self.ofile.write('NinjaKeyboard.sendKeyStroke(KEY_SCROLL_LOCK);\n')
		return True

	def space(self):
		[self.ofile.write("\t") for tabs in range(self.tab)]
		self.ofile.write('NinjaKeyboard.sendKeyStroke(KEY_SPACE);\n')
		return True

	def tab(self):
		[self.ofile.write("\t") for tabs in range(self.tab)]
		self.ofile.write('NinjaKeyboard.sendKeyStroke(KEY_TAB);\n')
		return True

	def enter(self):
		[self.ofile.write("\t") for tabs in range(self.tab)]
		self.ofile.write('NinjaKeyboard.sendKeyStroke(KEY_ENTER);\n')
		return True
