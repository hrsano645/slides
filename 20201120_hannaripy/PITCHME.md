### zoneinfoを紹介します⏰

#### はんなりPython #34 python3.9を語る LT会

#### 2020/11/20 Hiroshi Sano

---

早々まとめ（Td,Lr）

---

タイムゾーンってなによ？

---

![timezone image by wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/World_Time_Zones_Map.png/640px-World_Time_Zones_Map.png)

by wikipedia

---

Python3.9でタイムゾーンを扱うなら`zoneinfo`便利

```python
>>> import datetime, zoneinfo
>>> jst_tz_zoneinfo = zoneinfo.ZoneInfo("Asia/Tokyo")
>>> datetime.datetime.now(tz=jst_tz_zoneinfo)
datetime.datetime(2020, 11, 19, 7, 13, 21, 542591, 
    tzinfo=zoneinfo.ZoneInfo(key='Asia/Tokyo'))
```

---

ご静聴ありが…🙇‍♂️

---

（これで終わりでもいいけど、30秒だとさすがにまずい）

---

### お前誰よ

- 佐野浩士（Hiroshi Sano）[@hrs_sano645](https://twitter.com/hrs_sano645)
- 🏠:静岡県の富士市🗻

- Job💼
  - [佐野設計事務所🚗⚙️📏🖊️](https://sano-design.info) 
    - 自動車系機械の3D設計事務所 IT/雑務何でも屋
  - 米農家🌾
- Community🧑‍💻
  - 🗻🐍: shizuoka.py, unagi.py, Python駿河
  - 🗻🐍: PyCon mini Shizuokaスタッフ
  - 🐍: PyCon JP 2020 チュートリアル講師

---

11/28にPython駿河勉強会やります

[[オン/オフライン同時]Python駿河 勉強会 #19 ～イベント振り返り会/OSCライブビュー～ - connpass](https://py-suruga.connpass.com/event/192889/)
  
---

本題のzoneinfo

---

の前にPythonとタイムゾーンの話

---

nativeとawareの2つが肝心

（公式ドキュメントによく出る）

---

datetimeモジュールの`datetime.now()`

```python
>>> import datetime
>>> now_dt = datetime.datetime.now()
```

---

Q: これにはタイムゾーンがある？ない？

---

A: `datetime.datetime.now()`「では」タイムゾーン入らない。

---

tz引数でタイムゾーンを指定する必要がある

```python
>>> jst_tz = datetime.timezone(datetime.timedelta(hours=9))
>>> now_dt_tz = datetime.datetime.now(tz=jst_tz)
>>> now_dt_tz
datetime.datetime(2020, 11, 17, 20, 6, 25, 384788, 
    tzinfo=datetime.timezone(datetime.timedelta(seconds=32400)))
```

---

生成されたdatetimeオブジェクトにはtzinfo属性があって

- tzinfoがない場合->native
- tzinfoがある場合->aware

```python
>>> now_dt_tz.tzinfo
datetime.timezone(datetime.timedelta(seconds=32400))
```

---

ところでnow()すると、「ちゃんとした」時間になってますよね？

```python
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2020, 11, 17, 21, 6, 14, 227581)
```

---

現在のローカル時間（PCの時間）がnativeで出てくる

```python
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2020, 11, 17, 21, 6, 14, 227581)
>>> exit()
(.env) hiroshi@py39test1:~/zoneinfo_exam$ date
Tue Nov 17 21:06:29 UTC 2020
```

結構紛らわしい

---

それで別に良いのでは？🤔

---

内部で時間操作するぐらいならまあ…😒

---

ただ、外部から取り込んだ時刻情報を扱う時には気をつける

- API経由で受け取ったり
- ファイルに書かれている

---

例えばiso時間

フォーマットはこれ

`YYYY-MM-DD[*HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]]`

例: `2020-11-20 21:00:00.534500+09:00`

---

pythonのdatetimeオブジェクトすると

```python
>>> iso_dt_str = '2020-11-20 21:00:00.534500+09:00'
>>> datetime.datetime.fromisoformat(iso_dt_str)
datetime.datetime(2020, 11, 20, 21, 0, 0, 534500, 
    tzinfo=datetime.timezone(datetime.timedelta(seconds=32400)))
```

timezone入ってる！

---

awareとnativeが混ざると比較演算するときに困る

```python
>>> dt_1 = datetime.datetime(2020,11,20,21,00,0,0)
>>> dt_2 = datetime.datetime(2020,11,20,21,00,0,0,jst_tz)
>>> dt_1
datetime.datetime(2020, 11, 20, 21, 0)
>>> dt_2
datetime.datetime(2020, 11, 20, 21, 0, 
    tzinfo=datetime.timezone(datetime.timedelta(seconds=32400)))
>>> dt_1 == dt_2
False
```

---

### まとめ

- タイムゾーンを意識したdatetime
- とくに外部からの日付情報はtimezoneがあることを前提に

時刻を扱う場合はタイムゾーン前提の設計にしよう

---

ごせいちょうあ...👏

---

まだzoneinfo説明してない

---

タイムゾーン設定はtimezoneとtimedeltaを使わないといけない

時間の指定も覚えていないといけない

```python
>>> jst_tz = datetime.timezone(datetime.timedelta(hours=9))
>>> now_dt_tz = datetime.datetime.now(tz=jst_tz)
```


---

ちょーめんどい🥺

---

よく見る「**Asia/Tokyo**」で指定したくなる

---

3.8まではpytz, dateutilを使う

最近はdateutilがいいらしいです

```bash
pip install python-dateutil
```

---

dateutilの例

```python
>>> import dateutil.tz
>>> jst_tz_dateutil = dateutil.tz.gettz("Asia/Tokyo")
>>> datetime.datetime.now(tz=jst_tz_dateutil)
datetime.datetime(2020, 11, 19, 7, 10, 54, 935598, 
    tzinfo=tzfile('/usr/share/zoneinfo/Asia/Tokyo'))
```

---

python3.9ならzoneinfoでやりましょう

Winの場合はtzinfo（タイムゾーン名のデータベース）必須

```bash
pip install tzinfo
```

---

zoneinfoの例

```python
>>> import zoneinfo
>>> jst_tz_zoneinfo = zoneinfo.ZoneInfo("Asia/Tokyo")
>>> datetime.datetime.now(tz=jst_tz_zoneinfo)
datetime.datetime(2020, 11, 19, 7, 13, 21, 542591, 
    tzinfo=zoneinfo.ZoneInfo(key='Asia/Tokyo'))
>>>
```

---

### まとめ🔚

- タイムゾーン意識したdatetimeを使おう
- Python3.9でタイムゾーンを扱うならzoneinfo便利
  - Winはtzinfoが必要
- 3.8以下ならdateutilを使うといいです

---

---

### おまけ🍬

---

#### おまけ1: システムのタイムゾーンを見る

time.tznameで見れる

---

#### おまけ2: datetimeでタイムゾーン設定できるオブジェクトは？

- datetime
- time

時刻の操作になるので、dateオブジェクトはしません

---

#### おまけ3: dateutilとzoneinfoのオブジェクト

Q: dateutil.tzのtzfileとzoneinfoのZoneInfoはどんなオブジェクト？

- `tzfile('/usr/share/zoneinfo/Asia/Tokyo')`とか
- `zoneinfo.ZoneInfo(key='Asia/Tokyo')` とか

---

#### おまけ3: dateutilとzoneinfoのオブジェクト

A: どちらもdatetime.tzinfoの基底にしたクラス

tz属性にはdatetime.tzinfoを基底にしたクラスが必須

```
>>> issubclass(dateutil.tz.tzfile, datetime.tzinfo)
True
>>> issubclass(zoneinfo.ZoneInfo, datetime.tzinfo)
True
```

---

#### 参考

- [datetime — Basic date and time types &#8212; Python 3.9.0 documentation](https://docs.python.org/3/library/datetime.html)
- [Python 3.9の新機能 - python.jp](https://www.python.jp/pages/python3.9.html#zoneinfo%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB)
- [tz &mdash; dateutil 2.8.1 documentation](https://dateutil.readthedocs.io/en/stable/tz.html)