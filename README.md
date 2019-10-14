# wqrf_selenium 简称 wqrfnium
封装的selenium和po模式，可自动维护元素和减少前端ui修改带来的麻烦工作量  
---------
## 更新：
  修复部分用户自动生成的xls文件打不开问题  
  新增首次无需手动粘贴html_element字段，系统会自动生成。  
  默认支持python2,目前python3报错问题修复
## 您需要维护的部分：  
  wqrfnium会自动生成一个excel表,并打印表位置，您需要把您selenium脚本中经常容易因前端变化导致定位失败的元素放入此表中  
  每行一个元素，列含义：  
  元素标识-icon：用户自行输入(如:seach_input/my_username),之后脚本中getelement方法中需要传入driver和icon    
  默认定位方式-tmp_find_method：用户需自行输入初始(如id/name等)，之后脚本会自行维护无需再度关心  
  默认定位值-tmp_find_value：用户需自行输入初始(如username/password/kw/login等),之后脚本会自行维护无需再度关心  
  下标-index：用户自行输入初始(如0/1/2/3....),之后脚本会自行维护无需再度关心  
  原始html标签内容-html_element-：系统自动生成，无需关心
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
  3.手动进入elements.xls,把要定位的页面元素手动输入定位方式和定位值,粘贴到excel表中，每行一个元素  
    第一列：元素的标识,用于之后代码中直接调用该元素，如示范代码中的“seachinput”  
    第二列：元素的默认定位方式，如id  
    第三列：元素的默认定位值，如 kw  
    第四列：元素的下标，默认0，算法获取元素是获取符合要求的所有元素    
    第五列：元素的html源码标签，无需注意，由系统自动生成。  
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
