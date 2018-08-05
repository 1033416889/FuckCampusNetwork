import requests
import subprocess
import shlex

# 统计断线重连的次数
count = 0

def login():
    url = "http://202.114.64.105:8080/eportal/userV2.do?"

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    }

    get_params = {
        'method': 'login',
        'param': 'true',
        'wlanuserip': '3a8ff21827e9725895d16a216147aa8e',
        'wlanacname': '29185648f4390d7911ef4b72391e17a9',
        'username': '****',
        'pwd': '****',
        'nasip': '07e38f2323f330cd5ffcc3a203a63100',
        'mac': 'd7e95c17ebfa93c63883aa996476b664',
        't': 'wireless-v2',
        'nasid': '29185648f4390d7911ef4b72391e17a9',
    }

    for k,v in get_params.items():
        url += '%s=%s&'%(k,v)

    url = url[:-1]
    
    r = requests.post(url,headers=headers)



def loop(code='gb2312'):
    global count
    ip = 'www.baidu.com'
    shell_cmd = 'ping %s -t' %ip
    cmd = shlex.split(shell_cmd)
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline()
        line = line.strip()
        if line:
            if line.decode(code).find('请求超时') != -1:
                login()
                count += 1
                print('已断线重连%d次'%count)
                
loop()