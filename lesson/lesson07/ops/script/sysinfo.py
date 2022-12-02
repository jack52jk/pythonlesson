'''
此脚本用于获取服务器信息
主机名,内网Ip,mac地址,cpu,磁盘,制造商,服务器类型,序列号,UUID,生产日期,操作系统
'''
import socket
import psutil
import subprocess
import json
import requests



#get hostname
def gethostname():
     hostname=socket.gethostname()
     #print(hostname)
     return hostname
#get private ip
def getprivateip():
    ifdict=psutil.net_if_addrs()
    
    privateinfo=[]
    for ifd,lstsb in ifdict.items():
     #   print("net card is {},info {}".format(ifd,lstsb))
     #   print("-------------------")
        if ifd != 'lo':
            for snic in lstsb :
                if snic.family.name == 'AF_INET':
                    # print("*************")
                    # print(snic)
                    privateip = snic.address 
                    privateinfo.append(privateip)
                    # print("private ip is {}".format(privateip))
                if snic.family.name == 'AF_PACKET':
                    macaddr = snic.address
                    # print("mac address is :{}".format(macaddr))
                    privateinfo.append(macaddr)           
    if len(privateinfo) !=0:
        return True,privateinfo
    else:
        return False,privateinfo                
    #     tmpnetdict =[]
    #     for snic in lstsb:
    #         ipaddress = snic.address
    #         ipnetmask = snic.netmask
    #         ipbroadcast=snic.broadcast
    #         tmpdict = {'ipaddress':ipaddress,'ipnetmask':ipnetmask,'ipbroadcast':ipbroadcast}
    #         print("snic type is {},info {}".format(type(snic),snic.address))
    #         tmpnetdict.append(tmpdict)
    #     tmpdict = {ifd:tmpnetdict}
    #     netdict.append(tmpdict)
    # print(netdict)
    # print(socket.gethostbyname(socket.gethostname()))

'''get CPU number'''
def getCPUcount():
    cpucount=psutil.cpu_count()
    # print(cpucount)
    return cpucount
'''get Disk '''
def getDiskInfo():
    #获取所有硬盘路径
    diskpartinfo = psutil.disk_partitions(all=False) 
    mountpoint =[]
    disktotal=0
    for partnameinfo in diskpartinfo:
        point = partnameinfo.mountpoint
        mountpoint.append(point)
    #统计包含sd的磁盘总容量
    for mpoint in mountpoint:
        if 'data' in mpoint:
            # print(mpoint,psutil.disk_usage(mpoint))
            disktotal = disktotal + psutil.disk_usage(mpoint).total
    diskhuman=psutil._common.bytes2human(disktotal)
    # print("disk total is {}".format(psutil._common.bytes2human(disktotal)))   
       # print(psutil.disk_usage(disk).total)
    return diskhuman

#get system info eg  制造商,服务器类型,序列号,UUID,
def getSystemInfo():
    cmd = "dmidecode -t 1"
    isok,res=subprocess.getstatusoutput(cmd)
    print(isok,res)

def run():
    sysinfo={}

    privateip=''
    macaddr=''
    hostname=gethostname()
    cpucount=int(getCPUcount())
    print("*****************cpucount {} {}".format(cpucount,type(cpucount)))
    disksize=getDiskInfo()
    manufacturer="华为"
    servertype="虚拟机"
    SerialNumber="VMware-56 4d 9f 33 8f df 36 35-71 77 76 15 53 72 1c 52"
    uuid="339f4d56-df8f-3536-7177-761553721c52"
    productdate="2022-11-04"
    os="linux"
    isok,ipinfo = getprivateip()
    if isok:
        privateip = ipinfo[0]
        macaddr = ipinfo[1]
    else:
        privateip='0.0.0.0'
        macaddr='aaaa-aaaa-aaaa-aaaa'
    
    sysinfo['hostname']=hostname
    sysinfo['private_ip']=privateip
    sysinfo['mac_address']=macaddr
    sysinfo['cpu']=cpucount
    sysinfo['vm_status'] = 0
    sysinfo['disk']=disksize
    sysinfo['manufacturers'] = manufacturer
    sysinfo['server_type']=servertype
    sysinfo['st'] = SerialNumber
    sysinfo['uuid']=uuid
    sysinfo['manufacturer_date'] = productdate
    sysinfo['os']=os
    sysinfo['vm_status'] = 0
    # sysinfo={
    #     'hostname':hostname,'private_ip':privateip,'mac_address':macaddr,# 'cpu':cpucount,
    #      'disk':disksize,
    #      'manufacturers':manufacturer,
    #      'server_type':servertype,'st':SerialNumber,'uuid':uuid,'manufacturer_date':productdate,
    #      'os':os, #'vm_status':0
    #     }
    print(json.dumps(sysinfo,indent=4))
    switchinfo(sysinfo)
    #return sysinfo
def switchinfo(data):
    url = "http://127.0.0.1:8000/api/v1/cmdb/collect"
    #print("data is  {},{}".format(data,type(data)))
    req=requests.post(url,data=data)
    print(req.ok)
    print(req.text)
    
    

# def main():
#     #gethostname()
#     #getprivateip()
#     #print(psutil.net_connections('inet4'))
#     #getCPUInfo()
#     #getDiskInfo()
#     #getSystemInfo()
#     # switchinfo()
#     dataProcess()







if __name__ == '__main__':
    run()