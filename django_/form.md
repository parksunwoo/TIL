# TIL
Today I Learned

## 02 HttpRequest와 HttpResponse
### HttpRequest 객체
- 클라이언트로부터의 모든 요청 내용을 담고 있으며
    - 함수 기반 뷰 : 매 요청 시마다 뷰 함수의 첫번째 인자 request로 전달
    - 클래스 기반 뷰 : 매 요청 시마다 self.request 를 통해 접근
- Form 처리 관련 속성들
    - .method : 요청의 종류 "GET" 또는 "POST" 로서 몸두 대문자
    - .GET : GET 인자 목록 (QueryDict 타입)
    - .POST : POST 인자 목록 (QueryDict 타입)
    - .FILES : POST 인자 중에서 파일 목록 (MultiValueDict 타입)
    
### MultiValueDict(1)
- dict을 상속받은 클래스
- 동일 key의 다수 value를 지원하는 사전
- URL의 QueryString은 같은 Key로서 다수 Value지정을 지원

### MultiValueDict(2)
- 동일 key의 다수 value를 지원하는 사전

### MultiValueDict(3)
- 수정 불가능한 Immutable 특성

### HttpResponse 객체
- 다양한 응답을 wrapping : HTML 문자열, 이미지 등등
- View에서는 반환값으로서 HttpResponse 객체를 기대
    - Middleware에서 HttpResponse 객체를 기대

### django.http.HttpResponse (3)
- 사전-like 인터페이스로 응답의 커스텀 헤더 추가/삭제
- 파일 첨부로 처리되기를 브라우저에게 알리기
    response = HttpResponse(excel_data, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="foo.xls"'
    
### django.http.StreamingHttpResponse (1)
- 효율적인 큰(긴) 응답을 위함
    - 혹은 메모리를 많이 먹는 응답 -> iterator를 통한 응답
- 하지만, django는 short-lived 요청에 맞게 디자인
    - 큰(긴) 응답 시에는 극심한 성능 저하로 이어질 수 있습니다.
- HttpResponse를 상속받지 않음.
    - 필히 iterator를 지정해야만, 제대로 동작
    - .content 속성 사용 X -> .streaming_content 사용
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    














