Day8
===

# 객체 검출
## 템플릿 매칭
> 입력 영상에서 작은 크기의 **부분 영상 위치**를 찾아내고 싶은 경우에 주로 **템플릿 매칭(template matching)** 기법을 사용 <br>
> 템플릿(template)은 찾고자 하는 대상이 되는 작은 크기의 영상 <br>
> 템플릿 매칭은 작은 크기의 템플릿 영상을 입력 영상 전체 영역에 대해 이동하면서 가장 비슷한 위치를 수치적으로 찾아내는 방식 <br>
![image](https://github.com/god102104/openCV_Practice/assets/43011129/779ce75d-61d8-46d8-b8d6-752d87f068d5)

> 입력 영상 전체 영역에 대해 이동하면서 <br>
> 템플릿 영상과 입력 영상 부분 영상과의 유사도(similarity) 또는 비유사도(dissimilarity)를 계산 <br>
> **matchTemplate()** 함수
<pre>
  <code>
        void matchTemplate(InputArray image, InputArray templ,
                   OutputArray result, int method, InputArray mask = noArray());
  </code>
</pre>

> templ : 템플릿 영상. 입력 영상 image보다 같거나 작아야 하며, image와 타입이 같아야 <br>
> mask : 찾고자 하는 템플릿의 마스크 영상. mask는 templ과 같은 크기, 같은 타입이어야  <br>

## QR코드 검출
> **QRCodeDetector::detect()** 함수
<pre>
  <code>
    bool QRCodeDetector::detect(InputArray img, OutputArray points) const;
  </code>
</pre>
> points : (출력) QR 코드를 감싸는 사각형의 네 꼭지점 좌표 <br>
> return : QR코드 검출 성공 시 true <br>

> QR 코드에 저장된 문자열 추출 함수 **QRCodeDetector::decode()** <br>
<pre>
  <code>
    std::string QRCodeDetector::decode(InputArray img, InputArray points, 
     OutputArray straight_qrcode = noArray());    
  </code>
</pre>

> QR 코드 검출과 해석을 한꺼번에 **QRCodeDetector::detectAndDecode()** <br>
