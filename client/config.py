import ConfigParser

class Config(object):
	def __init__(self, configFile):
		self.configObject = ConfigParser.ConfigParser()
		self.configObject.read(configFile)
	
	#TODO: define getters for sections/options