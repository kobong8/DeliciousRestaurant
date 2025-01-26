- Django 코드 개발 단계

1. Model: 요구사항에 맞추어 모델에 속성 추가(모델과 함수 등을 추가)

2. View: 요구사항의 화면에 맞추어 입력과 출력에 관점으로 뷰 작성

3. URL: 작성한 뷰를 URL에 등록

4. Template: 필요한 경우 HTML 기반의 템플릿 작성(뷰에서 렌터링)

- HTTP 상태 코드
1XX: 정보 응답
<br/>
2XX: 성공 응답
<br/>
3XX: 리다이렉션 응답
<br/>
4XX: 클라이언트 오류 응답
<br/>
5XX: 서버 오류 응답
<br/>

| Code | Status                |
|------|-----------------------|
| 200  | OK                    |
| 201  | Created               |
| 301  | Moved Permanently     |
| 302  | Found                 | 
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |   
| 404  | Not Found             |    
| 500  | Internal Server Error |

