# fzbk
备份文件扫描 fuzz 网站备份文件 支持多线程 支持单个 支持批量 更多功能待开发 


自动生成 相关备份并扫描 ，常见备份文件扫描 默认：20 线程

python fzbk.py -u https://www.baidu.com #单个
                                                
python fzbk.py -f urls.txt              #批量



常见 后缀 houzhui = ['.gz', '.sql.gz', '.tar.gz','.tar.tgz','.rar','.zip','.tar','.tar.bz2','.sql','.7z','.bak','.txt','.git','.svn','.swp','.mdb','.old','.log']


https://baidu.com            生成相关域名：1440 个
 
https://www.baidu.com        生成相关域名：1440 个

https://pan.baidu.com        生成相关域名：1440 个

https://www.pan.baidu.com    生成相关域名：1440 个


效果展示
![image](https://user-images.githubusercontent.com/63041902/110199916-d1cc8300-7e95-11eb-83db-b1d3b01507b5.png)




