### 格安でMicroPython🐍を試してみよう

#### 【オンライン】はんなりPython #33 LT会

#### 2020/10/16 Hiroshi Sano

---

## お前誰よ

- 佐野浩士（Hiroshi Sano）[@hrs_sano645](https://twitter.com/hrs_sano645)
- 静岡県の富士市🗻

- Job💼
    - [佐野設計事務所🚗⚙️📏](https://sano-design.info) 設計以外何でも屋
    - 米農家🌾

- Community🧑‍💻
    - 🗻🐍: shizuoka.py, unagi.py, Python駿河
    - 🗻🐍: PyCon mini Shizuokaスタッフ
    - 🐍: PyCon JP 2020 チュートリアル講師

---

### 宣伝

[Unagi.py 勉強会34枚目～トーク未経験大歓迎LT大会～ - connpass](https://unagi-py.connpass.com/event/191172/)

---

### MicroPython🐍ご存じの方？

手を上げて！

---

### micropythonとは？

- マイコン向けのPython環境
- Pythonの文法でハードウェアの操作
- 通信規格のライブラリも豊富
  - GPIO、SPI、I2C、チップ系のドライバ
  - WiFi、BLE

---

### お手軽にMicroPythonを使って見よう

---

これを使います

![height=256, alt=AtomMatrix](https://camo.githubusercontent.com/b79dc8ac6f64f859f6972860bb836fa8884358f3/68747470733a2f2f6d35737461636b2e6f73732d636e2d7368656e7a68656e2e616c6979756e63732e636f6d2f696d6167652f6d352d646f63735f686f6d65706167652f636f72652f61746f6d5f6d61747269785f30312e77656270)
![height=256, alt=AtomLite](https://camo.githubusercontent.com/cf43e2305efcefc96778b4e34e519dc00980366a/68747470733a2f2f6d35737461636b2e6f73732d636e2d7368656e7a68656e2e616c6979756e63732e636f6d2f696d6167652f6d352d646f63735f686f6d65706167652f636f72652f61746f6d5f6c6974655f30312e77656270)

---

### M5Atom -> AtomMatrix, AtomLiteとは

- コインサイズの超小型なIoTデバイス
- ESP32(ESP32-Pico)が入ってます
  - 最近よく聞くIoT向けのチップ
  - Wifi、BLEついてる
  - 開発: C、Arduinoも使える（こちらがデフォ）
- I/F: ボタン、LED、赤外線LED, USB-C 

---

### **（超重要）お値段**

- AtomMatrix: ¥1,397
  - http://ssci.to/6260
- AtomLite: ¥968
  - http://ssci.to/6262

とってもお買い得💸

---

とっても小さい。とっても安い。

![height=256,alt=M5Atomの写真](20201016_hannnaripy/img/PXL_20201010_060716412.jpg)

（左にあるのはESP32の開発キット:ESP32-DevKitC）

---

### micropythonファームウェアを入れる

YouTubeで公開されてる！のでインストールもかんたん！

[M5Stack Micropython programming for M5Atom - YouTube](https://www.youtube.com/watch?v=m3pynuxs0)

---

(インストールしたときの様子)

![height=500](20201016_hannnaripy/img/ss_2020-10-08_15.20.04.png)

---

電子工作定番のLチカ

（今日は手抜きでただ光るだけです）

---

### LEDを光らせる

（AtomLiteの例）

```python
>>> from machine import Pin
>>> from neopixel import NeoPixel
>>> npx = NeoPixel(Pin(27, Pin.OUT), 1)
>>> npx[0] = (255, 255, 255)
>>> npx.write()
```

---

### ボタンを押し続けるとLEDが光るスクリプト

一つ前のスライドの続きで

```python
>>> from time import sleep_ms
>>> btnpin = Pin(39, Pin.IN)
>>> while True:
...     if btnpin.value() == 0:
...         npx[0] = (255, 0, 0)
...     else:
...         npx[0] = (0, 0, 0)
...     npx.write()
...     sleep_ms(500)
```

---

もっとかんたんな手段 -> UiFlow

![height=500,alt=インストールの様子](20201016_hannnaripy/img/ss_2020-10-07_21.49.04.png)

---

## UiFlow


![height=500,alt=Blocklyの様子](20201016_hannnaripy/img/ss_2020-10-08_15.08.14.png)

---

### とりあえず試した結果

https://photos.app.goo.gl/JeUyZb1m2JNx6JYG7

---

なんでこれ使おうと思ったか

---


### おふろIoTとは

太陽熱温水器をIoT化するもの

- 温度と水位を測る
- 蛇口を止める

![height=256,alt=おふろIoTシステム図](20201016_hannnaripy/img/ohutoiot_system_image.png)

Ref:[【オンライン】IoT縛りの勉強会! IoTLT vol.68 @Youtube - connpass](https://iotlt.connpass.com/event/189403/)

---

![(おふろIoT Mk2の発表)](20201016_hannnaripy/img/iotlt_51_ohuroiot_01.png)

---

![height=256,alt=(蛇口IoTの裏側)](20201016_hannnaripy/img/FJIMG_20190429_174617.jpg)

そもそもこれお風呂に持っていくのありなのか？基板ごと持っていくのは…

---

M5Atomは小さいし開発もしやすそう？

これならおふろIoTに組み込めるのでは🤔

---

（多分続く！！）

ありがとうございました！

---

付録

---

（Bluetooth LEで、AtomMatrixのLEDをAtomLiteのボタンでポチポチできたら見せる）
