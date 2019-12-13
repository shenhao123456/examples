##解析mib文件获得企业私有oid
### 下载pysmi库
把mibs文件解压到  /usr/share/snmp/mibs    
执行 mibdump.py --generate-mib-texts  --destination-format json MIB文件名
生成json的文件
