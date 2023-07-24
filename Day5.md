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


## 이동 변환 (translation transformation)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/0c47a231-e345-4149-b785-b3bb48b6a21d)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/2e7f547d-8e23-4f4b-9f7f-efb3bcac5ade)
> 위와 같은 2x3 affine 행렬을 만들어서 쓰면 됨. **함수는 따로 있지 않고** warpAffine() 쓰면 됨. <br>

## 전단 변환 (shear transformation)
> 직사각형 형태의 영상을 한쪽 방향으로 밀어서 **평행사변형 모양으로** 변형되는 변환 **(층밀림 변환)** <br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/4476569e-d69b-4989-8c15-6356f717cce2)
> 따로 함수 없음, warpAffine() 쓰면 됨

 
## 크기 변환 (scale transformation)
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


## 회전 변환 (rotation transformation)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/b61375f7-d6a1-4efe-8a5b-887b312b7667)

## 대칭 변환 
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

## 투시 변환 (perspective transform)
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

> 위의 투시 행렬을 가지고 있을 때, 결과를 보려면 **warpPerspective()** 함수 사용. <br>
<pre>
	<code>
		
void warpPerspective(InputArray src, OutputArray dst,
                     InputArray M, Size dsize,
                     int flags = INTER_LINEAR,
                     int borderMode = BORDER_CONSTANT,
                     const Scalar& borderValue = Scalar());
	</code>
</pre>

> 투시 변환 행렬 M은 CV_32FC1 또는 CV_64FC1 타입이어야. <br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/835576b9-4cea-4e79-b059-56ea852c2753)


# 에지 검출과 응용

## 미분
![image](https://github.com/god102104/openCV_Practice/assets/43011129/06f5109d-b89e-4d5c-a064-d7ba69330a4c)
> 픽셀 값이 급격하게 변하는 지점 찾기 (f′(x) 값이 0보다 훨씬 크거나 또는 훨씬 작은 위치를 찾아야) <br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/6aaf64d9-0b6b-4969-adeb-0d97b5b21ae6)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/9770c095-ee93-4c49-b79d-dc1f780d2714)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/b025ccd5-4835-4f2d-8b81-34825a2acfea)

> 위의 세 방식 (전진, 후진, 중앙 차분) 중에서 **중앙 차분**이 근사오류가 가장 적다. <br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/efba92a8-50b4-4cf4-b279-ce18230f5c17)

> 위는 중앙 차분에 의한 미분 근사 Mask
![image](https://github.com/god102104/openCV_Practice/assets/43011129/22d1b71e-25c8-4d6f-8e28-8f9b20ae5bbd)

## 그래디언트 
![image](https://github.com/god102104/openCV_Practice/assets/43011129/d44a347a-8b61-48ad-ab7e-53005ba9ffbe)

>  f(x, y)가 있을 때 이 함수의 x축 방향 미분과 y축 방향 미분을 한꺼번에 **벡터로 표현**한 것 <br>
> 그래디언트 벡터의 **방향**은 픽셀 값이 가장 **급격하게 증가하는 방향** <br>
> 그래디언트 벡터의 **크기**는 픽셀 값의 차이 정도, **변화량** <br>

![image](https://github.com/god102104/openCV_Practice/assets/43011129/350aae51-612e-454b-a128-d8951f22e408)

> 위의 그림에서 경계상의 세 점 a, b, c를 선택하고, 각 점에서의 그래디언트 벡터를 빨간색 화살표로 표현 <br>
> 노란색으로 표시된 화살표는 **그래디언트 벡터와 수직인 방향**을 표시, **'에지의 방향'** <br>
> 2차원 영상에서 에지를 찾는 기본적인 방법은 **그래디언트 크기가 특정 값보다 큰 위치를 찾는 것** <br>
> 임계값을 높게 설정하면 밝기 차이가 급격하게 변하는 에지 픽셀만 검출 <br>
> 임계값을 낮게 설정하면 약한 에지 성분도 검출 <br>

### 2D 벡터의 크기 계산 함수
<pre>
	<code>
		cv2.magnitude(x, y, magnitude=None) -> magnitude
	</code>
</pre>

### 2D 벡터의 방향 계산 함수
<pre>
	<code>
		cv2.phase(x, y, angle=None, angleInDegrees=None) -> angle
	</code>
</pre>

## Mask 기반 Edge 검출 
### Sobel filter 
![image](https://github.com/god102104/openCV_Practice/assets/43011129/576867b4-eb81-49e2-93d7-5d3b3c88a754)

> 축 방향 미분 마스크는 현재 행에 대한 중앙 차분 연산을 2회 <br>
> 이전 행과 다음 행에 대해서도 중앙 차분 연산을 1회 <br>
> (현재 행과 이웃 행에서의 픽셀 값 변화가 유사하다는 점을 이용하여 잡음의 영향을 줄이기 위함) <br>
> (현재 행에서 두 번의 중앙 차분 연산을 수행하는 것은 현재 행의 중앙 차분 근사에 더 큰 가중치를 주기 위함) <br>
> (b)는 y축 방향 미분 계산 <br>

### Sobel filter 를 이용한 Edge 검출 예제
<pre>
	<code>
		src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

mag = cv2.magnitude(dx, dy)
mag = np.clip(mag, 0, 255).astype(np.uint8)

dst = np.zeros(src.shape[:2], np.uint8)
dst[mag > 120] = 255 # threshold(120) 역할
	</code>
</pre>

### 샤르 필터 (Scharr filter)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/a4dd2782-2eb0-4fa9-a3e4-38d9c25a46d2)

> **Sobel 보다 더 정확함**


### Edge 검출 결과 (Sobel)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/fa8c9d99-de71-4bfa-b8c6-046b391aca64)

### 캐니 에지 검출기 (canny edge detector)

![image](https://github.com/god102104/openCV_Practice/assets/43011129/dd52a5fe-b866-4fd9-b9e2-28206fbab508)

> 위는 캐니 에지 검출기 수행 과정

> 1. 가우시안 필터링 <br>
> 2. 그래디언트 계산 : 3x3 Sobel mask 주로 사용. Canny 에서는 정확한 Edge 검출을 위해 **Gradient 방향도 고려**. <br>
> 3. 비최대 억제 : 단순히 그래디언트 크기가 특정 임계값보다 큰 픽셀을 선택할 경우, <br>
>    에지 근방의 여러 픽셀이 한꺼번에 에지로 선택될 수도 있음. <br>
>    **에지가 두껍게 표현되는 현상을 방지**하기 위해 캐니 에지 검출기에서는 <br>
>    비최대 억제(non-maximum suppression) 과정을 사용 <br>
>    그래디언트 크기가 국**지적 최대(local maximum)인 픽셀만을 에지 픽셀로** 설정 <br>
>    **가장 변화율이 큰 위치**의 픽셀만 에지로 <br>
> ### Canny - 이중 임계값을 이용한 히스테리시스 에지 트래킹
> 소벨 에지 검출 방법에서는 그래디언트 크기가 특정 임계값보다 크면 에지 픽셀로, <br>
> 작으면 에지가 아닌 픽셀로 판단. <br>
> 이 경우 **조명**이 조금 바뀌거나 또는 **임계값**을 조금만 조절해도 **에지 픽셀 판단 결과가 크게 달라질 수**도. <br>
> 캐니 에지 검출기에서는 **두 개의 임계값**
> Canny() 함수

<pre>
	<code>
		void Canny(InputArray image, OutputArray edges,
           double threshold1, double threshold2,
           int apertureSize = 3, bool L2gradient = false);
void Canny(InputArray dx, InputArray dy, OutputArray edges,
           double threshold1, double threshold2,
           bool L2gradient = false);
	</code>
</pre>

### Canny Edge 검출 예제
<pre>
	<code>
		 void canny_edge()
    {
        Mat src = imread("lenna.bmp", IMREAD_GRAYSCALE);
     
        if (src.empty()) {
            cerr << "Image load failed!" << endl;
            return;
        }
     
        Mat dst1, dst2;
        Canny(src, dst1, 50, 100);
        Canny(src, dst2, 50, 150);
     
        imshow("src", src);
        imshow("dst1", dst1);
        imshow("dst2", dst2);
     
        waitKey();
        destroyAllWindows();
    }
	</code>
</pre>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/b46216b2-b9f1-4cc3-928a-98f035b470a3)

> 각각 임계값 100, 150 인 경우. 
