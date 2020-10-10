### MicroPython🐍でM5Atomを触ってみた

#### 【オンライン】IoT縛りの勉強会! IoTLT vol.68 @Youtube

#### 2020/10/13 Hiroshi Sano

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

IoTLT 久しぶりにきました！

---

前回参加

-> 【令和初！】IoT縛りの勉強会! IoTLT vol.51 @日本オラクル

---

![(おふろIoT Mk2の発表)](./img/iotlt_51_ohuroiot_01.png)

懐かしい...

---

### おふろIoTとは

太陽熱温水器をIoT化するもの

- 温度と水位を測る
- 蛇口を止める

![おふろIoTシステム図](./img/ohutoiot_system_image.png)

---

そもそもこれお風呂に持っていくのありなのか？

---

![(蛇口IoTの裏側)](./img/FJIMG_20190429_174617.jpg)

基板ごと持っていくのは…

ESP32の開発キットだと大きい（縦長5cm程度）

---

筐体は3Dプリンターで何とかするとして

（まだ何もしてないけど）

🤔

---

最近こちらを教わる

![width=256px alt=AtomMatrix](https://camo.githubusercontent.com/b79dc8ac6f64f859f6972860bb836fa8884358f3/68747470733a2f2f6d35737461636b2e6f73732d636e2d7368656e7a68656e2e616c6979756e63732e636f6d2f696d6167652f6d352d646f63735f686f6d65706167652f636f72652f61746f6d5f6d61747269785f30312e77656270)
![width=256px alt=AtomLite](https://camo.githubusercontent.com/cf43e2305efcefc96778b4e34e519dc00980366a/68747470733a2f2f6d35737461636b2e6f73732d636e2d7368656e7a68656e2e616c6979756e63732e636f6d2f696d6167652f6d352d646f63735f686f6d65706167652f636f72652f61746f6d5f6c6974655f30312e77656270)

---

### M5Atom -> AtomMatrix, AtomLiteとは

- コインサイズの超小型なマイコン
- ESP32-Pico:ESP32のシールドやアンテナを外したもの
- ESP32なのでMicropythonが乗る

---

とっても小さい

![M5Atomの写真](./img/PXL_20201010_060716412.jpg)

---

これならおふろIoTに組み込めるのでは🤔

---

早速入門

---

## UiFlow

![インストールの様子](./img/ss_2020-10-07_21.49.04.png)

![Blocklyの様子](./img/ss_2020-10-08_15.08.14.png)

---

### とりあえず試した結果

https://photos.app.goo.gl/JeUyZb1m2JNx6JYG7

---

### micropythonとは？

- マイコン向けのPython環境
- Pythonの文法でハードウェアの操作
- ESP32でつかえる通信規格のライブラリも豊富
  - SPI,I2C,チップ系のドライバ
  - WiFi,BLE

---

### micropythonファームウェアを入れる

YouTubeで公開されてる！のですぐ使えます！

[M5Stack Micropython programming for M5Atom - YouTube](https://www.youtube.com/watch?v=m3Pxpynuxs0)

---

(インストールしたときの様子)

![micropython](./img/ss_2020-10-08_15.20.04.png)

---

最後に

---

（Bluetooth LEで、AtomMatrixのLEDをAtomLiteのボタンでポチポチできたら見せる）

---

ありがとうございました