---
marp: true
header: "**ラズパイとDashで環境ダッシュボードを作ろう** PyCon JP 2021 2021/10/16"
backgroundColor: #eee
---

# ラズパイとDashで環境ダッシュボードを作ろう

PyCon JP 2021
2021/10/15 ~ 10/16

---

## お前誰よ

- 佐野浩士（Hiroshi Sano）[@hrs_sano645](https://twitter.com/hrs_sano645)
  - 🏠:静岡県の富士市🗻
- Job💼
  - [株式会社佐野設計事務所](https://sano-design.info)
    - 自動車向けプレス金型の機械設計
  - 米農家🌾
- Community🙋
  - Python駿河, PyCon mini Shizuokaスタッフ
  - Code for ふじのくに

<!-- _footer:  -->

---

## 目次

- 環境ダッシュボードを作った話
- PythonとIoT
  - PythonでIoTを行う選択肢
  - ラズパイとCurcitPythonを使う選択
  - センサー情報を取得するデモ
- Dashでダッシュボードアプリを作る
  - Dashの特徴を紹介
  - センサー情報を可視化するデモ
- まとめ

<!-- _footer: この部分でツッコミや補足等を入れていきます -->

---

### このトークの趣旨、モチベーション

趣味プロジェクトを紹介しつつ、Pythonを使ったIoTとデータ可視化を
デモを交えてお伝えします

- IoT: ラズパイ+CircitPythonを合わせる選択肢
- データ可視化: Dashでダッシュボードアプリを作る

本日お伝えしたいこと

<!-- TODO:2021-10-13 ここでいうことがスライドで全体的に言えているか -->

- 自分の欲しい物が無ければ作ろう
- 身の回りで見えない数字を可視化してみよう
  - 身近だけど見えないデータ

---

本日のテーマ

# ラズパイとDashで環境ダッシュボードを作ろう

<!-- _footer:  -->

---

- ラズパイ = **Raspberry Pi**

- Dash = **Plotly Dash**
（Webアプリフレームワークのこと）

- 環境ダッシュボード => 環境センサーの情報が見れる**ダッシュボードアプリ**

---

### homeenvdashプロジェクトの紹介

![bg left:40% 60%](img/2021-10-09-12-00-46.png)

このプロジェクトの概要とモチベーションを
紹介します

---

### homeenvdashの全体構成

![](https://docs.google.com/drawings/d/e/2PACX-1vR6NyaVJv9P6mVH4wCfPot4IbAtuBWNaP-wvr2_8SkwpkCfYD2qxP5LHsPo1iW311P9WVHtUSIBHLCm/pub?h=500)

---

- センサーノードはラズパイ + センサーを接続
- センサーノードは複数対応
- ダッシュボードはDash + Plotly
- センサーで取得した情報はGoogleスプレッドシートで保存
  - 今後はローカルなDBに保持して、エクスポートする形が望ましい

<!-- _footer: 現在は、温度湿度気圧のBME280に対応。今後はCO2や非接触温度センサなどに対応したい -->

---

### なぜ作ったのか？

![bg left:40% 70%](img/2021-10-09-12-03-48.png)

そもそも、センサーやダッシュボードはすでに製品サービスが多数ある

---

![bg left:40% 120%](https://docs.google.com/drawings/d/e/2PACX-1vQXMlRsnlBNhLizyfzQwirXjXnXSzhTnddZEfyb3w2HPayW-ide6twZFT7R2BA-oivWwawkJZNadUHG/pub?w=960&h=720)

- 環境センサーは市販にも販売されている
  - クラウド対応とか
  - 高価な製品は精度がいい
- ダッシュボードサービスも多数ある
  - OSSなサーバーアプリ
  - サービスとして提供されているもの: [Anbient](https://ambidata.io),[Machinist](https://machinist.iij.jp/), [MotionBoard](https://www.wingarc.com/product/motionboard/scene/iot.html)

<!-- _footer: 車輪の再開発になるけどどうなのか？ -->

---

なんで作る必要があるか？

- 自分の欲しい物がなかった
- 身の回りで見えない数字を可視化する

---

![bg left:35% 70%](img/2021-10-09-11-52-55.png)

### 低気圧の体調不良に対応したかった

- 低気圧に弱いので不調の前兆を調べたい
  - 予報サービスはあるけど現状を見たい
- 世の中にはIoTの製品はあるものの
**手を出しずらい製品**
  - 選択肢が少ない
  - 独自のサービス
  - 高価な製品
  
<!-- _footer: 教えていただきましたが、オムロンの環境センサーは高価ですが扱いやすそうです: https://www.omron.co.jp/ecb/product-detail?partNumber=2JCIE-BL -->

---

![bg left:35% 70%](img/2021-10-09-11-54-18.png)

### 見守りに使う

- 実家の祖母の部屋の状況確認に利用
- 高齢者は気温の変化を感じづらい
  - 体感より数値化された状態を見た方が
  対応しやすい
- **センシティブ**な環境なので扱ったことが
ない外部サービスだと不安
  - できればローカルのみで扱いたい
  （そうしたかった）

<!-- _footer: 外部サービスとしてGoogleSheetを使ってますが、スライド作っていて矛盾に気が付く🤦‍♂️ -->
---

### 欲しいものを自分で作る

![bg left:35% 70%](img/2021-10-09-11-58-08.png)

- Maker（メイカー）という文化にあこがれる
  > **メイカーとは「テクノロジー」という言葉を、できる限り開放的に解釈、自分で学び利用出来る技能全般のことを理解して、冒険と実験への招待状だと考えている人のことだ**
  > オライリージャパン「私たちはみなメイカーだ」より引用
- 世の中に存在していなければ自分で作る精神！

<!-- _footer: 車輪の再開発、楽しいよ！ -->

---

![h:430](https://docs.google.com/drawings/d/e/2PACX-1vQrMi7_CD1k7DgHPmkrSJIwCLcJfn_ZjmgHnl4dXM-tNIMMXb5oCacRyf9nZbG2Y91zXvZ5TU5O5hwQ/pub?w=1393&h=615)

- 小池さん: http://workpiles.com/2016/08/ccb9-prototype2-complete/
- からあげさん: https://karaage.hatenadiary.jp/entry/2019/11/06/073000

<!-- note: -->
<!-- PyCon JPのキーノートスピーカーもされたきゅうり農家小池さんです。機械学習できゅうりの仕分けを行うプロジェクトでは、位置から仕分け機を作り、仕分け用の画像は自身の農園で育てたものも利用されているので、まさにないものは自分で作ることをされている方です。 -->
<!-- もう1人、PyCon mini Shizuokaでキーノートスピーカーをされたからあげさんです。さまざまなことに取り組まれていますが、ルンバをAI化するプロジェクトではルンバに外部インターフェイスがあることに気がつかれて、ロボット系のOSとして使われているROSと接続してハックしています。専用の自作基板まで作られる気合の入りっぷりがすごい -->

---

個人的に解決したい問題

---

![bg left:40% 70%](img/2021-10-09-14-45-08.png)

ガジェット好きなもので...

ラズパイが大量に転がっているので有効活用したい

<!-- _footer:  実際のところみなさんもありますよね？積みボード -->

---

しかし先人はこういいます

![drop-shadow](img/2021-10-02-14-31-48.png)

> https://twitter.com/karaage0703/status/1413347181705105410?s=20

<!-- _footer: やっぱり闇のエンジニアはちげーわ！ -->
--- 

<!-- note: -->
<!-- こういったマイコンやボードは積んでからが勝負と言われています。みなさんの中にも引き出しに眠っている積みボードが気になる方も出てきたと思いますが -->

積みボードがある方は贅沢に使って快適な日常を手に入れる！

<!-- note: -->
<!-- もちろん、新しく購入して初めてトライしてもらってもいいと思います！ -->

<!-- _footer: ラズパイは一応2台ぐらい有効活用してます。踏み台サーバーとか実験用とか... -->

---


## トークの進め方

今日は `homeenvdash-mini` というデモ用のアプリを使い扱う技術について
デモを交えて解説します。

https://github.com/hrsano645/homeenvdash-mini

---

### homeenvdashとの違い

- ダッシュボードアプリとセンサー値取得を同時に行ってます
- センサーの値を取得して現在情報とグラフ表示はほぼ同じ
- センサーの値はCSVファイルへ保存される
- （デモの都合上）ダッシュボード起動時にしかセンサー値の記録はされません

---

## PythonとIoT

より手軽にPythonとIoTを行う方法を紹介します

---

### PythonでIoTを行う選択肢

- Raspberry Pi + CPython
- MicroPython / CircuitPython
- Raspberry Pi + CircuitPython

<!-- _footer: 上記は私が知っている限りで一例です。ほかにも選択したがある場合は教えていただけると嬉しいです -->

---

- **Raspberry Pi + CPython**
- MicroPython / CircuitPython
- Raspberry Pi + CircuitPython

---

### Raspberry Piとは

- もともとは教育目的のLinuxが動作するシングルボードコンピューター（SBC）
  - 工場自動化やサイネージ、センサーノードとして業務利用も
  - クラスター構成を作ってクラウドっぽく（おうちクラウドと呼ばれている）
- インターフェイスが豊富
  - WLAN, Ethernet, USB, Bluetooth, HDMI出力
- GUI/CUIで利用可能
  - 最新版は高性能なのでデスクトップ端末としても
  - ヘッドレスなサーバーとしても扱える

<!-- _footer: ちょっと工夫はいるけどルーターを作ることもできます。便利ですよ -->

---

## Raspberry PiとIoT

特徴は

- Linuxが動きCPythonを扱える
- GPIO（デジタル）でセンサーと接続可能
- シリアル通信規格対応: SPI, I2C
- ディスプレイを繋ぐとサイネージ的なデバイスも作れる

⭕️ 安価ながら高機能なIoT端末として扱える
🔺 **ACアダプタなど給電環境が必要** 電源がない環境では扱いづらい

---

- Raspberry Pi + CPython
- **MicroPython / CircuitPython**
- Raspberry Pi + CircuitPython

---

### MicroPythonとは

![bg left:40% 80%](img/2021-10-09-15-18-30.png)

- MicroPythonはマイコンボード向けの処理系
  - マイコン=マイクロコントローラ
  - CPUより用途が限られている
  - 特定の機器制御に最適化された集積回路
- [クラウドファンディング](https://www.kickstarter.com/projects/214379695/micro-python-python-for-microcontrollers)で生まれたpyboardの開発環境として作られた

<!-- _footer: MicroPython micropython.org -->

---

### CircuitPythonとは

![bg left:40% 80%](img/2021-10-09-11-48-25.png)

- MicroPythonの派生版
  - adafruitというSTEAM系に取り組んでる電子部品の販売や教育分野のメーカーが作成
- adafruitのボードに対応したり、専用のライブラリを用意
  - メーカーのセンサーデバイスと接続しやすい

<!-- _footer: CircuitPython https://circuitpython.org -->

---
![bg left:40% 130%](https://docs.google.com/drawings/d/e/2PACX-1vR6Kfmi6lFMG-UlxtRCNep0R2tOzNiIFSakbMOT3TNiCh6MZuQZrw1jUGC_f7TU99_vCmWtWZeItGnJ/pub?w=960&h=720)


### MicroPython/CircuitPythonの特徴

- CPythonの3系（3.4, 3.5の一部）の文法をベースにした独自の実装系
- マイクロコントローラー向けカスタムした標準ライブラリやサードパーティライブラリがある
- シリアルコンソールからREPLが動く
- 他のボードにもポートされてインストール可能

⭕️ Raspberry Piより安価。電源はバッテリーも
🔺 CPythonライクだが完全互換ではない

<!-- _footer: 写真はESP32+MicroPythonで水栓を開け閉めするものを作ってました -->

---

- Raspberry Pi + CPython
- MicroPython / CircuitPython
- **Raspberry Pi + CircuitPython）*

---

### CircuitPythonのライブラリをRaspberry Piで扱う

- blinkaというライブラリを使う
  - [CircuitPython on Linux and Raspberry Pi](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux)
  - CircuitPythonで使うマイコンボードの機能をRaspberry Pi向けに変換するレイヤー
- CircuitPython向けのライブラリをRaspberry Piで扱うことができる（すべてではない） 
  - Raspberry PiとCircityPythonのコードの相互利用もやりやすい（らしいです）

⭕️ CircityPythonのライブラリを使うことで接続センサーの扱いが楽
🔺 どちらかの環境依存のコードを書く場合は扱いが難しい

---

![bg 80%](https://docs.google.com/drawings/d/e/2PACX-1vT_1IVFkLGrAzqOTQElWpsYjsMq_NCQvbUkF0FMq2DgscdKyWwFeJGgJ0DmXTBsg4GR7zE5iulV_i-2/pub?w=1440&h=810)

---

### センサー情報取得の実例: BME280という温度湿度センサーから情報を取得する

![bg left:40% 80%](img/2021-10-09-15-29-48.png)

Rasberry Pi + Blinkaライブラリを使って、
デモしながら様子を見せていきます

- 実際にラズパイ4BとBME280を接続します
- BME280はこちらものを使ってます
  - SPI接続です（I2Cの場合接続方法とセンサーのコードが少し違います）

---

![bg left:40% 100%](https://docs.google.com/drawings/d/e/2PACX-1vSfoVxBK7x3Q2Zvx6yfWzpsfyrsHkt7FYiqbbD0_tEVkzwomfw8BcrRta_-VscBz0QkM6lnI3l92Blh/pub?w=922&h=1083)

### デモを試す時に必要なもの

- 利用する部品: ブレットボード、ワイヤー、BME280（利用するセンサー）
- 道具: はんだごて、はんだ、はんだこて台
  （センサーにピンが実装されていない場合は必要です）
- 購入先:
  Amazonとかでも集まる。
  [秋月電子通商](https://akizukidenshi.com/catalog/default.aspx)、[スイッチサイエンス](https://www.switch-science.com/)、[aitendo](https://www.aitendo.com/)、[マルツオンライン](https://www.marutsu.co.jp/)、[せんごくネット通販](https://www.sengoku.co.jp/) がおすすめ

---

配線の様子を見せます

---

### 配線方法まとめ

![bg left 50% 100%](https://docs.google.com/drawings/d/e/2PACX-1vRDhv5roVz3g6nr87qmO39TdlWHT1DTQ1jizOjaE6P6TTGJUJDw3wBXpu6SrFNx-K6hjTp9T1-G5jBS/pub?w=960&h=720)

- 配線は一例です。
- 画像で利用しているBME280はAE-BME280ではないので、表を元に配線してください

---

環境作成してデモを見せながら披露

---

動作させたテストコードの例

```python
import time
import board
from adafruit_bme280 import basic as adafruit_bme280
import digitalio

# SPI接続
spi = board.SPI()
bme_cs = digitalio.DigitalInOut(board.D5)
bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

# 海の気圧を描くこと。大体1013hPaとのこと
bme280.sea_level_pressure = 1013.25

while True:
    print(f"温度: {bme280.temperature:.1f} C")
    print(f"湿度: {bme280.relative_humidity:.1f} %%")
    print(f"気圧: {bme280.pressure:.1f} hPa")
    print(f"高度: {bme280.altitude:.2f} meters")
    time.sleep(2)
```

---

### Tips: Raspberry Pi上で開発をしやすくする

VS Codeのリモート開発が便利です -> Remote-SSH

- ssh経由で扱うといい。ただpi3あたりからでないと、リモート開発できない（vscodeのリモートサーバーが対応するCPUアーキテクチャの問題）
- <https://www.raspberrypi.org/blog/coding-on-raspberry-pi-remotely-with-visual-studio-code/>
> Remote SSH needs a Raspberry Pi 3 or 4. It is not supported on older Raspberry Pis, or on Raspberry Pi Zero.

---

## Dashでセンサー情報を可視化する

Dashライブラリを使ってセンサー情報を表示する
ダッシュボードを作ります

---

### Dashの紹介

- Plotlyが作成しているWebアプリフレームワーク
  - Plotlyはグラフライブラリの名称でもある: `Plotly.js`、`Plotly.py`
- Plotlyとセットで使うと、データ分析向けのプロトタイピングがしやすい
- サンプル（有料機能を使ったものもあるので注意）<https://dash.gallery/Portal/>
  - ライブラリのサンプルには自動運転時の状況の可視化とかもある。
  かなりおもしろい

---

### Dashの特徴

- Dashはflask + reactで作られている。
  > Built on top of Plotly.js, React and Flask, Dash ties modern UI elements like dropdowns, sliders, and graphs directly to your analytical Python code.
  > https://github.com/plotly/dash
- （ほぼ）PythonのみでWebサイト構成が作れる
- コールバック機能を使ってインタラクティブ操作が可能
- データセットやDBを扱いたい場合は自前で用意
  - pandasを使ってplotlyのグラフを作れるので、pandas経由で何かしらをするときに便利

---

### （ほぼ）PythonのみでWebサイト構成が作れる

- HTMLを書く必要がない
- htmlのフォームや構造をラッピングしたコンポーネントを呼び出して構成を用意する
- Plotlyと連携して豊富なグラフを扱うことができる
- htmlな操作は知らないと扱いづらい

---

```python
from dash import Dash, callback, html, dcc, Input, Output

# dashアプリの初期化
app = Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
app.title = "Hello Dash App"

def _layout():
    """アプリの全体のレイアウト"""
    return html.Div(
        [
            html.H2(app.title),
            html.Label("PythonのみでWEBアプリを作ります")
        ],
    )

if __name__ == "__main__":
    app.layout = _layout
    app.run_server(debug=True, host="0.0.0.0")
```

---

![bg right:45% 100%](https://docs.google.com/drawings/d/e/2PACX-1vT9jRrJQciSzPbd5fUG2_6kNyV1aCbJWgamL1UF4j52s5dOK3oehShiohxU1J6HbNd14Iy046pVgDBe/pub?w=960&h=720)

```python
from dash import Dash, callback, html, dcc, Input, Output

# dashアプリの初期化
app = Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
app.title = "Hello Dash App"

def _layout():
    """アプリの全体のレイアウト"""
    return html.Div(
        [
            html.H2(app.title),
            html.Label("PythonのみでWEBアプリを作ります")
        ],
    )

if __name__ == "__main__":
    app.layout = _layout
    app.run_server(debug=True, host="0.0.0.0")
```

---

### フォームなどの操作から動的な変更:コールバック機能

- dashは動的な操作を可能にするためのコールバックという機能がある
- たとえばグラフの種類を変更することができる
- homeenvdashでは
  - ドロップダウンリストで部屋単位のセンサーグラフの切り替え
  - 定期的な表示の更新を行う（dcc.Interval）

---

```python
from dash import Dash, callback, html, dcc, Input, Output

# dashアプリの初期化
app = Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
app.title = "Hello Dash Callback"

def _layout():
    return html.Div(
        [
            html.H1(app.title),
            html.Hr(),
            html.P("文字を入力すると、出力の部分が更新されます"),
            html.Div(
                [
                    html.Span("入力: "),
                    dcc.Input(id="input-form", value="Callbackを試しています", type="text"),
                ]
            ),
            html.P(id="output-p"),
        ]
    )
# 次へ続く
```

---

```python
# 続き
@app.callback(Output("output-p", "children"), Input("input-form", "value"))
def update_output_text(input_value):
    # 引数がInputのvalueの値を取得
    # return側に更新したいコンポーネントを指定する。childrenは指定コンポーネントの子要素の事
    return "出力: {}".format(input_value)

if __name__ == "__main__":
    app.layout = _layout
    app.run_server(debug=True, host="0.0.0.0")
```

---

![bg center 100%](https://docs.google.com/drawings/d/e/2PACX-1vR-TInuDS_1OjtVrtHimZvNfZzks7sDHMuj_O7As0r71FBXlTt9moSIlEADgJ-gIkwOzT0JA7pu47N7/pub?w=1440&h=1080)

---

![bg center 100%](https://docs.google.com/drawings/d/e/2PACX-1vRviOLeuAbH7SQJ4sJBHM3xVafcGgwPKERUkNqtXdTBlhkhbM3hfan5BsWl5H5Zv_yFeIKwIjk1C7PA/pub?w=1663&h=1079)

---

### Tips:ホットリロードによる開発

- 自動的にリロードしてくれる。デバッグモードを有効にしておくと開発しやすい

```python
if __name__ == "__main__":
    app.layout = _layout
    app.run_server(debug=True, host="0.0.0.0")
```

![bg left 50% 80%](img/2021-10-12-11-13-30.png)

---

### デモ: センサー情報を可視化する

センサー情報の取得方法は、直接センサーの値を取りに行く

- 時系列グラフを作るなら、データの記録は必須になる。
  - 実際のところはファイルかDB, 外部のデータソースへ保存して
  扱う方がわかりやすい
  - 今回はCSVファイルに1分ごと、30回分の測定結果を保存

---

### センサーの最新の値を見る

---

```Python
# センサー取得用関数
def get_sensor_values():
    """センサーの値を取得する。記録は文字列にする"""
    temperature = f"{bme280.temperature:.1f}"
    relative_humidity = f"{bme280.relative_humidity:.1f}"
    pressure = f"{bme280.pressure:.1f}"
    return (temperature, relative_humidity, pressure)

# callback関数部分
def update_sensor_values(n):

    now_dt = datetime.datetime.now().astimezone()
    sensor_values = get_sensor_values()
    #中略
    latest_values = latest_sensor_values(sensor_values, now_dt)
    return latest_values
```

---

```python
# レイアウト
def latest_sensor_values(sensor_values: tuple, now_datetime: datetime.datetime):
    """現在のセンサー値を描写する。"""
    latest_datetime = now_datetime.strftime("%Y-%m-%d %H:%M:%S")
    latest_temperature = sensor_values[0]
    latest_pressure = sensor_values[1]
    latest_humidity = sensor_values[2]

    return html.Div(
        [
            html.Label(f"更新時間 :{latest_datetime}"),
            html.Div(
                [
                    html.P(f"気温: {latest_temperature}℃"),
                    html.P(f"湿度: {latest_pressure}%"),
                    html.P(f"気圧: {latest_humidity}hPa"),
                ],
            ),
        ],
        id="latest_values",
    )
```

---

### 記録したセンサーの値をグラフ化する

---

```Python
import pandas
import plotly.express as px
# 中略
from dash import Dash, callback, html, dcc, Input, Output
# 中略
def sensor_graphs():
     # センサー値を記録しているCSVファイルをDataFrameにする
    sensor_values_df = pandas.read_csv(
        SENSOR_VALUES_FILE, names=("datetime", "temperature", "humidity", "pressure")
    )
    # DataFrameをグラフに展開
    fig1 = px.line(sensor_values_df, x="datetime", y="temperature", title="温度")
    fig2 = px.line(sensor_values_df, x="datetime", y="humidity", title="湿度")
    fig3 = px.line(sensor_values_df, x="datetime", y="pressure", title="気圧")
    # レイアウトのコンポーネントを返す
    return html.Div(
        [
            dcc.Graph(id="tempature", figure=fig1),
            dcc.Graph(id="humidity", figure=fig2),
            dcc.Graph(id="pressure", figure=fig3),
        ],
        id="graphs",
    )
# 後略...
```

---

### Tips: 複雑化したらまとめてコンポーネント化する

複雑なアプリやレイアウトを作ると、構造も複雑になりがち

- 複雑になることはしょうがない
- 複雑になるので関数などで部品（カプセル）化していく
- コールバックで更新したい部分をカプセル化すると、コールバック側の更新処理を作る時に呼び出しやすい


慣れてくるとwebアプリを書いている様な扱いになってくる

---

最初にレイアウトの一部を関数化しておく

```Python
# 中略, 関数化しておくと呼び出しやすくなり管理もしやすい
def sensor_graphs():
    """過去に記録したセンサーの値をグラフにする"""

    # センサー値を記録しているCSVファイルをDataFrameにする
    sensor_values_df = pandas.read_csv(
        SENSOR_VALUES_FILE, names=("datetime", "temperature", "humidity", "pressure")
    )
    # DataFrameをグラフに展開
    fig1 = px.line(sensor_values_df, x="datetime", y="temperature", title="温度")
    fig2 = px.line(sensor_values_df, x="datetime", y="humidity", title="湿度")
    fig3 = px.line(sensor_values_df, x="datetime", y="pressure", title="気圧")
    # レイアウトのコンポーネントを返す
    return html.Div(
        [
            dcc.Graph(id="tempature", figure=fig1),
            dcc.Graph(id="humidity", figure=fig2),
            dcc.Graph(id="pressure", figure=fig3),
        ],
        id="graphs",
    )
```
---

最後にレイアウト上で呼び出す

```python
def _layout():
    now_dt = datetime.datetime.now().astimezone()
    sensor_values = get_sensor_values()
    save_sensor_values(sensor_values, now_dt, 50)

    return html.Div(
        [
            html.H2(app.title),
            html.Hr(),
            # 現在の値を取得
            latest_sensor_values(sensor_values, now_dt),
            # 温度、湿度、気圧のグラフ

            sensor_graphs(), # <= 関数でレイアウトオブジェクトを生成して呼び出す
            dcc.Interval(
                id="interval-component",
                interval=UPDATE_MINITS * 60 * 1000,  # in milliseconds
                n_intervals=0,
            ),
        ],
    )
```

---

### Tips: Bootstrapを使ってデザインを良くする

Dashの便利なライブラリ: dash-bootstrap-componets（dbc）によるデザインの整え方

- Dashのデメリットは、CSSを扱ったデザインがしづらい
  - レスポンシブ対応とか
- CSSフレームワークのBootstrapを扱いやすくコンポーネント化されている
- 扱いやすいもののBootstrapを知っている必要あり

※Dashのv2バージョンアップに伴って、dash-bootstrap-componetsも追従したバージョンアップが行われます。
デモ中は最新バージョンのリリース候補版を利用してます。

<!-- _footer: 発表資料作っている途中でバージョンアップされたので、対応がめっちゃ大変だった… -->

---

### デモ: デザインを整えてみる

- 実際にコードを見せつつ解説します
- レスポンシブ対応を例にします
- （スライドにコードを収めるには長すぎるので、詳しくはこちらをご覧ください）
  - (url掲載する)

---

### まとめ

homeenvdashプロジェクトを紹介しつつ、Pythonを使ったIoTとデータ可視化を
  デモを交えてお伝えしました。

- PythonとIoT
- Plotly Dashでダッシュボードを作る

本日お伝えしたかったこと

- 世の中にないけど、ほしいなら自分で作ろう
- 世の中に存在しないデータを集めて見てみよう
  - 身近だけど見えないデータ
- 積みボードを活用していこう

---

## 最後にお知らせ

---

### PyCon  mini Shizuoka 2021 やります

開催します🎉是非来てください🙌

- 2021/11/20 土曜日
- 詳しくは公式サイトをチェック
  - https://shizuoka.pycon.jp/2021
  - Twitterアカウント: @PyconShizu
- LTと参加者募集をします
- 同時にイベントの詳しい内容は近日公開します！


---

質問対策

---

- Dashを使うメリット,デメリットは？
  - メリットはHTMLを書く必要なくWEBアプリ作成ができる
  - デメリットはDB接続や高度な動的処理（ログイン処理やセッション管理）、API連携はそれほど得意ではない
    - それを解決する有償のサービスが提供されている
- 気圧センサーいろいろあるよ！
  - 知らなかったのでありがたいです！
- 精度はどう？
  - 数字というより変化を見たかったので、精度については今回は扱ってない
  - 実際にキャリブレーションする必要はあると思うし、高度なセンサーもあるので、用途によると思います。

---

- 