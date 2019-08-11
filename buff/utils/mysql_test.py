from pymysql import *

class MysqlClient:
    def __init__(self,user,password,database,host='localhost',port=3306):
        self.conn = connect(host=host,port=port,user=user,password=password,database=database,charset='utf8')
        self.cs = self.conn.cursor()

    def close(self):
        self.cs.close()
        self.conn.close()

    def run_sql(self,sql,*args):
        try:
            # 执行sql语句
            sql = sql.replace('None','NULL')
            self.cs.execute(sql,args)
            self.conn.commit()  # 把修改提交到数据库
        except Exception as e:
            print(e)
            self.conn.rollback()

    def show(self,type='all'):
        if type=='all':
            return self.cs.fetchall()
        elif type=='one':
            return self.cs.fetchone()
        elif isinstance(type,int):
            return self.cs.fetchmany(type)

    def insert_one(self,*args):
        '''id(default 0),goods_id,tags_id,price,goods_url,query_url'''
        sql = "insert into goods values({},{},{},{},'{}','{}');".format(*args)
        self.run_sql(sql)

    def update_one(self,*args,**kwargs):
        set_content = ''
        for key in kwargs:
            if isinstance(kwargs[key],str):
                set_content += f"{key}='{kwargs[key]}',"
            else:
                set_content+=f"{key}={kwargs[key]},"
        if len(args)==1:
            sql = "update goods set "+set_content[:-1]+f" where goods_id={args[0]};"
        else:
            sql = "update goods set "+set_content[:-1]+f" where goods_id={args[0]} and tag_ids={args[1]};"
        self.run_sql(sql)

    def delete_one(self,*args):
        if len(args)==1:
            sql = f"delete from goods where goods_id={args[0]};"
        else:
            sql = f"delete from goods where goods_id={args[0]} and tag_ids={args[1]};"
        self.run_sql(sql)

    def find(self,*args,col_list=[],**kwargs):
        col_content = ''
        if col_list:
            for i in col_list:
                col_content += i+','
        else:
            col_content='* '

        if kwargs:
            query_content = ''
            for key in kwargs:
                if isinstance(kwargs[key], str):
                    query_content += f"{key}='{kwargs[key]}' and "
                else:
                    query_content += f"{key}={kwargs[key]} and "
            sql = "select " + col_content[:-1] + " from goods where "+query_content[:-4]
        else:
            if not args:
                sql = "select " + col_content[:-1] + f" from goods;"
            elif len(args) == 1:
                sql = "select " + col_content[:-1] + f" from goods where goods_id={args[0]};"
            else:
                sql = "select " + col_content[:-1] + f" from goods where goods_id={args[0]} and tag_ids={args[1]};"
        self.cs.execute(sql)
        return self.show()


    def create_table(self):
        sql = '''create table goods(id int unsigned primary key auto_increment not null,
         goods_id int unsigned,
         tag_ids int unsigned,
         price float ,
         goods_url varchar(300),
         query_url varchar(300));'''
        self.run_sql(sql)

    def drop_table(self):
        sql = 'drop table goods;'
        self.run_sql(sql)

if __name__ == '__main__':
    s = MysqlClient('root','312429','goods')
    # print(s.create_table())
    #
    s.insert_one(0,12345,None,9.6,'qeqeweqwew','qweqeqwewe')
    # s.update_one(12345,price=8,goods_url='aaaa')
    # s.delete_one(12345)
    # print(s.find(12345, col_list=['goods_url', 'query_url'],))
    s.close()

