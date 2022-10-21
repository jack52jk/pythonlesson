import pymysql



'''
 def __init__(
        self,
        *,
        user=None,  # The first four arguments is based on DB-API 2.0 recommendation.
        password="",
        host=None,
        database=None,
        port=0,
        ...
        ):

'''
# 1 创建连接  conn=pymysql.connect(host,user,password,port,database)
conn=pymysql.connect(host="192.168.6.85",
                    user="yanfa",
                    password="yanfa",
                    database="test",
                    port=13301
                    #autocommit=True
                    )
print(conn)
#print(conn.select_db('huaplus'))
print(conn.db)
print(dir(conn))

#增加记录
#sql = '''insert into users(username,age,tel,email) values('kk1',29,'133xxx','kk1@163.com');'''
#修改记录
#sql = '''update users set age = 25 where username='kk';'''
#
#查询记录
sql = '''select * from users '''

print(sql)
# 2 创建游标
cursur = conn.cursor()

#3 使用游标执行sql
cursur.execute(sql)
#conn.commit()
data = cursur.fetchall()
print(data)
cursur.close()
conn.close






''' 
with conn.cursor() as cursor:
    sql = """
        select * from t1_is"""
    isSucess=cursor.execute(sql)
    
    print(isSucess)
    res = cursor.fetchall() 
    print("res is {},type:{}".format(res,type(res)))
    cursor.close()
with conn.cursor() as cursor:
    dmlsql = "update t1_is set id=2 where id=0"
    isSucess = cursor.execute(dmlsql)
    print(isSucess)
    conn.commit() 
'''