NEU_GDMAP:这是关于简单离线地图服务器的程序.主要使用的是高德地图.具体过程是: 1 制作某一区域的瓦片 2 将gps坐标系转换到高德坐标系,并进一步转换到像素坐标系,获取像素坐标 3 获取瓦片坐标 4 利用opencv工具在相应的瓦片上的像素点进行标注

CLOUD_VERIFY:该python程序包主要实现对CloudROS系统运行的数据进行处理,包括验证性数据分析和Qos分析. QOS分析:Qos中的QoSPlot.py 云服务验证:
time_task,hz_topics