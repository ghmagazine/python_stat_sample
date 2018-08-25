# 『Pythonで理解する統計解析の基礎』のサポートページ

谷合廣紀 著、辻真吾 監修  
B5変／320ページ／本体価格3,000円＋税  
ISBN978-4297100490  
技術評論社、2018年発行  

## サンプルコード

- notebook: 本文中に掲載されているコードが書かれたnotebook
- animation: 本文中に <img src="samplecode.png" height=13px> と記載されているインタラクティブに操作できたりアニメーションを再生できるコードが書かれたnotebook
- data: 本文中で使うデータ

## Pythonとライブラリのインストール方法

### Windows10

### MacOS

### Ubuntu16.04

## ライブラリの使い方

ライブラリの基本的な使い方を学ぶためのnotebookがtutorialディレクトリに入っています。

- [NumPyの使い方](https://github.com/ghmagazine/python_stat_sample/blob/master/tutorial/numpy.ipynb)
- [Pandasの使い方](https://github.com/ghmagazine/python_stat_sample/blob/master/tutorial/pandas.ipynb)
<!-- - [Matplotlibの使い方](https://github.com/ghmagazine/python_stat_sample/blob/master/tutorial/matplotlib.ipynb) -->

## Matplotlibの設定

Matplotlibの設定はmatplotlibrcというファイルで変更できます。  
このmatplotlibrcの場所はPythonで次のコードを実行することでわかります。

```python
import matplotlib
matplotlib.matplotlib_fname()
```

```
.../site-packages/matplotlib/mpl-data/matplotlibrc
```

### 日本語の設定

Matplotlibのデフォルトのフォントは日本語に対応していないため、日本語のキャプションをつけようとすると文字化けしてしまいます。
そのため、matplotlibrcで日本語対応のフォントを使うように設定します。

#### Windows10

- まずIPAexゴシックを[ここ](https://ipafont.ipa.go.jp/node26)からダウンロードしてください。
- ダウンロードした後、フォルダを展開してください。`ipaexg.ttf`というファイルが見つかるはずです。
- コントロールパネル->デスクトップのカスタマイズ->フォントでフォントの設定にいき、そこに`ipaexg.ttf`をドラッグ＆ドロップしてください。これでIPAexゴシックをインストールすることができます。

matplotlibrcには次の1行を追記してください。
```
font.family: IPAexGothic
```

最後に[このnotebook](https://github.com/ghmagazine/python_stat_sample/blob/master/tutorial/matplotlib_ja.ipynb)を実行して、日本語表示できているか確認してみましょう。

#### MacOS

Appleゴシックというフォントが使えるはずです。
matplotlibrcに次の1行を追記してください。
```
font.family: AppleGothic
```

最後に[このnotebook](https://github.com/ghmagazine/python_stat_sample/blob/master/tutorial/matplotlib_ja.ipynb)を実行して、日本語表示できているか確認してみましょう。

#### Ubuntu 16.04

Takaoゴシックというフォントが使えるはずです。
matplotlibrcに次の1行を追記してください。
```
font.family: TakaoGothic
```

最後に[このnotebook](https://github.com/ghmagazine/python_stat_sample/blob/master/tutorial/matplotlib_ja.ipynb)を実行して、日本語表示できているか確認してみましょう。

### グラフの設定
本書のようにグラフに罫線を出力したい場合は、さらに次の設定もmatplotlibrcに追記してください。

```
axes.grid: True
axes.axisbelow: True
grid.alpha: 0.5
```
