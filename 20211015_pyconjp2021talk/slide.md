---
marp: true
header: "**ラズパイとDashで環境ダッシュボードを作ろう** 2021/07/16 はんなりPython LT"
# footer: "by [@hrs_sano645](https://twitter.com/hrs_sano645)"
paginate: true
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

---

アウトライン

- 導入（7min
  - 自己紹介
  - 著者作成のWebアプリの紹介
    - homeenvdashプロジェクト
    - 何で作ったか: IoTで気温や湿度は見やすくなった。そのほかのセンサーも見たい
    - 見守りに使う: 実家の祖母の部屋の状況を見れるようにして、気を付けたかった。
    - 世の中にはIoTの製品はあるものの、気圧が意外と見れるものがなかったので自作してみた
  - あと家にラズパイが大量に転がっているので有効活用することが目的
  - （ここでからあげさんの積みボードの話をしておく
  - Webアプリの全体構成
    - 構成を図で表す
    - 主に二つのブロックを紹介。センサー部とダッシュボード部
    - ブロックごとのキーワードを紹介（技術や扱うライブラリ）
- PythonとIoT（10min
  - micropython/CircuitPythonの紹介
    - micropythonはpyboardというクラウドファンディングで生まれた言語系
      - [Micro Python: Python for microcontrollers by Damien George — Kickstarter](https://www.kickstarter.com/projects/214379695/micro-python-python-for-microcontrollers)
      - 特徴は、
        - CPythonの3系（3.4, 3.5の一部）の文法をベースにした独自の実装系
        - マイクロコントローラー向けにカスタマイズした標準ライブラリやサードパーティライブラリを備える
        - シリアルコンソールからREPLが扱える
    - 他のボードにもポートされ、arduino系のボードで扱える
      - 便利なのはESP32系です。M5Stackシリーズでほとんど対応していて手に入りやすい
    - circuitpythonはmicropythonの派生版。adafruitというSTEAM系に取り組んでる電子部品の販売や教育分野のメーカーが作成
    - [Welcome To CircuitPython | Welcome to CircuitPython! | Adafruit Learning System](https://learn.adafruit.com/welcome-to-circuitpython)
    - そのメーカーのボードに対応したり、専用のライブラリを用意して、メーカーのセンサーデバイスと接続しやすい
  - CircuitPythonのライブラリをRaspberry Piで扱う
    - blinkaというライブラリを使う。 [Overview | CircuitPython on Linux and Raspberry Pi | Adafruit Learning System](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux)
    - このcircuitpythonはraspberry piでも利用できる。というより、circuitpython向けのコードやライブラリをraspberry pi上でも扱える様にしているライブラリがある。
    - blinkaはcircuitpythonで使うマイコンボードの機能をraspberry pi向けに変換するレイヤー。
    - それらを扱うことで、ラズパイやマイコン向けに同じコードで作業できる。（もちろんラズパイ向けのコードやライブラリはcircuitpythonでは動かないので注意）
      ~~TODO: 2021/09/27 ちゃんとその通りかチェックする~~
  - センサー情報取得の実例: BME280という温度湿度センサーから情報を取得する
    - 実践する
    - BME280を接続して動かしてみる
    -
  - ここでtips: Raspberry PiでPythonを扱う方法:VSCodeのリモート開発が便利です
    - ssh経由で扱うといい。ただpi3あたりからでないと、リモート開発できない（vscodeのリモートサーバーが対応するCPUアーキテクチャの問題）
    - <https://www.raspberrypi.org/blog/coding-on-raspberry-pi-remotely-with-visual-studio-code/>
    > Remote SSH needs a Raspberry Pi 3 or 4. It is not supported on older Raspberry Pis, or on Raspberry Pi Zero.
- Dashでセンサー情報を可視化する（10min
  - Dashの紹介
    - plotlyという企業、またグラフライブラリ、が作成しているWebアプリフレームワーク
    - plotlyがこのグラフライブラリを使いつつwebアプリを簡単に作ってデータ分析向けにプロトタイピングしやすくしたライブラリがdash
      - サンプルもたくさん（有料機能を使ったものもあるので注意）<https://dash.gallery/Portal/>
    - もう時期新しいバージョンが出てくるらしい: 2.0
  - Dashの基本的な構成の紹介:
    - dashは flask + reactで作られている。
      > Built on top of Plotly.js, React and Flask, Dash ties modern UI elements like dropdowns, sliders, and graphs directly to your analytical Python code. Read our tutorial proudly crafted ❤️ by Dash itself.
    - HTMLを書く必要がない -> PythonのみでWebサイト構成が作れる
      - tips: と言ってもhtmlっぽい構造は作る必要がある。これらは関数などでカプセル化していくとわかりやすい。
      　慣れてくるとwebアプリを書いている様な扱いになってくる。（コンポーネント用意して呼び出すなど）
    <!-- - ホットリロードによる開発
      - 自動的にリロードしてくれる。デバッグモードを有効にしておくと開発しやすい -->
    - コールバック機能を使って動的な操作が可能
      - ライブラリのサンプルには自動運転時の状況の可視化とかもある。かなり面白い
    - dbを扱いたい場合は自前で用意。
      - pandasを使ってplotlyのグラフを作れるので、pandas経由で何かしらをするときに便利
  - フォームなどの操作から動的な変更:コールバック機能
    - dashは動的な操作を可能にするためのコールバックという機能がある
    - たとえばグラフの種類を変更することができる: 実演
    - homeenvdashではフォームで部屋ごとや温度湿度気圧を含めて操作をする
  - センサー情報を可視化する
    - 実演:センサー情報の取得方法は、直接センサーの値を取りに行く
    - 実際のところはファイルかDB, 外部のデータソースへ保存して扱う方がわかりやすい
      - 時系列グラフを作るなら、データの記録は必須になる。
  - Dashの便利なライブラリ: Dash bootstrap componets（dbc）によるデザインの整え方
    - dashの利点は扱いやすいが、CSSなどのデザインはややしづらい
    - そこで、bootstrapを扱いやすいコンポーネントでまとめたライブラリがある
    - それらを使うことで、レスポンシブデザインがしやすいし、bootstrapのコンポーネントがdas上で扱いやすい
- まとめ（3min
  - 自作のダッシュボードであるhomeenvdashをネタに
  - ラズパイでセンサー情報を取りに行く手段でおすすめな方法を紹介
  - ダッシュボードアプリをplotlyのdashで作成
- おしらせ: pycon mini shizuoka やります。 LTと参加者募集をしていきますー
