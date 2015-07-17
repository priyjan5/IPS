import sys
from main_controller import MainController
import os.path 

def main():
	if len(sys.argv) != 2:
		print "Error: Incorrect usage - must have one argument"
		return
		
	configFile = sys.argv[1]
	
	if not(configFile.endswith('.conf')):
		print "Error: Incorrect usage - first argument must be a .conf filename"
		return
	
	if not os.path.isfile(configFile):
		print "Error: File does not exist"
		return
	
	#Run test based on the config file
	run_tests(configFile)

def run_tests(configFile):
	main = MainController(configFile)
	main.start()
	
if __name__ =="__main__":
	main()