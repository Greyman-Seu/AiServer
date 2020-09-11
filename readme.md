# Introduction

This is a simple server for WEB deployment.

**directory structure**:

```
server
   |-- app : python code
   |-- 
```




# 简介

针对CV设计的服务框架，主要用于快速学习掌握web部署，并将任务迁移至该框架中。


目录结构：

```
server
   |-- app ：核心算法等脚本
   |-- docker：部署用脚本
   |-- docs：文档
   |-- requirements：用于存放依赖文件
   |-- test：针对各项功能进行测试
   |-- script_bash: 关键bash脚本
```



# 安装
安装redis
"""
https://www.cnblogs.com/wangchunniu1314/p/6339416.html
sudo apt-get install redis-server
"""


安装docker
安装docker-compose



# TODO
1. docker部署（dockerfile docker-compose）
2. redis启动，自启，需要配置文件


# BUG
1. celery日志有问题,命名使用实时时间到秒时，会出现两个文件
2. celery目前只能输出用户定义的输出，celery输出信息无法保存，即目前celery日志完全和celery本身的日志系统独立。
3. celery输出两遍 
4. uvicorn命令行启动有些问题，日志文件需要改成ini输出
5. 接口开放好像有点问题
6. 启动sh脚本需要读取yml中的配置文件


# 改进
1. 需要一个完善的日志，需求可以满足多进程线程以及celery日志输出
2. celery加跨域