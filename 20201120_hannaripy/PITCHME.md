### zoneinfoを紹介します

#### はんなりPython #34 python3.9を語る LT会

#### 2020/11/20 Hiroshi Sano

---

タイムゾーンってなによ？

---


<timezoneの画像>

by wikipedia

---

Python3.9でタイムゾーンを扱うなら`zoneinfo`便利

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

Pythonのdatetimeとタイムゾーンについては

nativeとawareの二つがきも

---

例えば datetimeモジュールの`datetime.now()`

```python
>>> import datetime
>>> now_dt = datetime.datetime.now()
```

---

Q:これにはタイムゾーンがあるのかないのか

---

A:`datetime.datetime.now()` ではつけられない、tz引数でつける必要がある

tzinfo属性というものがあって、

- tzinfoがない場合はタイムゾーンあり->nativeと呼ぶ
- ある場合はawareと呼ぶ

---


### まとめ🔚

- Python3.9でタイムゾーンを扱うならzoneinfo便利
  - Winはtzinfo入れましょう
- 3.8以下ならdateutilを使うといいです（日本）
