import json
from prettytable import PrettyTable
from time import sleep,time
import pymysql




FILE_NAME = 'slow.txt'
RESULT={}
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
            return None,True
        else:
            conn.close()
            return data,True

def getslowsql():
        l = []
        sql = '''
            select now(),time,INFO from information_Schema.PROCESSLIST where command='query' and time>60;
            '''
        result,ok = select(sql)
        if not ok or result == None:
            print("result len is   {}".format(result))
            result = [("now","0","None")]
        
        # print(result,type(result))
        # print("sql is {}".format(result[0][1]))
            #l.append(row)
        # print(pt)
        # print("html: {},type is {}".format(pt.get_html_string(),type(pt.get_html_string)))


        pt = PrettyTable()
        pt.field_names=("datetime","executing_time","sql_info")
        for i in result:
            row = {"datetime":i[0],"executing_time":i[1],"sql_info":i[2]}
            pt.add_row(list(i))
        htmlstr = pt.get_html_string()
        with open(FILE_NAME,'a+') as fd:
            fd.write(htmlstr)

def save():
    """ 
    内存中的文件 写入磁盘
    """
    with open(FILE_NAME,'w') as fd:
        fd.write(json.dumps(RESULT))



def main():
    i = 0 
    endi = 1*60*24
    
    #getslowsql()
    while i < endi:
        getslowsql()
        sleep(60)
        i = i +1
        
        

    


if __name__ == '__main__':
    main()