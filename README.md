# FuckCampusNetwork
WHU校园网断线重连

需要安装python3。

首先，使用Chrome访问老版校园网登陆界面，我的是：http://202.114.64.105:8080/eportal/index.jsp?wlanuserip=3a8ff21827e9725895d16a216147aa8e&wlanacname=29185648f4390d7911ef4b72391e17a9&ssid=&nasip=07e38f2323f330cd5ffcc3a203a63100&snmpagentip=&mac=d7e95c17ebfa93c63883aa996476b664&t=wireless-v2&url=096e8e7059e430e05980c3c547fed4ab7ccaeae90dfffda4ace4874ac81c5ad69031883e2cfd5141&apmac=&nasid=29185648f4390d7911ef4b72391e17a9&vid=09cdf5983594be55&port=e65ae3d6b3555e50&nasportid=ac41d60d7f1382081362a1ed29e6af27765f700f39a3c6faab4fcef7ba2a66115e5ea510602ede97  
  
然后，按F12打开浏览器检查工具，点击Network标签页，然后去登陆页面填入账号密码登陆一次，此时在Network下面会出现几个网络包，找到一个地址包含userV2.do?method=login  
的包点开，查看其参数。  

然后，用记事本打开这个py文件，把变量 get_params 中对应的参数修改成你在上面找到的。  

在当前文件夹下打开命令行输入 python autoLogin.py 运行这个py文件即可。  

如果提示没有安装requests模块，打开命令行输入 pip install requests 即可。  
