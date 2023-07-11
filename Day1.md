Day 1 
=====
Grayscale image 를 이용할 때 C/C++ 에서는 주로 unsigned char를 이용한다. 
unsigned char는 1byte 크기를 가지며 부호 없는 8bit int 값을 저장할 수 있는데, 이는 0~255 를 의미한다.
그러므로 Grayscale 값을 표현하기 가장 적절한 자료형이다.

openCV function 관련
---
### Mat  imread(const String& filename, int flags = IMREAD_COLOR);
> filename 파일을 불러와서 Mat object 로 변환하여 반환
> 파일이 존재하지 않거나 잘못된 형식의 경우, Return empty Mat object
> imread()를 사용하려고 하는 경우 Mat::empty()를 이용하여 Object 생성 여부를 확인하자.

### Mat imwrite(const String& filename, InputArray img, const std::vector<int>& params = std::vector<int>());
> img 를 filename 이름으로 저장
> filename 문자열에 포함된 확장자로 결정

<pre>
  <code>
    vector<int> params;
      params.push_back(IMWRITE_JPEG_QUALITY);
      params.push_back(95);
      imwrite("lena.jpg", img, params);
  </code>
</pre>

> IMWRITE_JPEG_QUALITY 플래그가 JPEG 압축률을 나타내는 옵션 플래그임.
> 상세한 내용은 OpenCV 문서 사이트 참조

### Point_ Class
> Template class 이므로, 어떤 자료형으로 좌표를 표현할지를 명시해야 한다.
> int 자료형 쓰고 싶다면 Point2i, float 쓰고 싶다면 Point2f 를 쓰면 된다.

<pre>
  <code>
    Point pt1;
    pt1.x = 5;
    pt1.y = 10;
    Point pt2(10, 30);
  </code>
</pre>

> 위의 코드에서 pt1은 기본 생성자를 사용하여 생성되었으므로 처음에는 pt1.x, pt1.y 는 둘 다 0으로 만들어진다.

### Size_ Class
> template class
> width와 height 라는 member variable 을 갖고 있음.
> int 쓰고 싶다면 Size2i, float 쓰고 싶다면 Size2f 쓰면 된다.
> Size Object 끼리 덧셈 연산을 하면 가로 세로를 더한 새로운 Object를 생성한다.

### Rect_ Class
> 사각형의 위치와 크기 정보
> template class
> Rect_ Object 끼리 & 와 | 를 이용한 연산이 가능하다.

![ex_screenshot]([./img/screenshot.png](https://postfiles.pstatic.net/MjAyMTA1MDlfMjgx/MDAxNjIwNTUwODE5NjU5.sHiYnIJZ0NA6iP4l6xQALluU8NyVVTt9-Dm5dEieT7sg.OekYqTLPwnJdYHNz2G1uGqJ3iipr6ARN_FmsOorIm-Yg.JPEG.sees111/%EC%BA%A1%EC%B2%98.JPG?type=w966)https://postfiles.pstatic.net/MjAyMTA1MDlfMjgx/MDAxNjIwNTUwODE5NjU5.sHiYnIJZ0NA6iP4l6xQALluU8NyVVTt9-Dm5dEieT7sg.OekYqTLPwnJdYHNz2G1uGqJ3iipr6ARN_FmsOorIm-Yg.JPEG.sees111/%EC%BA%A1%EC%B2%98.JPG?type=w966)

