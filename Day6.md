![image](https://github.com/god102104/openCV_Practice/assets/43011129/6b5c43e6-2829-4ab4-9dc4-a2e11a833fa9)Day6
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

![image](https://github.com/god102104/openCV_Practice/assets/43011129/abdc3947-b4bd-4a71-aa07-87699e28bcea)


## 색상 채널 나누기
> **split()** 함수
<pre>
  <code>
    void split(const Mat& src, Mat* mvbegin);
    void split(InputArray src, OutputArrayOfArrays mv);
  </code>
</pre>

> mv : 분리된 1 채널 행렬을 저장할 벡터 <br>
> mvbegin : 분리된 1채널 행렬을 저장할 Mat 배열 주소. 영상 배열 개수는 src 영상 채널 수와 같아야. <br>

> 합치고 싶은 경우에는 **merge()**
<pre>
  <code>
    void merge(const Mat* mv, size_t count, OutputArray dst);
    void merge(InputArrayOfArrays mv, OutputArray dst);
  </code>
</pre>

> 분리된 각 채널은 CV_8UC1 타입의 Grayscale 임. (즉, imshow()로 볼 수 있다.) <br>

![image](https://github.com/god102104/openCV_Practice/assets/43011129/202c438b-6b92-493b-9dff-120a7b44dbd4)


## 컬러 히스토그램 평활화
> 이전에 학습한 히스토그램 정보를 이용하여 명암비를 증가시키는 히스토그램 평활화 기법 <br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/bdce803f-6dcd-456a-a3e8-b52e70e57e7b)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/def311e7-de08-432d-8343-aa04b95c286d)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/87184e72-b74b-4241-92a1-496842e6efd4)

> 위는 잘못된 사용 방법 <br>
> 원본 영상과 다른 색상의 결과 영상이 만들어진다. <br>

![image](https://github.com/god102104/openCV_Practice/assets/43011129/7f27aead-d783-4c41-a790-915599d1ce41)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/3a883234-36b9-40d1-a289-564d8ecbffe5)

> 제대로 된 사용 방법 <br>
> 색감은 변경하지 않고 명암비만 높힘 (영상의 밝기 정보만을 이용)
> 입력 영상을 밝기와 색상으로 분리 후 히스토그램 평활화

## 색상 범위 지정에 의한 영역 분할
> 컬러 영상에서 R,G, 등의 대표적인 색상 영역을 구분할 때에는 RGB 보단 HSV 가 유리 <br>
> **HSV**에서 녹색은 H값이 60 근방이므로, 60근처의 픽셀을 찾아 녹색 픽셀 검출 가능. <br>
> 이 때, **inRange()** 함수를 이용 <br>

<pre>
  <code>
      void inRange(InputArray src, InputArray lowerb,
               InputArray upperb, OutputArray dst);
  </code>
</pre>

> lowerb : 하한 값 (Mat or Scalar) <br>
> upperb : 상한 값 (Mat or Scalar) <br>
> 입력 영상 src의 픽셀 값이 지정한 밝기 또는 색상 범위에 포함되어 있으면 흰색, <br>
> 그렇지 않으면 검은색으로 채워진 마스크 영상 dst를 반환 <br>

![image](https://github.com/god102104/openCV_Practice/assets/43011129/ccd5a187-879f-4ae2-918b-f8998e917740)


## 히스토그램 역투영 (histogram backprojection)
> inRange() 로 영역 검출하는 방식의 한계점으로 만든 방법 <br>
> (사람의 피부색처럼 미세한 변화가 있거나 색상 값을 수치적으로 지정하기 어려운 경우에는 적합하지 않음) <br>
> 기준 영상으로부터 찾고자 하는 **객체의 컬러 히스토그램을 미리 구하고**, <br>
> 주어진 입력 영상에서 **해당 히스토그램에 부합하는 영역을 찾아내는 방식** <br>
> calcBackProject() <br>

<pre>
  <code>
      void calcBackProject(const Mat* images, int nimages,
       const int* channels, InputArray hist,
       OutputArray backProject, const float** ranges,
       double scale = 1, bool uniform = true);
  </code>
</pre>

> backProject : 출력 히스토그램 역투영 영상. 입력 영상과 같은 크기, 같은 깊이를 갖는 1채널 행렬 <br>
