
**Pythone Run Server**

<!-- `python3 manage.py runserver` -->

```
python3 manage.py runserver
```

http://127.0.0.1:8000/

หน้าหลักค้นหาทรัพย์
http://asset.led.go.th/newbidreg/asset_search_province.asp?search_asset_type_id=&search_tumbol=&search_ampur=&search_province=%CD%D8%B4%C3%B8%D2%B9%D5&search_sub_province=&search_price_begin=&search_price_end=&search_bid_date=&search_rai=&search_rai_if=1&search_quaterrai=&search_quaterrai_if=1&search_wa=&search_wa_if=1&search_status=1&search_person1=&search=ok


ใช้โค้ดใน auto-search-on-map.js 
เลือกจังหวัดในแผนที่ http://dolwms.dol.go.th/tvwebp/

Local MongoDB Connect
mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false

Deploy to Heroku.com
    heroku login
    heroku create
    heroku git:remote -a tranquil-river-23134   //tranquil-river-23134 is heroku app name
    pip install gunicorn
    gunicorn assetled.wsgi
    touch Procfile
        Add text to Procfile:  'web: gunicorn assetled.wsgi'   // remove (')
    heroku local   
    pip freeze > requirements.txt
    git add .   

