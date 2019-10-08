# -*- coding:utf-8 -*-
import sys,requests,json
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')
import re,time
from selenium import webdriver
from wqrf_selenium import *
#------------------------公共工具函数

driver = webdriver.Chrome()
driver.get("http://wwww.baidu.com/")
time.sleep(2)


getelement(driver,"kw").send_keys('xiaozhu')


driver.quit()



