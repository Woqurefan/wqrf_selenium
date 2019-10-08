import sys,requests,json
reload(sys)
sys.setdefaultencoding('utf-8')
import re,time
from selenium import webdriver
from wqrfnium import *

driver = webdriver.Chrome()
driver.get("http://wwww.baidu.com/")
time.sleep(2)
getelement(driver,"kw").send_keys('xiaozhu')


driver.quit()

