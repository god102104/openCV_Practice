Day 3
===
# 영상의 밝기 조절

## Grayscale 영상 다루기
> Grayscale 영상을 저장할 새로운 Mat object 생성하려면 **CV_8UC1** 타입 Object 생성해야 함. <br>
> 이미 3채널 컬러 영상을 가지고 있는데, 이를 Grayscale 로 변환하려면 **cvtColor()** 함수를 사용해야 한다. <br>

## 영상의 밝기 조절
> 간단히 좌표에 값을 더해주면 끝 <br>
> 최댓값 255로, 최솟값은 0으로 설정해주는 과정이 필요하다. <br>
> 삼항 조건 연산자를 이용하면 좋다. <br>
> 트랙바를 이용한 밝기 조절 기능을 추가하는 것도 좋다. <br>
> 하지만... 픽셀 값에 상수를 더하는 방식은 **명암비** 를 조절하는데는 적절하지 않다. <br>
> 명암비는 밝은 픽셀은 더욱 밝게, 어두운 픽셀은 더욱 어둡게 해야한다. <br>
> 일반적으로 Grayscale 의 중간 값인 128 기준으로 더 크게 또는 더 낮게 만든다. <br>

## 히스토그램 분석
![image](https://github.com/god102104/openCV_Practice/assets/43011129/3081f341-02c0-4941-b7ed-979d5f845d5f)
> **Grayscale** 히스토그램은 위와 같이 **0~255** 까지의 값을 갖는다. <br>
> 막대 하나를 **bin**이라 부름. <br>
> 히스토그램의 bin 갯수가 항상 픽셀 값 범위와 같아야 하는 것은 아님.
> calcHist() 함수를 이용하면 히스토그램을 구할 수 있지만, 복잡하다.

<pre>
  <code>
    
      void cv::calcHist(const Mat* images,
      int nimages, 
      const int* channels, 
      InputArray mask, 
      OutputArray hist, 
      int dims, 
      const int*	histSize,
      const float ** 	ranges,
      bool 	uniform = true,
      bool 	accumulate = false 
      )	
  </code>
</pre>
