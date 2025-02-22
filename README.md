# Delicious Restaurant

- Fast campus 강의 "파이썬으로 개발하는 빅데이터 기반 맛집 추천 서비스 (ft. Django, FastAPI)" 를 수강한 내용에 대한 정리
- 실습 코드: [파이썬으로 개발하는 빅데이터 기반 맛집 추천 서비스 (ft. Django, FastAPI)](https://github.com/fastcampus-plan1/Online-Backend-Python)
- 2025.01~

## proj_example 및 proj_service

- NOTE: setting.py 파일은 DB 정보를 포함하고 있어 제외됨

- CODE

```powershell
"c:\Program Files\MySQL\MySQL Server 8.4\bin\mysql.exe" -uroot -p
```

- 데이터 베이스 생성 및 권한 부여

```sql
SHOW DATABASES;
CREATE DATABASE {database name};
CREATE USER '{user name}'@'%' IDENTIFIED BY '{password}';
GRANT ALL PRIVILEGES ON {database name}.* TO '{user name}'@'%';
FLUSH PRIVILEGES;
```

- 데이터 베이스 비밀번호 변경(새로운 비밀번호를 ''로 감싸기)

```sql
ALTER USER 'root'@'localhost' IDENTIFIED BY '{new password}';
FLUSH PRIVILEGES;
```

- PyCharm에서 프로젝트를 생성하거나, startproject 명령으로 프로젝트 생성

```powershell
python -m django startproject {porject name} {folder path}
```

```powershell
python manage.py runserver
python manage.py migrate
```

- restaurant 모델 추가

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

- migration 파일 정리

```powershell
python manage.py migrate restaurant zero
(특정 migrate으로 돌아가기) python manage.py migrate restaurant 0001_contents
python manage.py makemigrations
python manage.py migrate
```

- test 실행하기 경로 및 명령어

```text
proj_service
├ manage.py
├ proj
└ restaurant
  ├ migrations
  ├ tests
  │ ├ __init__.py
  │ └ test_models.py
  ├ __init__.py
  ├ tests.py
  └ 그외 파일들
```

```powershell
python manage.py test

Found 10 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..........
----------------------------------------------------------------------
Ran 10 tests in 0.023s

OK
Destroying test database for alias 'default'...
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

environ.Env.read_env("django_proj_example/.env")  # .env 파일 불러오기
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

## pre-commit_test

- pre-commit 설치 및 실행

```powershell
pip install per-commit

pre-commit install
pre-commit installed at .git\hooks\pre-commit

pre-commit run
```

- pre-commit 건너뛰기

```powershell
git commit -m "commit message" --no-verify
```

- pre-commit 삭제하기

```powershell
rm .git/hooks/pre-commit
or
pre-commit uninstall
```

1. [CLOSED] WARNING 내용 확인 필요 - .pre-commit-config.yaml 파일의 모든 버전을 업데이트

```powershell
pre-commit run
[INFO] Initializing environment for https://github.com/pre-commit/pre-commit-hooks.
[WARNING] repo `https://github.com/pre-commit/pre-commit-hooks` uses deprecated stage names (commit, push) which will be removed in a future version.  Hint: often `pre-commit autoupdate --repo https://github.com/pre-commit/pre-commit-hooks` will fix this.  if it does not -- consider reporting an issue to that repo.
...
[WARNING] repo `https://github.com/pycqa/isort` uses deprecated stage names (commit, merge-commit, push) which will be removed in a future version.  Hint: often `pre-commit autoupdate --repo https://github.com/pycqa/isort` will fix this.  if it does not -- consider reporting an issue to that repo.
...
trim trailing whitespace.............................(no files to check)Skipped
fix end of files.....................................(no files to check)Skipped
black................................................(no files to check)Skipped
isort................................................(no files to check)Skipped
flake8...............................................(no files to check)Skipped
```

완료 이후 적용할 때는 git add 및 git commit

```powershell
pre-commit run
[ERROR] Your pre-commit configuration is unstaged.
`git add .pre-commit-config.yaml` to fix this.
```

```powershell
git commit -m "update version"
[INFO] Initializing environment for https://github.com/pre-commit/pre-commit-hooks.
[INFO] Initializing environment for https://github.com/psf/black.
[INFO] Initializing environment for https://github.com/pycqa/isort.
[INFO] Initializing environment for https://github.com/pycqa/flake8.
[INFO] Installing environment for https://github.com/pre-commit/pre-commit-hooks.
...
trim trailing whitespace.................................................Passed
fix end of files.........................................................Passed
black................................................(no files to check)Skipped
isort................................................(no files to check)Skipped
flake8...............................................(no files to check)Skipped
```

2. [CLOSED] isort, autoflake, flake8의 차이

- flake8: 코드의 스타일과 오류를 검사하고 리포트
- autoflake: 코드 내 불필요한 import 등 정리를 자동으로 수행
- isort: 남아 있는 import 문을 정렬하고 그룹화

## Web Crawler

```powershell
pip install webdriver-manager
```
