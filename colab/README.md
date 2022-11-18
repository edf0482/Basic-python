# Numpy, Pandas　入門

[Data Science Handbook][0] を参考にして進める。
Python課題と同様に、Google ColabをGithub上で提出してもらいます。


[svg]: https://colab.research.google.com/assets/colab-badge.svg

## 課題の進め方

1. 個人でリポジトリを作成する。
1. 作成したリポジトリをクローンする。
1. 課題を解く。<br>
  3.1. 作業ブランチを作成して移動する。ブランチ名は `<topic>` とする。ex: `numpy`<br>
  3.2. 公式ドキュメントや参考資料を読む。<br>
  3.3. 解答を colab ディレクトリ内の該当するファイルに作成する。<br>
1. 提出する。提出は A, B, C, D のように問題ごとにするのではなく、1, 2, ... のようにトピックごとにする。<br>
  4.1. ブランチ `<topic>` からブランチ `main` に向けてプルリクエストを作成する。<br>
  4.2. プルリクエストのステータスが ❌ だった場合、コーディングスタイルを修正して再提出する。<br>
  4.3. #dev_data_python にあるスプレッドシートに課題情報を記入する。<br>
  4.4. #dev_data_python でレビュワーを(プルリクエストのリンクと一緒に) メンションする。<br>
  ※メンションを見落としてしまうことがあるので、2日以上返信がなかったらもう一度メンションしてください。
1. レビュワーの行動<br>
  5.1. レビュワーは `Files changed` タブでレビューを行い、修正依頼を出す。<br>
  5.2. レビューが通ったら `<topic>` を `main` にマージする。

## Introduction-to-Numpy
Numpy の章の進め方は、[こちらのwiki][1]を参照してください。<br>
確認課題は [![Open In Colab][svg]][2] をクリックして notebook で解答を作成してください。「ドライブにコピー」ボタンを押してマイドライブに保存してから解いてください。
解答が作成できたら、answerディレクトリに解答を入れてプルリクエストをだして提出してください。

## Data Manipulation with Pandas
Pandas の章の進め方は、[こちらのwiki][3]を参照してください。<br>
確認課題は [![Open In Colab][svg]][4] をクリックして notebook で解答を作成してください。「ドライブにコピー」ボタンを押してマイドライブに保存してから解いてください。
解答が作成できたら、answerディレクトリに解答を入れてプルリクエストをだして提出してください。


## Data Visualization with Matplotlib
お題の図と同じグラフを作ってください。（色は同じじゃなくて大丈夫です。）使用するデータはmatplotlib_quizの中にあります。<br>
確認課題は [![Open In Colab][svg]][5] をクリックして notebook で解答を作成してください。「ドライブにコピー」ボタンを押してマイドライブに保存してから解いてください。
解答が作成できたら、answerディレクトリに解答を入れてプルリクエストをだして提出してください。

### [参考][6]
データサイエンスハンドブックのサンプルコードにあるcsvデータを読み込むセルの実行方法についての説明です。


[0]: https://jakevdp.github.io/PythonDataScienceHandbook/
[1]: https://github.com/shinonome-inc/Basic-Python/wiki/Introduction-to-Numpy
[2]: https://drive.google.com/file/d/1AcB5_rpqpw3uhlLyTtChylbktQml4O2U/view?usp=sharing
[3]: https://github.com/shinonome-inc/Basic-Python/wiki/Data-Manipulation-with-Pandas
[4]: https://drive.google.com/file/d/1xKx_9GQ9mYujKZ4ga3xlAyJw7Kp6LLpk/view?usp=sharing
[5]: https://drive.google.com/file/d/1iIp7PWSYFQ0EEQrvlUE38qX4pR-3j9UI/view?usp=sharing
[6]: https://github.com/shinonome-inc/Basic-Python/wiki/csv%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%81%BF%E6%96%B9

