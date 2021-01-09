# Alexa_random  

# 概要  
１秒に１回１から５０の間の乱数を発生させ、１が出た場合にその時間を記録するプログラムです。  
スマートスピーカーのAlexaを使用すると、１が出た１番最新の時刻を教えてくれます。  

---

# 動作環境  
・Raspberry Pi 4 Model B    
・Ubuntu 20.04  
・ROS Noetic  
・Python 2.7.18  

---

# 環境構築  
1.ROSのsrcフォルダにこのパッケージをインストールします。  
```
cd ~/catkin_ws/src  
git clone https://github.com/Kenta-Akiyama/Alexa_random.git  
cd ..  
catkin_make  
```

2.時刻を記録するためにgoogleスプレッドシートを作成します。  
  ファイル名は何でもいいですが、シート名はlogにしてください。  
  
3.Google Apps Scriptで、送られてきたデータを書き込むプログラムを作成します。  
```
function doPost(e) {

  var rand = e.parameter.rand;  

  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('log');  

  sheet.appendRow([new Date(), rand]);  
}  
```
  作成したら、メニューから「ウェブアプリケーションとして導入」を開き、指示に従い進んでください。
  spreadsheet.pyの20行目にあるURLを作成したURLに変更してください。
  
4.VoiceflowでAlexaのアプリを作成します。  
![flow](https://i.gyazo.com/21ae26e2f805be880c6a57a3fe7f0324.png)　　

　上記の画像のように作成してください。
 
 
---

# 実行方法  
1.ROSとパッケージを起動します。  
```
roscore　&  
rosrun Alexa_random rannsuu.py &  
rosrun Alexa_random spreadsheet.py &  
```

2.Voiceflowのテストボタンを押します  

---

# 動画  
・Youtube  
[<img src=https://i.gyazo.com/ba68dda0f6cefacc1bce6efb195132b4.png>](https://youtu.be/XsgV7s5SGYI) 
