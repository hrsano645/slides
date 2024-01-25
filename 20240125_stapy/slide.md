---
marp: true
paginate: true
---


# 非同期タスクキューを使って業務効率化した話

みんなのPython勉強会#100
2024-01-25  

@hrs_sano645

---

## みんなのPython勉強会#100 おめでとうございます🎉👏🥳

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

![bg](../images/sano-design_info.png)

<!-- 

* 株式会社佐野設計事務所は自動車プレス金型という機械を3D CADで設計する事務所です。他業種製品の3Dモデリング等やっております
* 普段扱うデータはほぼデジタルデータです、Pythonでデータを元にクラウドサービスを組み合わせて業務改善し、製造業のニッチな分野のDXも推進してます。
-->

---

## 2023年の社内個人的目標: 業務効率化を限界まで進める

---

## 効率化する理由

* とある依頼ベースの案件業務
* 今まではそれほど多くなかったが、**年を跨いで急激に増える**
  * 人力でやっていては**追いつかなそう**。やばい
* 人間が必要な部分以外、**あらゆる手作業を止める！** → **成功した🎉**

---

## どんなことを効率化？

* **手作業していたこと自動化**
  * 依頼受注（メール）→ボイラープレートツールで作業プロジェクト
    フォルダーを生成
  * Googleスプレッドシート連携して案件管理
  * 会計サービスと連携して見積書/請求書生成（書類作成）
  * 依頼企業側のシステム連携: WEBスクレイピング
* **自動処理の実行をChatOpsで**
  * 処理を動かしていいか確認した上で実行させる
  * Google Chatでチャットボット作成
  * **スマホから実行もできる**

---

## 究極には指一本で仕事をしたい

![w:500px](../images/illust_1.png)

---

## 業務タスク自動化サービスの構成

![w:800px](https://docs.google.com/drawings/d/e/2PACX-1vRxi-CGrIr6lu1K4wroeMLzybS4htY3PNTZCq3mxcXidHcejks1liceIsuXuCTrsiWORufyDXyKa7ZB/pub?w=900&amp;h=560)

---

**「非同期タスクキュー」** を使って作業させています

非同期で動かすため + 処理をまとめたタスクを + キューに入れて実行させる

<!-- _footer: キューは待ち行列の意味です。行列に並べて実行させます -->

---

## なんでタスクキューを使う？

* 自動処理→重い処理だった
  * ファイル操作、APIアクセス -> I/Oバウンド処理
  * 組み合わせると**数秒ではなく数十秒〜分単位**の処理
  * 結果が返ってくるタイミングはその時次第
* **チャットボットの仕様->素早く応答しないといけない**
  * チャット側がすぐにボット側に応答を求める
  * チャットボットは非同期前提

<!-- _footer: バウンドとは制限という意味 -->

---

Google Chatの場合

> 「同期的に応答するには、Chat アプリが 30 秒以内に応答し、その応答をインタラクションが発生したスペースに投稿する必要があります。それ以外の場合は、Chat アプリは非同期で応答できます。」
> <https://developers.google.com/chat/api/guides/message-formats?hl=ja#sync-response>

（[Slackの3秒](https://api.slack.com/interactivity/slash-commands#responding_basic_receipt:~:text=This%20confirmation%20must,ignore%20the%20request.)よりも全然緩いけど、非同期前提な様子）

---

## RQ(python-rq)を使いました

python-rq: <https://python-rq.org/>

以下の3つの要素で構成される

* アプリ: タスク発行→キューへ入れる→ワーカーから処理結果を受け取る
* ワーカー: タスクの処理を行う
* redis: アプリとワーカーの間に入りキューとして利用する

---

## RQのざっくりイメージ
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

**ドキュメント見ていたら簡単に見えて良かった**

* celeryと悩んだ -> celeryを使うほどの規模ではなかった
* asyncioと悩んだ -> **RQがシンプルだった**

※I/Oバウンズ処理はasyncio, multiprocessingは制限にならないので、
この選択肢がベストとは限らない（速度とか）  

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

## ファイル操作をしてみる

tasks.py

```python
from pathlib import Path
import random
import string
import sys


def create_random_string(length):
    """指定された長さのランダムな文字列を生成する関数"""
    letters = string.ascii_letters + string.digits
    return "".join(random.choice(letters) for i in range(length))


def create_files(num_files, file_size, directory="test_files"):
    """指定された数とサイズのファイルを生成する関数"""
    Path(directory).mkdir(parents=True, exist_ok=True)

    for i in range(num_files):
        savefile = Path(f"{directory}/file_{i}.txt")
        with savefile.open("w") as f:
            f.write(create_random_string(file_size))
```

---

app.py
  
```python
import os
import redis
from rq import Queue
from tasks import create_files


NUM_FILES = 100
FILE_SIZE = 1048576
NUM_TASKS = 3

q = Queue(connection=redis.from_url(os.environ.get("RQ_REDIS_URL")))

# タスクの実行をキューに投げる
tasks = [
    q.enqueue(create_files, args=(NUM_FILES, FILE_SIZE, f"test_files_{i}"))
    for i in range(NUM_TASKS)
]
```

---

## 実行

```bash
# シングルワーカー
$ docker compose up

# マルチワーカー: 3つのワーカーを起動
$ docker compose up --scale worker=3
## ログは別途ファイルでみせます
```

---

## ワーカーのログ: シングルワーカー

1つのワーカーにタスクが順番に渡されて実行される

```bash
file_task-worker-1  | 03:20:35 Worker rq:worker:81027d039a944dc3b8a230519243f68e started with PID 1, version 1.15.1
file_task-worker-1  | 03:20:35 Subscribing to channel rq:pubsub:81027d039a944dc3b8a230519243f68e
file_task-worker-1  | 03:20:35 *** Listening on default...
file_task-worker-1  | 03:20:35 default: tasks.create_files(50, 1048576, 'test_files_0') (f18592d2-16ba-4c82-98ef-11da85c44493)
file_task-app-1 exited with code 0
file_task-worker-1  | 03:20:52 default: Job OK (f18592d2-16ba-4c82-98ef-11da85c44493)
file_task-worker-1  | 03:20:52 Result is kept for 500 seconds
file_task-worker-1  | 03:20:52 default: tasks.create_files(50, 1048576, 'test_files_1') (9f4a596f-73af-4973-9007-af03da8f5057)
file_task-worker-1  | 03:21:09 default: Job OK (9f4a596f-73af-4973-9007-af03da8f5057)
file_task-worker-1  | 03:21:09 Result is kept for 500 seconds
file_task-worker-1  | 03:21:09 default: tasks.create_files(50, 1048576, 'test_files_2') (bf5c15ad-3222-45be-ab8a-3f214a57700d)
file_task-worker-1  | 03:21:27 default: Job OK (bf5c15ad-3222-45be-ab8a-3f214a57700d)
file_task-worker-1  | 03:21:27 Result is kept for 500 seconds
```

---

## ワーカーのログ: マルチワーカー

3つそれぞれが並列に動いて実行される

```bash
file_task-worker-3  | 03:19:26 Worker rq:worker:a3fae5de17c34f658f597ce4d5543dbc started with PID 1, version 1.15.1
file_task-worker-3  | 03:19:26 Subscribing to channel rq:pubsub:a3fae5de17c34f658f597ce4d5543dbc
file_task-worker-3  | 03:19:26 *** Listening on default...
file_task-worker-3  | 03:19:26 Cleaning registries for queue: default
file_task-worker-3  | StartedJobRegistry cleanup: Moving job to FailedJobRegistry (due to AbandonedJobError)
file_task-worker-3  | StartedJobRegistry cleanup: Moving job to FailedJobRegistry (due to AbandonedJobError)
file_task-worker-3  | StartedJobRegistry cleanup: Moving job to FailedJobRegistry (due to AbandonedJobError)
file_task-worker-2  | 03:19:26 Worker rq:worker:3f33ea404d2040e99961f0a2d5d46b1f started with PID 1, version 1.15.1
file_task-worker-2  | 03:19:26 Subscribing to channel rq:pubsub:3f33ea404d2040e99961f0a2d5d46b1f
file_task-worker-2  | 03:19:26 *** Listening on default...
file_task-worker-1  | 03:19:26 Worker rq:worker:32c4d2c46a944ba3b05dcb295cc522c2 started with PID 1, version 1.15.1
file_task-worker-1  | 03:19:26 Subscribing to channel rq:pubsub:32c4d2c46a944ba3b05dcb295cc522c2
file_task-worker-1  | 03:19:26 *** Listening on default...
file_task-worker-3  | 03:19:27 default: tasks.create_files(50, 1048576, 'test_files_0') (a2767c5e-2caa-47ed-b8f2-204881f671ac)
file_task-worker-2  | 03:19:27 default: tasks.create_files(50, 1048576, 'test_files_1') (288a07b9-80eb-4736-9e1c-56887781babe)
file_task-worker-1  | 03:19:27 default: tasks.create_files(50, 1048576, 'test_files_2') (49f43d8d-b0c2-4edb-a4b3-711852102a9f)
file_task-app-1 exited with code 0
file_task-worker-2  | 03:19:44 default: Job OK (288a07b9-80eb-4736-9e1c-56887781babe)
file_task-worker-2  | 03:19:44 Result is kept for 500 seconds
file_task-worker-1  | 03:19:44 default: Job OK (49f43d8d-b0c2-4edb-a4b3-711852102a9f)
file_task-worker-1  | 03:19:44 Result is kept for 500 seconds
file_task-worker-3  | 03:19:44 default: Job OK (a2767c5e-2caa-47ed-b8f2-204881f671ac)
file_task-worker-3  | 03:19:44 Result is kept for 500 seconds
```

---

## dockerで動かす時

* 手っ取り早い方法として**タスク側もワーカー側も同じ環境=Dockerfileを使う**
* [RQはredis（キュー）へタスクを渡すときはpickleを使ってる](https://python-rq.org/docs/#:~:text=Lastly%2C%20it%20does%20not%20speak%20a%20portable%20protocol%2C%20since%20it%20depends%20on%20pickle%20to%20serialize%20the%20jobs%2C%20so%20it%E2%80%99s%20a%20Python%2Donly%20system.)
  * ワーカー側でもpickleで渡されたオブジェクトが理解できないといけない
  -> ワーカー側にも同じライブラリをインストールする必要がある
* タスクとワーカーを同時に動かすならcomposeが便利
* コード参照や利用するボリュームも同じ箇所を参照すると楽

---

## まとめ

* **膨大な手作業は間違えるので自動化しよう**
* 自動化は重い処理をよく扱う -> 非同期前提で考える
  * **外部サービス連携、チャットボット、LLMのAPIとの連携も**
* 非同期タスクキューを使うことで、重い処理を任せられ、
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
