# wqrf_selenium 简称 wqrfnium
封装的selenium和po模式，可自动维护元素和减少前端ui修改带来的麻烦工作量  
---------
## 功能：  
  封装新的selenium定位方式，基于po模式，本框架把元素的定位都放在了同级的excel表中。其中包含：元素标识，默认定位方式，默认定位值，下标和原始html标签内容  
## 原理：  
  selenium定位时默认先利用excel表中的默认定位方式和默认值定位，若定位失败，则启动自动定位算法，找到最符合要求的元素返回，并把新元素的tagname定位方式和内容写入excel表中以便下次调用。  
## 优点：
  1.使用简单，只需要变化定位语句即可。  
  2.源码简单，方便进行二次开发。  
  3.其中的所有分数权重参数可自行根据公司项目风格更改，来达到99%以上的成功率。  
  4.博主更新快，框架优化和前景非常nice。  
  5.可稍加变化应用到appium中  
## 下载方法:  
  1.可以用pip install wqrfnium  
  2.可以download本项目
## 使用方法:  
  1.示范代码:
  
    from selenium import webdriver
    from wqrfnium import *
    driver = webdriver.Chrome()
    driver.get("http://wwww.baidu.com/")
    time.sleep(2)
    getelement(driver,"seachinput").send_keys('xiaozhu')
  2.首次运行一下，会自动生成存放elements.xls文件，会打印出此文件地址  
  3.手动进入elements.xls,把要定位的页面元素手动复制粘贴到excel表中，每行一个元素  
    第一列：元素的标识,用于之后代码中直接调用该元素，如示范代码中的“seachinput”  
    第二列：元素的默认定位方式，如id  
    第三列：元素的默认定位值，如 kw  
    第四列：元素的下标，默认0，算法获取元素是获取符合要求的所有元素    
    第五列：元素的html源码标签，可以在浏览器的调试/检查中直接选中元素，然后右键copy_element    
  4.在代码中调用getelement方法，传入driver和元素标识即可，后续前端页面的各种更改，这个定位代码都会成功找到  
## 依赖包:  
  1.selenium  
  2.Levenshtein  
  3.python2  
  4.xlrd  
  5.xlutils  
## 升级预告:  
  1.增加csv文件存放elements  
  2.增加数据库存放elements  
  3.增加xpath自动生产算法  
  4.增加自动录入html源码功能  
