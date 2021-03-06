### 家環境ダッシュボード🏠🌡️📉を作ってみた話

#### みんなのＰyhton勉強会 #63 懇親会LT

#### 2020/11/12 Hiroshi Sano

---

### 唐突ですが皆さん

---

### ダッシュボードはお好きですか？

---

![height=480, alt=degital_dashboard](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Opsview_Monitor_6.0_Dashboard.jpg/800px-Opsview_Monitor_6.0_Dashboard.jpg)

こういうもの

---

ダッシュボードかっこいい！😎

憧れていたので、作りました！🔧🔨

---

家環境ダッシュボードの紹介です

百聞は一見にしかず

いま動かしているものを紹介🧐

---

### お前誰よ

- 佐野浩士（Hiroshi Sano）[@hrs_sano645](https://twitter.com/hrs_sano645)
- 🏠:静岡県の富士市🗻

- Job💼
  - [佐野設計事務所🚗⚙️📏🖊️](https://sano-design.info) IT/雑務何でも屋
  - 米農家🌾

- Community🧑‍💻
  - 🗻🐍: shizuoka.py, unagi.py, Python駿河
  - 🗻🐍: PyCon mini Shizuokaスタッフ
  - 🐍: PyCon JP 2020 チュートリアル講師

---

### 唐突に宣伝

[[オフライン/オンライン同時開催]Python駿河 勉強会 #19 ～TBD～ - connpass](https://py-suruga.connpass.com/event/192889/)

---

### 宣伝終わり

---

### Why build Home Env Dashboard?


- COVID19で家にいること多い=家の環境が気になる
- 家の環境を数値で見れるとストレス減るのでは？

![height=320, alt=work_from_home_irasutoya](https://1.bp.blogspot.com/-jlHonWZdPp0/Xq5vQuVPQrI/AAAAAAABYtI/S0mjN1WK-wEJBBSS2M6xTEhEmVjM5mUwwCEwYBhgL/s1600/shigoto_zaitaku_cat_man.png)

---

### Why build Home Env Dashboard?

- 実家の祖母が98歳で見守り的な意味も

![height=320,alt=granma_irasutoya](https://4.bp.blogspot.com/-E5SFXjWPayU/WR6ns-9naMI/AAAAAAABEVw/d2cE-VM_B_AnQp3PHoFIG8esHWmBB6YXgCLcB/s800/keirou_obaachan_smile2.png)

---

### システムの全体像

![height=480, alt=home env dashboard system image](https://docs.google.com/drawings/d/e/2PACX-1vQfSWRWP7uD7ffXyjrEStTYVhyFakLvQ0pREvuE8n5v0iceLlHyska3toXvUdRfhh7v_se6CTvm6DBO/pub?w=960&amp;h=720)

---

### センサーノード🌡️

ラズパイ + センサー:BME280 温度と湿度と気圧

- センサーはシリアル通信規格でデータ取得: I2C, SPI
  - データを取り出すのにちょっと苦労する🥺
  - AdafruitのCircitPythonが提供するライブラリが使える

@size[0.5em]ref: [Adafruit BME280 Humidity + Barometric Pressure + Temperature Sensor Breakout](https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout/python-circuitpython-test)

---

![height=480, sensor node](https://docs.google.com/drawings/d/e/2PACX-1vTYhZg5yz9pLjrt0OJQ87xG396d-8jKKyUwIAPZ2MMy9Nv3SgaTOINHsHpFXwocK1gXgcgxRkSwHP9Q/pub?w=960&amp;h=720)

---

### センサー情報記録📝

Google Sheetにため込んでます

ライブラリはGoogle公式から（APIドキュメントに載ってるので割愛）

- 認証にはサービスアカウントを利用
  - IoTなので鍵配布だけで連携できるのは楽でいい
  
---

![height=480, sensor_recode](./20201112_stapy_63/img/sensor_recode_gsheet.JPG)

---

### ダッシュボード📉

[Plotly Dash](https://dash.plotly.com/)で作る

- htmlを直接書かなくてもPythonのオブジェクトで操作、グラフもPlotlyをそのまま使う
- コールバック機能で自動更新やドロップダウンリストからの変更もリアルタイム

データ入力はGoogle Sheet -> Pandas

---

![height=480, dashboard](https://docs.google.com/drawings/d/e/2PACX-1vThEcyEPO9SzCVYEpL0WCAZ4Ceou004nnlmlYci07FiQKklRLvgLDLilj0ipzY30cdp_NcBYhY0Jde7/pub?w=960&amp;h=720)

---

### まとめ🔚

- 家の環境が見れるようになって、体調管理しやすくなったと思う💪
- **ほかのセンサー（CO2）**とか、**防犯カメラ📹** が見れると面白そう
- アラート🚨に対応: Dashだと有料になる💸

---

### まとめ🔚

- 複数ノード（部屋ごと）対応するのが次の目標
- IoTとGoogleAPIの連携を楽するならサービスアカウント認証おすすめ
- Plotly Dashはアプリ作成にも使える気がする

---

## ダッシュボードはいいぞ🥳

