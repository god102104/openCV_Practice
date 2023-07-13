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
> **calcHist()** 함수를 이용하면 히스토그램을 구할 수 있지만, 복잡하다.

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
      bool 	accumulate = false)	
  </code>
</pre>

> uniform 과 accumulate 는 default parameter가 있다. (각각 true, false) <br>
> 이 경우 hist 배열을 0으로 초기화 한 후 등간격 히스토그램을 계산. <br>
> calcGrayHist()는 Grayscale 영상 히스토그램. <br>
> 히스토그램의 픽셀 분포 그래프를 통해 영상의 밝기와 명암비를 가늠할 수 있다. <br>


### 히스토그램 스트레칭 (Histogram stretching)
> 영상의 히스토그램이 전 구간에 걸쳐 나타나도록 변경하는 선형 변환 기법 <br>
> 명암비가 높아지므로 대체로 보기 좋은 사진이 됨. <br>
> **OpenCV에서 따로 제공하는 함수가 없음**
<pre>
  <code>
        void histogram_stretching()
    {
    	Mat src = imread("hawkes.bmp", IMREAD_GRAYSCALE);
    
    	if (src.empty()) {
    		cerr << "Image load failed!" << endl;
    		return;
    	}
    
    	double gmin, gmax;
    	minMaxLoc(src, &gmin, &gmax);
    
    	Mat dst = (src - gmin) * 255 / (gmax - gmin);
    
    	imshow("src", src);
    	imshow("srcHist", getGrayHistImage(calcGrayHist(src)));
    
    	imshow("dst", dst);
    	imshow("dstHist", getGrayHistImage(calcGrayHist(dst)));
    
    	waitKey();
    	destroyAllWindows();
    }
  </code>
</pre>


### 히스토그램 평활화 (Histogram equalization)
> 영상의 픽셀 값 분포가 Grayscale 전체 영역에서 골고루 나타나도록. <br>
> equalizeHist() <br>
<pre>
  <code>
    void cv::equalizeHist(InputArray src, OutputArray dst)	
  </code>
</pre>
> CV_8CU1 (Grayscale 영상만 input으로 넣을 수 있다.) <br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/8daba3c1-eab6-4dba-b22b-6bcb6accf297)

