
===
# 레이블링
> 레이블링(labeling) : 객체 픽셀 집합에 고유 번호를 매기는 작업. <br>
> 전처리 과정으로 주로 쓰임. <br>
> 주로 이진화된 영상에서 수행 <br>
> 검은색 픽셀은 배경으로 간주하고, 흰색 픽셀은 객체로 간주 <br>
> 나의 객체는 한 개 이상의 인접한 픽셀 <br>
> 하나의 객체를 구성하는 모든 픽셀에는 같은 레이블 번호 <br>
> 4-방향 연결성(4-way connectivity) 또는  8-방향 연결성(8-way connectivity) <br>
> ![image](https://github.com/god102104/openCV_Practice/assets/43011129/bc86780e-0266-49a6-99be-401e218b08d6) <br>
> 아래는 생성된 레이블 맵 <br>
> ![image](https://github.com/god102104/openCV_Practice/assets/43011129/39757b1a-15ac-40a0-8a2c-c295d90e8fb7) <br>
> **connectedComponents()** 함수 <br>
<pre>
  <code>
        int connectedComponents(InputArray image, OutputArray labels,
            int connectivity = 8, int ltype = CV_32S);
  </code>
</pre>
> connectivity : 연결성. 8 또는 4를 지정할 수 있음. <br>
> 반환값 : 레이블 개수. 반환값이 N이면 0부터 N-1까지의 레이블 번호가 존재하며, 이 중 0번 레이블은 배경을 나타냄. 실제 객체 개수는 N-1. <br>

## 레이블링 응용
> **connectedComponentsWithStats()** 함수, **레이블 맵**과 각 **객체 영역의 통계 정보**를 한꺼번에 반환 <br> 
> ![image](https://github.com/god102104/openCV_Practice/assets/43011129/2d0fb1f9-a4a1-4c5b-b319-50ad20a56a20)
> 레이블링을 응용해서 바운딩 박스 만들 수 있음. 아래 코드 참조. <br>

### 레이블링 예제 코드
<pre>
  <code>
    #include "opencv2/opencv.hpp"
    #include <iostream>
    
    using namespace cv;
    using namespace std;
    
    void labeling_basic();
    void labeling_stats();
    
    int main()
    {
    	labeling_basic();
    	labeling_stats();
    
    	return 0;
    }
    
    void labeling_basic()
    {
    	uchar data[] = {
    		0, 0, 1, 1, 0, 0, 0, 0,
    		1, 1, 1, 1, 0, 0, 1, 0,
    		1, 1, 1, 1, 0, 0, 0, 0,
    		0, 0, 0, 0, 0, 1, 1, 0,
    		0, 0, 0, 1, 1, 1, 1, 0,
    		0, 0, 0, 1, 0, 0, 1, 0,
    		0, 0, 1, 1, 1, 1, 1, 0,
    		0, 0, 0, 0, 0, 0, 0, 0,
    	};
    
    	Mat src = Mat(8, 8, CV_8UC1, data) * 255;
    
    	Mat labels;
    	int cnt = connectedComponents(src, labels);
    
    	cout << "src:\n" << src << endl;
    	cout << "labels:\n" << labels << endl;
    	cout << "number of labels: " << cnt << endl;
    }
    
    void labeling_stats()
    {
    	Mat src = imread("keyboard.bmp", IMREAD_GRAYSCALE);
    
    	if (src.empty()) {
    		cerr << "Image load failed!" << endl;
    		return;
    	}
    
    	Mat bin;
    	threshold(src, bin, 0, 255, THRESH_BINARY | THRESH_OTSU);
    
    	Mat labels, stats, centroids;
    	int cnt = connectedComponentsWithStats(bin, labels, stats, centroids);
    
    	Mat dst;
    	cvtColor(src, dst, COLOR_GRAY2BGR);
    
    	for (int i = 1; i < cnt; i++) {
    		int* p = stats.ptr<int>(i);
    
    		if (p[4] < 20) continue;
    
    		rectangle(dst, Rect(p[0], p[1], p[2], p[3]), Scalar(0, 255, 255));
    	}
    
    
    	imshow("src", src);
    	imshow("dst", dst);
    
    	waitKey();
    	destroyAllWindows();
    }
  </code>
</pre>

![image](https://github.com/god102104/openCV_Practice/assets/43011129/f61080a6-e65d-42fc-87a5-42183647b435)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/5fe51659-0ea4-4c48-b333-f9b8768d1306)


# 외곽선 검출
![image](https://github.com/god102104/openCV_Practice/assets/43011129/d65281f4-699d-4059-89a2-4064b201ce30) <br>
> **findContours()** 함수
<pre>
  <code>
    void findContours(InputArray image, OutputArrayOfArrays contours,
                      OutputArray hierarchy, int mode,
                      int method, Point offset = Point());
    void findContours(InputArray image, OutputArrayOfArrays contours,
                      int mode, int method, Point offset = Point());
  </code>
</pre>
> **contours** : 검출된 외곽선 정보. vector<vector<Point>> 타입의 변수를 지정 <br>
> hierarchy : 외곽선 계층 정보. vector<Vec4i> 타입의 변수를 지정 <br>
> mode : 외곽선 검출 모드. RetrievalModes 열거형 상수를 지정 <br>
> method : 외곽선 근사화 방법. ContourApproximationModes 열거형 상수를 지정 <br>
> offset : 외곽선 점 좌표의 오프셋(이동 변위) <br>
> 입력 영상으로는 threshold() 등으로 만들어진 이진 영상 <br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/3219258f-fdc0-4b39-aa94-097624d9bede)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/1b5ce341-43a7-4de1-9db2-18bc85738cc7)

### 방식에 따라 다른 외곽 검출
![image](https://github.com/god102104/openCV_Practice/assets/43011129/43c38112-c2f5-49b3-809d-b42b7c830156)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/fce54163-c248-4c3f-92b0-adc0a5045cd3)
> RETR_EXTERNAL 외곽선 검출 모드를 사용하면 흰색 객체의 바깥쪽 외곽선만 검출<br>
> 체 내부의 홀 외곽선은 검출되지 않음<br>
> RETR_LIST 검출 모드를 사용하면 바깥쪽과 안쪽 홀 외곽선을 모두 검출<br>
> RETR_EXTERNAL 또는 RETR_LIST 모드를 사용할 경우, 외곽선의 부모/자식 계층 정보는 생성되지 않음<br>
> RETR_CCOMP로 설정하면 모든 흰색 객체의 바깥쪽 외곽선을 먼저 검출하고, 각 객체 안의 홀 외곽선을 자식 외곽선으로 설정<br>
> RETR_CCOMP 모드에서는 상하 계층이 최대 두 개 층으로만 구성. 만약 흰색 객체에 여러 개의 홀이 존재할 경우, 그중 하나만 자식 외곽선으로 설정<br>
RETR_TREE로 설정하면 외곽선 전체의 계층 구조를 생성. 만약 객체 내부에 홀이 있고, 그 홀 안에 또 다른 작은 객체가 있다면 작은 객체의 외곽선은 홀 외곽선의 자식으로 설정<br>

> findContours() 함수로 검출한 외곽선 정보를 이용하여 영상 위에 외곽선을 그리고 싶다면 **drawContours()** 함수 <br>
<pre>
  <code>
    void drawContours(InputOutputArray image, InputArrayOfArrays contours,
                      int contourIdx, const Scalar& color,
                      int thickness = 1, int lineType = LINE_8,
                      InputArray hierarchy = noArray(),
                      int maxLevel = INT_MAX, Point offset = Point());
  </code>
</pre>
> thickness : 외곽선 두께. FILLED 또는 -1을 지정하면 외곽선 내부를 채움 <br>
> maxLevel : 그릴 외곽선의 최대 레벨. 이 값이 0이면 지정한 번호의 외곽선만 그리고, 1보다 같거나 크면 그에 해당하는 하위 레벨의 외곽선까지<br>
> contourIdx : 외곽선 번호. 음수를 지정하면 전체 외곽선 <br>

### 외곽선 예제 코드
<pre>
  <code>
    #include "opencv2/opencv.hpp"
    #include <iostream>
    
    using namespace cv;
    using namespace std;
    
    void contours_basic();
    void contours_hier();
    
    int main(void)
    {
    	contours_basic();
    	contours_hier();
    
    	return 0;
    }
    
    void contours_basic()
    {
    	Mat src = imread("contours.bmp", IMREAD_GRAYSCALE);
    
    	if (src.empty()) {
    		cerr << "Image load failed!" << endl;
    		return;
    	}
    
    	vector<vector<Point>> contours;
    	findContours(src, contours, RETR_LIST, CHAIN_APPROX_NONE);
    
    	Mat dst;
    	cvtColor(src, dst, COLOR_GRAY2BGR);
    
    	for (int i = 0; i < contours.size(); i++) {
    		Scalar c(rand() & 255, rand() & 255, rand() & 255);
    		drawContours(dst, contours, i, c, 2);
    	}
    
    	imshow("src", src);
    	imshow("dst", dst);
    
    	waitKey();
    	destroyAllWindows();
    }
    
    void contours_hier()
    {
    	Mat src = imread("contours.bmp", IMREAD_GRAYSCALE);
    
    	if (src.empty()) {
    		cerr << "Image load failed!" << endl;
    		return;
    	}
    
    	vector<vector<Point> > contours;
    	vector<Vec4i> hierarchy;
    	findContours(src, contours, hierarchy, RETR_CCOMP, CHAIN_APPROX_SIMPLE);
    
    	Mat dst;
    	cvtColor(src, dst, COLOR_GRAY2BGR);
    
    	for (int idx = 0; idx >= 0; idx = hierarchy[idx][0]) {
    		Scalar c(rand() & 255, rand() & 255, rand() & 255);
    		drawContours(dst, contours, idx, c, -1, LINE_8, hierarchy);
    	}
    
    	imshow("src", src);
    	imshow("dst", dst);
    
    	waitKey();
    	destroyAllWindows();
    }
  </code>
</pre>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/8ea67095-8324-4f90-a788-66f3325c6f58)


## 외곽선 처리 함수
> 외곽선 점들을 감싸는 가장 작은 크기의 사각형 **바운딩 박스** 구하는 함수 **boundingRect()** <br>
<pre>
  <code>
    Rect boundingRect(InputArray points);
  </code>
</pre>
> 특정 객체의 바운딩 박스는 connectComponentsWithStats() 함수를 이용해서도 구할 수 있음.<br>
> 다만 이미 외곽선 정보를 가지고 있는 경우에는 boundingRect() 함수를 이용하여 바운딩 박스를 구하는 것이 효율적.<br>
> return : 력 점들을 감싸는 최소 크기의 **사각형**<br>

> 외곽선 또는 점들을 감싸는 최소 크기의 회전된 사각형을 구하고 싶을 때에는 **minAreaRect()** 함수<br>
> RotatedRect 클래스 객체를 반환 <br>
<pre>
  <code>
    RotatedRect minAreaRect(InputArray points);
  </code>
</pre>
> return : 입력 점들을 감싸는 최소 크기의 **회전된** 사각형<br>

> 외곽선 또는 점들을 감싸는 최소 크기의 원을 구하고 싶을 때에는 **minEnclosingCircle()** 함수 <br>
<pre>
  <code>
    void minEnclosingCircle(InputArray points,
            Point2f& center, float& radius);
  </code>
</pre>

> 임의의 곡선을 형성하는 점들의 집합을 가지고 있을 때, 해당 곡선의 길이를 구하고 싶다면 **arcLength()** 함수 <br>
> return : 입력 곡선의 길이 <br>

> 외곽선이 감싸는 영역의 면적을 알고 싶다면 **contourArea()** 함수 <br>
<pre>
  <code>
    double contourArea(InputArray contour, bool oriented = false);
  </code>
</pre>
> return : 입력 **곡선이 감싸는 면적** <br>

> 외곽선 또는 곡선을 근사화하는 **approxPolyDP()** 함수. <br>
> 주어진 곡선의 형태를 단순화하여 작은 개수의 점으로 구성된 곡선을 생성 <br>
<pre>
  <code>
        void approxPolyDP(InputArray curve, OutputArray approxCurve,
                      double epsilon, bool closed);
  </code>
</pre>
> closed : true 면 폐곡선 <br>

### 예제 코드
<pre>
  <code>
    #include "opencv2/opencv.hpp"
    #include <iostream>
    
    using namespace cv;
    using namespace std;
    
    void setLabel(Mat& img, const vector<Point>& pts, const String& label)
    {
    	Rect rc = boundingRect(pts);
    	rectangle(img, rc, Scalar(0, 0, 255), 1);
    	putText(img, label, rc.tl(), FONT_HERSHEY_PLAIN, 1, Scalar(0, 0, 255));
    }
    
    int main(int argc, char* argv[])
    {
    	Mat img = imread("polygon.bmp", IMREAD_COLOR);
    
    	if (img.empty()) {
    		cerr << "Image load failed!" << endl;
    		return -1;
    	}
    
    	Mat gray;
    	cvtColor(img, gray, COLOR_BGR2GRAY);
    
    	Mat bin;
    	threshold(gray, bin, 200, 255, THRESH_BINARY_INV | THRESH_OTSU);
    
    	vector<vector<Point>> contours;
    	findContours(bin, contours, RETR_EXTERNAL, CHAIN_APPROX_NONE);
    
    	for (vector<Point> pts : contours) {
    		if (contourArea(pts) < 400)
    			continue;
    
    		vector<Point> approx;
    		approxPolyDP(pts, approx, arcLength(pts, true) * 0.02, true);
    
    		int vtc = (int)approx.size();
    
    		if (vtc == 3) {
    			setLabel(img, pts, "TRI");
    		}
    		else if (vtc == 4) {
    			setLabel(img, pts, "RECT");
    		}
    		else {
    			double len = arcLength(pts, true);
    			double area = contourArea(pts);
    			double ratio = 4. * CV_PI * area / (len * len);
    
    			if (ratio > 0.85) {
    				setLabel(img, pts, "CIR");
    			}
    		}
    	}
    
    	imshow("img", img);
    
    	waitKey();
    	return 0;
    }
  </code>
</pre>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/f1a53323-51db-45bb-afd4-6ce18f1cd23f)
