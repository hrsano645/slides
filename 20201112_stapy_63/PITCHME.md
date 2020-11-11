### 家環境ダッシュボードを作ってみた話

#### みんなのＰyhtonb円協会 #63 懇親会LT

#### 2020/11/12 Hiroshi Sano

---

### 唐突ですが

---

### ダッシュボードはお好きですか？

---

google.com ナレッジパネル ダッシュボード 


![自動車とかではなく](20201112_stapy_63/img/car_dashborad_by_googlesearch.png)

これではなく


---

![デジタルのほう](20201112_stapy_63/img/degital_dashborad.png)

こういうもの

---

こんなものとか


---

ダッシュボードかっこいいよね！😎

---

作りたくなってきたので作りました！🔧🔨


家環境ダッシュボードの紹介をします

（名前がアレなのは気にしない）

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

### 唐突に宣伝

[[オフライン/オンライン同時開催]Python駿河 勉強会 #19 ～TBD～ - connpass](https://py-suruga.connpass.com/event/192889/)

---

### 宣伝終わり

---

### Why build Dashboard?

- 家の環境ってもっと厳密に見れるとストレス減るのでは？
- COVID19で家にいることが多すぎるのもあって、家の環境が気になってしょうがない


- 実家の祖母が98歳なんだけど、見守り的な意味でほしい

![granma_irasutoya](https://4.bp.blogspot.com/-E5SFXjWPayU/WR6ns-9naMI/AAAAAAABEVw/d2cE-VM_B_AnQp3PHoFIG8esHWmBB6YXgCLcB/s800/keirou_obaachan_smile2.png)

---

### システム紹介

<img src="https://docs.google.com/drawings/d/e/2PACX-1vQfSWRWP7uD7ffXyjrEStTYVhyFakLvQ0pREvuE8n5v0iceLlHyska3toXvUdRfhh7v_se6CTvm6DBO/pub?w=960&amp;h=720">

---

#### センサーノード: ラズパイ + センサー

センサーはシリアル通信規格を使うけど、中のデータを取り出すのにちょっと苦労する
-> 既存のライブラリを使うと楽

- 
- CircitPythonをラズパイで動かすことができる


---

- センサー情報記録: G Sheet。サービスアカウントで認証周りをしている。IoTなので鍵配布だけで連携できるのは楽でいい

---

- ダッシュボード: Plotly Dashで作る。データ入力はG Sheet -> Pandas
  - htmlを直接書かなくてもPythonのオブジェクトで操作、グラフもPlotlyをそのまま使うことになる
  - コールバック機能で動的に更新できる。自動更新やドロップダウンリストからの変更もリアルタイムに動く

---

### まとめ

- 家の環境が見れるようになって、体調管理しやすくなったと思う
  - 改善はまた別の話だけどｗ
- 今は複数ノード対応してないので、複数ノード対応するのが次の目標
- ほかのセンサーとか、防犯カメラ（Atom cam）とかでつかえる

---

### まとめ

- 認証周りを楽するならサービスアカウントおすすめ
- Dashはアプリ作成にも使えると思う。


### ダッシュボードはいいぞー