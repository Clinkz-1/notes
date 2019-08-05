from pymysql import *
conn = connect(host='localhost',port=3306,user='root',password='root',database='test',charset='utf8')
cs = conn.cursor()
sql = 'select * from goods'
cs.execute(sql)
print(cs.fetchall())

cs.close()
conn.close()
