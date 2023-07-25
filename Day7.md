Day7  
===

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
