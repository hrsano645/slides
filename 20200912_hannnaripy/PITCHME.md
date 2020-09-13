### pathlibを推してみようと思う

#### はんなりPython #32 標準ライブラリなLT会

#### 2020/09/13 Hiroshi Sano

---

## お前誰よ

佐野浩士（Hiroshi Sano）[@hrs_sano645](https://twitter.com/hrs_sano645)
静岡県の富士市在住🗻

[佐野設計事務所🚗](https://sano-design.info) IT何でも屋
米農家です🌾

静岡のPythonコミュニティに参加
- shizuoka.py, unagi.py, Python駿河
- PyCon mini Shizuokaスタッフ

---

### 推しライブラリ

## pathlib

https://docs.python.org/ja/3/library/pathlib.html

---

### os.pathの置き換えが出来そうなもの

---

#### os.pathは昔からある（1系から）

https://docs.python.org/ja/3/library/os.path.html

---

昔からお世話になっていたけど、不満点

---

OSごとに扱いを変える必要がある

---

- 統一したAPIにしたい（難しいところはあるけど）

---

### そこでpathlib

- 3.4から使える
- Pathオブジェクトとして操作する
- os.path, globといったパスを扱うライブラリをこれ1つで対応できる

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
>>> str(posix_kugiri)
'~\\Documents\\hellopathlib.txt'
```

---

### API的に統一感がある

- UnixとWinとほぼ同じ用につかえる
- os.pathだと

---

- スラッシュの演算子をパスのジョインにつかえる。これがいい

---

- globとかもある。

---

- 注意点

---

- 一部のライブラリだと、pathオブジェクトを扱えない（文字列としてパスをとる場合）str関数に通すとパスを文字列で生成してくれる

---

### まとめ

---

- ほとんど悩むことがないので、python3.4以降で使うならもうpathlibで良し！

