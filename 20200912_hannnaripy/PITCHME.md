### pathlibを推してみようと思う

#### はんなりPython #32 標準ライブラリなLT会

#### 2020/09/13 Hiroshi Sano

---

## お前誰よ

- 佐野浩士（Hiroshi Sano）[@hrs_sano645](https://twitter.com/hrs_sano645)
- 静岡県の富士市在住🗻

- 💼
    - [佐野設計事務所🚗](https://sano-design.info) IT何でも屋
    - 米農家🌾

- コミュニティ
    - shizuoka.py, unagi.py, Python駿河
    - PyCon mini Shizuokaスタッフ

---

### 推しライブラリ

## pathlib

https://docs.python.org/ja/3/library/pathlib.html

---

### os.pathの置き換え

---

#### os.pathは昔からある（1系から）

https://docs.python.org/ja/3/library/os.path.html

---

昔からお世話になっていたけど、不満点

---

OSごとに扱いを変える必要がある

- とくに区切り文字！
  - Winだと `\\` , Unixだと `/`
  - ハードコードすると結構トラブル起こしがち
- osモジュールはOSの操作でその一部
  - ファイル操作をするときに
- os.pathと書いて操作するとコードが汚い

---

区切り文字混ぜるな危険

```python
# Ubuntu 18.04です
>>> import os.path
>>> os.path.abspath("\\Documents\\test")
'/home/hiroshi/Documents/\\Documents\\test'
```

---

パス操作をするときにjoinすると面倒だよね

```python
>>> os.path.join(os.path.abspath("\\Document"), "test")
'/home/hiroshi/Documents/\\Document/test'
```

---

### そこでpathlib

- Python3.4から使える
- Pathオブジェクトとして操作 -> 統一性がある
- os, os.path, globといったパスを扱うライブラリをこれ1つで対応できる

---

### pathlibのいいところ

---

### オブジェクトとして管理

```python
# Windowdでやってる
>>> form pathlib import path
>>> p = Path("~/Documents/hellopathlib.txt")
>>> p
WindowsPath('~/Documents/hellopathlib.txt')
```

---

### パス区切り文字をどちらでもいい

```python
# winの区切り文字も対応
>>> win_kugiri =  Path("~\\Documents\\hellopathlib.txt")
>>> win_kugiri
WindowsPath('~/Documents/hellopathlib.txt')

>>> posix_kugiri =  Path("~/Documents/hellopathlib.txt")
>>> posix_kugiri
WindowsPath('~/Documents/hellopathlib.txt')

```

---

### str関数に通すと文字列としてとれる

```python
>>> str(win_kugiri)
'~\\Documents\\hellopathlib.txt'
```

---

### API的に統一感がある

os.pathはパスを扱うことがメインだけどファイルへのアクセスは別

- os.mkdirとかありますよね -> osモジュール
- 検索のときにglobモジュール使いますよね
- 組み込みのopen関数

---

pathlibはファイル操作もできる

- Path.mkdirができる
- globもできる -> Path.glob, Path.rglob（再帰検索専用）
- Path.openメソッドが使える（openとほぼ変わりはないですが）

---

### osモジュールとの対応表

[os モジュールにあるツールとの対応付け](https://docs.python.org/ja/3/library/pathlib.html#correspondence-to-tools-in-the-os-module)

---

スラッシュの演算子をパスのジョインにつかえる

これがとてもいい

```python
>>> from pathlib import Path
>>> Path.home()
WindowsPath('C:/Users/hiroshi')
>>> Path.home() / "Documents"
WindowsPath('C:/Users/hiroshi/Documents')
>>> home_docsdir = Path.home() / "Documents"
>>> home_docsdir.is_dir()
True
```

---

### パスにまつわる操作系はほぼ全部pathlibからできる

---

### 注意点

---

古めのライブラリだとPathオブジェクトを扱えない（文字列としてパスをとる場合）

str関数に通すとパスを文字列で生成してくれる

```python
# os.pathは文字列を生成する
>>> type(os.path.abspath("\\Documents"))
<class 'str'>
>>> type(home_docs)
<class 'pathlib.WindowsPath'>
>>> str(home_docs)
'C:\\Users\\hiroshi\\Documents'
>>> type(str(home_docs))
<class 'str'>
>>>
```

---

### まとめ

---

pathlibは操作も統一性があるので悩むことがないです

Python3.4以降でパス操作するならpathlibを使いましょう💪
