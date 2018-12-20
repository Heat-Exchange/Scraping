import sqlite3 as sql
dbpath="H:\Data\yieldcurve.db"
class connect_db:
    def __init__(self, path):
        self.conn=sql.connect(path)
                
    def POST_FLOAT(self,tablename,date,data):
        __cur=self.conn.cursor()
        #デバッグ用
        #__cur.execute("DROP TABLE IF EXISTS %s" % name)
        query="CREATE TABLE IF NOT EXISTS "+tablename+"(date DATE PRIMARY KEY,data FLOAT)"
        __cur.execute(query)
        __cur.execute("INSERT INTO "+tablename+"(date,data) VALUES (?,?)" ,[date,data])
        self.conn.commit()

    def POST_INT(self,tablename,date,data):
        __cur=self.conn.cursor()
        #デバッグ用
        #cur.execute("DROP TABLE IF EXISTS %s" % name)
        cur.execute("""CREATE TABLE IF NOT EXISTS table_info('%s')(
                date DATE PRIMARY KEY,
                data INTEGER)
            """ % (tablename,tablename))
        __cur.execute("INSERT INTO table_info('%s')(date,data) VALUES (?,?)",[date,data])
        self.conn.commit()

    def get_data(self,tablename):
        __cur=self.conn.cursor()
        __cur.execute("SELECT * FROM "+tablename)
        __dataList=__cur.fetchall()
        return __dataList

    def __del__(self):
        self.conn.close()

data1='2018-06-07'
data2=1.7
name='FFRate'
a=connect_db(dbpath)
a.POST_FLOAT(name,data1,data2)
data1='2018-06-08'
data2=2
name='FFRate'
a=connect_db(dbpath)
a.POST_INT(name,data1,data2)
data1='2018-06-09'
data2=1.2
name='FFRate'
a=connect_db(dbpath)
a.POST_FLOAT(name,data1,data2)
list=a.get_data(name)
print(list)