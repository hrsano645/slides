---
marp: true
paginate: true
---


# 調整さんの調整結果をカレンダーへ登録するGPTsを作った話

ITネタ・自動化ネタ ライトニングトーク～アマギフ1万円争奪戦～
RPACommunity YouTube登録者数1万名達成記念 特別イベント！
2024-02-09  

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

![w:180px](../images/sns-logo.jpg)![w:360px](../images/shizuokaLogo.png) ![w:180px](https://lh3.googleusercontent.com/pw/AIL4fc9DDT9ootdGiDNZiGUybbHE5WRnm68hFp6XknmZc2lVttIBKJ180GVq0NE2qtcGRbx8OBVAak3E4qHa7H5iXw8gtQqkY4l6tWrFkIHUA96q1jcqE2_f) ![w:180px](https://lh3.googleusercontent.com/pw/AIL4fc_3zxLYLoa5SSL_apqpJ3WCY9BRMfXRL4jUYaYouX3MvqiMU5eSCi8be6eQIvboRzgNZ3ZvdZAIET40tJD7I4y8dSHF6UByo-u8jXhLFFGv5rAw_kZU)

---

今回のテーマ: 調整さんの調整結果をカレンダーへ登録するGPTsを作った話

---

何で作った？

---

趣味のイベント運営がいろいろありまして

* 静岡Pythonコミュニティ
* PyCon mini Shizuoka
* Startup Weekend 富士
* 地元の子供向けのイベント

<!-- _footer: なんでそんなにたくさんやってるかというと、いろいろと関わったらこうなってたやつw -->

---

ミーティング時間調整に調整さんを使ってる

---

## 調整さんを使う理由

* 割と利用したことがある人が多い

Googleカレンダーの予定調整とか使ってみたいけど、使い方がわからない人が多いと思う

---

調整さんで困ること

---

調整結果をカレンダーに登録するのは手動

---

なので登録し忘れて、たまにミーティングを忘れてる

---

やばい／(^o^)＼

---

エンジニアなので、テック的に対応したい....と思ったけど

---

これChatGPTでやらせたらいいのでは🤔

---

本題: 調整さんの調整結果をカレンダーへ登録するGPTsを作った話

---

作り方

---

---

調整さんのサイトを読んでくることが出来る？ -> 出来なかった

---

なのでわざわざ張り付けることにしている。スクレイピングな手段を間に挟むことも考えたけど、面倒だったのでw

---

## カスタムGPTを使うときに苦労したこと

---

作るときにチャットベースで作ってくれるが、プロンプトが上書きされてしまう

---

プロンプトの上書きは結構あったので作業時はエディタなどでバックアップとっておくといいと思う

---

アイコン作ってと言ったら上書きされてしまってたので結構焦る

---

GPTがmarkdownで出力したリンクがそのまま利用できない

---

対処としては、urlを生成してもらうようにした。ただモバイル版だと使えるから環境の何かかもしれない

---

中身見られないようにする対策

---

色々あるっぽいけど、こちらを使ってみてる

---

意味があるのかは今のところ不明

---

## まとめ

* 調整さんの調整結果をカレンダーへ登録するGPTsを作った
* カスタムGPTを使うときに苦労したこと
* まだまだ使いこなせてないけど、楽しい

---

## 発展として

* メールやチャットの文章から予定作るGPTも作って、使い倒したい
* GPT側でカレンダーの連携もできるはずなので、そちらを使ったほうがよりアクションが減るはず
