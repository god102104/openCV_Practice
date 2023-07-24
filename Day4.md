
Day 4
===
# 영상의 산술 연산

영상은 기본적으로 2차원 행렬이므로 산술 연산 (arithmetic operation)을 그대로 적용 가능.
## 덧셈 연산 예시
![image](https://github.com/god102104/openCV_Practice/assets/43011129/8e5f625b-865f-4e1d-a83a-fe728fb8c589)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/9fb36b06-5f84-4fcf-b9c8-858d6e43965e)
> α+β=1이면 결과 영상에서 포화되는 픽셀이 발생하지 않습니다. <br>
> 만약 α=0.1, β=0.9로 설정하면 src1 영상의 윤곽은 조금만 나타나고 <br>
> src2 영상의 윤곽은 많이 나타나는 결과 영상이 생성됩니다. <br>
<pre>
  <code>
    Mat src1 = imread("aero2.bmp", IMREAD_GRAYSCALE);
    Mat src2 = imread("camera.bmp", IMREAD_GRAYSCALE);
    
    Mat dst;
    addWeighted(src1, 0.5, src2, 0.5, 0, dst);
  </code>
</pre>
> 두 입력 영상의 평균 영상을 생성하는 코드
![image](https://github.com/god102104/openCV_Practice/assets/43011129/26ec52fe-f194-4439-a118-ac536dc6e5b7)

## 뺄셈도 마찬가지지만, 두 입력 영상 type이 다르다면 -가 아니라 subtract() 를 써야한다.
> 덧셈 연산과 달리 뺄셈 연산은 뺄셈의 대상이 되는 영상 순서에 따라 결과가 달라진다.
![image](https://github.com/god102104/openCV_Practice/assets/43011129/433f5f58-09e1-46c7-94f0-d3b7fd60ca1b)
> 위와 같은 예시를 통해 연산 순서의 중요성을 알 수 있음.

### 아래는 subtract를 이용해 영상 변화 찾는 예시
![image](https://github.com/god102104/openCV_Practice/assets/43011129/037ff00d-4611-4c2a-8e14-7414862d060f)


## 곱셉 
> **multiply()** 와 **divide()** 를 이용한다. <br>
> 영상을 이용하여 행렬 곱셈 수행하는 경우는 거의 없음.


### 산술 연산 예시 코드
<pre>
  <code>
    #include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int main(void)
{
	Mat src1 = imread("lenna256.bmp", IMREAD_GRAYSCALE);
	Mat src2 = imread("square.bmp", IMREAD_GRAYSCALE);

	if (src1.empty() || src2.empty()) {
		cerr << "Image load failed!" << endl;
		return -1;
	}

	imshow("src1", src1);
	imshow("src2", src2);

	Mat dst1, dst2, dst3, dst4;

	add(src1, src2, dst1);
	addWeighted(src1, 0.5, src2, 0.5, 0, dst2);
	subtract(src1, src2, dst3);
	absdiff(src1, src2, dst4);

	imshow("dst1", dst1);
	imshow("dst2", dst2);
	imshow("dst3", dst3);
	imshow("dst4", dst4);
	waitKey();

	return 0;
}
  </code>
</pre>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/550c5d57-73a6-4fc5-ab16-4a21ebe04ad3)

## 비트 연산 
> bitwise_and(), bitwise_or(), bitwise_xor(), bitwise_not() 함수를 이용. <br>
> bitwise_and(), bitwise_or(), bitwise_xor() 함수는 두 개의 영상을 입력으로 받고,<br>
> bitwise_not() 함수는 하나의 영상을 입력. <br>

### 비트 연산 예시
<pre>
	<code>
		#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int main(void)
{
	Mat src1 = imread("lenna256.bmp", IMREAD_GRAYSCALE);
	Mat src2 = imread("square.bmp", IMREAD_GRAYSCALE);

	if (src1.empty() || src2.empty()) {
		cerr << "Image load failed!" << endl;
		return -1;
	}

	imshow("src1", src1);
	imshow("src2", src2);

	Mat dst1, dst2, dst3, dst4;

	bitwise_and(src1, src2, dst1);
	bitwise_or(src1, src2, dst2);
	bitwise_xor(src1, src2, dst3);
	bitwise_not(src1, dst4);

	imshow("dst1", dst1);
	imshow("dst2", dst2);
	imshow("dst3", dst3);
	imshow("dst4", dst4);
	waitKey();

	return 0;
}
	</code>
</pre>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/39c82128-a0d6-4556-8b42-0457a3652798)

# 영상의 필터링

## 필터링 연산 방법
![image](https://github.com/god102104/openCV_Practice/assets/43011129/812a640d-f7f8-484c-8498-be24a65f33e8)
> 진한 색으로 표시된 지점 : **고정점 (anchor point)** <br>
> 대부분의 경우 마스크 행렬 정중앙이 고정점. <br>

![image](https://github.com/god102104/openCV_Practice/assets/43011129/9d7f3c23-43ea-4bcf-adf0-d2e0ee2963c0)
![image](https://github.com/god102104/openCV_Practice/assets/43011129/0dc4b88d-dfa1-4e94-86f9-39e801b14c8d)

> 가장자리 픽셀에서는 수식을 그대로 적용하기 어려움. -> **padding** 을 이용 <br>
> **padding : 가상의 픽셀 공간** <br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/2151f7f3-3a86-4119-9cd3-43e1066a56f5)

### 일반적인 가장자리 픽셀 처리 방법
![image](https://github.com/god102104/openCV_Practice/assets/43011129/bccc4423-c2a8-4237-9b69-c7f39a6d1422)

> 일반적인 필터링은 **filter2D()** 함수를 이용.
<pre>
	<code>
		
void filter2D(InputArray src, OutputArray dst, int ddepth,
              InputArray kernel, Point anchor = Point(-1,-1),
              double delta = 0, int borderType = BORDER_DEFAULT);
	</code>
</pre>
> • src : 입력 영상 <br>
> • dst : 출력 영상. src와 같은 크기, 같은 채널 수를 갖습니다. <br>
> • ddepth : 결과 영상의 깊이 <br>
> • kernel : 필터링 커널. 1채널 실수형 행렬 <br>
> • anchor : 고정점 좌표. Point(-1, -1)을 지정하면 커널 중심을 고정점으로 사용합니다. <br>
> • delta : 필터링 연산 후 추가적으로 더할 값 <br>
> • borderType : 가장자리 픽셀 확장 방식 <br>

## 엠보싱 필터링
> 올록볼록한 느낌이 나게 처리하는 것. <br>
> 픽셀 값 변화가 적은 부분은 평탄하게, 객체 경계 부분은 밝거나 어둡게 <br>

### 엠보싱 필터 예시
<pre>
	<code>
		#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

void filter_embossing();

int main(void)
{
	filter_embossing();

	return 0;
}

void filter_embossing()
{
	Mat src = imread("rose.bmp", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	float data[] = { -1, -1, 0, -1, 0, 1, 0, 1, 1 };
	Mat emboss(3, 3, CV_32FC1, data);

	Mat dst;
	filter2D(src, dst, -1, emboss, Point(-1, -1), 128);

	imshow("src", src);
	imshow("dst", dst);

	waitKey();
	destroyAllWindows();
}
	</code>
</pre>

> 예시의 엠보싱 필터를 적용할 경우, 대각선 방향으로 필셀 값이 급격하게 변하는 부분에서 <br>
> 픽셀값이 0보다 훨씬 크거나 훨씬 작은 값을 갖게된다. <br>
> 픽셀 값이 크게 바뀌지 않는 영역에서는 0에 가까운 값을 가지게 된다. <br>
> 이렇게 나온 결과 영상을 그대로 쓰면 음수 값은 포화연산에 의해 0이 되어버리므로, <br>
> 엠보싱 필터 이용 시에는 주로 128을 더한다. (보기에 좋음) <br>


# 블러링 (Bluring)
> 영상을 부드럽게, 노이즈 제거

## 1. 평균값 필터
> Mask 크기가 커질수록 부드러운 느낌의 결과 <br>
> 대신 연산량이 늘어난다는 것을 인지할 것. <br>
> blur() 함수로 간단하게 이용 가능. <br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/4cf0e4f1-9cd5-4200-90f3-f1d45db258bd)

## 2. 가우시안 필터
> 평균값 필터보다 자연스러운 블러링 결과 생성 <br>
> 정규 분포 형태 <br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/a1aecc97-2c5d-408c-9b2b-12b4da2b5d24)

### 2차원 가우시안 분포 함수 그래프 
![image](https://github.com/god102104/openCV_Practice/assets/43011129/4a5acebf-0e0f-49ec-83c1-66f61498edc3)
> x={-4, -3, -2, -1, 0, 1, 2, 3, 4}, y={-4, -3, -2, -1, 0, 1, 2, 3, 4}인 경우에만 <br>
> 가우시안 분포 함수 값을 추출하여 필터 마스크를 생성 <br>
> (연속 함수이지만 이산형의 마스크를 만들기 위해서) <br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/e32d85db-a348-465a-8707-b00f961d723c)

> 중앙부에서 비교적 큰 값을 가지고, 주변부로 갈수록 행렬 원소 값이 0에 가까운 작은 값 <br>
> 9x9 이므로 연산량이 크지만, 2차원 가우시안 분포 함수를 1차원 행렬 곱으로 분리 가능 <br>
> x 축 함수와 y축 함수 각각으로 분리 <br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/d1a2f666-8312-45ca-80be-f187a6c15a15)
> 행렬 g를 이용해 필터링 수행 후 전치 행렬인 gT 를 이용하면 2차원으로 한 것이랑 같음 <br>
> 함수로는 **GaussianBlur()**
<pre>
	<code>
		void GaussianBlur(InputArray src, OutputArray dst, Size ksize,
                  double sigmaX, double sigmaY = 0,
                  int borderType = BORDER_DEFAULT);
	</code>
</pre>
>• src : 입력 영상. 다채널 영상은 각 채널별로 블러링을 수행 <br>
>• dst : 출력 영상. src와 같은 크기, 같은 타입을 가짐 <br>
>• ksize : 가우시안 커널 크기. <br>
>	ksize.width와 ksize.height는 0보다 큰 홀수여야. <br>
>	ksize에 Size()를 지정하면 표준 편차로부터 커널 크기를 자동으로 결정. <br>
>• sigmaX : x 방향으로의 가우시안 커널 표준 편차. <br>
>• sigmaY : y 방향으로의 가우시안 커널 표준 편차. <br>
>	만약 sigmaY = 0이면 sigmaX와 같은 값을 사용. <br>
>	만약 sigmaX와 simgaY가 모두 0이면 ksize의 width와 height 값으로부터 표준 편차를 계산하여 사용. <br>
>• borderType : 가장자리 픽셀 확장 방식. <br>

### bluring 예시 코드
<pre>
	<code>
		#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

void blurring_mean();
void blurring_gaussian();

int main(void)
{
	blurring_mean();
	blurring_gaussian();

	return 0;
}

void blurring_mean()
{
	Mat src = imread("rose.bmp", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	imshow("src", src);

	Mat dst;
	for (int ksize = 3; ksize <= 7; ksize += 2) {
		blur(src, dst, Size(ksize, ksize));

		String desc = format("Mean: %dx%d", ksize, ksize);
		putText(dst, desc, Point(10, 30), FONT_HERSHEY_SIMPLEX, 1.0, 
				Scalar(255), 1, LINE_AA);

		imshow("dst", dst);
		waitKey();
	}	

	destroyAllWindows();
}

void blurring_gaussian()
{
	Mat src = imread("rose.bmp", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	imshow("src", src);

	Mat dst;
	for (int sigma = 1; sigma <= 5; sigma++) {
		GaussianBlur(src, dst, Size(0, 0), (double)sigma);

		String desc = format("Gaussian: sigma = %d", sigma);
		putText(dst, desc, Point(10, 30), FONT_HERSHEY_SIMPLEX, 1.0, 
				Scalar(255), 1, LINE_AA);

		imshow("dst", dst);
		waitKey();
	}

	destroyAllWindows();
}
	</code>
</pre>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/835790cf-d642-47bb-9ce7-73b4baa4e472)
> GaussianBlur() 내부에는 x축 방향, y축 방향 각각 1차원 가우시안 필터 마스크 생성하여 필터링 수행.
> 그래서 내부에는 **getGaussianKernel()** 함수가 들어 있음.
### getGaussianKernel() 함수 원형
<pre>
	<code>
		Mat getGaussianKernel(int ksize, double sigma, int ktype = CV_64F);
	</code>
</pre>
> • ksize : 커널 크기. ksize는 0보다 큰 홀수이어야 합니다. <br>
> • sigma : 가우시안 표준 편차.<br>
> 만약 0 또는 음수를 지정하면 sigma = 0.3*((ksize-1)*0.5 - 1) + 0.8 형태로 sigma를 계산합니다.<br>
> • ktype : 필터의 타입. CV_32F 또는 CV_64F<br>
> • 반환값 : ksize×1 크기의 가우시안 필터 커널<br>

# 샤프닝 (Sharpening)
> 영상을 날카로운 느낌이 나게끔 <br>
> 객체의 **윤곽이 뚜렷하게** 구분되게 <br>
> **Bluring 이 선행**되어야 좋음 <br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/c44c1af8-9673-4245-ae54-99e576e20e91)

> 7-12(b)에서 파란색 실선 그래프는 f(x, y)에 블러링을 적용한 결과 <br>
> 7-12(c)는 입력 영상 f(x, y)에서 블러링된 영상 를 뺀 결과 <br>
> 7-12(d)에서 h(x, y)=f(x, y)+g(x, y)가 샤프닝이 적용된 결과 <br>

### 샤프닝 예제 코드 
<pre>
	<code>
		#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

void unsharp_mask();

int main(void)
{
	unsharp_mask();

	return 0;
}

void unsharp_mask()
{
	Mat src = imread("rose.bmp", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	imshow("src", src);

	for (int sigma = 1; sigma <= 5; sigma++) {
		Mat blurred;
		GaussianBlur(src, blurred, Size(), sigma);

		float alpha = 1.f;
		Mat dst = (1 + alpha) * src - alpha * blurred;

		String desc = format("sigma: %d", sigma);
		putText(dst, desc, Point(10, 30), FONT_HERSHEY_SIMPLEX, 1.0, 
				Scalar(255), 1, LINE_AA);

		imshow("dst", dst);
		waitKey();
	}

	destroyAllWindows();
}
	</code>
</pre>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/d30a3423-08a9-42bd-8b75-edf8e95428c5)
> **sigma 값**이 커짐에 따라 다소 과장된 느낌의 샤프닝 결과 영상이 만들어질 수도 있으니 주의 <br>

# Noise 제거 필터링
> 디지털 카메라  광학적 신호를 전기적 신호로 변환하는 **센서(sensor)에서 주로 잡음이 추가** <br>
> 보통 가우시안 필터 이용해서 Noise 제거 <br>
> 그러나 픽셀 값이 급격하게 변경되는 에지 근방에 <br>
> 동일한 가우시안 필터가 적용되면 잡음뿐만 아니라 에지 성분까지 함께 감소 <br>
> → 엣지가 무뎌지므로 윤곽이 흐릿하게 됨. <br>
> 즉, 엣지 정보는 유지하면서 Noise 만 제거하는 에지 보전 잡음 제거 필터(edge-preserving noise removal filter) 필요 <br>
> 양방향 필터(bilateral filter) 가 효과적이다. <br>
> **bilateralFilter()** 함수 <br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/9fbcab17-8a05-4d94-8a69-59bf42bdc529)

> 균이 0이고 표준 편차가 5인 가우시안 잡음이 추가 → 표준 편차가 5인 가우시안 필터링을 수행한 결과 <br>
> 
