---
marp: true
header: "**M1 MacでPythonと機械学習をやろう** "
footer: "by [@hrs_sano645](https://twitter.com/hrs_sano645)"
---

# M1 MacでPythonと機械学習をやろう

### Unagi.py 勉強会37枚目～【祝4周年】機械学習・データサイエンスLT会～

2020/11/20 Hiroshi Sano

---

# お前誰よ

- Hiroshi Sano [@hrs_sano645](https://twitter.com/hrs_sano645) 🏠:静岡の🗻見えるところ
- Job💼
  - [佐野設計事務所🚗⚙️📏](https://sano-design.info)::自動車系機械の3D設計事務所
  - 米農家🌾
- Community🧑‍💻
  - 🗻🐍: shizuoka.py, unagi.py, Python駿河
  - 🗻🐍: PyCon mini Shizuokaスタッフ
  - 🐍: PyCon JP 2020 チュートリアル講師

---

# M1 Macbook Air買いました🎉

---

おススメ！
今日は~~自慢~~布教しに来ました。

---

# まとめ

- M1 Macめちゃくちゃ快適
- Python使うならrossetaモードが基本的におすすめ
- M1最適化のTensorflowを試してみた

---

# M1 Macめちゃくちゃ快適です

---

# M1 Macめちゃくちゃ快適です

買ったもの

- M1 Macbook Air: 124,800円
- CPU 8core / GPU 7 Core
- 256GB: そんなに入れるものがなければ十分
  - 必要なら外付けSSD: 1TB1万円ぐらいで買える
- メモリ 16GB: 8GB

---

# M1 Mac快適なこと一覧

- Macbook Airはファンレス。他のものも通常はファン回らない
- 4K動画流していても平然としてる
- よく使うアプリはほぼ動く: chrome, vscode, office, などなど

---



---

気になったら今すぐ買おう！💸

(mac miniはもっと安いので、そっちもおすすめ)

---

# M1 Macめちゃくちゃ快t...

冬場は冷えたアルミの板

---

# Python使うならrossetaモード

---

macOS BugSurにはPythonは標準で入ってない

---

XCode or Command line tools 必須

---

Command line toolsを入れることでPython3.8のUniversal版が入ります

---

## Universal版とは

- M1 Macはarmとintelの両方が動く
  - armはnative
  - intelはrosseta2（というバイナリトランスレーター）
- armとrosseta両方対応のバイナリをUnivseral Binaryと呼ぶ

両方動くので、両方確認する方法もある。

---



---

# PythonのApple Siricon対応

- Appleからは、Pyhton3.8のUniversal版が提供
- Python.orgからはPython3.9(3.9.1)でUniveral版提供済み

---

# そのPythonどうやって動いてるの？

---

# ArmのPythonって使える？

---


# ArmのPythonって使える？

- 標準では至って普通に動く

- venvも普通に動く。Pure Pyhtonなら問題ない（と思われる
- pipが問題


---

# pipがmacos armに対応してない

- そもそもアーキテクチャに乗ってないので、wheelが作れない
- 依存関係でちょっとでも引っかかると色々面倒（手動で解決しないといけない）

[Python 3.9.1の macOS Big Sur/Apple Siliconサポート - python.jp](https://www.python.jp/news/2020-12-07-macos-bigsur.html)

[pip 20.3 release (Q4 2020) · Issue #8936 · pypa/pip](https://github.com/pypa/pip/issues/8936#issuecomment-735450632)

---

# 現時点だとM1 MacでArmネイティブのPythonの常用は難しい

---

# Rossetaだとどうなの？

- 至って普通に動く。venv, pip などなど
- ただpipは最新版にする必要あり:
  - 正しくバイナリ判定がされなくてソースビルドが走ることが多々
  - pipの最新: pip-20.3.3
  - `pip install -U pip` これ絶対
- 性能はrosseta依存: GPUとかの扱いよくわからん

Web開発ぐらいなら問題なく使えると思います。

---

# Rossetaだとどうなの？

（やっていて気がついたこと

- 現時点でpandasをpipenvで入れるとpip lockがちゃんとできない
  - 今のところ、素直にvenv, pipを使ったほうがいいと思う

---

# rossetaでpyhtonのベンチマーク

提供: o-ishiさん

比較対象は

- Ryzen 5800X / メモリ32GB
- python3.8.2

---

# rossetaでpyhtonのベンチマーク 結果


---

気になったら今すぐ買おう！💸

---

# M1最適化のTensorflowを試してみた

---

# tensorflow-macosがある

- Appleが専用のビルドをしたものを公開
  - 
- numpyもビルドずみ: armネイティブでビルドさせようとしてもできなかった
- pandasは入ってないらしい。


---

からあげ先生のAI本のコードを試す

---



---

# まとめ

- M1 Macめちゃくちゃ快適
- Python使うならrossetaモードが基本的におすすめ
- M1最適化のTensorflowを試してみた

---

気になったら今すぐ買おう！💸

ただ冬場は冷たいです
