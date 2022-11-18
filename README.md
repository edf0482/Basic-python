# Python-Basic
## ＊注意＊
課題を提出する際は必ず
  * コード規約が守られている(詳細は下の方）
  * python3で解いている
  * python課題はAOJのサイトに提出をしてACがでている

ということを確認してから提出するようにしてください。


**※　課題は貯めずに、終わり次第毎回提出する**

## 教材
基礎的なPythonの書き方について学べます(教材途中で課題を出してもOKです）
  * [東京大学のpython講座ノートブック][3]

## 個人レポジトリの作成
個人でレポジトリを作成してもらい、そこで課題をレビューしていくことになります。詳細は以下を見てください。

## 課題の進め方

1. 個人でリポジトリを作成する。<br>
  1.1.このページの右上のUse This Templateをクリック<br>
  <img width="287" alt="スクリーンショット 2022-04-04 10 43 57" src="https://user-images.githubusercontent.com/70427875/161460844-add34447-42c7-40c2-9b2e-d662e24eef34.png"><br>
  1.2.Ownerを自分（あなた）に変更し、Publicでリポジトリを作成する(include all branchesにはチェック入れない)<br>
  <img width="761" alt="スクリーンショット 2022-04-04 10 46 24" src="https://user-images.githubusercontent.com/70427875/161460958-acb2c2e8-edde-44d9-bc76-3e05a24cbf5b.png"><br>



2. 作成したリポジトリをクローンする。

1. 課題を解く。<br>
  ・Python課題の場合<br>
  3.1. 作業ブランチを作成して移動する。ブランチ名は `<topic number>` とする。ex: `topic-1` .<br>
  3.2. 公式ドキュメントや参考資料を読む。<br>
  3.3. AIZU ONLINE JUDGE (以下、AOJ) の問題文を読む。<br>
  3.4. 解答を `AOJ` ディレクトリ内の該当するファイルに作成する。<br>
  3.5. AOJのサイトに提出をして判定が `AC`となったら次へ進む。<br>
  ・numpy, pandas, matplotlibの場合<br>
  3.1. 作業ブランチを作成して移動する。ブランチ名は `<topic>` とする。ex: `numpy` .<br>
  3.2. 公式ドキュメントや参考資料を読む。<br>
  3.3. 解答を `colab` ディレクトリ内の該当するファイルに作成する。<br>
  
1. 提出する。提出は A, B, C, D のように問題ごとにするのではなく、1, 2, ... のようにトピックごとにする。<br>
  4.1. ブランチ `<topic number>`or`<topic>` からブランチ `main` に向けてプルリクエストを作成する。<br>
  4.2. プルリクエストのステータスが ❌ だった場合、コーディングスタイルを修正して再提出する。<br>
  4.3. #dev_data_python でレビュワーに(プルリクエストのリンクと一緒に) メンションする。<br>
  ※メンションを見落としてしまうことがあるので、2日以上返信がなかったらもう一度メンションしてください。

1. 提出後<br>
  5.1. レビュワーは `Files changed` タブでレビューを行い、修正依頼を出す。<br>
  5.2. 修正依頼が出たら、コードを修正して再度レビュー依頼を出す。<br>
  5.2. レビューが通ったら `<topic number>` を `main` にマージする。<br>

## 概要
現在このコースには、以下の4章があります。詳しい説明はディレクトリのリンク先の `README.md` を読んでください。

|技術|ディレクトリ|内容|提出方法
|:-|:-|:-|:-
|Python|[AOJ][1]|プログラミング入門|直接ファイルを編集してPull request
|Numpy|[colab][2]|データ処理|ノートブック(ipynb)を編集してanswerフォルダーにいれてPull requestを出す
|Pandas|[colab][2]|データ操作|ノートブック(ipynb)を編集してanswerフォルダーにいれてPull requestを出す
|matplotlib|[colab][2]|可視化|ノートブック(ipynb)を編集してanswerフォルダーにいれてPull requestを出す

### 課題のレビューについて
課題をやったら以下の表に従って担当者にslackでメンションしてレビューを依頼してください。

|課題|レビュー担当者|
|:-:|:-:|
|AOJ１|Daichi|
|AOJ２|wataru|
|AOJ３|Shunji|
|AOJ４|wataru|
|AOJ６|Shunji|
|AOJ７|Daichi|
|AOJ８|Taichi(Ando)|
|AOJ11|wataru|
|pandas|Shunji|
|numpy|Daichi|
|matplotlib|Taichi(Ando)|

# ※注意※コード規約について

課題を提出をするときは、

- コードがコード規約に従っている（PEP8）
- python3で解いている
- AOJのサイトに提出をしてACが出ている

ということを必ず確認してから提出するようにしてください。

<aside>
💡 **コード規約**

[PEP8](https://pep8-ja.readthedocs.io/ja/latest/)とは、Pythonにおけるスタイルガイドのこと。

スタイルガイドとは、変数や関数名の付け方、空白に関する内容や、インデントの仕方、コメントの書き方など様々な基本的なルールを定義しているもの。

実際の開発では複数人で作業することが一般的である。その際にコード規約に従うことでコードに一貫性が生まれ、可読性・保守性が高まり品質の向上につながる。

</aside>
このサイトで自分のコードがコード規約に従っているかチェックすることができます。(http://pep8online.com)

### vscodeのsettings.jsonを編集してコード規約を自動的に守る方法

下のsettings.jsonファイルをダウンロードして.vscode直下に置いてください。(GitHubからリポジトリをクローンすれば、自動的にvscode直下に置かれます。)自動で保存時にコード規約に従ったコードへと変換されます。詳しくは[こちら](https://maku.blog/p/tfq2cnw/)。

black, flake8をインストールしていないとvscodeで警告が出るので自身の環境にあわせて(conda or pip)インストールしてください。↓
<img width="450" alt="スクリーンショット 2022-04-04 0 24 03" src="https://user-images.githubusercontent.com/70427875/161435394-b5018694-aee2-4a89-813d-9cfa4e9b7c15.png">


わからないことがあればslackで@eriにお願いします。

↓GitHubからクローンしてもvscode直下に置かれなかった方用<br>
[settings.json.zip](https://github.com/shinonome-inc/Basic-Python/files/8357521/settings.json.zip)


<img width="287" alt="スクリーンショット 2022-03-20 19 31 34" src="https://user-images.githubusercontent.com/83397726/160279459-afeb9b5e-cfb1-4aa3-b26d-1e1433ae816e.png">


（フォーマッターを使わない方は[こちら](https://atmarkit.itmedia.co.jp/ait/articles/1912/10/news045.html)を参考にしてください。）

[1]: https://github.com/shinonome-inc/Basic-Python/tree/master/AOJ
[2]: https://github.com/shinonome-inc/Basic-Python/tree/master/colab
[3]: https://colab.research.google.com/github/utokyo-ipp/utokyo-ipp.github.io/blob/master/colab/index.ipynb
[4]: https://www.notion.so/c1f04389a0434720a9ee980c1d6200c0
[5]: http://pep8online.com/checkresult
