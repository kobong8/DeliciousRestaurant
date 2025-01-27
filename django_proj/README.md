- NOTE
1. setting.py 파일은 DB 정보를 포함하고 있어 제외됨

- CODE
```powershell
"c:\Program Files\MySQL\MySQL Server 8.4\bin\mysql.exe" -uroot -p
```

```sql
SHOW DATABASES;
CREATE DATABASE {database name};
CREATE USER '{user name}'@'%' IDENTIFIED BY '{password}';
GRANT ALL PRIVILEGES ON {database name}.* TO '{user name}'@'%';
FLUSH PRIVILEGES;
```

```powershell
python manage.py runserver
python manage.py migrate
```

```powershell
python manage.py startapp restaurant
-> "setting.py" "INSTALLED_APPS"에 추가
python manage.py runserver
```

```powershell
-> models에 Restaurant 생성 후
1. python manage.py makemigrations -> 모든 모델
2. python manage.py makemigrations {model name} -> 특정 모델
   ex) python manage.py makemigrations restaurant -> 특정 모델
-> migrations folder에 0001_initial.py 생성
pyton manage.py migrate
```

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

```powershell
python manage.py createsuperuser
-> setting.py LANGUAGE_CODE = 'ko-kr'
-> 'en-us' --> 'ko-kr'
```

```powershell
python manage.py changepassword USER_ID
```

- TODO LIST
1. [CLOSED] Not Found: /favicon.ico - runserver에서 발생 - favicon은 웹페이지 탭에 작게 보이는 이미지, 추가할 경우 오류 발생X

```text
Not Found: /favicon.ico
[DD/MMM/YYYY HH:MM:SS] "GET /favicon.ico HTTP/1.1" 404 2206
```

2. [CLOSED] Pillow is not installed - models.ImageField를 사용하려고 할 경우 발생
```text
ERRORS: restaurant.Restaurant.image: (fields.E210) Cannot use ImageField because Pillow is not installed. 
        HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".
```

3. [CLOSED] Unknown column - 설정 변경 후, makemigrations와 migrate 재실행 필요
```text
OperationalError at /admin/restaurant/restaurant/
(1054, "Unknown column 'restaurant_restaurant.category' in 'field list'")
```

4. [*CLOSED] rating_count = models.PositiveIntegerField("별점 개수") - 우선적으로 null=True 사용, 추후 확인 필요
```text
It is impossible to add a non-nullable field 'rating_count' to restaurant without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
```

```python
# rating_count = models.PositiveIntegerField("별점 개수")
rating_count = models.PositiveIntegerField("별점 개수", null=True)
```

5. [CLOSED] .env 파일 사용하기
AttributeError: 'NoneType' object has no attribute 'startswith'
```text
# requirements.txt
django-environ==0.11.2
```

```python
import os
import environ

environ.Env.read_env(".env") # .env 파일 불러오기
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': os.environ.get("DB_HOST"),
        # 'PORT': 'PORT',
        'CHARSET': 'utf8mb4',
    }
}
```

6. [CLOSED] from ..restaurant.models import Restaurant <br/>
ImportError: attempted relative import beyond top-level package

```python:serializers.py
# serializers.py
from restaurant.models import Restaurant
```

```python:veiws.py
# views.py
from restaurant.models import Restaurant
```

7. [TODO] templates - forms.py의 역할, views.py에 추가되는 내용들(생성 뷰, 수정 뷰)

8. [TODO] 필드 등록 이후 실행에서 어떻게 바뀌는지에 대한 부분

9. [TODO] 관계형 필드 생성하기, foreign key 설정 방법

10. [TODO] 쿼리에서 "__" 사용을 어떻게 사용하는지