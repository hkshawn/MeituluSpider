# MeituluSpider

> - 爬取[美图录网小清新](https://www.meitulu.com/t/qingxin/)美女图
> - 放弃利用MD5命名方式去重，太丑没必要，使用作品名称加序号命名照片。
> - 对比作品与文件夹内文件数量进行去重。
<br><br/>

### 运行环境

Win10<br>
Python3.6<br>
<br/>

## 安装
```python
pip install -r requirements.txt
```

## 配置
- qingxin可以替换成标签
```python
url = 'https://www.meitulu.com/t/qingxin/' + str(page_num) + '.html'
```

- 按情况增加或减少进程数
```python
pool = Pool(3)
```

## 运行

```python
python run meituluspider.py
```


### 运行效果
```
C:\Anaconda3\python.exe C:/PythonProjects/RequestsProjects/downgirls.py
合集名称： [BoLoLi波萝社]BOL040夏美酱-白裙夏美写真图片[87] URL: https://www.meitulu.com/item/10363.html
合集名称： [Qingdouke青豆客]杨诺依-小清新大眼女神[53] URL: https://www.meitulu.com/item/9202.html
合集名称： [Ugirls尤果网]U125顾欣怡II[62] URL: https://www.meitulu.com/item/7746.html
合集名称： 林岗怡Didy-甜妹子唯美小清新超高清写真[55] URL: https://www.meitulu.com/item/6910.html
正在下载： [BoLoLi波萝社] BOL040 夏美酱 - 白裙夏美 写真图片第1张
正在下载： [Qingdouke青豆客] 杨诺依 - 小清新大眼女神第1张
正在下载： [Ugirls尤果网] U125 顾欣怡II 第1张
正在下载： [BoLoLi波萝社] BOL040 夏美酱 - 白裙夏美 写真图片第2张
正在下载： [Ugirls尤果网] U125 顾欣怡II 第2张
正在下载： [BoLoLi波萝社] BOL040 夏美酱 - 白裙夏美 写真图片第3张
正在下载： [Ugirls尤果网] U125 顾欣怡II 第3张
正在下载： [Qingdouke青豆客] 杨诺依 - 小清新大眼女神第2张
正在下载： 林岗怡Didy - 甜妹子唯美小清新超高清写真第1张
正在下载： [BoLoLi波萝社] BOL040 夏美酱 - 白裙夏美 写真图片第4张
正在下载： [Ugirls尤果网] U125 顾欣怡II 第4张
正在下载： [Qingdouke青豆客] 杨诺依 - 小清新大眼女神第3张
正在下载： 林岗怡Didy - 甜妹子唯美小清新超高清写真第2张
正在下载： [Ugirls尤果网] U125 顾欣怡II 第5张
正在下载： [Qingdouke青豆客] 杨诺依 - 小清新大眼女神第4张
正在下载： [Ugirls尤果网] U125 顾欣怡II 第6张
正在下载： 林岗怡Didy - 甜妹子唯美小清新超高清写真第3张
正在下载： [BoLoLi波萝社] BOL040 夏美酱 - 白裙夏美 写真图片第5张
```

### 注意事项
- 程序已设置适当延迟，请合理使用
