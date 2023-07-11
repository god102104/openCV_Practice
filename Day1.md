Day 1 
=====
Grayscale image 를 이용할 때 C/C++ 에서는 주로 unsigned char를 이용한다.<br> 
unsigned char는 1byte 크기를 가지며 부호 없는 8bit int 값을 저장할 수 있는데, 이는 0~255 를 의미한다.<br>
그러므로 Grayscale 값을 표현하기 가장 적절한 자료형이다.<br>

openCV function 관련
---
### Mat  imread(const String& filename, int flags = IMREAD_COLOR);<br>
> filename 파일을 불러와서 Mat object 로 변환하여 반환<br>
> 파일이 존재하지 않거나 잘못된 형식의 경우, Return empty Mat object<br>
> imread()를 사용하려고 하는 경우 Mat::empty()를 이용하여 Object 생성 여부를 확인하자.<br>

### Mat imwrite(const String& filename, InputArray img, const std::vector<int>& params = std::vector<int>());
> img 를 filename 이름으로 저장<br>
> filename 문자열에 포함된 확장자로 결정<br>

<pre>
  <code>
    vector<int> params;
      params.push_back(IMWRITE_JPEG_QUALITY);
      params.push_back(95);
      imwrite("lena.jpg", img, params);
  </code>
</pre>

> IMWRITE_JPEG_QUALITY 플래그가 JPEG 압축률을 나타내는 옵션 플래그임.<br>
> 상세한 내용은 OpenCV 문서 사이트 참조<br>

### Point_ Class
> Template class 이므로, 어떤 자료형으로 좌표를 표현할지를 명시해야 한다.<br>
> int 자료형 쓰고 싶다면 Point2i, float 쓰고 싶다면 Point2f 를 쓰면 된다.<br>

<pre>
  <code>
    Point pt1;
    pt1.x = 5;
    pt1.y = 10;
    Point pt2(10, 30);
  </code>
</pre>

> 위의 코드에서 pt1은 기본 생성자를 사용하여 생성되었으므로 처음에는 pt1.x, pt1.y 는 둘 다 0으로 만들어진다.<br>

### Size_ Class
> template class
> **width**와 **height** 라는 member variable 을 갖고 있음.<br>
> int 쓰고 싶다면 Size2i, float 쓰고 싶다면 Size2f 쓰면 된다.<br>
> Size Object 끼리 덧셈 연산을 하면 가로 세로를 더한 새로운 Object를 생성한다.<br>

### Rect_ Class
> 사각형의 위치와 크기 정보<br>
> template class<br>
> Rect_ Object 끼리 **&** 와 **|** 를 이용한 연산이 가능하다.<br>

![Rect_example](https://postfiles.pstatic.net/MjAyMTA1MDlfMjgx/MDAxNjIwNTUwODE5NjU5.sHiYnIJZ0NA6iP4l6xQALluU8NyVVTt9-Dm5dEieT7sg.OekYqTLPwnJdYHNz2G1uGqJ3iipr6ARN_FmsOorIm-Yg.JPEG.sees111/%EC%BA%A1%EC%B2%98.JPG?type=w966)

### String class
> std::string 이랑 똑같음


## Mat Class ★
> **Mat::dims** 라는 member variable 은 행렬의 차원 <br>
> **Mat::rows** 와 **Mat::cols** 라는 member variable 은 Mat object가 2차원인 경우에만 의미있는 값을 가진다. (3차원 이상인 경우 -1이 저장됨)<br>
> 3차원 이상의 행렬 크기 정보는 Mat::size 이용해서 **참조** 가능.<br>
> **Mat::data**는 행렬의 원소 data가 저장되어 있는 **메모리 공간**을 가리키는 **포인터형** 변수<br>
> Mat class의 모든 member variable 은 **public**

### Mat Class 생성 시 주의 점
> 가로- 세로 크기 순이 아니라, 세로-가로 크기 순서
<pre>
  <code>
	Mat img(480, 640, CV_8UC1); //unsigned char, 1-channel
	Mat img2(480, 640, CV_8UC3); //unsigned char, 3-channels
	Mat img3(Size(640, 480), CV_8UC3); //Size(width, height)
	Mat img4(480, 640, CV_8UC1, Scalar(128)); //initial values, 128
	Mat img5(480, 640, CV_8UC3, Scalar(0, 0, 255)); //initial values, red
  </code>
</pre>

![image](https://github.com/god102104/openCV_Practice/assets/43011129/f8080d0a-5031-4ea4-bc87-2d60e3ca38b5)

> Mat::zeros(int rows, int cols, int type)
> Mat::ones(int rows, int cols, int type)
> Mat::eye(int rows, int cols, int type)

### 외부 배열을 행렬의 원소값으로 사용해보기
<pre>
	<code>
		float data[] = { 1, 2, 3, 4, 5, 6 };
		Mat mat(2, 3, CV_32FC1, data);
		cout << "mat"<< endl << mat << endl;
	</code>
</pre>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/2ce6069a-1317-4e2b-976b-2f3083146c81)

> 외부 메모리 공간을 **참조**하여 Mat Object 를 생성하는 경우, Object의 원소 값과 외부 **메모리 값이 공유**된다는 사실은 몹시 중요하다.<br>
> 둘 중 한 쪽을 수정하더라도 양 쪽 모두에 적용됨.<br>
> 동적 할당 된 Memory의 경우 Mat Object가 소멸될 때 까지 남으므로, 직접 메모리 해제 해주는 것을 잊지 말자.<br>

### Mat_ Class
> Mat_ Class와 Mat Object는 간단하게 상호 변환이 가능<br>
> Mat_ 은 **<<**와 **,** Operator 를 이용해서 간단히 행렬 원소 값을 설정 가능함.<br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/3c5832a0-0e24-4d92-b68c-add82b31d00c)<br>
> ![image](https://github.com/god102104/openCV_Practice/assets/43011129/0f57e1ca-674e-44cd-a201-987776e60496)<br>



### Mat::create(int rows, int cols, int type)
> 비어 있는 Mat obejct 또는 이미 생성된 Mat object에 새로운 행렬을 할당 하려면, Mat::create()<br>
> 이미 행렬 데이터가 있을 때, Mat::create()를 호출하면 <br>
> 1. 행렬 크기와 타입이 같다면 -> 아무것도 하지 않고 함수 종료. <br>
> 2. 행렬 크기 또는 타입이 다르다면 -> 기존 **메모리 공간 해제 후** 새로운 행렬 데이터 저장을 위한 **메모리 공간 할당.** <br>
> Mat::create() 는 새로 만든 행렬의 원소 값을 **초기화 하는 기능이 없다.** 그래서 별도의 함수를 이용해줘야 함<br>
> 주로 **=** 연산자 또는 **setTo**(InputAraay value, InputArray masek = noArray()); 를 이용한다.<br>
<pre>
	<code>
		Mat mat4, mat5;
		mat4.create(256, 256, CV_8UC3);
		mat5.create(4, 4, CV_32FC1);
	
		mat4 = Scalar(255, 0, 0);
		mat5.setTo(1.f);
	
		imshow("mat4", mat4);
		imshow("mat5", mat5);
	</code>
</pre>
> 이렇게 코드를 돌리면, **mat5에서 오류** 발생한다.<br>
> imshow 는 unsigned char를 쓰기 때문인데, 이를 해결하기 위해서는 **cv2.normalize()** 함수로 Scaling 해줘야만 한다.<br>
> **normalize(mat5, mat5, 0, 255, NORM_MINMAX, CV_8U);**
