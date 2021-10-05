---
marp: true
header: "**ラズパイとDashで環境ダッシュボードを作ろう** 2021/10/16 PyCon JP 2021"
backgroundColor: #eee
---

# ラズパイとDashで環境ダッシュボードを作ろう

PyCon JP 2021
2021/10/15, 10/16

---

## お前誰よ

- 佐野浩士（Hiroshi Sano）[@hrs_sano645](https://twitter.com/hrs_sano645)
  - 🏠:静岡県の富士市🗻
- Job💼
  - [佐野設計事務所](https://sano-design.info)
  - 米農家🌾
- Community🧑‍💻
  - 🐍: Python駿河, PyCon mini Shizuokaスタッフ
  - 🏙💻: Code for ふじのくに

<!-- _footer:  -->

---

## 目次

- 環境ダッシュボードを作った話
- ラズパイとセンサーを扱う
  - CurcitPythonを使う選択肢
- Plotly Dashでダッシュボードアプリを構築する
  - PythonコードだけでWebアプリを構築する
  - 動的な操作
  - センサー情報を可視化する
- まとめ

<!-- _footer:  -->

---

本日のテーマ

## ラズパイとDashで環境ダッシュボードを作ろう

<!-- _footer:  -->

---

7分

- 著者作成のWebアプリの紹介:7分
  - homeenvdashプロジェクト

---

<左側に画像>

ラズパイ+環境センサー


<!-- _footer: 今は温度湿度気圧のセンサーのみに対応 -->

---

### なんで作ったか

- 何で作ったか: IoTで気温や湿度は見やすくなった。そのほかのセンサーも見たい


- 見守りに使う: 実家の祖母の部屋の状況を見れるようにして、気を付けたかった。

---


- 世の中にはIoTの製品はあるものの、気圧を見られるものが意外となかったので自作してみた

---

あと家にラズパイが大量に転がっているので有効活用することが目的

---

<家にあるラズパイを積む->写真撮影>

---

![](img/2021-10-02-14-31-48.png)

<!-- _footer: https://twitter.com/karaage0703/status/1413347181705105410?s=20 -->
---

積みボードがある方は贅沢に使って快適な日常を手に入れましょう

---

- ダッシュボードの全体構成

![](https://docs.google.com/drawings/d/e/2PACX-1vR6NyaVJv9P6mVH4wCfPot4IbAtuBWNaP-wvr2_8SkwpkCfYD2qxP5LHsPo1iW311P9WVHtUSIBHLCm/pub?w=960)

  - ブロックごとのキーワードを紹介（技術や扱うライブラリ）

---

- PythonとIoT（10min


---

### PythonでIoTを行う選択肢

- ラズパイ + CPython
- MicroPython/CircuitPython

![](https://docs.google.com/drawings/d/e/2PACX-1vT_1IVFkLGrAzqOTQElWpsYjsMq_NCQvbUkF0FMq2DgscdKyWwFeJGgJ0DmXTBsg4GR7zE5iulV_i-2/pub?w=960&h=540)

---

## MicroPython/CircuitPythonの紹介

<左に画像>

- MicroPythonはマイコンボード向けの処理系
- クラウドファンディングで生まれたpyboardという

<!-- _footer: MicroPython Kickstarterページ https://www.kickstarter.com/projects/214379695/micro-python-python-for-microcontrollers -->

---

<左に画像>

- 特徴は
  - CPythonの3系（3.4, 3.5の一部）の文法をベースにした独自の実装系
  - マイクロコントローラー向けにカスタマイズした標準ライブラリやサードパーティライブラリを備える
  - シリアルコンソールからREPLが扱える
- 他のボードにもポートされ、arduino系のボードで扱える
- 便利なのはESP32系です。M5Stackシリーズでほとんど対応していて手に入りやすい

---

### CurcitPythonとは

<左に画像>

- circuitpythonはMicroPythonの派生版。adafruitというSTEAM系に取り組んでる電子部品の販売や教育分野のメーカーが作成
- そのメーカーのボードに対応したり、専用のライブラリを用意
  - メーカーのセンサーデバイスと接続しやすい


<!-- _footer: CircuitPython: https://learn.adafruit.om/welcome-to-circuitpython  -->

---

<ラズパイ+micropythonたちの比較画像を載せる。>

---

### CircuitPythonのライブラリをRaspberry Piで扱う

  - blinkaというライブラリを使う。 [Overview | CircuitPython on Linux and Raspberry Pi | Adafruit Learning System](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux)
  - circuitpython向けのコードやライブラリをraspberry pi上でも扱える様にしているライブラリがある。
  - blinkaはcircuitpythonで使うマイコンボードの機能をraspberry pi向けに変換するレイヤー。

<!-- _footer: もちろんラズパイ向けのコードやライブラリはcircuitpythonでは動かないので注意 -->

---

### センサー情報取得の実例: BME280という温度湿度センサーから情報を取得する

- 実践する
- BME280を接続して動かしてみる
- デモを見せながら披露

---

  - ここでtips: Raspberry PiでPythonを扱う方法:VSCodeのリモート開発が便利です
    - ssh経由で扱うといい。ただpi3あたりからでないと、リモート開発できない（vscodeのリモートサーバーが対応するCPUアーキテクチャの問題）
    - <https://www.raspberrypi.org/blog/coding-on-raspberry-pi-remotely-with-visual-studio-code/>
    > Remote SSH needs a Raspberry Pi 3 or 4. It is not supported on older Raspberry Pis, or on Raspberry Pi Zero.

---

- Dashでセンサー情報を可視化する（10min

---

  - Dashの紹介
    - plotlyという企業、またグラフライブラリ、が作成しているWebアプリフレームワーク
    - plotlyがこのグラフライブラリを使いつつwebアプリを簡単に作ってデータ分析向けにプロトタイピングしやすくしたライブラリがdash
      - サンプルもたくさん（有料機能を使ったものもあるので注意）<https://dash.gallery/Portal/>
    - もう時期新しいバージョンが出てくるらしい: 2.0

---

### Dashの基本的な情報
- dashは flask + reactで作られている。
  > Built on top of Plotly.js, React and Flask, Dash ties modern UI elements like dropdowns, sliders, and graphs directly to your analytical Python code. Read our tutorial proudly crafted ❤️ by Dash itself.
- HTMLを書く必要がない -> PythonのみでWebサイト構成が作れる
- コールバック機能を使ってインタラクティブ操作が可能
  - ライブラリのサンプルには自動運転時の状況の可視化とかもある。かなり面白い
- dbを扱いたい場合は自前で用意。
  - pandasを使ってplotlyのグラフを作れるので、pandas経由で何かしらをするときに便利

---

HTMLを書く必要がない -> PythonのみでWebサイト構成が作れる

- htmlのフォームや構造をラッピングしたコンポーネントを呼び出して構成を用意する
- plotlyと連携することが可能
- htmlな操作は知らないと扱いづらいはづらい


---

- フォームなどの操作から動的な変更:コールバック機能
  - dashは動的な操作を可能にするためのコールバックという機能がある
  - たとえばグラフの種類を変更することができる: 実演
  - homeenvdashではフォームで部屋ごとや温度湿度気圧を含めて操作をする


---
### tips: ホットリロードによる開発

- 自動的にリロードしてくれる。デバッグモードを有効にしておくと開発しやすい

---

### tips: と言ってもhtmlっぽい構造は作る必要がある。これらは関数などでカプセル化していくとわかりやすい

慣れてくるとwebアプリを書いている様な扱いになってくる。（コンポーネント用意して呼び出すなど）



---

### デモ: センサー情報を可視化する

- 実演:センサー情報の取得方法は、直接センサーの値を取りに行く
- 時系列グラフを作るなら、データの記録は必須になる。
  - 実際のところはファイルかDB, 外部のデータソースへ保存して扱う方がわかりやすい


---

### tips: Bootstrapを使ってデザインを良くする

- Dashの便利なライブラリ: Dash bootstrap componets（dbc）によるデザインの整え方
  - dashの利点は扱いやすいが、CSSなどのデザインはややしづらい
  - そこで、bootstrapを扱いやすいコンポーネントでまとめたライブラリがある
  - それらを使うことで、レスポンシブデザインがしやすいし、bootstrapのコンポーネントがdas上で扱いやすい

---

### デモ: デザインを整えてみる

---

### まとめ（3min
- 自作のダッシュボードであるhomeenvdashをネタに
- ラズパイでセンサー情報を取りに行く手段でおすすめな方法を紹介
- ダッシュボードアプリをplotlyのdashで作成
- 言いたいこと
  - PythonのIoT活用をしてみよう
  - 日常のデータを見れる世にしてみよう
  - 積みボードを活用していこう。
  - 

### おしらせ: pycon mini shizuoka やります。 LTと参加者募集をしていきますー

---

つまづきポイントの記事は参考になる -> https://qiita.com/chromia/items/4b91d8b6ca520782672c