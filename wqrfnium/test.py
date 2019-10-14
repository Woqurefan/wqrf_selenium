import sys,requests,json
reload(sys)
sys.setdefaultencoding('utf-8')
import re,time
from selenium import webdriver
from wqrfnium import *

driver = webdriver.Chrome()
driver.get("http://wwww.baidu.com/")
time.sleep(2)
getelement(driver,"seachinput").send_keys('xiaozhu')
time.sleep(3)
driver.quit()

