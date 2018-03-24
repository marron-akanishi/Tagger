# Tagger
Tagging tool for ML  

## なにこれ
機械学習をする際に必要なタグ付けを行うためのツールです。  
タグ付けをWebUIで行い、その結果をjsonファイルで出力します。  

## 動作環境  
Python 3.xなら動くと思います。  
flask, opencv-pythonが必要なのでpipでインストールしてください。  

## ファイル構造
static -> WebUIに必要なファイルが入ります。  
templates -> レンダリング用HTMLファイルが入っています。  
tools -> 通常は使用しないスクリプトです。説明しません。  
app.py -> WebUI本体のスクリプトです。  

## 使い方
まず、taglist.jsonにタグ付けをしたいタグを入力します。  
この時、一番最初に`"-1":"None",`を必ず入れてください。  
次にタグ付けする画像を`./static/images/`にすべて入れます。  
次に`python makelist.py`を実行します。  
これでファイルリストであるlist.jsonが作成されます。  
次にlist.jsonが出来た状態で`python app.py`を実行し、`localhost:5000`にアクセスします。  
これでWebUIが表示されるはずです。  
タグ付けが完了したら、`python move.py`を実行します。  
これで`./files/study/`に90％の画像が、`./files/test/`に10％の画像がコピーされ、study.jsonとtest.jsonが作成されます。  
この2つのフォルダーは自動作成されないので、先に作成してください。  
また、画像はコピーした際にタグごとにフォルダー分けされます。  