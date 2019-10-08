# -*- coding:utf-8 -*-
import os,sys
import re,time
import Levenshtein
import xlrd,xlwt
from xlutils.copy import copy
import os
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')
#----------------------------------

elements_xls_path = "elements.xls"
if not os.path.exists(elements_xls_path):
    os.system(r"touch {}".format(elements_xls_path))

def get_elements(icon):
    # element_tmp 为列表：【查找方式，查找内容，具体下标】
    Data = xlrd.open_workbook(elements_xls_path)
    table = Data.sheet_by_name("Sheet1")
    nrows = table.nrows
    for i in range(nrows):
        element_tmp = table.cell(i,0).value
        if element_tmp == icon:
            return [table.cell(i,1).value,table.cell(i,2).value,int(table.cell(i,3).value),table.cell(i,4).value,i]
    print '未找到该元素'
    return 'error'

def update_elements(id,html,tmp,tmp_value,index):
    Data = xlrd.open_workbook(elements_xls_path)
    ww = copy(Data)
    ww.get_sheet(0).write(id, 1,tmp)
    ww.get_sheet(0).write(id, 2,tmp_value)
    ww.get_sheet(0).write(id, 3,index)
    ww.get_sheet(0).write(id, 4,html)
    os.remove(elements_xls_path)
    ww.save(elements_xls_path)

def getelement(driver,icon):
    #考虑触发时机和成本
    time1 = time.time()
    element = get_elements(icon)
    if element == 'error':
        raise Exception
    print '定位: %s 中...'%icon
    try:
        el = driver.find_elements(element[0],element[1])[element[2]]
        print '定位成功! 耗时:%s 秒'%str(time.time()-time1)[:5]
        return el
    except:
        #启动重新锁定算法
        old_html = element[3]
        print '定位失败，启动自动维护算法...'
        newel_detail = search_new(driver,old_html)
        newel = newel_detail[0]
        new_html = newel_detail[1]
        new_tmp = newel_detail[2]
        new_tmp_value = newel_detail[3]
        new_index = newel_detail[4]
        update_elements(element[4],html=new_html,tmp=new_tmp,tmp_value=new_tmp_value,index=new_index)
        print '维护成功，已找到元素！耗时:%s 秒'%str(time.time()-time1)[:5],
        return newel


def likescore(oldstr,newstr):
    score = Levenshtein.ratio(str(oldstr), str(newstr))
    return score


def search_new(driver,old_html):
    #--------------------------------------------------------
    #结构性，可拓展性，提升空间，容错性，风险性，效率性，幂等性，方便用户/麻烦留给自己,考虑边界，考虑空
    #--------------------------------------------------------获取旧的各项数据用作对比相似度
    try:old_id = re.findall(r'id="(.*?)"',old_html)[0]
    except:old_id = None
    try:old_name = re.findall(r'name="(.*?)"',old_html)[0]
    except:old_name=None
    try:old_class = re.findall(r'class="(.*?)"',old_html)[0]
    except:old_class=None
    try:old_text = re.findall(r'>(.*?)<',old_html)[0]
    except:old_text=''
    try:old_value = re.findall(r'value="(.*?)"',old_html)[0]
    except:old_value=''
    try:old_onclick = re.findall(r'onclick="(.*?)"',old_html)[0]
    except:old_onclick=None
    try:old_style = re.findall(r'style="(.*?)"',old_html)[0]
    except:old_style=''
    try:old_placeholder = re.findall(r'placeholder="(.*?)"', old_html)[0]
    except:old_placeholder=None
    try:old_href = re.findall(r'href="(.*?)"',old_html)[0]
    except:old_href=None
    try:old_type = re.findall(r'type="(.*?)"',old_html)[0]
    except:old_type = None
    #--------------------------------------------------------获取新的所有元素的各参数
    bq = re.findall(r'<(.+?) ',old_html)[0]
    new_elements = driver.find_elements_by_tag_name(bq)
    end_element = new_elements[0]
    end_index = 0
    tmp_score = 0
    for i in range(len(new_elements)):
        score = 0
        new_id = new_elements[i].get_attribute("id")
        new_name = new_elements[i].get_attribute("name")
        new_class = new_elements[i].get_attribute("class")
        new_text = new_elements[i].text
        new_value = new_elements[i].get_attribute("value")
        new_onclick = new_elements[i].get_attribute("onclick")
        new_style = new_elements[i].get_attribute("style")
        new_placeholder = new_elements[i].get_attribute("placeholder")
        new_href = new_elements[i].get_attribute("href")
        try:new_type = re.findall(r'type="(.*?)"',new_elements[i].get_attribute("outerHTML"))[0]
        except:new_type = None
        score += likescore(old_id, new_id)
        score += likescore(old_name, new_name)
        score += likescore(old_class, new_class)
        score += likescore(old_text, new_text)
        score += likescore(old_value, new_value)
        score += likescore(old_onclick, new_onclick)
        score += likescore(str(old_style).replace(' ',''), str(new_style).replace(' ',''))
        score += likescore(old_placeholder, new_placeholder)
        score += likescore(old_href, new_href)
        score += likescore(old_type,new_type)
        if score > tmp_score:
            end_element = new_elements[i]
            end_index = i
            tmp_score = score
    new_html = end_element.get_attribute("outerHTML")
    new_tmp = 'tag name' #可选其他如id，name等
    new_tmp_value = bq
    new_index = end_index
    return [end_element,new_html,new_tmp,new_tmp_value,new_index]




