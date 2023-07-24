
Day 4
===
# 영상의 산술 연산

영상은 기본적으로 2차원 행렬이므로 산술 연산 (arithmetic operation)을 그대로 적용 가능.
### 덧셈 연산 예시
![image](https://github.com/god102104/openCV_Practice/assets/43011129/8e5f625b-865f-4e1d-a83a-fe728fb8c589)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/9fb36b06-5f84-4fcf-b9c8-858d6e43965e)
> α+β=1이면 결과 영상에서 포화되는 픽셀이 발생하지 않습니다. <br>
> 만약 α=0.1, β=0.9로 설정하면 src1 영상의 윤곽은 조금만 나타나고 <br>
> src2 영상의 윤곽은 많이 나타나는 결과 영상이 생성됩니다. <br>
<pre>
  <code>
    Mat src1 = imread("aero2.bmp", IMREAD_GRAYSCALE);
    Mat src2 = imread("camera.bmp", IMREAD_GRAYSCALE);
    
    Mat dst;
    addWeighted(src1, 0.5, src2, 0.5, 0, dst);
  </code>
</pre>
> 두 입력 영상의 평균 영상을 생성하는 코드
![image](https://github.com/god102104/openCV_Practice/assets/43011129/26ec52fe-f194-4439-a118-ac536dc6e5b7)

### 뺄셈도 마찬가지지만, 두 입력 영상 type이 다르다면 -가 아니라 subtract() 를 써야한다.
> 덧셈 연산과 달리 뺄셈 연산은 뺄셈의 대상이 되는 영상 순서에 따라 결과가 달라진다.
![image](https://github.com/god102104/openCV_Practice/assets/43011129/433f5f58-09e1-46c7-94f0-d3b7fd60ca1b)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/526e1f0d-560e-43e9-bb48-3dca4010b484)
> 위와 같은 예시를 통해 연산 순서의 중요성을 알 수 있음.
