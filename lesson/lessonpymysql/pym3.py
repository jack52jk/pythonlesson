'''
pymysql模块实现对数据库的增,删,改,查,功能 并测试数据从内存保存到数据库,以及从数据库到内存
'''

#第三方模块
import configparser
import pymysql

configFile='my.cnf'

host=None
user=None
password=None
port=None
database=None

RESULT={}
#RESULT = {'monkey1': {'name': 'monkey1', 'age': 12, 'tel': '132xxx', 'email': 'monkey1@qq.com'}, 'monkey10': {'name': 'monkey10', 'age': 10, 'tel': '1310xx', 'email': 'monkey10@qq.com'}, 'monkey11': {'name': 'monkey11', 'age': 11, 'tel': '1311xx', 'email': 'monkey11@qq.com'}, 'monkey12': {'name': 'monkey12', 'age': 12, 'tel': '1312xx', 'email': 'monkey12@qq.com'}, 'monkey13': {'name': 'monkey13', 'age': 13, 'tel': '1313xx', 'email': 'monkey13@qq.com'}, 'monkey14': {'name': 'monkey14', 'age': 14, 'tel': '1314xx', 'email': 'monkey14@qq.com'}, 'monkey15': {'name': 'monkey15', 'age': 15, 'tel': '1315xx', 'email': 'monkey15@qq.com'}, 'monkey16': {'name': 'monkey16', 'age': 16, 'tel': '1316xx', 'email': 'monkey16@qq.com'}, 'monkey17': {'name': 'monkey17', 'age': 17, 'tel': '1317xx', 'email': 'monkey17@qq.com'}, 'monkey18': {'name': 'monkey18', 'age': 18, 'tel': '1318xx', 'email': 'monkey18@qq.com'}, 'monkey19': {'name': 'monkey19', 'age': 19, 'tel': '1319xx', 'email': 'monkey19@qq.com'}}

'''
test db into mem
'''
def loadDB():
    sql = "select username,age,tel,email from users"
    res,ok = select(sql)
    if not ok:
        print("加载数据失败")
        print(res)
    else:
         for listv in res:
            global RESULT
            RESULT[listv[0]]={"name":listv[0],"age":listv[1],"tel":listv[2],"email":listv[3]}
    print(RESULT)     

'''
test save db
'''
def saveDB():
    TABLE = 'users'
    FILEDS_NAME=('username','age','tel','email')
    if(len(RESULT) == 0):
        print("RESULT is null")
        return "RESULT is null",True
    for username,userinfo in RESULT.items():
        selectsql="select {} from {} where username=\"{}\"".format(','.join(FILEDS_NAME),TABLE,username)
        print(selectsql)
        res,ok = select(selectsql)
        if not ok:
            userinfovalue = list(userinfo.values())
            insertsql="insert into {} ({}) values (\"{}\",{},\"{}\",\"{}\")".format(TABLE,",".join(FILEDS_NAME),userinfovalue[0],int(userinfovalue[1]),userinfovalue[2],userinfovalue[3])
            print(insertsql) 
            res,ok = insert(insertsql)
            if not ok:
                print(res)
            else:
                print("save sucess")   
        else:
            print(res)
            print("user {} already exist".format(username))

'''解析配置文件'''
def parseConfig():
    confpar = configparser.ConfigParser()
    confpar.read(configFile)
    return confpar

def Connect():
    cnf = parseConfig()
    host=cnf['mysql']["host"]
    user=cnf['mysql']['user']
    password = cnf['mysql']['password']
    port = int(cnf ['mysql']['port'])
    database= cnf['mysql']['database']
   # print("mysql connect info : \n host : {}\n user:{} \n password: {} \n port : {}\n database : {}".format(host,user,password,port,database))
    try:
        conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=database)
        return conn,True
        print(conn)
    except Exception as e :
        #print("connection mysql exception: {}".format(e))
        return 'connection exception: {}'.format(e),False
    # finally:
    #     conn.close()

'''deal with insert sql'''
def insert(sql):
    if(len(sql) == 0):
        return 'sql error!',False
    conn,ok = Connect()
    if not ok:
        return conn,False

    with conn.cursor() as cursor:
        try:
            cursor.execute(sql)
            rowcount=cursor.rowcount
            #print(rowcount)
            if(rowcount == 0):
                conn.rollback()
                return '{} fail'.format(sql),False
            else:
                conn.commit()
                return "{} sucess".format(sql),True
        except Exception as e:
            return 'execute sql Exception:{}'.format(e),False

'''deal with update sql'''
def update(sql):
    if(len(sql) == 0):
        return 'sql error!',False
    conn,ok = Connect()
    if not ok:
        return conn,False

    with conn.cursor() as cursor:
        try:
            cursor.execute(sql)
            rowcount=cursor.rowcount
            #print(rowcount)
            if(rowcount == 0):
                conn.rollback()
                return '{} fail'.format(sql),False
            else:
                conn.commit()
                return "{} sucess".format(sql),True
        except Exception as e:
            return 'execute sql Exception:{}'.format(e),False
'''deal with delete sql'''
def delete(sql):
    if(len(sql) == 0):
        return 'sql error!',False
    conn,ok = Connect()
    if not ok:
        return conn,False

    with conn.cursor() as cursor:
        try:
            cursor.execute(sql)
            rowcount=cursor.rowcount
            if(rowcount == 0):
                conn.rollback()
                return '{} fail'.format(sql),False
            else:
                conn.commit()
                return "{} sucess".format(sql),True
        except Exception as e:
            return 'execute sql Exception:{}'.format(e),False


'''deal with select sql'''
def select(sql):
    conn,ok = Connect()
    if not ok:
        return conn,False
    if(len(sql) == 0):
        return 'sql error!',False
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




def main():
    loadDB()
    #saveDB()
    # conn,ok = Connect()
    # if not ok:
    #     print(conn)
    # sql = "select * from users where id=1"
    # res,ok = select(sql)
    # if not ok:
    #     print(res)
    # else:
    #     data = res
    #     print(data,type(data)) 
    # username="kk33"
    # age = 33
    # tel = "132xxx"
    # email = "kk3@163.com"
    # sql = "insert into users(username,age,tel,email) values(\"{}\",{},\"{}\",\"{}\");".format(username,age,tel,email)
    # res,ok = insert(sql)
    # if not ok:
    #     print(res)
    # else:
    #     print("sql sucess")
    # username="kk30"
    # age=11
    # sql = "update users set age={} where username = \"{}\"".format(age,username)
    # res,ok = update(sql)
    # if not ok:
    #     print(res)
    # else:
    #     print("sql sucess")


if __name__=="__main__":
    main() 
