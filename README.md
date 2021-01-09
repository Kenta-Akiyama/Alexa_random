# Alexa_random

##概要
１秒に１回１から５０の間の乱数を発生させ、１が出た場合にその時間を記録するプログラムです。
スマートスピーカーのAlexaを使用すると、１が出た１番最新の時刻を教えてくれます。

---

##動作環境
・Raspberry Pi 4 Model B  
・Ubuntu 20.04
・ROS Noetic
・Python 2.7.18

---

##環境構築
1.ROSのsrcフォルダにこのパッケージをインストールします。
```
cd ~/catkin_ws/src
git clonehttps://github.com/Kenta-Akiyama/Alexa_random.git
cd ..
catkin_make
```

2.時刻を記録するためにgoogleスプレッドシートを作成します.

3.Google Apps Scriptで、送られてきたデータを書き込むプログラムを作成します

4.VoiceflowでAlexaのアプリを作成します。

---

##実行方法
1.ROSとパッケージを起動します。
```
roscore　&
rosrun Alexa_random random.py &
rosrun Alexa_random spreadsheet.py &
```

2.Voiceflowのテストボタンを押します

---

##動画
##ライセンス
GNU General Public License v3.0 
