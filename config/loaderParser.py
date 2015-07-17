import ConfigParser

parser = ConfigParser.ConfigParser()
parser.read('sample.conf')
attacks = parser.get('Attacks' , 'ipreputation').replace(" " , "").split(",")
print int(attacks[0])
