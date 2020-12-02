from django.db.models.query_utils import Q
from django.shortcuts import render
from django.http import HttpResponse
from .models import Asset

def get_html_content(a_type, a_province, a_ampur, bid_date, min_price,max_price, page): #search_url
    import requests
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = requests.get(f'http://asset.led.go.th/newbidreg/asset_search_province.asp?search_asset_type_id={a_type}&search_ampur={a_ampur}&search_province={a_province}&search_bid_date={bid_date}&search_price_begin={min_price}&search_price_end={max_price}&search_status=1&search=ok&page={page}')
    # html = requests.get(f'{searchUrl}')
    return html

def isChanode(law_suit_no, law_suit_year,Law_Court_ID,deed_no,addrno): #search_url
    import requests
    from bs4 import BeautifulSoup 
    import pandas as pd 
    import re
    import time
    from urllib.parse import quote
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    
    law_suit_no = str(law_suit_no.encode('cp874'))
    # addrno = quote(addrno.encode('cp874'))
    law_suit_no  = law_suit_no.replace("b'","").replace("'","")
    response = requests.get(f'http://asset.led.go.th/newbidreg/asset_open.asp?law_suit_no={law_suit_no}&law_suit_year={law_suit_year}&Law_Court_ID={Law_Court_ID}&deed_no={deed_no}&addrno={addrno}')
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(law_suit_no, law_suit_year, Law_Court_ID, deed_no, addrno)
    
    col_lg_7 = soup.findAll("div", {"class": "col-lg-7"})[2]
    cardbody = col_lg_7.findAll("div", {"class": "card-body"})[0]
    cardbody_row = cardbody.findAll("div", {"class": "row"})[0]
    cardtext = cardbody_row.findAll("div", {"class": "card-text"})[4]
    chanode = re.findall("โฉนด", str(cardtext))
    if chanode:
        # print('1')
        # print(f'--------------------')
        return "1"
    else:
        # print(f'--------------------')
        return "0"

def Home(request):
    # stop = False
    import pymongo
    from bs4 import BeautifulSoup 
    import pandas as pd 
    import re
    import csv
    from urllib.parse import quote

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["asset_led"]
    mycol = mydb["dashboard_asset"]

    province_code = {
        ""  : "ทุกจังหวัด",     
        'กระบี่' : "81",
        'กรุงเทพมหานคร' : "10",
        'กาญจนบุรี' : "71",
        'กาฬสินธุ์' : "46",
        'กำแพงเพชร' : "62",
        'ขอนแก่น' : "40",
        'จันทบุรี' : "22",
        'ฉะเชิงเทรา' : "24",
        'ชลบุรี' : "20",
        'ชัยนาท' : "18",
        'ชัยภูมิ' : "36",
        'ชุมพร' : "86",
        'เชียงราย' : "57",
        'เชียงใหม่' : "50",
        'ตรัง' : "92",
        'ตราด' : "23",
        'ตาก' : "63",
        'นครนายก' : "26",
        'นครปฐม' : "73",
        'นครพนม' : "48",
        'นครราชสีมา' : "30",
        'นครศรีธรรมราช' : "80",
        'นครสวรรค์' : "60",
        'นนทบุรี' : "12",
        'นราธิวาส' : "96",
        'น่าน' : "55",
        'บึงกาฬ' : "38",
        'บุรีรัมย์' : "31",
        'ปทุมธานี' : "13",
        'ประจวบคีรีขันธ์' : "77",
        'ปราจีนบุรี' : "25",
        'ปัตตานี' : "94",
        'พระนครศรีอยุธยา' : "14",
        'พะเยา' : "56",
        'พังงา' : "82",
        'พัทลุง' : "93",
        'พิจิตร' : "66",
        'พิษณุโลก' : "65",
        'เพชรบุรี' : "76",
        'เพชรบูรณ์' : "67",
        'แพร่' : "54",
        'ภูเก็ต' : "83",
        'มหาสารคาม' : "44",
        'มุกดาหาร' : "49",
        'แม่ฮ่องสอน' : "58",
        'ยโสธร' : "35",
        'ยะลา' : "95",
        'ร้อยเอ็ด' : "45",
        'ระนอง' : "85",
        'ระยอง' : "21",
        'ราชบุรี' : "70",
        'ลพบุรี' : "16",
        'ลำปาง' : "52",
        'ลำพูน' : "51",
        'เลย' : "42",
        'ศรีสะเกษ' : "33",
        'สกลนคร' : "47",
        'สงขลา' : "90",
        'สตูล' : "91",
        'สมุทรปราการ' : "11",
        'สมุทรสงคราม' : "75",
        'สมุทรสาคร' : "74",
        'สระแก้ว' : "27",
        'สระบุรี' : "19",
        'สิงห์บุรี' : "17",
        'สุโขทัย' : "64",
        'สุพรรณบุรี' : "72",
        'สุราษฎร์ธานี' : "84",
        'สุรินทร์' : "32",
        'หนองคาย' : "43",
        'หนองบัวลำภู' : "39",
        'อ่างทอง' : "15",
        'อำนาจเจริญ' : "37",
        'อุดรธานี' : "41",
        'อุตรดิตถ์' : "53",
        'อุทัยธานี' : "61",
        'อุบลราชธานี' : "34"
    }
    ampur_code = {
        ""  : "",     
        "เมืองอุดรธานี" : "01",
        "เมือง" : "01",
        "กุดจับ" : "02",
        "หนองวัวซอ" : "03",
        "กุมภวาปี" : "04",
        "โนนสะอาด" : "05",
        "หนองหาน" : "06",
        "ทุ่งฝน" : "07",
        "ไชยวาน" : "08",
        "ศรีธาตุ" : "09",
        "วังสามหมอ" : "10",
        "บ้านดุง" : "11",
        "บ้านผือ" : "17",
        "น้ำโสม" : "18",
        "เพ็ญ" : "19",
        "อำเภอสร้างคอม" : "20",
        "สร้างคอม" : "20",
        "หนองแสง" : "21",
        "นายูง" : "22",
        "พิบูลย์รักษ์" : "23",
        "กู่แก้ว" : "24",
        "ประจักษ์ศิลปาคม" : "25"
        }

    asset_type_code = {
        ""  : "ทุกประเภท",            
        "001" : "ที่ดินว่างเปล่า",
        "0010" : "หุ้น",
        "0011" : "หน่วยลงทุน",
        "0012" : "พันธบัตร",
        "0013" : "ใบสำคัญ",
        "0014" : "สลากออมสิน",
        "0015" : "สลากออมทรัพย์",
        "002" : "ห้องชุด",
        "003" : "ที่ดินพร้อมสิ่งปลูกสร้าง",
        "004" : "กรรมสิทธิ์ห้องชุด",
        "005" : "สิทธิการเช่า",
        "006" : "สิทธิการเช่าอาคารพาณิชย์",
        "007" : "สิทธิการเช่าที่ดิน",
        "008" : "ทรัพย์สินต่างๆ",
        "009" : "สิ่งปลูกสร้าง",
        "010" : "สิทธิการเช่าที่ดินฯ",
        "011" : "สิทธิการเช่าสิ่งปลูกสร้าง",
        "012" : "บัตรธนาคาร(เป็นเงินที่ชำระหนี้ได้ตามกฎหมาย)",
        "013" : "สิทธิการเช่าอาคารราชพัสดุ",
        "014" : "สิทธิการเช่าอาคาร",
        "016" : "สิทธิการไถ่คืน",
        "017" : "สิทธิการเช่าช่วงที่ดิน",
        "018" : "อาวุธปืน",
        "019" : "บัตรเงินฝาก",
        "020" : "ธนบัตร",
    }
    search_a_ampur_value = ""
    search_a_type_value = ""
    search_a_type_text = ""
    search_bid_date = ""
    search_min_price = ""
    search_max_price = ""
    encoded_law_suit_no = ""
    last_page = 1
    if 'province' in request.GET:
        search_a_ampur_value = ampur_code[request.GET.get('ampur')]
        search_a_type_value = request.GET.get('asset_type')
        search_a_type_text = asset_type_code[request.GET.get('asset_type')]
        search_bid_date = request.GET.get('bid_date')
        search_min_price = request.GET.get('min_price')
        search_max_price = request.GET.get('max_price')

        a_province = quote(request.GET.get('province').encode('cp874'))
        a_ampur = quote(request.GET.get('ampur').encode('cp874'))
        a_type = request.GET.get('asset_type')
        bid_date = request.GET.get('bid_date')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')

        mycol.delete_many({})
        
        fields = ['a_lot_no',
            'a_sell_order',
            'a_law_suit',
            'a_type',
            'a_rai',
            'a_ngan',
            'a_wa',
            'a_price',
            'a_tumbon',
            'a_ampur',
            'a_province',
            'a_ampur_code',
            'a_province_code',
            'a_law_suit_no',
            'a_law_suit_year',
            'a_law_court_id',
            'a_deed_no',
            'a_addrno',
            'is_chanode',
        ]
        # titles = ['ล๊อตที่ - ชุดที่','เลขที่โฉนด','ลำดับที่การขาย','หมายเลขคดี','ประเภททรัพย์','ไร่','งาน','ตารางวา','ราคาประเมิน','ตำบล','อำเภอ','จังหวัด']
        # cvswriter = csv.writer(csvfile)
        # cvswriter.writerow(titles)
        page = 1
        response = get_html_content(a_type, a_province, a_ampur, bid_date, min_price, max_price, page)
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        data = []
        asset_dict = {}
        table = soup.find(id="box-table-a").find("table")
        unwanted = table.find('thead')
        unwanted.extract()
        for row in table.findAll("tr"):
            if re.findall("deed_no=.+&amp;addrno", str(row))[0]:
                deed_no = re.findall("deed_no=.+&amp;addrno", str(row))[0]
                deed_no = deed_no.replace("deed_no=","").replace("&amp;addrno","")
                addrno = re.findall("addrno=.+',", str(row))[0]
                addrno = addrno.replace("addrno=","").replace("',","")
                law_suit_no = re.findall("law_suit_no=.+&amp;law_suit_year", str(row))[0]
                law_suit_no = law_suit_no.replace("law_suit_no=","").replace("&amp;law_suit_year","")
                law_suit_year = re.findall("law_suit_year=.+&amp;Law_Court_ID", str(row))[0]
                law_suit_year = law_suit_year.replace("law_suit_year=","").replace("&amp;Law_Court_ID","")
                law_court_id = re.findall("Law_Court_ID=.+&amp;deed_no", str(row))[0]
                law_court_id = law_court_id.replace("Law_Court_ID=","").replace("&amp;deed_no","")
                
                for index,column in enumerate(row.findAll("td")):
                    for data in column:
                        data.strip()
                        data = data.replace('"','')
                        data = data.replace('\n','')
                        data = data.replace('\t','')
                        data = data.replace('\xa0','')
                        data = data.replace('&nbsp;','')
                        data = data.replace(' ','')
                        asset_dict[fields[index]] = data.strip()

                asset_dict['a_deed_no'] = deed_no
                asset_dict['a_addrno'] = quote(addrno.encode('cp874'))
                asset_dict['a_province_code'] = province_code[request.GET.get('province')]
                asset_dict['a_law_suit_no'] = quote(law_suit_no.encode('cp874'))
                asset_dict['a_law_suit_year'] = law_suit_year
                asset_dict['a_law_court_id'] = law_court_id
                asset_dict['a_ampur_code'] = ampur_code[asset_dict['a_ampur']]
                asset_dict['is_chanode'] = isChanode(
                                            asset_dict['a_law_suit_no'], 
                                            asset_dict['a_law_suit_year'], 
                                            asset_dict['a_law_court_id'], 
                                            asset_dict['a_deed_no'], 
                                            asset_dict['a_addrno']
                                            )
                mycol.insert_one(asset_dict) 
                asset_dict = {}
    
            # for asset in Asset.objects.all():
            #     is_chanode = isChanode(asset.a_law_suit_no, asset.a_law_suit_year, asset.a_law_court_id, asset.a_deed_no, asset.a_addrno)
            #     Asset.objects.filter( Q(a_law_suit = asset.a_law_suit) and Q(a_deed_no = asset.a_deed_no)).update(is_chanode = is_chanode)
       
        try:
            last_page = re.findall(">หน้าที่ 0/.+<", str(soup))[0]
            last_page = last_page.replace(">หน้าที่ 0/","").replace("<","")
        except:
            last_page = 1
            pass
        # print(f'PRINT:{last_page}')

        asset_data = Asset.objects.all()
    else:
        asset_data = Asset.objects.all()

    search_a_ampur_text = request.GET.get('ampur')
    if search_a_ampur_text=="":
        search_a_ampur_text = "-ทุกอำเภอ-"

    context = {
        'all_asset'     : asset_data , 
        'search_a_ampur_text'  : search_a_ampur_text,
        'search_a_ampur_value' : search_a_ampur_value,
        'search_a_type_value'  : search_a_type_value,
        'search_a_type_text'   : search_a_type_text,
        'search_bid_date'      : search_bid_date,
        'search_min_price'     : search_min_price,
        'search_max_price'     : search_max_price,
        'last_page'            : last_page
    }

    return render(request, 'dashboard/home.html', context)
    
def ViewMap(request):
    if 'province' in request.GET:
        from urllib.parse import quote
        province = request.GET.get('province')
        ampur = request.GET.get('ampur')
        deedno = request.GET.get('deedno')
            
        import time
        from selenium import webdriver
        from selenium.webdriver.support.ui import Select
        driver = webdriver.Chrome('/Users/chawput/Google Drive/dev/chromedriver')  # Optional argument, if not specified will search path.
        driver.get('http://dolwms.dol.go.th/tvwebp/');
        # time.sleep(1) # Let the user actually see something!
        
        time.sleep(2)
        driver.find_element_by_class_name('bts-popup-close').click()
        time.sleep(2)
        Select(driver.find_element_by_id('ddlProvince')).select_by_value(province)
        time.sleep(2)
        Select(driver.find_element_by_id('ddlAmphur')).select_by_value(ampur)
        time.sleep(0.5)
        driver.find_element_by_id('txtPacelNo').send_keys(deedno)
        time.sleep(0.5)
        driver.find_element_by_id('btnFind').click()
    return render(request, 'dashboard/viewmap.html')

def Favorite(request):
    # import pymongo
    # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # mydb = myclient["asset_led"]
    # mycol = mydb["dashboard_asset"]
    # mydict = { "name": "John", "address": "Highway 37" }
    # mycol.insert_one(mydict)

    return render(request, 'dashboard/favorite.html')

