Day6
===

# 컬러 영상의 픽셀 값 참조

> 컬러 영상에서 하나의 픽셀은 **세 개의 색상 성분** <br>
> Vec3b 자료형을 사용해야 한다. (크기가 3인 uchar 자료형 배열을 member variable로 갖고 있음) <br>

### 색상 반전 예시 코드
<pre>
  <code>
    #include "opencv2/opencv.hpp"
    #include <iostream>
    
    using namespace cv;
    using namespace std;
    
    void color_op();
    void color_inverse();
    void color_grayscale();
    void color_split();
    
    int main(void)
    {
    	color_op();
    	color_inverse();
    	color_grayscale();
    	color_split();
    
    	return 0;
    }
    
    void color_op()
    {
    	Mat img = imread("butterfly.jpg", IMREAD_COLOR);
    
    	if (img.empty()) {
    		cerr << "Image load failed!" << endl;
    		return;
    	}
    
    	Vec3b& pixel = img.at<Vec3b>(0, 0);
    	uchar b1 = pixel[0];
    	uchar g1 = pixel[1];
    	uchar r1 = pixel[2];
    
    	Vec3b* ptr = img.ptr<Vec3b>(0);
    	uchar b2 = ptr[0][0];
    	uchar g2 = ptr[0][1];
    	uchar r2 = ptr[0][2];
    }
    
    void color_inverse()
    {
    	Mat src = imread("butterfly.jpg", IMREAD_COLOR);
    
    	if (src.empty()) {
    		cerr << "Image load failed!" << endl;
    		return;
    	}
    
    	Mat dst(src.rows, src.cols, src.type());
    
    	for (int j = 0; j < src.rows; j++) {
    		for (int i = 0; i < src.cols; i++) {
    			Vec3b& p1 = src.at<Vec3b>(j, i);
    			Vec3b& p2 = dst.at<Vec3b>(j, i);
    
    			p2[0] = 255 - p1[0]; // B
    			p2[1] = 255 - p1[1]; // G
    			p2[2] = 255 - p1[2]; // R
    		}
    	}
    
    	imshow("src", src);
    	imshow("dst", dst);
    
    	waitKey();
    	destroyAllWindows();
    }
    
    void color_grayscale()
    {
    	Mat src = imread("butterfly.jpg");
    
    	if (src.empty()) {
    		cerr << "Image load failed!" << endl;
    		return;
    	}
    
    	Mat dst;
    	cvtColor(src, dst, COLOR_BGR2GRAY);
    
    	imshow("src", src);
    	imshow("dst", dst);
    
    	waitKey();
    	destroyAllWindows();
    }
    
    void color_split()
    {
    	Mat src = imread("candies.png");
    
    	if (src.empty()) {
    		cerr << "Image load failed!" << endl;
    		return;
    	}
    
    	vector<Mat> bgr_planes;
    	split(src, bgr_planes);
    
    	imshow("src", src);
    	imshow("B_plane", bgr_planes[0]);
    	imshow("G_plane", bgr_planes[1]);
    	imshow("R_plane", bgr_planes[2]);
    
    	waitKey();
    	destroyAllWindows();
    }
  </code>
</pre>

![image](https://github.com/god102104/openCV_Practice/assets/43011129/226a3ce6-46c3-478c-b696-49a45e4fa4e9)

<pre>
  <code>
    for (int j = 0; j < src.rows; j++) {
      for (int i = 0; i < src.cols; i++) {
          dst.at<Vec3b>(j, i) = Vec3b(255, 255, 255) - src.at<Vec3b>(j, i);
      }
    }
  </code>
</pre>

> 위 처럼 간단하게 고치기도 가능. <br>

## 색 공간 변환
> OpenCV에서는 컬러 영상을 Mat 객체 저장할 때 BGR 표현 <br>
> 컬러 영상 처리에서는 색상 구분이 용이한 **HSV, HSL** 색 공간을 주로 이용. <br>
> OpenCV에서의 영상의 색 공간을 다른 색 공간으로 변환할 때에는 **cvtColor()** 함수를 사용. <br>

> **색상 정보의 활용도가 높지 않은 경우**에는 **Grayscale 로 변환하여 처리**하는 것이 효율적 <br>
> Color → grayscale 변환할 경우 아래의 공식 이용하는 것이 좋다. <br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/07905832-2104-45e0-a4ba-a5d7dafd1040)

![image](https://github.com/god102104/openCV_Practice/assets/43011129/be1989a8-3583-4bfd-a62f-437528c8bd82)

