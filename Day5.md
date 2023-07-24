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
> • M : 2×3 어파인 변환 행렬 (CV_32FC1 또는 CV_64FC1 타입이어야)  <br>
> • dsize : 결과 영상 크기 <br>
> • flags : 보간법 알고리즘. 만약 OR 연산자를 이용하여 <br>
> WARP_INVERSE_MAP 플래그를 함께 지정하면 역방향으로 변환을 수행. <br>
> • borderMode : 가장자리 픽셀 확장 방식. BorderTypes 열거형 상수 중 하나를 지정. <br>
> 만약 BORDER_TRANSPARENT를 지정하면 입력 영상의 픽셀 값이 복사되지 않는 영역은 dst 픽셀 값을 그대로 유지.
> • borderValue : borderMode가 BORDER_CONSTANT일 때 사용할 상수 값. 기본값으로 검은색이 지정되어 있음.

### 어파인 변환 예시 코드
<pre>
  <code>
    #include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

void affine_transform();
void affine_translation();
void affine_shear();
void affine_scale();
void affine_rotation();
void affine_flip();

int main(void)
{
	affine_transform();
	affine_translation();
	affine_shear();
	affine_scale();
	affine_rotation();
	affine_flip();

	return 0;
}

void affine_transform()
{
	Mat src = imread("tekapo.bmp");

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	Point2f srcPts[3], dstPts[3];
	srcPts[0] = Point2f(0, 0);
	srcPts[1] = Point2f(src.cols - 1, 0);
	srcPts[2] = Point2f(src.cols - 1, src.rows - 1);
	dstPts[0] = Point2f(50, 50);
	dstPts[1] = Point2f(src.cols - 100, 100);
	dstPts[2] = Point2f(src.cols - 50, src.rows - 50);

	Mat M = getAffineTransform(srcPts, dstPts);

	Mat dst;
	warpAffine(src, dst, M, Size());

	imshow("src", src);
	imshow("dst", dst);

	waitKey();
	destroyAllWindows();
}

void affine_translation()
{
	Mat src = imread("tekapo.bmp");

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	Mat M = Mat_<double>({ 2, 3 }, { 1, 0, 150, 0, 1, 100 });

	Mat dst;
	warpAffine(src, dst, M, Size());

	imshow("src", src);
	imshow("dst", dst);

	waitKey();
	destroyAllWindows();
}

void affine_shear()
{
	Mat src = imread("tekapo.bmp");

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	double mx = 0.3;
	Mat M = Mat_<double>({ 2, 3 }, { 1, mx, 0, 0, 1, 0 });

	Mat dst;
	warpAffine(src, dst, M, Size(cvRound(src.cols + src.rows * mx), src.rows));

	imshow("src", src);
	imshow("dst", dst);

	waitKey();
	destroyAllWindows();
}

void affine_scale()
{
	Mat src = imread("rose.bmp");

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	Mat dst1, dst2, dst3, dst4;
	resize(src, dst1, Size(), 4, 4, INTER_NEAREST);
	resize(src, dst2, Size(1920, 1280));
	resize(src, dst3, Size(1920, 1280), 0, 0, INTER_CUBIC);
	resize(src, dst4, Size(1920, 1280), 0, 0, INTER_LANCZOS4);

	imshow("src", src);
	imshow("dst1", dst1(Rect(400, 500, 400, 400)));
	imshow("dst2", dst2(Rect(400, 500, 400, 400)));
	imshow("dst3", dst3(Rect(400, 500, 400, 400)));
	imshow("dst4", dst4(Rect(400, 500, 400, 400)));

	waitKey();
	destroyAllWindows();
}

void affine_rotation()
{
	Mat src = imread("tekapo.bmp");

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	Point2f cp(src.cols / 2.f, src.rows / 2.f);
	Mat M = getRotationMatrix2D(cp, 20, 1);

	Mat dst;
	warpAffine(src, dst, M, Size());

	imshow("src", src);
	imshow("dst", dst);

	waitKey();
	destroyAllWindows();
}

void affine_flip()
{
	Mat src = imread("eastsea.bmp");

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	imshow("src", src);

	Mat dst;
	int flipCode[] = { 1, 0, -1 };
	for (int i = 0; i < 3; i++) {
		flip(src, dst, flipCode[i]);

		String desc = format("flipCode: %d", flipCode[i]);
		putText(dst, desc, Point(10, 30), FONT_HERSHEY_SIMPLEX, 1.0, Scalar(255, 0, 0), 1, LINE_AA);

		imshow("dst", dst);
		waitKey();
	}

	destroyAllWindows();
}
  </code>
</pre>

![image](https://github.com/god102104/openCV_Practice/assets/43011129/fa1fd91f-fb37-48ca-9c1f-9a06be859bd8)


# 이동 변환 (translation transformation)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/0c47a231-e345-4149-b785-b3bb48b6a21d)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/2e7f547d-8e23-4f4b-9f7f-efb3bcac5ade)
> 위와 같은 2x3 affine 행렬을 만들어서 쓰면 됨. **함수는 따로 있지 않고** warpAffine() 쓰면 됨. <br>

# 전단 변환 (shear transformation)
> 직사각형 형태의 영상을 한쪽 방향으로 밀어서 **평행사변형 모양으로** 변형되는 변환 **(층밀림 변환)** <br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/4476569e-d69b-4989-8c15-6356f717cce2)
> 따로 함수 없음, warpAffine() 쓰면 됨

 
# 크기 변환 (scale transformation)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/c8315544-20a7-4f1b-bc5a-3d1135b66bc6)
> **resize()** 함수 사용
<pre>
	<code>
		void resize(InputArray src, OutputArray dst,
            Size dsize, double fx = 0, double fy = 0,
            int interpolation = INTER_LINEAR);
	</code>
</pre>

> **interpolation**: 보간법 지정. <br> 
> INTER_NEAREST, INTER_LINEAR, INTER_CUBIC, INTER_AREA, INTER_LANCZOS4 중 하나를 지정. <br> 
![image](https://github.com/god102104/openCV_Practice/assets/43011129/9c1974d2-94d3-45ae-873d-6b250056cff8)


# 회전 변환 (rotation transformation)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/b61375f7-d6a1-4efe-8a5b-887b312b7667)

# 대칭 변환 
![image](https://github.com/god102104/openCV_Practice/assets/43011129/0b051342-7929-40c3-82bb-f7f09bf0bdd3)
> 위 수식은 **좌우 대칭** 변환 <br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/3d457e68-36ff-4b73-a2c9-72e628cac1e5)
> 위 식은 **상하 대칭** 변환 <br>

> 함수로는 **flip()** 함수가 있다.
<pre>
	<code>
		void flip(InputArray src, OutputArray dst, int flipCode);
	</code>
</pre>
>  flipCode : flipCode가 양수이면 좌우 대칭, 0이면 상하 대칭, 음수이면 상하 대칭과 좌우 대칭

# 투시 변환 (perspective transform)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/480ba330-969c-4431-a5bf-8006645659d0)
> 보는 시점을 옮긴다고 보면 됨 <br>
> 보통 **3x3** 크기의 실수행렬 <br>
> **getPerspectiveTransform()** <br>
<pre>
	<code>
		Mat getPerspectiveTransform(const Point2f src[], const Point2f dst[], 
                            int solveMethod = DECOMP_LU);
		Mat getPerspectiveTransform(InputArray src, InputArray dst,
                            int solveMethod = DECOMP_LU);
	</code>
</pre>
