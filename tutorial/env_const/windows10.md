# Pythonの環境構築と使い方（Windows10）

- [環境構築](##環境構築)
    - [pyenvのインストール](###pyenvのインストール)
    - [Anacondaのインストール](###Anacondaのインストール)
    - [仮想環境の作成](###仮想環境の作成)
    - [ライブラリのversion](###ライブラリのversion)
- [Jupyter Notebookの起動](##JupyterNotebookの起動)
- [Matplotlibの設定](##Matplotlibの設定)
    - [日本語の設定](###日本語の設定)
    - [罫線の設定](###罫線の設定)

## 環境構築

### Anacondaのインストール

PythonのインストールはAnacondaをオススメします。
Anacondaは科学技術計算用のライブラリ群があらかじめパッケージングされたPythonです。

https://www.anaconda.com/download/
からPython3.6 versionをDownloadし、指示に従ってインストールしていきましょう。

### 仮想環境の作成

まずは本書専用の仮想環境を作ります。

Windowsキーを押したあとにanaconda promptと入力して、Anaconda Promptを起動しましょう。

黒い画面（プロンプト）が起動し、
```
(base) C:\Users\hoge>
```
のような文字が出力されていると思います。

仮想環境を作るには次のコマンド(>より右部分)を入力します。
`pyst`の部分には好きな名前を入れてもらっても構いません。
```
(base) > conda create -n pyst python=3.6 anaconda
```
途中いろいろ聞かれるかもしれませんが、すべてyesで大丈夫です。

この仮想環境を有効するには次のコマンドを実行します。
```
(base) > activate pyst
```

baseがpystになっていればOKです。

### ライブラリのversion

本書のコードは次のバージョンで実行できることを確認しています。

|パッケージ名|バージョン|
|:-:|:-:|
|python|3.6.5|
|jupyter|1.0.0|
|ipython|6.2.1|
|notebook|5.5.0|
|numpy|1.14.3|
|pandas|0.23.0|
|matplotlib|2.2.2|
|statsmodels|0.9.0|

ライブラリのバージョンは次のコマンドで確認できます。
```
(pyst) > conda list
```

特にipythonのバージョンによってはnotebookで桁数を抑制するための
```python
%precision 3
```
がうまく動かない場合があります。
その場合は、次のコマンドでバージョン6.2のipythonをインストールしてください。
```
(pyst) > conda install ipython=6.2
```

## JupyterNotebookの起動

Jupyter Notebookは次のコマンドで起動します。
```
(pyst) > jupyter notebook
```

ブラウザが立ち上がり次のような画面が出ていれば成功です。
![](images/notebook1.png)

notebookは次のようにして立ち上げることができます。
![](images/notebook2.png)

notebookが立ち上がると次のようになります。
ここにコードを記述すると実行できるようになります。
![](images/notebook3.png)

フォルダの作成や移動などは直感的に行うことができると思うので、管理しやすいように適当なフォルダを作って作業スペースとしてください。

## Matplotlibの設定

Matplotlibの設定はmatplotlibrcというファイルで変更できます。  
[このnotebook](https://github.com/ghmagazine/python_stat_sample/blob/master/tutorial/matplotlib_ja.ipynb)
の最初のセルを実行してmatplotlibrcの場所を調べましょう。

matplotlibrcにはいろいろと記述されていると思いますが、これまで特に設定を変更していなければ、それらはすべてコメントアウトされている行になっているはずです。  
そのため、これからmatplotlibの設定するにあたって、それらの行はすべて消してもらっても構いません。

### 日本語の設定

Matplotlibのデフォルトのフォントは日本語に対応していないため、日本語のキャプションをつけようとすると文字化けしてしまいます。
ここではそのような文字化けを回避するための設定をしていきます。

- まずIPAexゴシックを[ここ](https://ipafont.ipa.go.jp/node26)からダウンロードしてください。
- ダウンロードした後、フォルダを展開してください。`ipaexg.ttf`というファイルが見つかるはずです。
- コントロールパネル->デスクトップのカスタマイズ->フォントでフォントの設定にいき、そこに`ipaexg.ttf`をドラッグ＆ドロップしてください。これでIPAexゴシックをインストールすることができます。

matplotlibrcには次の1行を追記してください。
```
font.family: IPAexGothic
```

最後に[このnotebook](https://github.com/ghmagazine/python_stat_sample/blob/master/tutorial/matplotlib_ja.ipynb)を参考に、日本語表示できているか確認してみましょう。

### 罫線の設定
本書のようにグラフに罫線を出力したい場合は、さらに次の設定もmatplotlibrcに追記してください。

```
axes.grid: True
axes.axisbelow: True
grid.alpha: 0.5
```
