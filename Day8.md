Day8
===

# 객체 검출
## 템플릿 매칭
> 입력 영상에서 작은 크기의 **부분 영상 위치**를 찾아내고 싶은 경우에 주로 **템플릿 매칭(template matching)** 기법을 사용 <br>
> 템플릿(template)은 찾고자 하는 대상이 되는 작은 크기의 영상 <br>
> 템플릿 매칭은 작은 크기의 템플릿 영상을 입력 영상 전체 영역에 대해 이동하면서 가장 비슷한 위치를 수치적으로 찾아내는 방식 <br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/779ce75d-61d8-46d8-b8d6-752d87f068d5)
>
> 입력 영상 전체 영역에 대해 이동하면서 <br>
> 템플릿 영상과 입력 영상 부분 영상과의 유사도(similarity) 또는 비유사도(dissimilarity)를 계산 <br>
> **matchTemplate()** 함수
> <pre>
>  <code>
>        void matchTemplate(InputArray image, InputArray templ,
>                   OutputArray result, int method, InputArray mask = noArray());
>  </code>
> </pre>
>
> templ : 템플릿 영상. 입력 영상 image보다 같거나 작아야 하며, image와 타입이 같아야 <br>
> mask : 찾고자 하는 템플릿의 마스크 영상. mask는 templ과 같은 크기, 같은 타입이어야  <br>


## QR코드 검출
### **QRCodeDetector::detect()** 함수
> <pre>
>  <code>
>    bool QRCodeDetector::detect(InputArray img, OutputArray points) const;
>  </code>
> </pre>
> points : (출력) QR 코드를 감싸는 사각형의 네 꼭지점 좌표 <br>
> return : QR코드 검출 성공 시 true <br>


### QR 코드에 저장된 문자열 추출 함수 **QRCodeDetector::decode()** <br>
> <pre>
>  <code>
>    std::string QRCodeDetector::decode(InputArray img, InputArray points, 
>     OutputArray straight_qrcode = noArray());    
>  </code>
> </pre>

### QR 코드 검출과 해석을 한꺼번에 **QRCodeDetector::detectAndDecode()** <br>


### 예제 코드
<pre>
  <code>
    #include "opencv2/opencv.hpp"
    #include <iostream>
    
    using namespace cv;
    using namespace std;
    
    void decode_qrcode();
    
    int main(void)
    {
    	decode_qrcode();
    
    	return 0;
    }
    
    void decode_qrcode()
    {
    	VideoCapture cap(0);
    
    	if (!cap.isOpened()) {
    		cerr << "Camera open failed!" << endl;
    		return;
    	}
    
    	QRCodeDetector detector;
    
    	Mat frame;
    	while (true) {
    		cap >> frame;
    
    		if (frame.empty()) {
    			cerr << "Frame load failed!" << endl;
    			break;
    		}
    
    		vector<Point> points;
    		String info = detector.detectAndDecode(frame, points);
    
    		if (!info.empty()) {
    			polylines(frame, points, true, Scalar(0, 0, 255), 2);
    			putText(frame, info, Point(10, 30), FONT_HERSHEY_DUPLEX, 1, Scalar(0, 0, 255));
    		}
    
    		imshow("frame", frame);
    		if (waitKey(1) == 27)
    			break;
    	}
    }
  </code>
</pre>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/4203b051-f18a-4b8a-98b9-f6ab09f4045f)


# 코너 검출

## 해리스 코너 검출 방법
> 기하학적 변환이 있어도 효과적으로 사용할 수 있는 지역 특징점 기반 매칭 방법. <br>
> 특징점(feature point) : 코너처럼 한 점의 형태로 표현할 수 있는 특징 <br>
> 해리스는 E(Δx, Δy)가 모든 방향으로 그 값이 크게 나타나는지를 검사하기 위해 테일러 급수(Taylor series), <br>
> 고윳값 분석(eigenvalue analysis) 등의 수학적 기법을 적용하여 코너 응답 함수 R을 유도 <br>
> ![image](https://github.com/god102104/openCV_Practice/assets/43011129/1158bb37-8fad-4344-9e40-dec0cb745bb7) <br>
> 앞 수식에서 Det()는 행렬식(determinant)을, Tr()은 대각합(trace)을 의미하고, 행렬 M은 다음과 같이 정의 <br>
> ![image](https://github.com/god102104/openCV_Practice/assets/43011129/22d69c0d-622b-4724-9a28-1be76f2b7576) <br>
> 앞 수식에서 Ix와 Iy는 입력 영상 I를 각각 x축 방향과 y축 방향으로 편미분한 결과입니다.<br>
> 코너 응답 함수 정의에서 상수 k는 보통 0.04~0.06 사이의 값을 사용<br>
> 해리스에 의해 정의된 코너 응답 함수 R은 입력 영상 각각의 픽셀에서 정의되는 실수 값이며,<br>
> 이 값을 분석하여 코너, 에지, 평탄한 영역을 판별할 수 있다. <br>
> R이 0보다 충분히 큰 양수이면 코너 점이라고 간주 <br>
> R이 0에 가까운 실수이면 평탄한 영역이고, 0보다 작은 음수이면 에지라고 판별 <br>
>
> 해리스 코너 응답 함수 값을 계산하는 **cornerHarris()** 함수 <br>
> <pre>
>  <code>
>    void cornerHarris(InputArray src, OutputArray dst, int blockSize,
>                  int ksize, double k, int borderType = BORDER_DEFAULT);
>  </code>
> </pre>
> blockSize : 행렬 M 연산에 사용할 이웃 픽셀 크기. 픽셀 주변 blockSize×blockSize 윈도우를 설정하여 행렬 M을 계산 <br>
> k : 해리스 코너 검출 상수 <br>

### 해리스 코너 검출 예제 코드
<pre>
  <code>
    #include "opencv2/opencv.hpp"
    #include <iostream>
    
    using namespace cv;
    using namespace std;
    
    void corner_harris();
    void corner_fast();
    
    int main(void)
    {
    	corner_harris();
    	corner_fast();
    
    	return 0;
    }
    
    void corner_harris()
    {
    	Mat src = imread("building.jpg", IMREAD_GRAYSCALE);
    
    	if (src.empty()) {
    		cerr << "Image load failed!" << endl;
    		return;
    	}
    
    	Mat harris;
    	cornerHarris(src, harris, 3, 3, 0.04);
    
    	Mat harris_norm;
    	normalize(harris, harris_norm, 0, 255, NORM_MINMAX, CV_8U);
    
    	Mat dst;
    	cvtColor(src, dst, COLOR_GRAY2BGR);
    
    	for (int j = 1; j < harris.rows - 1; j++) {
    		for (int i = 1; i < harris.cols - 1; i++) {
    			if (harris_norm.at<uchar>(j, i) > 120) {
    				if (harris.at<float>(j, i) > harris.at<float>(j - 1, i) &&
    					harris.at<float>(j, i) > harris.at<float>(j + 1, i) &&
    					harris.at<float>(j, i) > harris.at<float>(j, i - 1) &&
    					harris.at<float>(j, i) > harris.at<float>(j, i + 1)) {
    					circle(dst, Point(i, j), 5, Scalar(0, 0, 255), 2);
    				}
    			}
    		}
    	}
    
    	imshow("src", src);
    	imshow("harris_norm", harris_norm);
    	imshow("dst", dst);
    
    	waitKey();
    	destroyAllWindows();
    }
    
    void corner_fast()
    {
    	Mat src = imread("building.jpg", IMREAD_GRAYSCALE);
    
    	if (src.empty()) {
    		cerr << "Image load failed!" << endl;
    		return;
    	}
    
    	vector<KeyPoint> keypoints;
    	FAST(src, keypoints, 60, true);
    
    	Mat dst;
    	cvtColor(src, dst, COLOR_GRAY2BGR);
    
    	for (KeyPoint kp : keypoints) {
    		Point pt(cvRound(kp.pt.x), cvRound(kp.pt.y));
    		circle(dst, pt, 5, Scalar(0, 0, 255), 2);
    	}
    
    	imshow("src", src);
    	imshow("dst", dst);
    
    	waitKey();
    	destroyAllWindows();
    }

  </code>
</pre>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/c03fbf69-45b9-4536-8c9a-cbc8821e9972)


## FAST 코너 검출 방법
> 단순한 픽셀 값 비교 방법을 통해 코너를 검출 <br>
> 매우 빠르게 동작하는 코너 검출 방법 <br>
> 영상의 모든 픽셀에서 픽셀을 둘러싸고 있는 16개의 주변 픽셀과 밝기를 비교하여 코너 여부를 판별 <br>
> ![image](https://github.com/god102104/openCV_Practice/assets/43011129/ed6b9948-dbc7-40b5-a7a7-448cd1d3dead)
> p에서의 밝기를 Ip, 만약 주변 16개의 픽셀 중에서 그 값이 Ip+t보다 큰 픽셀이 아홉 개 이상 연속으로 나타나면 <br>
> 점 p는 어두운 영역이 뾰족하게 돌출되어 있는 코너 <br>
> 특정 코너 점 **주변 픽셀들도 함께 코너로 검출하는 경우가 많기 때문에** <br>
> 주변 코너 픽셀 중에서 가장 코너에 적합한 픽셀을 선택하는 <br>
> **비최대 억제 작업을 추가적으로** 수행하는 것이 좋음. <br>
> **FAST()** 함수
> <pre>
>  <code>
>    void FAST(InputArray image, std::vector<KeyPoint>& keypoints,
>          int threshold, bool nonmaxSuppression = true);
>  </code>
> </pre>
> **nonmaxSuppression** : 비최대 억제 수행 여부. true이면 비최대 억제를 수행. <br>
