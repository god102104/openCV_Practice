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

### VideoCaputre::read()
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
> 만약 여러 대의 카메라로부터 동시에 영상을 획득하고 싶다면, read() 보다 grab()와 retrieve()를 따로 호출 하는 것이 유리 <br>

### VideoCapture::get()
<pre>
  <code>
      virtual double cv::VideoCapture::get(int propId) const
  </code>
</pre>
> 인자로 지정한 속성 ID에 해당하는 속성 값 반환. 상세 내용은 ref 참조 <br>
> 카메라 또는 동영상 파일 속성을 dobule 자료형으로 반환 <br>
> 그러므로, 실제 코드에 정수형 변수에 프레임 크기를 저장하려면 **반올림** 해주는 것이 좋음. **cvRound()** <br>

### VideoCaputre::set()
<pre>
  <code>
    virtual bool cv::VideoCapture::set(int propId,double 	value)		
  </code>
</pre>
> get()과 반대로, 현재 **열려 있는** 카메라 또는 비디오 파일 재생과 관련된 속성 값을 설정할 때 쓰는 함수. <br>


## 카메라 입력 처리하기

### 동영상 파일 처리하기
> 동영상 파일의 경우 **FPS** 값을 신경 써야한다. <br>
<pre>
  <code>
    //동영상 FPS 값을 확인하는 코드
    double fps = cap.get(CAP_PROP_FPS);
  </code>
</pre>
> FPS 값을 이용하면 매 프레임 사이의 시간 간격을 계산 가능. <br>
<pre>
  <code>
    int delay = cvRound(1000/ fps);
  </code>
</pre>
> delay 값은 동영상 프레임을 받아와서 화면에 출력하는 반복문 안에서 waitKey() 함수의 인자로 사용됨. <br>

### 동영상 파일 저장하기
> 동영상 파일 생성하고 프레임을 저장하기 위해서는 **VideoWriter Class** 를 사용해야 한다. <br>
> VideoWriter::open() 를 쓰기 모드로 열어야 함. <br>
<pre>
  <code>
    virtual bool cv::VideoWriter::open(const String &filename, int fourcc, double fps, Size frameSize, bool isColor = true)	
  </code>
</pre>
> fourcc는 4-문자 코드 (four character code)의 약자 <br>
> 파일 코덱, 압축 방식, 색상 혹은 픽셀 포맷 등을 정의하는 정수 값 <br>
> fourcc 에 해당하는 정수 값은 VideoWriter::fourcc() 함수를 사용하여 생성할 수 있다. 아래 참조 <br>
> static int VideoWriter::fourcc(char c1, char c2, char c3, char c4); <br>
> c1, c2, c3, c4 : 코덱을 표현하는 1byte 문자 네 개 <br>
> return : 정수형 4-문자 코드 <br>

### VideoWriter::write()
> 열려 있는 동영상 파일에 **새로운 프레임을 추가**할 때 사용 <br>
> **VideoWriter::operator << (const Mat& image)** 와 같은 기능 <br>
> 프레임 크기는 동영상 파일을 생성할 때 지정했던 **프레임 크기와 같아야** 한다. <br>
> 컬러 동영상에 Grayscale 영상 추가 시 정상 저장되지 않으므로 주의 <br>
> 프레임 저장 완료 시 VideoWriter::release() 호출할 것 <br>

# OpenCV 데이터 파일 입출력

## FileStorage Class
> OpenCV에서 데이터 파일 입출력을 담당하는 Class <br>
> XML, YAML, JSON 형식의 파일 입출력 지원. <br>
> 사용할 파일 형식은 filename의 확장자에 의해 자동 결정 (.xml 확장자일 시 XML형식 사용) <br>
> 파일에 데이터를 저장 할 때에는 << 연산자, 읽어 올 때는 >> 연산자
> 작업 후 FileStorage::release() 호출할 것.
<pre>
  <code>
    #include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

void writeData();
void readData();

// String filename = "mydata.xml";
// String filename = "mydata.yml";
String filename = "mydata.json";

int main(void)
{
	writeData();
	readData();

	return 0;
}

void writeData()
{
	String name = "Jane";
	int age = 10;
	Point pt1(100, 200);
	vector<int> scores = { 80, 90, 50 };
	Mat mat1 = (Mat_<float>(2, 2) << 1.0f, 1.5f, 2.0f, 3.2f);

	FileStorage fs;
	fs.open(filename, FileStorage::WRITE);

	if (!fs.isOpened()) {
		cerr << "File open failed!" << endl;
		return;
	}

	fs << "name" << name;
	fs << "age" << age;
	fs << "point" << pt1;
	fs << "scores" << scores;
	fs << "data" << mat1;

	fs.release();
}

void readData()
{
	String name;
	int age;
	Point pt1;
	vector<int> scores;
	Mat mat1;

	FileStorage fs(filename, FileStorage::READ);

	if (!fs.isOpened()) {
		cerr << "File open failed!" << endl;
		return;
	}

	fs["name"] >> name;
	fs["age"] >> age;
	fs["point"] >> pt1;
	fs["scores"] >> scores;
	fs["data"] >> mat1;

	fs.release();

	cout << "name: " << name << endl;
	cout << "age: " << age << endl;
	cout << "point: " << pt1 << endl;
	cout << "scores: " << Mat(scores).t() << endl;
	cout << "data:\n" << mat1 << endl;
}
  </code>
</pre>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/0ea223ae-f49f-4612-863f-b90070b50aaf)

> 파일 이름과 열기 모드를 지정하는 생성자를 이용해서 한 번에 작업할 수 있음
<pre>
	<code>
		FileStorage fs("mydata", FileStorage::READ);
	</code>
</pre>
