# Python入門

## 概要

1. [AIZU ONLINE JADGE プログラミング入門コース][1] の問題を抽出したものを課題として、その解答をレビューする形式で進める。
2. 最も正しい情報は公式ドキュメントだが内容が難しいため、公式ドキュメントの内容を分かりやすく説明している参考記事を参照することもおすすめである。
* 公式ドキュメント
  - [Python チュートリアル][2]
  - [Python 標準ライブラリ][3]
* 参考記事
  - [Pythonに関する情報 | note.nkmk.me][4]
  - [Chainer チュートリアル][5]

[1]: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all
[2]: https://docs.python.org/ja/3.9/tutorial/index.html
[3]: https://docs.python.org/ja/3/library/index.html
[4]: https://note.nkmk.me/python/
[5]: https://tutorials.chainer.org/ja/tutorial.html


## 課題の進め方

1. 個人でリポジトリを作成する。
1. 作成したリポジトリをクローンする。
1. 課題を解く。<br>
  3.1. 作業ブランチを作成して移動する。ブランチ名は `<topic number>` とする。ex: `topic-1` .<br>
  3.2. 公式ドキュメントや参考資料を読む。<br>
  3.3. AIZU ONLINE JUDGE (以下、AOJ) の問題文を読む。<br>
  3.4. 解答を `AOJ` ディレクトリ内の該当するファイルに作成する。<br>
  3.5. AOJの判定が [`AC`][6] となったら次へ進む。<br>
1. 提出する。提出は A, B, C, D のように問題ごとにするのではなく、1, 2, ... のようにトピックごとにする。<br>
  4.1. ブランチ `<topic number>` からブランチ `main` に向けてプルリクエストを作成する。<br>
  4.2. プルリクエストのステータスが ❌ だった場合、コーディングスタイルを修正して再提出する。<br>
  4.3. #dev_data_python でレビュワーに(プルリクエストのリンクと一緒に) メンションする。<br>
  ※メンションを見落としてしまうことがあるので、2日以上返信がなかったらもう一度メンションしてください。
1. レビュワーの行動<br>
  5.1. レビュワーは `Files changed` タブでレビューを行い、修正依頼を出す。<br>
  5.2. レビューが通ったら `<topic number>` を `main` にマージする。

## 質問
質問がある場合は [Question Template][7] の形式に従ってイシューを作成する。
[記入例 #1][8]。
この時、コードに以下のようにシンタックスハイライトが効いているかに注意すること。

```python
def f(a=1):
    pass
```


[6]: https://onlinejudge.u-aizu.ac.jp/judges_replies
[7]: https://github.com/shinonome-inc/Basic-Python/issues/new/choose
[8]: https://github.com/shinonome-inc/Basic-Python/issues/1


## 課題
[AIZU ONLINE JADGE プログラミング入門コース][1]

<details>
<summary>1. 入門</summary>

### flake8をインストールしてください！！

### 課題
- 1_A
- 1_B
- 1_C
- 1_D

### Pythonチュートリアル
* [3.1.1. 数](https://docs.python.org/ja/3/tutorial/introduction.html#numbers) 
* [7.1. 出力を見やすくフォーマットする](https://docs.python.org/ja/3/tutorial/inputoutput.html#fancier-output-formatting) 
* [4.8. 間奏曲: コーディングスタイル](https://docs.python.org/ja/3/tutorial/controlflow.html#intermezzo-coding-style) 

### 参考
* [【Python】競技プログラミング 基本入力まとめ - Qiita](https://qiita.com/ell/items/1f519aff0cdc3cf16284)
* [Pythonのf文字列（フォーマット済み文字列リテラル）の使い方 | note.nkmk.me](https://note.nkmk.me/python-f-strings/)
* [Pyhtonの算術演算子（四則演算、べき乗、リスト・文字列の結合など） | note.nkmk.me](https://note.nkmk.me/python-arithmetic-operator/)
* [Pythonでタプルやリストをアンパック（複数の変数に展開して代入） | note.nkmk.me](https://note.nkmk.me/python-tuple-list-unpack/)
- [Flake8 Rules](https://lintlyci.github.io/Flake8Rules/)

### 備考
* 早めにコーディングスタイルを身につけて欲しい。
</details>

<details>
<summary>2. 条件分岐</summary>

### 課題
- 2_A
- 2_B
- 2_C
- 2_D

### Pythonチュートリアル
* [4.1. if 文](https://docs.python.org/ja/3/tutorial/controlflow.html#if-statements) 

### 参考
* [Pythonのif文による条件分岐の書き方 | note.nkmk.me](https://note.nkmk.me/python-if-elif-else/)
</details>

<details>
<summary>3. 繰り返し処理</summary>

### 課題
- 3_A
- 3_B
- 3_C
- 3_D

### Pythonチュートリアル
* [4.2. for 文](https://docs.python.org/ja/3/tutorial/controlflow.html#for-statements) 
* [4.3. range() 関数](https://docs.python.org/ja/3/tutorial/controlflow.html#the-range-function)
* [4.4. break 文と continue 文とループの else 節](https://docs.python.org/ja/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
* [5.6. ループのテクニック](https://docs.python.org/ja/3/tutorial/datastructures.html#looping-techniques) 
### 参考
* [Pythonのfor文によるループ処理（range, enumerate, zipなど） | note.nkmk.me](https://note.nkmk.me/python-for-usage/)
### 備考
* while文の使用はなるべく避けて欲しい。
* AOJは一般的な競プロとは異なり、繰り返し文内で逐次的に結果を出力しても正解となる。
</details>

<details>
<summary>4. 計算</summary>

### この章の計算部分は関数を使って実装してください。（関数の例：半径を受け取って円の面積を返す）
### 関数は自分で実装したものではなく、組み込み関数でもOKです。

### 課題
- 4_A
- 4_B
- 4_C
- 4_D

### Pythonチュートリアル
- [数値と数学モジュール — Python 3.8.2 ドキュメント](https://docs.python.org/ja/3/library/numeric.html)
* [4.6. 関数を定義する](https://docs.python.org/ja/3/tutorial/controlflow.html#defining-functions) 
* [組み込み関数 — Python 3.8.2 ドキュメント](https://docs.python.org/ja/3/library/functions.html)
### 参考
* [Pythonの組み込み関数と標準ライブラリ、サードパーティライブラリ | note.nkmk.me](https://note.nkmk.me/python-built-in-standard-library-third-pary-library/)
* [Pythonで関数を定義・呼び出し（def, return） | note.nkmk.me](https://note.nkmk.me/python-function-def-return/)
</details>

<details>
<summary>5. 構造化プログラムI</summary>

### 課題
- なし
</details>

<details>
<summary>6. 配列</summary>

### 課題
- 6_A
- 6_B
- 6_C
### Pythonチュートリアル
- [5. データ構造 — Python 3.8.2 ドキュメント](https://docs.python.org/ja/3/tutorial/datastructures.html)
### 参考
- [Pythonのスライスによるリストや文字列の部分選択・代入 | note.nkmk.me](https://note.nkmk.me/python-slice-usage/)
- [リストに関する情報 | note.nkmk.me](https://note.nkmk.me/list/)
</details>

<details>
<summary>7. 構造化プログラムⅡ</summary>

### 課題
- 7_B
### Pythonチュートリアル
- [itertools — 効率的なループ実行のためのイテレータ生成関数 — Python 3.8.2 ドキュメント](https://docs.python.org/ja/3/library/itertools.html)
### 参考
- [Pythonで階乗、順列・組み合わせを計算、生成 | note.nkmk.me](https://note.nkmk.me/python-math-factorial-permutations-combinations/)
</details>

<details>
<summary>8. 文字</summary>

### 課題
- 8_B
- 8_C
- 8_D
### Pythonチュートリアル
なし
### 参考
- [Pythonで文字列を置換（replace, translate, re.sub, re.subn） | note.nkmk.me](https://note.nkmk.me/python-str-replace-translate-re-sub/)
- [PythonのCounterでリストの各要素の出現個数をカウント | note.nkmk.me](https://note.nkmk.me/python-collections-counter/)
- [Pythonのin演算子でリストなどに特定の要素が含まれるか判定 | note.nkmk.me](https://note.nkmk.me/python-in-basic/)
</details>

<details>
<summary>9. 文字列</summary>

### 課題
- なし
</details>

<details>
<summary>10. 数学関数</summary>

### 課題
- なし
</details>

<details>
<summary>11. 構造体とクラス</summary>

### 課題
- 11_A
- 11_C
- 11_D
### Pythonチュートリアル
なし
### 参考
- [2.9. クラス | Chainer チュートリアル](https://tutorials.chainer.org/ja/02_Basics_of_Python.html#%E3%82%AF%E3%83%A9%E3%82%B9)
### 備考
- 難しい。
- サイコロを転がす問題はfor文でしらみつぶしに解けば現実的な難易度になる。
- この章よりも、Numpy, Pandas課題の方が優先度は高いので飛ばしてもOK。
</details>
