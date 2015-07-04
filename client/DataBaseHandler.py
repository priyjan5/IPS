# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('attack.db')
cur = con.cursor()

cur.execute('SELECT * from malware')
data = cur.fetchall()
attack  = data[0][1]
print attack
	
con.close()