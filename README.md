# API implemented by Python, Flask

- Python(3.4.1)
  - Flask
  - SQLAlchemy

## Preparation

### Python Modules

```sh
pip install -r requirements.txt
```

### Database Preparation

Download SQL file containes zip\_address information.
[住所データSQL【住所.jp】](http://jusyo.jp/sql/new.php)

```sh
wget http://jusyo.jp/downloads/new/sql/sql_zenkoku.zip
unzip sql_zenkoku.zip
# => zenkoku.sql
```

```sh
mysql -u user -p -e 'create database zip_address default charset=utf8;'
mysql -u user -p zip_address < zenkoku.sql
```

## Run 

```sh
python run.py
```

[http://localhost:12345/zip/001-0000](http://localhost:12345/zip/001-0000)

``` sh
$ curl http://localhost:12345/zip_search/001-0000
[{"ken_furi": "\u30db\u30c3\u30ab\u30a4\u30c9\u30a6", "office_name": "", "block_name": "", "id": 1000000, "city_name": "\u672d\u5e4c\u5e02\u5317\u533a", "office_furi": "", "office_flg": 0, "ken_id": 1, "town_furi": "\u3000", "town_id": 11020000, "office_address": "", "delete_flg": 0, "zip": "001-0000", "memo": "", "kyoto_street": "", "town_memo": "\uff08\u8a72\u5f53\u306a\u3057\uff09", "city_id": 1102, "town_name": "", "city_furi": "\u30b5\u30c3\u30dd\u30ed\u30b7\u30ad\u30bf\u30af", "block_furi": "", "ken_name": "\u5317\u6d77\u9053", "new_id": 0}] 
```
