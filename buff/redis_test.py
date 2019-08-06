import redis

# 默认有序集合名字
DEFAULT_NAME = 'test'

class RedisClient:
    def __init__(self,host='',port='',password=''):
        host = host if host else 'localhost'
        port = port if port else '6379'
        password = password if password else ''
        self.db = redis.StrictRedis(host,port,password=password)

    def close(self):
        self.db.close()

    def zadd(self,key,score,name=DEFAULT_NAME):
        return self.db.zadd(name,{key:score})

    def zscore(self,value,name=DEFAULT_NAME):
        return self.db.zscore(name,value)

    def zrange(self,start=0,end=-1,withscores=True,name=DEFAULT_NAME,desc=False):
        member_list = self.db.zrange(name, start, end, withscores=withscores,desc=desc)
        new_member_list = []
        for member in member_list:
            if isinstance(member,bytes):
                new_member_list.append(member.decode())
            else:
                new_member_list.append((member[0].decode(),member[1]))
        return new_member_list

    def zrangebyscore(self,min=0,max=-1,withscores=True,start=None, num=None,name=DEFAULT_NAME):
        member_list = self.db.zrangebyscore(name, min, max, withscores=withscores,start=start, num=num)
        new_member_list = []
        for member in member_list:
            if isinstance(member,bytes):
                new_member_list.append(member.decode())
            else:
                new_member_list.append((member[0].decode(),member[1]))
        return new_member_list

    def zcount(self,min,max,name=DEFAULT_NAME):
        return self.db.zcount(name,min,max)

    def zcard(self,name=DEFAULT_NAME):
        return self.db.zcard(name)

    def zrem(self,*values,name=DEFAULT_NAME):
        return self.db.zrem(name,*values)

    def zremall(self):
        return self.zrem(*self.zrange(withscores=False))

if __name__ == '__main__':

    r = RedisClient()
    # r.zadd('c',1)
    print(r.zrange())
    a = r.zremall()
    print(a)
    print(r.zrange())

    r.close()
