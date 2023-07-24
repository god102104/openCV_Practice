Day5
===

# 어파인 변환 
![image](https://github.com/god102104/openCV_Practice/assets/43011129/925407d9-8bfc-4c59-893d-c34490b01468)
> 위와 같은 **2X3** 형태의 행렬을 어파인 행렬이라고 하고, 유도식은 다음과 같다. <br>


![image](https://github.com/god102104/openCV_Practice/assets/43011129/89b983b3-a2d1-4a1e-8494-bf3a400e7bce)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/4807b05f-518e-4e1d-9e69-9f9a1bddb3bc)

> 입력 영상의 좌표 (x,y)에 가상의 좌표 1 추가
![image](https://github.com/god102104/openCV_Practice/assets/43011129/981768bd-b8b4-4eaf-83ad-709316e561e5)


> **getAffineTransform()** 함수 <br> 
> 입력 영상에서 세 점의 좌표와 <br>
> 이 점들이 이동한 결과 영상의 좌표 세 개를 입력으로 받아 <br>
> 2×3 어파인 변환 행렬을 계산 <br>

> **warpAffine()** 함수 <br>
> 2×3 어파인 변환 행렬을 가지고 있을 때, 영상을 **어파인 변환한 결과 영상**을 생성 <br>
<pre>
  <code>
    
void warpAffine(InputArray src, OutputArray dst,
                InputArray M, Size dsize,
                int flags = INTER_LINEAR,
                int borderMode = BORDER_CONSTANT,
                const Scalar& borderValue = Scalar());
  </code>
</pre>

> • src : 입력 영상 <br>
> • dst : 결과 영상. src와 같은 타입이고, 크기는 dsize에 의해 결정. <br>
> • M : 2×3 어파인 변환 행렬 <br>
> • dsize : 결과 영상 크기 <br>
> • flags : 보간법 알고리즘. 만약 OR 연산자를 이용하여 <br>
> WARP_INVERSE_MAP 플래그를 함께 지정하면 역방향으로 변환을 수행. <br>
> • borderMode : 가장자리 픽셀 확장 방식. BorderTypes 열거형 상수 중 하나를 지정. <br>
> 만약 BORDER_TRANSPARENT를 지정하면 입력 영상의 픽셀 값이 복사되지 않는 영역은 dst 픽셀 값을 그대로 유지.
> • borderValue : borderMode가 BORDER_CONSTANT일 때 사용할 상수 값. 기본값으로 검은색이 지정되어 있음.
