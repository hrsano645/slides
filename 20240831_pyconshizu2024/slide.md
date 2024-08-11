---
marp: true
paginate: true
---


# Pythonで3Dモデリングをしてみよう: CadQuery Basic

PyCon mini Shizuoka 2024
2024-08-318

@hrs_sano645

---

## お前誰よ / Self Introduction

佐野浩士（Hiroshi Sano）[@hrs_sano645](https://twitter.com/hrs_sano645)

* 🗺️: 静岡県富士市🗻
* 🏢: 株式会社佐野設計事務所　代表取締役
* 👥🤝
  * 🐍: PyCon mini Shizuoka Stuff / Shizuoka.py / Unagi.py / Python駿河
  * CivicTech, Startup Weekend Organizer
* Hobby: Camp🏕️, DIY⚒️, IoT💡

![w:180px](../images/sns-logo_2024.jpg)![w:360px](../images/shizuokaLogo.png) ![w:180px](https://lh3.googleusercontent.com/pw/AIL4fc9DDT9ootdGiDNZiGUybbHE5WRnm68hFp6XknmZc2lVttIBKJ180GVq0NE2qtcGRbx8OBVAak3E4qHa7H5iXw8gtQqkY4l6tWrFkIHUA96q1jcqE2_f) ![w:180px](https://lh3.googleusercontent.com/pw/AIL4fc_3zxLYLoa5SSL_apqpJ3WCY9BRMfXRL4jUYaYouX3MvqiMU5eSCi8be6eQIvboRzgNZ3ZvdZAIET40tJD7I4y8dSHF6UByo-u8jXhLFFGv5rAw_kZU)

---

![bg](./images/sano-design_info.png)

<!-- 

* 株式会社佐野設計事務所は自動車プレス金型という機械を設計する事務所です。3D CADを使い設計、また自動車業界に限らず、製品の3Dモデリングも扱っております。
* こういった設計データはデジタルデータになります。データを使い関連業務の改善に、Pythonやクラウドサービスなどを組み合わせて実現しています。
* 製造業なのですがデジタル化で取り組んでいまして、同じように取り組まれている方や、ご興味ある方がいましたら、後ほどのパーティでぜひ意見交換できたらと思います。
* もちろん静岡のPythonコミュニティとしても参加していますので、コミュニティスタッフとしてもお気軽にお声がけください！
-->

---

## 本日の内容

* 3Dデータを作ってみよう
* 3DCADの基礎
* CadQueryの使い方: デモをしつつ最後に3Dプリンターで出力

離さないこと

* Pythonの基礎的な話: Python Boot Campレベル
*

---
3Dデータを自分たちで作れるようになるために
Maker文化を紹介します
3Dプリンタを扱う上では必要不可欠な存在

3DCADの概要
二次元と三次元について: 2DCAD, 3DCADの違い、3Dのメッシュデータとソリッドデータ。
3DCADの種類: プロプライエタリやOSSを交えて
パラメトリック/ノンパラメトリックの違い: 特徴を説明します
点、エッジ、フェース、ソリッド、サーフェス、スプラインの概要

CadQueryとは
プログラマブルな3DCAD: そのほかの同種のCADもご紹介: OpenSCAD
Open CASCADE kernelを使ったプログラマブルな3DCAD
環境の作り方: VSCode での作り方を紹介

How to Use CadQuery Basic: デモを交えて紹介します
作業面について:
ソリッドを作る: 立方体、球体など
モデルを組み合わせたり、ブーリアン演算について扱います。
ファイルを出力する。メッシュデータのSTL、 ソリッドデータのSTEPを書き出します。
3Dプリンタで出力してみる: 実際に3Dプリンタを動かす様子もお見せします（遠隔で操作をするので通信環境によっては中断する可能性もあります）
まとめ

---
