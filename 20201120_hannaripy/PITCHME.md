### zoneinfoを紹介します⏰

#### はんなりPython #34 python3.9を語る LT会

#### 2020/11/20 Hiroshi Sano

---

早々まとめ（Td,Lr）

---

タイムゾーンってなによ？

---


<timezoneの画像>

by wikipedia



---

Python3.9でタイムゾーンを扱うなら`zoneinfo`便利

```python
>>> import zoneinfo
>>>


```


---

ご静聴ありがとうご…🙇‍♂️

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

<pysurugaの宣伝>
  
---

Pythonのdatetimeとタイムゾーン

nativeとawareの二つが肝

---

例えば datetimeモジュールの`datetime.now()`

```python
>>> import datetime
>>> now_dt = datetime.datetime.now()
```

---

Q:これにはタイムゾーンがあるのかないのか

---

A:`datetime.datetime.now()`「では」タイムゾーン入らない。

tzinfo属性というものがあって

- tzinfoがない場合->native
- tzinfoがある場合->aware

---

正確にはtz属性でタイムゾーンを指定する必要がある
```python
>>> jst_tz = datetime.timezone(datetime.timedelta(hours=9))
>>> now_dt_tz = datetime.datetime.now(tz=jst_tz)
>>> now_dt_tz
datetime.datetime(2020, 11, 17, 20, 6, 25, 384788, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400)))
>>> now_dt_tz.tzinfo
datetime.timezone(datetime.timedelta(seconds=32400))
```

---

ところで、nowすると、ちゃんとその時間になってない？

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

結構紛らわしい¥

---

それで別に良いのでは？🤔

---

内部で時間操作するぐらいならまあ…😒

---

ただ、外部から取り込んだ時刻情報を扱う時には気をつける

- API経由で受け取ったり
- ファイルにあるiso時間とか

---

例えばiso時間

フォーマット -> ``

---

pythonのdatetimeオブジェクトにしようとする

```python
isoformat
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
datetime.datetime(2020, 11, 20, 21, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400)))
>>> dt_1 == dt_2
False
```

---

### まとめ

- タイムゾーンを意識したdatetime
- 特に外部からの日付情報はtimezoneがあることを前提に

時刻を扱う場合はタイムゾーン前提の設計にしよう

---

ごせいちょうあ...

---

タイムゾーン設定はtimedeltaを使わないといけない

```python
>>> jst_tz = datetime.timezone(datetime.timedelta(hours=9))
>>> now_dt_tz = datetime.datetime.now(tz=jst_tz)
```

---

ちょーめんどい🥺

---

よく見る"Asia/Tokyo"とか"JST" で指定したくなる

---

3.8まではpytz, dateutil

最近はdateutilがいいらしい

```bash
pip install python-dateutil
```

---

（dateutil）

```python
>>> 
```

---

python3.9ならzoneinfoでやりましょう

Winの場合はtzinfo（タイムゾーン名のデータベース）必須

```bash
pip install tzinfo
```
---

(zoneinfoの例)

```python
>>> 
```

---

### まとめ🔚

- タイムゾーン意識したdatetimeを使おう
- Python3.9でタイムゾーンを扱うならzoneinfo便利
  - Winはtzinfoが必要
- 3.8以下ならdateutilを使うといいです（日本）

---

---

おまけ

---

#### おまけ1: システムのタイムゾーンを見る

time.tznameで見れる

