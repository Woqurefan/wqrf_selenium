import os,sys
import re,time
import Levenshtein
import xlrd,xlwt
from xlutils.copy import copy
import os,platform
import configparser



#----------------------------------

# diy your elements_xls_path

def create_xls(elements_xls_path):
    if not os.path.exists(elements_xls_path):
        book = xlwt.Workbook(encoding='utf-8',style_compression=0)
        book.add_sheet('Sheet1',cell_overwrite_ok=True)
        book.save(elements_xls_path)

def get_elements(icon):
    try:
        Data = xlrd.open_workbook(elements_xls_path)
    except Exception,e:
        print e
        print('Please put the element into the elements.xls first!')
        print('First column:icon,Second column:tmp_find_method,Third column:tmp_find_value,Fourth column:index,Fifth column:html_element')
        print('For example:seachinput,id,kw,0,<input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">')
        exit(0)
    table = Data.sheet_by_name("Sheet1")
    nrows = table.nrows
    for i in range(nrows):
        element_tmp = table.cell(i,0).value
        if element_tmp == icon:
            try:
                html_element = table.cell(i,4).value
            except:
                html_element = ''
            return [table.cell(i,1).value,table.cell(i,2).value,int(table.cell(i,3).value),html_element,i]
    print('not fonund the element: [ %s ],please fixed it by yourself...'%icon)
    exit(0)

def update_elements(id,html,tmp,tmp_value,index):
    Data = xlrd.open_workbook(elements_xls_path)
    ww = copy(Data)
    ww.get_sheet(0).write(id, 1,tmp)
    ww.get_sheet(0).write(id, 2,tmp_value)
    ww.get_sheet(0).write(id, 3,index)
    ww.get_sheet(0).write(id, 4,html)
    os.remove(elements_xls_path)
    ww.save(elements_xls_path)

def input_html_element(id,html):
    Data = xlrd.open_workbook(elements_xls_path)
    ww = copy(Data)
    ww.get_sheet(0).write(id, 4, html)
    os.remove(elements_xls_path)
    ww.save(elements_xls_path)

def likescore(oldstr,newstr):
    score = Levenshtein.ratio(str(oldstr), str(newstr))
    return score

def search_new(driver,old_html):
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
    #--------------------------------------------------------get all par
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
    new_tmp = 'tag name' #use id,name
    new_tmp_value = bq
    new_index = end_index
    return [end_element,new_html,new_tmp,new_tmp_value,new_index]

def getelement(driver,icon):
    time1 = time.time()
    element = get_elements(icon)
    if element == 'error':
        raise Exception
    print('find: %s ...'%icon)
    old_html = element[3]
    try:
        el = driver.find_elements(element[0],element[1])[element[2]]
        print('success in %s s'%str(time.time()-time1)[:5])
        if old_html == '':
            print('you forget input the html_element for %s then wqrfnium help you input it.'%icon)
            html_element = el.get_attribute("outerHTML")
            input_html_element(element[-1],html_element)
        return el
    except Exception,e:
        print e
        print('find_faild,begin fix....')
        newel_detail = search_new(driver,old_html)
        newel = newel_detail[0]
        new_html = newel_detail[1]
        new_tmp = newel_detail[2]
        new_tmp_value = newel_detail[3]
        new_index = newel_detail[4]
        update_elements(element[4],html=new_html,tmp=new_tmp,tmp_value=new_tmp_value,index=new_index)
        print('find success in %s s'%str(time.time()-time1)[:5])
        return newel

try:
    cfp = configparser.ConfigParser()
    cfp.read('wqrfnium.ini')
    elements_xls_path = cfp.get('Excel','elements_xls_path')
except: # create wqrfnium.ini
    cfp = configparser.ConfigParser()
    cfp["Excel"] = {"elements_xls_path":""}
    with open('wqrfnium.ini','w') as fp:
        cfp.write(fp)
    elements_xls_path = cfp.get('Excel','elements_xls_path')

def begin_wqrf(path):
    global elements_xls_path
    if 'xls' not in path.split('.')[-1]:
        if path[-1] == '/':
            path += 'elements.xls'
        else:
            path += '/elements.xls'
    if elements_xls_path != path:
        print("----------------------------------")
        print("You are changeing the elements_xls_path,the new path is %s now!"%path)
        print("You'd better handle the old elements_xls : %s by yourself."%elements_xls_path)
        create_xls(path)
    cfp.set("Excel","elements_xls_path",path)
    with open("wqrfnium.ini","w+") as f:
        cfp.write(f)
    elements_xls_path = path


if elements_xls_path == '': #no path
    # begin to set the elements
    if 'arwin' in platform.system() or 'inux' in platform.system() :
        elements_xls_path =os.environ['HOME']+"/elements.xls"
    else:
        elements_xls_path = "C:\\elements.xls"
    print('You are first use wqrfnium,it is creating elements.xls,you must edit elements.xls and play wqrfnium after!')
    print('Your elements.xls tmp path is %s' % elements_xls_path)
    print("First colum is element's icon,second is element's tmp_find_method,third is element's tmp_find_value,forth is element's index,the last is element's html_element")
    print("You can also read the README to get help or wirte email to 1074321997@qq.com")
    print('You can use code [begin_wqrf("your diy new elements_xls_path ")] to diy your elements_xls_path!')
    create_xls(elements_xls_path)
    cfp.set("Excel", "elements_xls_path", elements_xls_path)
    with open("wqrfnium.ini", "w+") as f:
        cfp.write(f)


elif elements_xls_path == os.environ['HOME']+"/elements.xls" or elements_xls_path == "C:\\elements.xls": # default path
    print('Your elements.xls tmp path is default : %s'%elements_xls_path)

else : #diy path
    print('Your elements.xls tmp path is diy by yourself : %s' % elements_xls_path)