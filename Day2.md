Day 2
====

# 카메라와 동영상 파일 다루기

## VideoCapture Class
> 멤버 변수는 모두 protected 로 되어있어 사용자가 직접 접근 불가<br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/dccbad72-9575-480b-a33f-5fb464ffe2b6)<br>
> Object 생성 시에 동영상 파일 이름을 지정하거나, 기본 생성자로 VideoCapture Object 생성 후 VideoCapture::open() member function 호출해야한다.


### VideoCaputre::open()
<pre>
  <code>
    bool cv::VideoCapture::open	(int cameraNum, int apiPreference)	
  </code>
</pre>
> index = camera_id + domain_offset_id <br>
> 컴퓨터에 한 대의 카메라만 연결되어 있다면 camera_id의 값은 0 <br>
> 카메라 장치 또는 동영상 파일의 사용이 끝나면 VideoCapture::release() 함수 호출하여 자원 해제해줘야 한다. <br>
> VideoCaputre class의 소멸자에도 자원 해제하는 부분이 있긴 함.<br>

###VideoCaputre::read()
> 한 프레임을 받아오기 위한 방법 <br>
> VideoCaputre::operator >>() 연산자 재정의 함수와 기능이 같다. <br>
<pre>
  <code>
    VideoCapture cap(0);
    Mat frame1, frame2;
    cap >> frame1;
    cap.read(frame2);
  </code>
</pre>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/3f1e2e2a-aaa0-4576-a0d8-c416fb425c4e)

> VideoCapture::grab() 함수는 카메라 장치에 다음 프레임을 획득 하라는 명령을 내리는 함수 <br>
> VideoCaputre::retrieve()는 획득한 프레임을 실제로 받아 오는 함수 <br>
> VieoCapture::read() 와 VideoCaputre::operator >>() 함수는 grab()와 retrieve()를 합쳐 놓은 것 <br>
