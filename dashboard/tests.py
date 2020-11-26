from socket import timeout
from django.test import TestCase

# Create your tests here.

# titles = ['ล๊อตที่ - ชุดที่','เลขที่โฉนด','ลำดับที่การขาย','หมายเลขคดี','ประเภททรัพย์','ไร่','งาน','ตร.วา','ราคาประเมิน','ตำบล','อำเภอ','จังหวัด']
# for index in range(len(titles)):
#     print(f'title[{index}] = {titles[index]}')


 
# import webbrowser
# webbrowser.open('http://google.com', new=2)

# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select

# driver = webdriver.Chrome('/Users/chawput/Google Drive/dev/chromedriver')  # Optional argument, if not specified will search path.
# driver.get('http://dolwms.dol.go.th/tvwebp/');
# # time.sleep(1) # Let the user actually see something!
# driver.find_element_by_class_name('bts-popup-close').click()
# Select(driver.find_element_by_id('ddlProvince')).select_by_visible_text('อุดรธานี')
# time.sleep(1)
# Select(driver.find_element_by_id('ddlAmphur')).select_by_value('01')
# time.sleep(0.5)
# txtPacelNo = driver.find_element_by_id('txtPacelNo').send_keys('117586')
# time.sleep(0.5)
# driver.find_element_by_id('btnFind').click()

import pymongo
from bs4 import BeautifulSoup 
import pandas as pd 
import re
import csv
from urllib.parse import quote
import requests
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
LANGUAGE = "en-US,en;q=0.5"
session = requests.Session()
session.headers['User-Agent'] = USER_AGENT
session.headers['Accept-Language'] = LANGUAGE
session.headers['Content-Language'] = LANGUAGE
response = requests.get('http://asset.led.go.th/newbidreg/asset_open.asp?law_suit_no=%BC%BA.662&law_suit_year=2557&Law_Court_ID=402&deed_no=117586&addrno=-')
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
cardbody_row = soup.findAll("div", {"class": "card-body"})[0].findAll("div", {"class": "row"})[0]
cardtext = cardbody_row.findAll("div", {"class": "card-text"})[4]
chanode = re.findall("โฉนดเลขที่.+", str(cardtext))[0]
if re.findall("โฉนดเลขที่", str(cardtext))[0]:
    print(chanode)
else:
    print("Not Found Chanode")

# html = requests.get(f'{searchUrl}')
# return status