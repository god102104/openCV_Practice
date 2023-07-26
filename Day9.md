Day9
===
# 머신러닝

## 개요
> 주어진 데이터를 분석하여 규칙성, 패턴 등을 찾고, 이를 이용하여 의미 있는 정보를 추출하는 과정 <br>
> 데이터로부터 규칙을 찾아내는 과정을 학습(train) <br>
> 학습에 의해 결정된 규칙을 모델(model) <br>
> 새로운 데이터를 학습된 모델에 입력으로 전달하고 결과를 판단하는 과정을 예측(predict) 또는 추론(inference) <br>
> 크게 지도 학습(supervised learning)과 비지도 학습(unsupervised learning)으로 구분 <br>
> **지도 학습** : **정답을 알고 있는 데이터**를 이용하여 학습을 진행하는 방식, <br>
> 훈련 데이터에 대한 정답에 해당하는 내용을 레이블(label) <br>
>
> ![image](https://github.com/god102104/openCV_Practice/assets/43011129/9af1ea39-1580-46be-99f9-79bc11365493) <br>
>
> 주로 **회귀(regression)** 또는 **분류(classification)** 에 사용 <br>
> 입력 영상이 사과인지 바나나인지를 구분하는 것을 인식(recognition)이라고도 부르지만 결국은 분류 문제에 해당 <br>
> **비지도 학습** : 훈련 데이터의 **정답에 대한 정보 없이** 오로지 데이터 자체만을 이용하는 학습 방식 <br>
> 주로 **군집화(clustering)** 에 사용 <br>
> **k-폴드 교차 검증(k-fold cross-validation)** : 훈련 데이터를 k개의 부분 집합으로 분할하여 학습과 검증(validation)을 반복 <br>


## OpenCV 머신 러닝 Class
>![image](https://github.com/god102104/openCV_Practice/assets/43011129/10bd1ee6-6424-48cb-88b3-2cf23e53a514) 
> **학습**을 수행하는 **StatModel::train()** 함수 <br>
> <pre>
>   <code>
>     virtual bool StatModel::train(InputArray samples, 
>                              int layout, 
>                              InputArray responses);
>   </code>
> </pre>
> responses : 각 훈련 데이터에 대응되는 응답(레이블) 행렬 <br>
> return : 학습 완료 시 true <br>
> layout : 훈련 데이터 배치 방법. ROW_SAMPLE 또는 COL_SAMPLE를 지정 <br>
>
> 테스트 데이터의 **응답**을 얻고 싶으면 **StatModel::predict()** 함수 <br>
> <pre>
>  <code>
>    virtual float StatModel::predict(InputArray samples, 
>                                 OutputArray results = noArray(), 
>                                 int flags = 0) const;
>   </code>
> </pre>
> flags : StatModel::Flags 열거형 상수 중 하나를 지정할 수 있으며, 모델에 따라 사용법이 다름 <br>
> return : 입력 벡터가 하나인 경우에 대한 응답 return. <br>
>
> 
