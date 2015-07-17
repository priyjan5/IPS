import ConfigParser

parser = ConfigParser.ConfigParser()
parser.read('sample.conf')

attacks = parser.get('Attacks' , 'denialofservice').replace(" " , "").split(",")

print attacks
