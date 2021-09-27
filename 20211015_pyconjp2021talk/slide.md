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
    - 主に二つのブロックを紹介
    - ブロックごとのキーワードを紹介（技術や扱うライブラリ）
- PythonとIoT（10min
  - micropython/CircuitPythonの紹介
  - Raspberry PiでPythonを扱う方法:VSCodeのリモート開発が便利です
  - CircuitPythonのライブラリをRaspberry Piで扱う
  - センサー情報取得の実例: BME280という温度湿度センサーから情報を取得する
- Dashでセンサー情報を可視化する（10min
  - Dashの紹介
  - Dashの基本的な構成の紹介:
  - HTMLを書く必要がない
  - ホットリロードによる開発
  - フォームなどの操作から動的な変更:コールバック機能
  - センサー情報を可視化する
  - Dashの便利なライブラリ: Dash bootstrap componets（dbc）によるデザインの整え方
- まとめ（3min
