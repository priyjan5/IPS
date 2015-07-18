import socket
import sqlite3 as lite
import random
#this attack will attempt to connect to a set of IP addresses that are globally classified as
#malicious using different port numbers, this should be enough to trigger IPS alarms

#TODO: musty configure the inputs of the class

class IPRepuAttack():
        def __init__(self , conf):
                self.conf = conf
                con = lite.connect(self.conf)
                cur = con.cursor()
                cur.execute('SELECT * from badip')
                self.data = cur.fetchall()

        def execute(self):
                for item in self.data:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(1)
                        host = (str(item[1]) , random.choice([80 , 443 , 21 , 25 , 1337 , 22]))
                        try:
                                sock.connect(host)
                                print 'Knocked on' , host , 'succesfully'
                        except:
                                print 'Connection to' , host , "was terminated"
                        sock.close()


		

if __name__ =="__main__":
	test = IPRepuAttack('../attack.db')
	test.execute()
