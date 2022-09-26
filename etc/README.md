# TIL
ML Ops

<h2>10/18 ML Ops 2회</h2>
<h3>도커 개념</h3>
<ul>
<li>VM으로도 가능하지만 성능상의 차이가 크다. </li>
<li>load balance the service</li>

</ul>
<h3>Flink</h3>
<p><strong>stream</strong>이라는 데이터 타입은 어떤것인가? 운전을 할때에 운전자의 입장에서 실시간으로 주변의 정보를 받아들이는 상황. 많은정보들을 들어오는대로 바로 처리하는</p>
<p><strong>배치프로세싱</strong>은 과거로부터 배우기 위해서 저장하는. 큰 의사결정, 기간 통계 그리고 트렌트 분석. 한정된 변하지 않는 데이터셋, spark은 배치프로세싱에 적합</p>
<p><strong>스트리밍 프로세싱</strong>은 주식매매나 신용카드 결제데이터와 같이 실시간 모니터링. 빠르고 tactical decison, 트윗과 같은 개인적 이벤트의 처리. Kafka, flink</p>
<p><strong>Hadoop</strong> 시스템적 기능들을 지원하면서 비즈니스 로직에 집중할수있는 토대마련
강제되는 파이프라인 구조. 기본적으로 맵리듀스의 입력은 1개만 가능. 중간 결과를 디스크에 저장
스트림 데이터에 대한 고려가 없음. 컴퓨터에서 가장 느린게 하드디스크// 하둡의 성능이 내려간다</p>
<p>새로운 것(2) - Apache Spark
메모리를 적극적으로 사용함으로써 성능 향상을 꾀하는 대용량</p>
<p>그리고 새로운 것(3) - Apache Flink
스트림데이터 대용량 데이터 처리 플랫폼</p>
<p>Gelly : Graph processing , FlinkML : ML on Flink</p>
<ul>
<li>Flink는 메모리를 직접 관리함, GC로 인한 성능 감소가 적음</li>
<li>Flink에 Inception 훈련된 모델을 넣어두고 실시간으로 사진을 입력값으로 넣었을때 결과가 바로 나온다</li>

</ul>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
