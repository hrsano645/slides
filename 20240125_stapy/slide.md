---
marp: true
paginate: true
---


# 非同期タスクキューを使って業務を自動化しまくった話

みんなのPython勉強会#100
2024-01-25  

佐野  浩士 @hrsano645

---

## お前誰よ / Self Introduction

佐野 浩士（Hiroshi Sano）[@hrs_sano645](https://twitter.com/hrs_sano645)

* 🗺️: 静岡県富士市🗻
* 🏢: 株式会社佐野設計事務所 CEO
* 👥🤝
  * 🐍: PyCon mini Shizuoka Stuff / Shizuoka.py / Unagi.py / Python駿河
  * CivicTech, Startup Weekend Organizer
* Hobby: Camp🏕️,DIY⚒️,IoT💡

![w:180px](../images/sns-logo.jpg)![w:360px](../images/shizuokaLogo.png) ![w:180px](https://lh3.googleusercontent.com/pw/AIL4fc9DDT9ootdGiDNZiGUybbHE5WRnm68hFp6XknmZc2lVttIBKJ180GVq0NE2qtcGRbx8OBVAak3E4qHa7H5iXw8gtQqkY4l6tWrFkIHUA96q1jcqE2_f) ![w:180px](https://lh3.googleusercontent.com/pw/AIL4fc_3zxLYLoa5SSL_apqpJ3WCY9BRMfXRL4jUYaYouX3MvqiMU5eSCi8be6eQIvboRzgNZ3ZvdZAIET40tJD7I4y8dSHF6UByo-u8jXhLFFGv5rAw_kZU)

---

![bg](../images/sano-design_info.png)

<!-- 

* 株式会社佐野設計事務所は自動車プレス金型という機械を設計する事務所です。3D CADを使い設計、また自動車業界に限らず、製品向けの3Dモデリングも扱っております。
* こういった設計データはデジタルデータになります。データを使い関連業務の改善に、Pythonやクラウドサービスなどを組み合わせて実現しています。
* 製造業のうえにニッチな領域ですがデジタル化も取り組み、ニッチな分野のDXとしても推進しているところです。
-->

---

## みんなのPython勉強会#100 おめでとうございます🎉👏🥳

---

## 時は2023年の半ば

## 目標: 業務の効率化を限界まで進める

---

## 業務自動化ガッツリやりました

* 依頼ベースの案件業務
* 今まではそれほど多くなかったが今年になって急激に増える
  * 人力でやっていては追いつかなそうでやばい
* 人が必要な部分以外人力でやるのを止める！
  -> **止めることに成功した！！🙌😆**

---

## 業務タスク自動化サービスの構成

![w:800px](https://docs.google.com/drawings/d/e/2PACX-1vRxi-CGrIr6lu1K4wroeMLzybS4htY3PNTZCq3mxcXidHcejks1liceIsuXuCTrsiWORufyDXyKa7ZB/pub?w=900&amp;h=560)

---

## どんなことを効率化？

* **自動生成** <= この部分を非同期タスクキューを使ってた
  * 依頼受注（メール）→ボイラープレートツールで作業プロジェクト
    フォルダーを生成
  * スケジュール管理→Googleスプレッドシート連携
  * 会計サービスと連携して見積書/請求書生成（書類作成）
  * 依頼企業側のシステム連携: WEBスクレイピング
* タスク操作をChatOps
  * Google Chatでチャットボット作成
* 過去の依頼からサマリー情報のデータベース化: (現在取り組み中）

<!-- _footer: 始まりと終わりを自動化することで、中身の作業に集中できるような体制 -->

---

## 自動生成の部分を非同期タスクキューを使って作業させています

---

## なんで非同期にしたの？

* これらは重い処理: ファイル操作、APIアクセス -> I/Oバウンド処理
  * 組み合わせると**数秒ではなく数十秒〜分単位**の処理
  * 結果が返ってくるタイミングはその時次第
* 同期処理でやると、処理が終わるまで待たされる
  -> ブロッキング処理
* **チャットボット側がロックされてしまう->応答が返せない**
  基本チャットボットは非同期前提

---

Google Chatの場合

> 「同期的に応答するには、Chat アプリが 30 秒以内に応答し、その応答をインタラクションが発生したスペースに投稿する必要があります。それ以外の場合は、Chat アプリは非同期で応答できます。」
> <https://developers.google.com/chat/api/guides/message-formats?hl=ja#sync-response>

（[Slackの3秒](https://api.slack.com/interactivity/slash-commands#responding_basic_receipt:~:text=This%20confirmation%20must,ignore%20the%20request.)よりも全然緩いけど、非同期前提な様子）

---

## 非同期とは

* 同期処理と非同期処理の違い:
  処理のオフロードと並列処理が可能。処理の待ち時間を有効活用できる
* チャットボットのために非同期処理を使うことになる: これが結局制約あるため
* ノンブロッキング処理: 処理が終わるまで待たされない（チャットの場合、応答が素早く返せる）

---

## Pythonでの非同期処理の選択肢

* 標準ライブラリ:（並列）threading,（並列）multiprocessing,
  （非同期）asyncio,（並列？3.12から）sub-interpreters
* メッセージキュー活用: celery, rq, pyzmq(ZeroMQ)
* クラウドのメッセージング: Cloud Pub/Sub（イベントベースで
* etc...

---

## 今回はRQ(python-rq)を使いました

python-rq: <https://python-rq.org/>

以下の3つの要素で構成される

* アプリ: タスク発行→キューへ入れる→ワーカーから処理結果を受け取る
* ワーカー: タスクの処理を行う
* redis: アプリとワーカーの間に入りキューとして利用する

---

## 非同期タスクのざっくりイメージ
<!-- 

* [業務]依頼を受ける
* [業務->アプリ->redis]依頼内容をタスクとしてキューに入れる
* [redis->ワーカー]キューからタスクを取り出し、ワーカーに渡す
* [ワーカー]ワーカーがタスクを実行する
* [ワーカー->redis->アプリ]ワーカーがタスクを完了したら、結果をキューに返す
* [アプリ->業務]キューの結果をアプリ側で受け取り結果を表示

これらをシーケンス図にする -->
![](https://mermaid.ink/img/pako:eNqFkstOwkAYhV-lmTW-QBesfAO3s5m0ozbaAUu7MITETgOKkHiJkZB4w4ghEsrKhQ2Rh_kZwBWv4JTCUIHELppJ5nzn_GdmisjImRTpqEBPPMoMumuRA4fYmGnyyxPHtQwrT5irjds9UWvOBhejKJoNqpsC4K8QNCD42NxyqGkVthBBH4IB8K78Y5bsr8XsZLPKV9dG348_LxK4FVcN8G-A1xJISaR8nrWUikpZhF8SAD4ELhd98DvgS_gdeA-Cdpzvd0W5Dbyu7OYWcXJqPl1LATXg1ZVjPM498EtxHoHfXEyUQrc4pdDwedqqb4UWTZRahPVRVIEzf_J5PX56mLdadZgO71S6KrA6un-Z9BmuXcKf7qFySi4h6Z6eatrqTN4izFAG2dSxiWXK91WMUzByD6lNMdLl0iTOEUaYlaSOeG5u75QZSHcdj2aQlzeJu3yLSN8nxwVa-gUEuG-Q?type=png)

---

## なぜRQを選んだのか

**ドキュメント見ていたら利用しやすいシンプルさが良かった**

* asyncioと悩んだ -> RQがシンプルにできそうだった
* celeryと悩んだ -> celeryを使うほどの規模ではなかったと思う

※I/Oバウンズ処理はasyncio, multiprocessingは制限にならないので、
この選択肢がベストとは限らない（速度とか）  

※redisの扱いに慣れたくて使いたかったという意味も😆

<!-- _footer: バウンドとは制限という意味 -->

---

ということで、ちょっぱやでDocckerで用意する場合の例

参考: [Python で分散タスクキュー (RQ 編) #Python - Qiita](https://qiita.com/hoto17296/items/39597f6e26c0186a6e1b) @[hoto17296](https://twitter.com/hoto17296)

---

Dockerfile

```Dockerfile
FROM python:3.11
RUN pip install rq
```

---

compose.yml

```yml
version: '3'
services:
  redis:
    image: redis
  worker:
    build: .
    depends_on:
      - redis
    environment:
      RQ_REDIS_URL: redis://redis
    command: rq worker
    volumes:
      - .:/app
    working_dir: /app
  app:
    build: .
    depends_on:
      - redis
      - worker
    environment:
      RQ_REDIS_URL: redis://redis
    command: python app.py
    volumes:
      - .:/app
    working_dir: /app
```

---

## 簡単なサンプル: ファイル操作をしてみる

tasks.py

```python
import logging

logger = logging.getLogger(__name__)

# ファイル操作: ランダムな文字列をファイルに書き込む？

def add(a, b):
    logger.debug("{} + {} = {}".format(a, b, a + b))
    return a + b
```

---

app.py
  
```python
import os
from time import sleep
import redis
from rq import Queue
from tasks import add

q = Queue(connection=redis.from_url(os.environ.get("RQ_REDIS_URL")))

# 10個のタスクの実行をキューに投げる
tasks = [q.enqueue(add, args=(i, 1)) for i in range(10)]

# タスク実行が完了するまで少し待つ
sleep(1)

# 結果を出力する
print([task.result for task in tasks])
```

---

## 実行

```bash
# シングルワーカー
$ docker-compose up

# マルチワーカー: 4つのワーカーを起動
$ docker-compose up --scale worker=4
## ログは別途ファイルでみせます
```

---

## dockerで動かす時

* [RQはredis（キュー）へタスクを渡すときはpickleを使ってる](https://python-rq.org/docs/#:~:text=Lastly%2C%20it%20does%20not%20speak%20a%20portable%20protocol%2C%20since%20it%20depends%20on%20pickle%20to%20serialize%20the%20jobs%2C%20so%20it%E2%80%99s%20a%20Python%2Donly%20system.)
  * ワーカー側でもpickleで渡されたオブジェクトが理解できないといけない
  -> ワーカー側にも同じライブラリをインストールする必要がある
* 手っ取り早い方法として
  * タスク側もワーカー側も同じ環境=Dockerfileを使う
  * コード参照や利用するボリュームも同じ箇所を参照すると楽
* タスクとワーカーを同時に動かすならcomposeが便利

---

## まとめ

* 膨大な~~退屈なこと~~手作業は間違えるので自動化しよう
* 自動化は重い処理をよく扱う->非同期前提で考える
* 非同期タスクキューを使うことで、重い処理を任せられ
  自動化の幅や連携方法が広がる（はず

Google Chatアプリの話はまたどこかで〜

---

## 参考

* [メッセージキュー - Wikipedia](https://ja.wikipedia.org/wiki/%E3%83%A1%E3%83%83%E3%82%BB%E3%83%BC%E3%82%B8%E3%82%AD%E3%83%A5%E3%83%BC)
* [python-rq](https://python-rq.org/)
* [【Pythonで高速化】I / Oバウンドとか並列処理とかマルチプロセスとかってなんぞや #Python - Qiita](https://qiita.com/nyax/items/659b07cd755f2ced563f)
* docker利用時の参考: [Python で分散タスクキュー (RQ 編) #Python - Qiita](https://qiita.com/hoto17296/items/39597f6e26c0186a6e1b)
* [Python3.12で新たにサポートされたsub-interpretersの紹介 | gihyo.jp](https://gihyo.jp/article/2023/11/monthly-python-2311)

サンプルコード
<https://github.com/hrsano645/exam-python-rq-by-docker>

---

## Google Chatと合わせる時

* チャットボット側で操作をする -> タスクをキューに入れる
* チャットボット側に応答をする
* ワーカー側でタスクを実行する
* ワーカー側でチャット側に非同期で応答を返す
  * Google ChatならGoogle Chat REST APIで非同期応答できる

---
