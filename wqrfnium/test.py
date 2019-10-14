from selenium import webdriver
from wqrfnium import *

begin_wqrf('./MyElements2.xls')

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
time.sleep(2)
getelement(driver,"seachinput").send_keys('xiaozhu')


