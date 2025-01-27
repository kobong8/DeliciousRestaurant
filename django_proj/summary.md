## Django 코드 개발 단계

1. Model: 요구사항에 맞추어 모델에 속성 추가(모델과 함수 등을 추가)

2. View: 요구사항의 화면에 맞추어 입력과 출력에 관점으로 뷰 작성

3. URL: 작성한 뷰를 URL에 등록

4. Template: 필요한 경우 HTML 기반의 템플릿 작성(뷰에서 렌터링)

### HTTP 상태 코드
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

<br/>

```text:requirements.txt
django==5.0.6
mysqlclient==2.2.1
django_extensions==3.2.3
django-environ==0.11.2
Pillow==10.3.0

djangorestframework==3.14.0
markdown==3.5.1
django-filter==23.5
drf-spectacular==0.27.0
```

1. Model 클래스 작성 - 모델/필드를 추가/수정/삭제
2. makemigrations
3. migrate
4. 데이터 이전

- migration 되돌리기
```powershell
python manage.py showmigrations
python manage.py migrate 앱이름 이전마이크레이션번호
(되돌릴 마이그레이션 파일 삭제)
python manage.py makemigrations
python manage.py migrate
```