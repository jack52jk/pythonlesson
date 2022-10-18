import pymysql





conn=pymysql.connect(host="192.168.6.85",
                    user="yanfa",
                    password="yanfa",
                    database="test",
                    port=13301
                    )
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