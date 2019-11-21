# wqrf_selenium 简称 wqrfnium
封装的selenium和po模式，可自动维护元素和减少前端ui修改带来的麻烦工作量  
---------
## 最新更新：
  增加api获取/更新 自动维护元素 的方式，可用 from wqrfnium.wqrfnium_api import * 替换 from wqrfnium.wqrfnium import *  
  具体使用方式请细读 使用方法-api  
## 您需要注意的部分：  
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
## 使用方法-exlce:  
  1.示范代码:
  
    from selenium import webdriver
    from wqrfnium.wqrfnium import *
    begin_wqrf('./MyElements.xls')
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com/")
    time.sleep(2)
    getelement(driver,"seachinput").send_keys('xiaozhu')
  2.首次运行一下，会自动生成存放elements.xls文件，会打印出此文件地址(begin_wqrf()为初始化语句，可传入自定义的excel表路径，若不写则会在默认位置生成)  
  3.手动进入elements.xls,把要定位的页面元素手动输入定位方式和定位值,粘贴到excel表中，每行一个元素  
    第一列：元素的标识,用于之后代码中直接调用该元素，如示范代码中的“seachinput”  
    第二列：元素的默认定位方式，如id  
    第三列：元素的默认定位值，如 kw  
    第四列：元素的下标，一般都写0，算法获取元素是获取符合要求的所有元素    
    第五列：元素的html源码标签，无需注意，由系统自动生成。  
  4.在代码中调用getelement方法，传入driver和元素标识即可，后续前端页面的各种更改，这个定位代码都会成功找到  
## 使用方法-api:
  1.示范代码:
  
    from selenium import webdriver
    from wqrfnium_api import *
    get_api_url = "http://xxx.xxx.xxx/aaa/get_element_test/***/"
    update_api_url = "http://xxx.xxx.xxx/bbb/update_element_test/***/"
    begin_wqrf(get_api_url,update_api_url)
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com/")
    time.sleep(2)
    getelement(driver,"searchinput").send_keys('xiaozhu')
  2.首次运行会把配置写入配置文件，之后无需再加入begin_wqrf()方法
  3.您的获取/更新元素接口需要满足如下要求  
  获取元素的api：  
  1.url 中必须有***来占位，这个***就是后来会替换成元素的icon  
  2.必为get  
  3.返回值根路径必须含有元素的五种属性即：{“icon”:"",“tmp_find_method”:"",“tmp_find_value”:"",“index”:"",“html_element”:"",}  
  更新元素的api：  
  1.url 中必须有***来占位，这个***就是后来会替换成元素的icon  
  2.必为post  
  3.请求体根路径必须含有元素的五种属性即：{“tmp_find_method”:"",“tmp_find_value”:"",“index”:"",“html_element”:"",}  
  具体使用帮助可参考博文：https://blog.csdn.net/qq_22795513/article/details/103182097
  
## 依赖包:  
  1.selenium  
  2.python-Levenshtein     
  3.python2/3  
  4.xlrd  
  5.xlutils  
  6.configparser  
  7.requests
## 联系作者:
  qq:1074321997
  
## 历史更新：
  修复部分用户自动生成的xls文件打不开问题  
  增加可自动移excle表位置代码：begin_wqrf('./MyElements.xls')  
  新增首次无需手动粘贴html_element字段，系统会自动生成。  
  同时支持py2,py3 
  
  
  
  
