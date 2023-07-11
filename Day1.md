Day 1 
=====
Grayscale image 를 이용할 때 C/C++ 에서는 주로 unsigned char를 이용한다. 
unsigned char는 1byte 크기를 가지며 부호 없는 8bit int 값을 저장할 수 있는데, 이는 0~255 를 의미한다.
그러므로 Grayscale 값을 표현하기 가장 적절한 자료형이다.

openCV function 관련
---
Mat  imread(const String& filename, int flags = IMREAD_COLOR);
> filename 파일을 불러와서 Mat object 로 변환하여 반환
