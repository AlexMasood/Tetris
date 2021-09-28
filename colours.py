from pygame import *
class Colours:
	def __init__(self):
		self.colours = []
		self.colours.append(Color(0,255,255,255))#line
		self.colours.append(Color(255,255,0,255))#square
		self.colours.append(Color(204,0,204,255))#tshape
		self.colours.append(Color(255,128,0,255))#lshape
		self.colours.append(Color(0,0,153,255))#jshape
		self.colours.append(Color(0,255,0,255))#sshape
		self.colours.append(Color(255,0,0,255))#zshape
		self.colours.append(Color(255,255,255,255))#white
		self.colours.append(Color(0,0,0,255))#black
		self.colours.append(Color(191,191,191,255))#light grey
		self.colours.append(Color(127,127,127,255))#dark grey
	def returnList(self):
		return self.colours