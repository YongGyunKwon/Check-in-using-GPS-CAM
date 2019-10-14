# Check-in-using-GPS-CAM
제2회 PATH HACK 해커톤 2019.07.26. ~ 2019.07.27.


기획자: 윤일승
개발자: 정종학, 김진규, 권용균

GPS와 CAMERA, 얼굴인식(인공지능)을 이용한 출석 및 Check in 서비스 Python으로 구현


1. GPS가 서비스 사용자의 위치를 인식하여 설정한 위치 반경 500m 이내에 있다면 출석 인증을 할 수 있는 카메라가 활성화 된다. 
   (설정한 위치는 "패스파인더 부산대" 이다.)

2. 카메라가 활성화 되면 학습되있는 사진 데이터와 CAMERA에 비춰진 얼굴을 비교하여 사용자 본인의 데이터와 일치하는지 판별한다. 
   (사용자는 "kwon"으로 설정되있으며 사용자 "kwon"이 카메라에 얼굴을 비추면 학습된 사진 데이터 중 "kwon"의 데이터와 일치하는지 판별)

3. 일치할 경우 카메라가 종료되어 출석되었다는 데이터를 넘겨준다.


ps. 사진 데이터는 kwon, yangpang, 류현진, 보겸, 손흥민 사진이 학습되어있다.


프로그램을 구현하기 위해서 app2.py 를 Run(실행) 시켜야 한다. (app2.py에 app.py를 import 시켰다.)



프로그램을 실행하기전 
pip install flask
pip install face_recognition
pip install opencv
pip install cv2
pip install geocoder
pip install math
pip install googlemaps

를 터미널에 입력해야 한다.(파이참 기준)


보완할점
: 현재 파이썬 코드를 이용하여 얼굴인식 까지밖에 되지 않았다. 
향후, GPS값을 받아서 원하는값과 일치하면 현재 존재하는 파이썬이 실행되고 
얼굴인식이 성공적이면 데이터를 넘겨줘서 출석완료되는 시스템으로 연결하여야 된다.

또, 이런 시스템을 모바일 어플리케이션에 접목시킨다면 활용도 역시 높아질 것이다.
