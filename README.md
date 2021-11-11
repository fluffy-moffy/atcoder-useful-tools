# atcoder-useful-tools

## check-and-get v.1.0

authoer: firerce

twitter: [@nekomimimoe3](https://twitter.com/nekomimimoe3)


## 説明
現在、このリポジトリはchekcer.pyとgetter.pyの二つのツールから構成されています。

checker.pyは`コンテスト番号(ex; agc055)`, `ユーザーの名前(ex; chokudai)`を引数に取り、該当する提出のうち、ACした問題の問題番号および問題名を出力します。

getter.pyは`コンテスト番号`, `ユーザーの名前`, `問題番号(ex; a)`を引数に取り、該当するコードを出力します。一度に取得できるコードは一つまでです。


## ダウンロード
以下のコマンドでカレントディレクトリにリポジトリを保存します。

`git clone https://github.com/moffuu/atcoder-useful-tools.git`

作成されたディレクトリに移動します。

`cd atcoder-useful-tools.git`

お好きな場所にcpコマンド等で移動されてください。
一例ですが、私は`~/work/atcoder`においています。


## 使い方
この二つのツールを組み合わせることで、他の人のコードを簡単に手元に保存することができます。以下にその手順を書きます。(ここではchokudaiさんのagc055、それのA問題のコードが見たいとします)

1. 取得したい問題が存在するかを確認します。以下のコマンドを実行します。

`python3 checker.py agc055 chokudai //コンテスト名・問題番号は半角で入力してください`

すると以下のような結果が出力されました。

`['D - ABC Ultimatum', 'C - Weird LIS', 'B - ABC Supremacy', 'A - ABC Identity']`

2. 該当するコードの存在が確認できたので、以下のコマンドにて該当するコードを取得します。(ここでは、a.cppという名前で保存しています)

`python3 getter.py agc055 chokudai a > a.cpp`

これで保存することができました。
