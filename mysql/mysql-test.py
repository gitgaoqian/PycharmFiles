# -*- coding: utf-8 -*-
import IPy
import MySQLdb
import MySQLdb.cursors
import os
conn = MySQLdb.connect(host="127.0.0.1", user="root", db="CloudROS", passwd="ubuntu", charset="utf8",
                   )
cur = conn.cursor()
subnet =  str((IPy.IP('192.168.1.100').make_net('255.255.255.0')))
usr_ip = "192.168.100"
#获取服务对应的镜像名称
service = "teleop"
rows = cur.execute("select * from docker_image where service=%s",service)#获取限制条件下的表的数据,返回符合条件的行数
result = cur.fetchall()#获取限制条件下的结果,默认返回数组,在链接函数中加上参数cursorclass = MySQLdb.cursors.DictCursor,返回字典形式
docker_image = str(result[0][1])
#usr_info插入一条空数据
cur.execute("insert into usr_info values (%s,%s,%s,%s,%s)",(usr_ip,None,None,None,None))
conn.commit()
#usr_info更新数据
cur("update usr_info set status=%s  where usr_ip=%s and service=%s",status,usr_ip,service,docker,image)


# file = os.popen(cmd)
# print file.read()