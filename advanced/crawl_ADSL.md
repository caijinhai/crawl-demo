## 爬虫ADSL

[参考链接](https://cuiqingcai.com/4596.html)

大体思路：
动态拨号主机(安装代理服务器) --> 固定主机

1. 拨号主机手动拨号，生成动态IP，请求固定主机
2. 固定主机获取动态拨号主机IP，记录到redis
3. 从redis中获取动态IP和端口，设置代理，开始爬虫
