---
marp: true
header: "**Python-Pelicanで楽々Webサイトを作ろう** - Start Python Club LT 2021/02/10"
footer: "by [@hrs_sano645](https://twitter.com/hrs_sano645)"
paginate: true
---

### Python-Pelicanで楽々Webサイトを作ろう

Start Python Club 2021/02/10

Hiroshi Sano

---
## お前誰よ

- Hiroshi Sano [@hrs_sano645](https://twitter.com/hrs_sano645) 🏠:静岡の🗻見えるところ
- Job💼
  - [佐野設計事務所🚗⚙️📏](https://sano-design.info): 自動車系機械の3D設計事務所
  - 米農家🌾
- Community🧑‍💻
  - 🗻🐍: shizuoka.py, unagi.py, Python駿河
  - 🗻🐍: PyCon mini Shizuokaスタッフ
  - 🐍: PyCon JP 2020 チュートリアル講師

---

静岡Pythonコミュニティの勉強会 Python駿河は 2/27（土）です！

「Pythonプロフェッショナルプログラミング 第3版 Chapter 05 課題管理とレビュー」

つまみ食い読書します。ぜひ遊びに来てください！

参加方法はconnpass検索か後で#stapyに流します

---

本日は

---

（宣伝と）Python-Pelicanをおすすめしに来ました

---

### Python-Pelicanとは

っ https://docs.getpelican.com/

- Static Site Generator:静的サイトジェネレーター
  - JekyllとかHugoとかと同じもの
- ブログやサイト作成ができます
- テーマ / プラグイン対応
- GitHub Pages, AWS S3 などなどにもアップ可能

---

ちょっとしたサイトを作るには便利です

---

Python駿河のサイト -> http://py-suruga.github.io

PyCon mini Shizuokaのサイト -> https://shizuoka.pycon.jp

この2つともPelicanで作ってます。

---

### 使い方

---

```
pip install pelican markdown
pelican-quickstart # 色々聞かれます。
git init #git管理すると便利です。
```

詳しくはドキュメントを見てね

https://docs.getpelican.com/en/latest/quickstart.html

---

### ブログを作ってみる

標準だと contentフォルダを作って、そこに入れます

```
[pelican-project]/content/firstpost.md #これを作成して作業
```

firstpost.md

```
Title: My First Post
Date: 2021-02-10 21:00
Category: 日記

最初の投稿です。
```
---

サイトを生成

```
pelican content

# unixならmakeコマンド使える
make publish
```
---

サイトの生成テスト

```
pelican content
pelican --listen

# unixならmakeコマンド使える
make devserver
```

http://127.0.0.1:8000 で確認できます。

---

実例見せます（生成したものを）

---

GitHub Pagesへアップしてみる

---

GitHub Pagesを使うとあっという間にサイト作れる

---

[githubのユーザー名].github.io というリポジトリを作ると

ユーザー名のGitHub Pagesが作れます（これをユーザーサイトという）

詳しくはGitHubのヘルプで -> [GitHub Pages について - GitHub Docs](https://docs.github.com/ja/github/working-with-github-pages/about-github-pages)

---

あとはGitHubへコンテンツをpushすればいい

---

あっという間にサイトが作れるはずなんですが

---

ちょっと手順多い

---

（手順とブランチ名は一例）

- pelicanプロジェクトを`main`ブランチで管理
- `make publish`で公開向けのサイトを生成 => `output`フォルダができる
- `output`フォルダをコピーして一時退避
- `gh-pages`ブランチを作って、git switch
- outputの中身をそこに入れる -> git add & git commit 
- GitHubのリポジトリの Settings>GitHub Pages で gh-pages/root で公開する

---

同じリポジトリでブログの管理をしているので操作多めで面倒

（もちろん、プロジェクトのリポジトリとPages用のリポジトリを分けてもいいけど本質変わらない）

---

手順多いので、これを自動化したい

---


GitHub Actionsとセットで使う

---

### GitHub Actionsとセットで使う

- GitHub Pagesの設定をする
- mainブランチへpush
- 設定したワークフロー自動的にビルドしてgh-pagesブランチを生成
  - Pyhtonのセットアップとpelicanのビルドを行ってgh-pagesへpushさせる

---

ワークフローは、こちらを参考にしてもらえるといいと思います

[pycon-mini-shizuoka.github.io/deploy.yml at master · pycon-mini-shizuoka/pycon-mini-shizuoka.github.io](https://github.com/pycon-mini-shizuoka/pycon-mini-shizuoka.github.io/blob/master/.github/workflows/deploy.yml)

---

### まとめ

---

Pythonでサイトやブログを速攻で作りたいならPython-Pelicanがおすすめです

---

GitHub Pages使えば無償で作れます

---

Pelican + GitHub Acitonsで楽々サイト作成しましょう！

---

EOL... Thanks!