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

<!-- _footer: こんにちは。フッターです。 -->

---

## 目次

- 環境ダッシュボードを作った話
- PythonとIoT
- Dashでダッシュボードアプリを作る
- まとめ

<!-- _footer: この部分でツッコミや補足等を入れていきます。 -->

---

### このトークの趣旨、モチベーション

趣味プロジェクトを紹介しつつ、Pythonを使ったIoTとデータ可視化を
デモを交えてお伝えします

- IoT: ラズパイ+CircitPythonを合わせる選択肢
- データ可視化: Dashでダッシュボードアプリを作る

本日お伝えしたいこと

- 自分の欲しい物が無ければ作ろう
- 身の回りで見えない数字を可視化してみよう
  - 身近だけど見えないデータ

---

本日のテーマ

# ラズパイとDashで環境ダッシュボードを作ろう

<!-- _footer: 久しぶりに長めのトークをやらせてもらってます。 -->

---

- ラズパイ = **Raspberry Pi**

- Dash = **Plotly Dash**
（Webアプリフレームワークのこと）

- 環境ダッシュボード => 環境センサーの情報が見れる**ダッシュボードアプリ**

<!-- _footer: 御見苦しい部分もありますが生暖かく見守ってもらえたら/やんわりマサカリ投げてください -->

---

## 目次

- **環境ダッシュボードを作った話**
- PythonとIoT
- Dashでダッシュボードアプリを作る
- まとめ

---

### homeenvdashプロジェクトの紹介

![bg left:40% 60%](img/2021-10-09-12-00-46.png)

趣味プロジェクトです

- センサーの情報をダッシュボードで見るアプリ/システム
- 計測した時の最新の数値が見れる
- グラフで1日分/1週間分の推移も確認

---

### homeenvdashの全体構成

![bg left:50% 100%](https://docs.google.com/drawings/d/e/2PACX-1vR6NyaVJv9P6mVH4wCfPot4IbAtuBWNaP-wvr2_8SkwpkCfYD2qxP5LHsPo1iW311P9WVHtUSIBHLCm/pub?h=500)

- センサーノード
  - ラズパイ + センサー
  - センサーノードは複数対応
- ダッシュボードはDash + Plotly
- センサーで取得した情報はGoogleスプレッドシートで保存
  - 今後はローカルなDBを検討

<!-- _footer: 現在は、温度湿度気圧のBME280に対応。今後はCO2や非接触温度センサなどに対応したい -->

---

### なぜ作ったのか？

![bg left:40% 70%](img/2021-10-09-12-03-48.png)

そもそもセンサーやダッシュボードは
すでに製品、サービスが多数ある

---

![bg left:40% 120%](https://docs.google.com/drawings/d/e/2PACX-1vQXMlRsnlBNhLizyfzQwirXjXnXSzhTnddZEfyb3w2HPayW-ide6twZFT7R2BA-oivWwawkJZNadUHG/pub?w=960&h=720)

- 環境センサーは市販にも販売されている
  - 単体でクラウド対応とか
  - 高価な製品は精度がいい
- ダッシュボードサービスも多数ある
  - OSSなサーバーアプリ: Grafana, Zabbix, Home Assistant...
  - サービスとして提供: [Anbient](https://ambidata.io), [Machinist](https://machinist.iij.jp/), [MotionBoard](https://www.wingarc.com/product/motionboard/scene/iot.html), [Google データポータル](https://marketingplatform.google.com/intl/ja/about/data-studio/)...

<!-- _footer: 車輪の再開発になるけどどうなのか？ -->

---

作った理由は自分の欲しい物がなかったため

---

![bg left:35% 70%](img/2021-10-09-11-52-55.png)

### 低気圧の体調不良に対応したかった

- 低気圧に弱いので不調の前兆を調べたい
  - 予報サービスはあるけど現状を見たい
- 世の中にはIoT/センサー製品はあるものの
気圧対応がされてるものは**手を出しずらかった**
  - 選択肢が少ない
  - 独自のサービス
  - 高価な製品
  
<!-- _footer: 教えていただきましたが、オムロンの環境センサーは高価ですが扱いやすそうです: https://www.omron.co.jp/ecb/product-detail?partNumber=2JCIE-BL -->

---

![bg left:35% 70%](img/2021-10-09-11-54-18.png)

### 見守りに使う

- 実家の祖母の部屋の状況確認に利用
- 高齢者は気温の変化を感じづらい
  - 体感より数値化されていた方が
  対応しやすい
- **センシティブ**な環境なので扱ったことが
ない外部サービスだと不安
  - できればローカルのみで扱いたい

<!-- _footer: 外部サービスとしてGoogleSheetを使ってますが、このスライド作っていて矛盾に気が付く🤦‍♂️ -->

---

### 欲しいものを自分で作る

![bg left:35% 70%](img/2021-10-09-11-58-08.png)

- Maker（メイカー）という文化
  > **メイカーとは「テクノロジー」という言葉を、できる限り開放的に解釈、自分で学び利用出来る技能全般のことを理解して、冒険と実験への招待状だと考えている人のことだ**
  > オライリージャパン「私たちはみなメイカーだ」より引用
- 世の中に存在していなければ自分で作る精神！

<!-- _footer: 車輪の再開発も楽しいよ！ -->

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

![bg left:40% 75%](img/2021-10-09-14-45-08.png)

ガジェット好きなもので...

ラズパイが大量に転がっている

<!-- _footer:  みなさんも引き出しにありますよね？積みボード -->

---

しかし先人はこう言います

![drop-shadow](img/2021-10-02-14-31-48.png)

> https://twitter.com/karaage0703/status/1413347181705105410?s=20

<!-- _footer: やっぱり闇のエンジニアはちげーわ！ -->
--- 

<!-- note: -->
<!-- こういったマイコンやボードは積んでからが勝負と言われています。みなさんの中にも引き出しに眠っている積みボードが気になる方も出てきたと思いますが -->

積みボードがある方は贅沢に使って快適な日常を手に入れる！

<!-- note: -->
<!-- もちろん、新しく購入して初めてトライしてもらってもいいと思います！ -->

<!-- _footer: ラズパイは一応2台ぐらい有効活用してます。踏み台サーバーや3Dプリンタのコントローラーが便利 -->

---

## トークで使うデモアプリ

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

## 目次

- 環境ダッシュボードを作った話
- **PythonとIoT**
- Dashでダッシュボードアプリを作る
- まとめ

<!-- _footer: この部分でツッコミや補足等を入れていきます -->

---

## PythonとIoT

より手軽にPythonとIoTを行う方法を紹介します

- ※IoTは広義だといろんな意味がありますが
ここではセンシングや電子機器操作をネットワーク経由で行うことを指します

<!-- _footer:  -->

---

### PythonでIoTを行う選択肢

1. Raspberry Pi + CPython
2. MicroPython / CircuitPython
3. Raspberry Pi + CircuitPython

<!-- _footer: 上記は私が知っている限りで一例です。ほかにも選択したがある場合は教えていただけると嬉しいです -->

---

### PythonでIoTを行う選択肢

1. **Raspberry Pi + CPython**
2. MicroPython / CircuitPython
3. Raspberry Pi + CircuitPython

---

### Raspberry Piとは

![bg left:45% 80%](img/2021-10-14-17-12-56.png)

- もともとは教育目的のLinuxが動作するシングルボードコンピューター（SBC）
  - 工場自動化やサイネージ、センサーノードとして業務利用も
- インターフェイスが豊富
  - 無線LAN, Ethernet, USB, Bluetooth, HDMI出力
- GUI/CUIで利用可能
  - デスクトップ端末、ヘッドレスなサーバー

<!-- _footer: 界隈ではK8sを使ってクラスター構成を作ったりもしてるそうです。楽しそう。 -->

---

## Raspberry PiとIoT

- Linuxが動きCPythonを扱える
- GPIO（デジタル入出力）でセンサーと接続可能
- シリアル通信規格: SPI, I2C  
- ディスプレイを繋ぐとサイネージ的なデバイスも作れる

⭕️ 安価ながら高機能なIoT端末として扱える
🔺 **ACアダプタなど給電環境が必要** 電源がない環境では扱いづらい

---

### PythonでIoTを行う選択肢

1. Raspberry Pi + CPython
2. **MicroPython / CircuitPython**
3. Raspberry Pi + CircuitPython

---

### MicroPythonとは

![bg left:35% 80%](img/2021-10-09-15-18-30.png)

- MicroPythonはマイコンボード向けの処理系
  - マイコン=マイクロコントローラー
  - 特定の機器制御に最適化された集積回路
- [クラウドファンディング](https://www.kickstarter.com/projects/214379695/micro-python-python-for-microcontrollers)で生まれたpyboardの開発環境として作られた

<!-- _footer: MicroPython micropython.org -->

---

### CircuitPythonとは

![bg left:35% 80%](img/2021-10-09-11-48-25.png)

- MicroPythonの派生版
  - adafruitが開発支援: オープンソースハードウェア企業で教育向け製品を扱う
- 当初はadafruitのマイコンボードに対応
  - その後他社製のマイコンボードにも広がる
- 専用ライブラリを使うとセンサーやLED
コントローラーが少ないコードで扱える

<!-- _footer: CircuitPython https://circuitpython.org adafruitは「えいだーふるーつ」と呼ぶそうです-->

---
![bg left:35% 130%](https://docs.google.com/drawings/d/e/2PACX-1vR6Kfmi6lFMG-UlxtRCNep0R2tOzNiIFSakbMOT3TNiCh6MZuQZrw1jUGC_f7TU99_vCmWtWZeItGnJ/pub?w=960&h=720)


### MicroPython/CircuitPythonの特徴

- CPythonの3系（3.4, 3.5の一部）の文法をベースにした独自の実装系
- マイクロコントローラー向けカスタムした標準ライブラリやサードパーティライブラリがある
- シリアルポートから直接REPLを実行
- 他のボードにもポートされてインストール可能

⭕️ Raspberry Piより安価。電源はバッテリーも
🔺 CPythonライクだが完全互換ではない

<!-- _footer: 写真はESP32+MicroPythonで水栓を開け閉めするものを作ってました -->

---

### PythonでIoTを行う選択肢

1. Raspberry Pi + CPython
2. MicroPython / CircuitPython
3. **Raspberry Pi + CircuitPython**

---

### 3. CircuitPythonのライブラリをRaspberry Piで扱う

- CircuitPythonの豊富なライブラリをRaspberry Piで扱う選択肢
- Adafruit-Blinkaライブラリを使う
  -Raspberry PiのGPIOをCircuitPythonのハードウェア向けに変換するレイヤーとなる
- Raspberry PiとCircityPython間でコードの相互利用がしやすい
  > CircuitPython features unified Python core APIs and a growing list of 300+ device libraries and drivers that work with it. These libraries also work on single board computers with regular Python via the Adafruit Blinka Library.
  > https://circuitpython.readthedocs.io/en/latest/docs/index.html

⭕️ CircityPythonのライブラリが使えセンサーモジュールの扱いが楽
🔺 どちらかの環境依存のコードを書く場合は扱いが難しい

<!-- _footer: "Blinkライブラリの概要: [CircuitPython on Linux and Raspberry Pi](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux)"  -->

---

![bg 82%](https://docs.google.com/drawings/d/e/2PACX-1vT_1IVFkLGrAzqOTQElWpsYjsMq_NCQvbUkF0FMq2DgscdKyWwFeJGgJ0DmXTBsg4GR7zE5iulV_i-2/pub?w=1440&h=810)

---

### デモ: 温度湿度気圧センサーから情報を取得する

![bg left:40% 80%](img/2021-10-09-15-29-48.png)

Rasberry Pi + Blinkaライブラリを使って、
デモしながら様子を見せていきます

- ラズパイ4BとBME280を接続
- BME280を搭載したモジュール製品
  - 今回は[AE-BME280](https://akizukidenshi.com/catalog/g/gK-09421/)（秋月電子通商）
  - ラズパイとの通信はSPI接続を利用

---

![bg left:40% 100%](https://docs.google.com/drawings/d/e/2PACX-1vSfoVxBK7x3Q2Zvx6yfWzpsfyrsHkt7FYiqbbD0_tEVkzwomfw8BcrRta_-VscBz0QkM6lnI3l92Blh/pub?w=922&h=1083)

### デモを試す時に必要なもの

- 利用する部品: ブレットボード、ワイヤー、BME280（利用するセンサー）
- 道具: はんだごて、はんだ、はんだこて台
  （センサーにピンが実装されていない場合は必要です）
- ラズパイも買ってください
- 購入先:
  Amazonとかでも集まる。
  [秋月電子通商](https://akizukidenshi.com/catalog/default.aspx)、[スイッチサイエンス](https://www.switch-science.com/)、[aitendo](https://www.aitendo.com/)、[マルツオンライン](https://www.marutsu.co.jp/)、[せんごくネット通販](https://www.sengoku.co.jp/) がおすすめ

<!-- _footer: 上記を用意できれば作れます。そのうちに工具も部材も増えていきます。沼ですね  -->
---

配線の様子を見せます

---

### 配線方法まとめ

![bg left 50% 100%](https://docs.google.com/drawings/d/e/2PACX-1vRDhv5roVz3g6nr87qmO39TdlWHT1DTQ1jizOjaE6P6TTGJUJDw3wBXpu6SrFNx-K6hjTp9T1-G5jBS/pub?w=960&h=720)

- 配線は一例です。
- 画像で利用しているBME280はAE-BME280ではないので、表を元に配線してください

<!-- _footer: このピン配置を行っているとUSBが偉大に見えますね。 -->

---

動作させたテストコードの例

https://github.com/hrsano645/homeenvdash-mini/blob/main/test_bme280.py

---

### Tips: Raspberry Pi上で開発をしやすくする

VS Codeのリモート開発が便利です -> Remote-SSH

- ssh経由で扱うといい。ただpi3あたりからでないと、リモート開発できない（vscodeのリモートサーバーが対応するCPUアーキテクチャの問題）
- <https://www.raspberrypi.org/blog/coding-on-raspberry-pi-remotely-with-visual-studio-code/>
> Remote SSH needs a Raspberry Pi 3 or 4. It is not supported on older Raspberry Pis, or on Raspberry Pi Zero.

---

## 目次

- 環境ダッシュボードを作った話
- PythonとIoT
- **Dashでダッシュボードアプリを作る**
- まとめ

---

## Dashでダッシュボードアプリを作る

Dashライブラリを使ってセンサー情報を表示する
ダッシュボードを作ります

---

### Dashの紹介

- Plotlyが作成しているWebアプリフレームワーク
  - Plotlyはグラフライブラリの名称でもある: `Plotly.js`、`Plotly.py`
- データ分析向けのプロトタイピングがしやすい
- サンプル（有料機能を使ったものもあるので注意）<https://dash.gallery/Portal/>

<!-- _footer: サンプルにある自動運転のデモが面白かったです https://dash.gallery/dash-avs-explorer/ -->
  

---

### Dashの特徴

- **ほぼPythonのみでWebアプリのレイアウトが作れる**
- **コールバック機能を使ってインタラクティブ操作**
- データセットやDBを扱いたい場合は自前で用意
  - PlotlyはPandasのDataFrameを使うのでPandas経由がやりやすいはず

ちなみにDashはFlask + Reactで作られている。
> Built on top of Plotly.js, React and Flask, Dash ties modern UI elements like dropdowns, sliders, and graphs directly to your analytical Python code.
> https://github.com/plotly/dash

<!-- _footer: 補足: 今回のスライドやデモで利用するDashのバージョンはv2.0です。最近更新されたので追従が大変だった… -->

---

### ほぼPythonのみでWebアプリのレイアウトが作れる

- HTMLタグを書く必要がない
  - HTMLを扱うコンポーネント
   => Pythonの操作のみでアプリが作れる
  - `dash-core-components`（`dcc`）を使うと高度なフォームや
  操作インターフェイスが扱える
- Plotlyと連携して豊富なグラフを扱うことができる

※ HTMLを書く必要がない≠HTMLの知識が必要ない


<!-- _footer: dash-core-components https://dash.plotly.com/dash-core-components -->
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

<!-- _footer: Flaskっぽいアプリの初期化 -->

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

<!-- _footer: あら簡単！ -->

---

### コールバック機能:動的な操作

- 動的な操作を可能にする
- たとえば
  - HTMlのフォーム操作
  - グラフの描写結果を更新する（日付別とか）
  - 定期的な表示の更新を行う（dcc.Interval）
- コールバック関数を用意してデコレーターで設定
  - アプリ上の操作を入力としてトリガーさせる
  - 入力された情報を元にデコレーター対象の関数が処理
  - 処理した結果をアプリ上へ出力する

<!-- _footer: 高度なコールバックとして、パターンマッチングやロングコールバック（v2.0から） があります -->

<!-- --- -->

<!-- TODO: 2021/10/14 画像一つ追加予定: コールバックのベーシックな説明を画像で説明。 -->


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
@callback(Output("output-p", "children"), Input("input-form", "value"))
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
    # debug=Trueでデバッグモード
    app.run_server(debug=True, host="0.0.0.0")
```

![bg left 50% 80%](img/2021-10-12-11-13-30.png)

<!-- _footer: host="0.0.0.0"は外部公開として扱います。この辺もFlask踏襲ですかね -->

---

### デモ: センサー情報を可視化する

センサー情報の取得方法は、直接センサーの値を取りに行く

- 時系列グラフを作るなら、データの記録は必須になる。
  - 実際のところはファイルかDB, 外部のデータソースへ保存して
  扱う方がわかりやすい
  - 今回はCSVファイルに1分ごと、30回分の測定結果を保存

<!-- _footer: 補足 センサー情報の記録は別スクリプトにする方が扱いやすいです -->

---

### センサーの最新の値を見る

デモ用アプリの該当箇所:
https://github.com/hrsano645/homeenvdash-mini/blob/main/homeenvdash-mini.py#L83

---

### 記録したセンサーの値をグラフ化する

デモ用アプリの該当箇所:
https://github.com/hrsano645/homeenvdash-mini/blob/main/homeenvdash-mini.py#L106

---

### Tips: 複雑化したらまとめてコンポーネント化する

複雑なアプリやレイアウトを作ると、構造も複雑になりがち

- 複雑になることはしょうがない
- 複雑になるので関数などで部品（カプセル）化していく
- コールバックで更新したいコンポーネント箇所をカプセル化すると、コールバック側の更新処理を作る時に呼び出しやすい

慣れてくるとwebアプリを書いている様な扱いに

- 説明箇所コードのリンク: https://github.com/hrsano645/homeenvdash-mini/blob/main/homeenvdash-mini.py#L103

<!-- _footer: 大いなる力には大いなる責任が伴う-->

---

### Tips: Bootstrapを使ってデザインを良くする

Dashの便利なライブラリ: dash-bootstrap-componets（dbc）によるデザインの整え方

- Dashのデメリットは、CSSを扱ったデザインがしづらい
  - レスポンシブ対応とか
- CSSフレームワークのBootstrapを扱いやすくコンポーネント化されている
- 扱いやすいもののBootstrapを知っている必要あり

※Dashのv2バージョンアップに伴って、dash-bootstrap-componetsも追従したバージョンアップが行われます。
デモ中は最新バージョンのリリース候補版を利用してます。

<!-- _footer: ライブラリのバージョンアップが資料作成のタイミングだとほんとね… -->

---

### デモ: デザインを整えてみる

- 実際にコードを見せつつ解説します
- レスポンシブ対応を例にします
- コードはこちらから見れます:
  https://github.com/hrsano645/homeenvdash-mini/blob/main/homeenvdash-mini-dbc.py

---

## 目次

- 環境ダッシュボードを作った話
- PythonとIoT
- Dashでダッシュボードアプリを作る
- **まとめ**

---

### まとめ

趣味プロジェクトを紹介しつつ、Pythonを使ったIoTとデータ可視化を
デモを交えてお伝えしました

- IoT: ラズパイ+CircitPythonを合わせる選択肢
- データ可視化: Dashでダッシュボードアプリを作る

本日お伝えしたいこと

- 自分の欲しい物が無ければ作ろう
- 身の回りで見えない数字を可視化してみよう
  - 身近だけど見えないデータ

---

## 終わりに

今日のトークで、

- IoTやダッシュボードを作ることが楽しいと思ってもらえたらうれしいです
- また作るきっかけにもなったらさらにうれしいです
- 手間暇はかかるけど、そこはモノづくりの大事な所だと思います

存分に手間暇かけてテクノロジーを楽しみましょう！

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

<!-- _footer: 実はこちらを宣伝したくてトーク応募したものです。ぜひこちらにも遊びに来てください！ -->

---

---

質問想定

---

- Dashを使うメリット、デメリットは？
  - メリットはHTMLを書く必要なくWEBアプリ作成ができる
  - デメリットはDB接続や高度な動的処理（ログイン処理やセッション管理）、API連携はそれほど得意ではない
    - それを解決する有償のサービスが提供されている
- 気圧センサーいろいろあるよ！
  - 知らなかったのでありがたいです！
- 精度はどう？
  - 数字というより変化を見たかったので、精度については今回は扱ってない
  - 実際にキャリブレーションする必要はあると思うし、高度なセンサーもあるので、用途によると思います。

---