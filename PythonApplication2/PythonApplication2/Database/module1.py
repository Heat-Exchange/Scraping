import sqlite3 as sql
dbpath="H:\Data\yieldcurve.db"
conn=sql.connect(dbpath)

cur=conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS yieldCurve;
    CREATE TABLE IF NOT EXISTS yieldCurve(
           date DATE PRIMARY KEY,
           FFRate FLOAT,
           M1 FLOAT,
           M3 FLOAT,
           M6 FLOAT,
           Y1 FLOAT,
           Y2 FLOAT,
           Y3 FLOAT,
           Y5 FLOAT,
           Y10 FLOAT,
           Y20 FLOAT,
           Y30 FLOAT
     )
''')
conn.commit()
cur=conn.cursor()
data=['2018-05-31', 1.7, 1.76, 1.93, 2.08, 2.23, 2.4, 2.54, 2.68, 2.83, 2.91, 3.0]
cur.execute(
    "INSERT INTO yieldCurve(date,FFRate,M1,M3,M6,Y1,Y2,Y3,Y5,Y10,Y20,Y30) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
    data)
conn.commit()
cur=conn.cursor()
cur.execute(
    "SELECT * FROM yieldCurve")
list=cur.fetchall()
for i in list:
    print(i)
