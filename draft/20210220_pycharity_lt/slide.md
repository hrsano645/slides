---
marp: true
header: "**Dash+環境センサーで家環境ダッシュボードを作った話** - PyCharity LT 2021/02/20"
footer: "by [@hrs_sano645](https://twitter.com/hrs_sano645)"
paginate: true
---

### Dash+環境センサーで家環境ダッシュボードを作った話

PyCharity LT 2021/02/20

Hiroshi Sano

---
## お前誰よ

- Hiroshi Sano [@hrs_sano645](https://twitter.com/hrs_sano645) 🏠:静岡の🗻見えるところ
- Job💼
  - [佐野設計事務所🚗⚙️📏](https://sano-design.info): 自動車系部品製造機械の3D設計事務所
  - 米農家🌾
- Community🧑‍💻
  - 🗻🐍: shizuoka.py, unagi.py, Python駿河
  - 🗻🐍: PyCon mini Shizuokaスタッフ
  - 🐍: PyCon JP 2020 チュートリアル講師

---

静岡Pythonコミュニティの勉強会 Python駿河は 2/27（土）です！

「Pythonプロフェッショナルプログラミング 第3版 Chapter 05 課題管理とレビュー」

つまみ食い読書します。ぜひ遊びに来てください！

参加方法はconnpass検索、#pycharityに流します

---

PyCon mini Shizuoka 2021 企画中！

開催日まだ未定ですが、年内までにはやりたい。スタッフ募集中です！

---

#pycharity 二回目🎉

<!-- footer: -->

---


LTラストバッターなので

緊張してます

そのLTですが

正直作ってる暇がなかったので

今日の朝から作りました

今日言いたいことは

Dashというダッシュボードアプリを簡単に作るフレームワーク便利

IoTとの連携をどうやってかと

そこから今のところ思ったことです

まずhomeenvdashという趣味プロジェクトの紹介します

画像1

一言でいうと

家の環境をセンシングしてダッシュボードに載せるという

まあよくあるプロジェクトですｗ

中身はこんな感じで

img2: iPadでお絵描きした



---

やってみて思うこと

データ分析 -> アプリ化で dash便利

Dash使ってみての感想

pandasを使えるならすぐにグラフ化出来ます

デザインするのが面倒 -> bootstrapを使えるコンポーネントがある

コンポーネントツリーが見づらい問題 -> 

<画像載せる>

日本語情報内

書籍買おう！

次に、IoTはPythonとの親和性が良すぎる

Pythonは元々教育向けの言語

小学生でもあつかえる

IoTで動かす環境が多い

ラズパイとかMicropythonとか

センサーをラズパイにつなげる -> 利用しやすいライブラリがそろってる

adafruitのCurcitPython(Micropythonのadafruit版）向けのライブラリは

ラズパイでも動かせるから、非常に手軽に

最後に

センシングとデータ可視化ってよくやるパターンではある

それだけじゃ意味ない

元々は家の環境の様子を手軽に見たくて始めた

実家では祖母が



---



---

Thanks!