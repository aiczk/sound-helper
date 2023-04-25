# 使用方法
sound-helper(GUI)を使うまでの準備についての解説
## 下準備
### 1. Source.zipのダウンロード
[こちら](https://github.com/aiczk/sound-helper)のCode下にある**Download ZIP**をクリックしてダウンロード後、解凍しましょう。

### 2. Pythonのインストール
[こちら](https://prog-8.com/docs/python-env-win)のサイトに記載されている通りにPythonをインストールします。
コマンドプロンプトで**必ず**`python --version`を実行し、バージョン情報が出てくることを確認したら次のステップに進みます。

### 2. ffmpegのインストール＆パスを通す
[こちら](https://rikoubou.hatenablog.com/entry/2019/11/07/144533)のサイトに記載されている通りにffmpegをインストールします。
コマンドプロンプトで**必ず**`ffmpeg`を実行し、下記画像のような文章が出てくることを確認したら下準備は完了です。
![ffmpeg](https://cdn-ak.f.st-hatena.com/images/fotolife/r/rikoubou/20191107/20191107144324.png)

### 3. pip -r requirement.txtの実行
解凍済したSource.zip内で**フォルダーの空いているところを**右クリックし、`ターミナルで開く(T)`を実行しましょう。
コマンドプロンプトが開きましたら`pip install -r requirements.txt`を実行しましょう。
#### エラーが出てインストールができない場合
`pip install --upgrade pip`または`pip3 install --upgrade pip`を実行し、pipをアップグレードしてみてください。

## GUIの表示
下準備おつかれさまでした。
`run-gui.bat`を実行しましょう。
