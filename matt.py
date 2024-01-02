matt.py

#-*-coding:utf-8 # 한글 인코딩

import paho.mqtt.client as mqtt     #Paho-MQTT 패키지 불러오기
from flask import Flask, render_template, request   # Flask 패키지 불러오기
app = Flask(__name__)                               # Flask 모듈 불러오기

#matt 클라이언트를 생성하여 연결
mqttc=mqtt.Client()     #클라이언트 객체 생성
mqttc.connect("localhost", 1883, 60)    #연결설정
mqttc.loop_start()                      # 메시지를 반복적으로 보낼 수 있게 설정

# led란 딕셔너리를 만듭니다. 'name'과 'state' 요소를 사용
led = {'name' : 'LED pin', 'state' : 'ON'}  # 디폴트를 on

# 웹서버의 URL 주소로 접근하면 아래의 main() 함수를 실행
@app.route("/")
def main():
    # led 딕셔너리를 templateData에 저장
    templateData = {
        'led' : led
    }
    return render_template('main.html', **templateData)     #리턴 값은 메인.html 리턴

#URL 주소 끝에 "/LED/<action>" 을 붙여서 접근시에 action 값에 따라 동작
@app.route("/LED/<action>")     # 액션에 주소 입력
def action(action):

    #만약에 action 값이 "on"과 같으면 mqtt 메시지를 토픽 "inTopic"에 "1"을 전송
    if action =="on":
        mqtt.publish("inTopic", "1") #토픽에다가 1을 전송 엘이디가 켜짐
        led[['state'] = "ON"
        message = "LED on." # 메시지 출력
    # 만약에 action 값이 "off"와 같으면 mqtt 메시지를 토픽 "inTopic"에 "0"을 전송
    if action =="off":
        mqttc.publish("inTopic", "0") # 토픽에다 0d을 전송 엘이디 꺼짐
        led['state'} = "OFF" # 상태값을 off
        message = "LED off." # 메시지 

    template Data = {
        'message' : message, #메시지 저장
        'led' : led
    }
    return render_template('main.html', **templateData) 매인 html 리턴 - 홈페이지 연결

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=False)
            
