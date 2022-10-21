


import pymysql


def connect():
    try:
        conn = pymysql.connect(
            host='192.168.6.85',
            user='yanfa',
            password='yanfa',
            port=13301,
            database='test'
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

def select():
    pass

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
    # for i in range(10,30):   
    #      sql = '''insert into users(username,age,tel,email) values('kk{}',{},'133xxx','kk1@163.com');'''.format(i,i)
    #      insertMsg,ok = insert(sql)
    #      if not ok:
    #          print(insertMsg) 

        sql = '''delete from users where username="kk10";'''
        deleteMsg,ok = delete(sql)
        if not ok:
            print(deleteMsg)

if __name__ == '__main__':
    main()