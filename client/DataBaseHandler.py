# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('attack.db')
cur = con.cursor()

cur.execute('SELECT * from badip')
data = cur.fetchall()
for item in data:
	print item[1]