import pymysql

def connect():
    try:
        conn = pymysql.connect(
            host='192.168.6.85',
            user='yanfa',
            password='yanfa',
            port=13301,
            database='dbms'
        )
    except Exception as e:
        return None
    return conn

def insert(sql):
    conn = connect()
    if not conn:
        return "conn db fail",False
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        return 'insert sucess',True
    except Exception as e:
        conn.rollback()
        return e ,False
    finally:
        cur.close()
        conn.close()
def update():
    pass

def select(sql):
    conn = connect()
    with conn.cursor() as cursor:
        try:
            cursor.execute(sql)
        except Exception as e:
            return 'execute sql Exception:{}'.format(e),False
        data = cursor.fetchall()
        rowcount= cursor.rowcount
        if rowcount == 0:
            print("NO data in sql")
            return None,False
        else:
            conn.close()
            return data,True
        print(cursor.rowcount,data)

def delete(sql):
    conn = connect()
    if not conn:
        return "conn db fail",False
    cur = conn.cursor()
    try:
        cur.execute(sql)
        if cur.rowcount != 1:
            return 'delete fail',False

        conn.commit()
        return 'delete sucess',True
    except Exception as e:
        conn.rollback()
        return e ,False
    finally:
        cur.close()
        conn.close()



def main():
    for i in range(10,30):   
         sql = '''insert into user(username,password,age) values('kk{}','pwd{}',{});'''.format(i,i,i)
         insertMsg,ok = insert(sql)
         if not ok:
             print(insertMsg) 

        # sql = '''select time,INFO from information_Schema.PROCESSLIST where command='query' and time>60;'''
        # deleteMsg,ok = select(sql)
        # if not ok:
        #     print(deleteMsg)
        # print(deleteMsg,type(deleteMsg))
        # print("sql is {}".format(deleteMsg[0][1]))
      

if __name__ == '__main__':
    main()