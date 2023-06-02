import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='pokemon123!')
cursor = conn.cursor()
cursor.close()
conn.close()