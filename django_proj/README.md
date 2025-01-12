- NOTE
1. setting.py 파일은 DB 정보를 포함하고 있어 제외됨

- CODE
```text
python manage.py runserver
python manage.py migrate

python manage.py startapp restaurant
-> "setting.py" "INSTALLED_APPS"에 추가
python manage.py runserver

-> models에 Restaurant 생성 후
1. python manage.py makemigrations -> 모든 모델
2. python manage.py makemigrations {model name} -> 특정 모델
   ex) python manage.py makemigrations restaurant -> 특정 모델
-> migrations folder에 0001_initial.py 생성
pyton manage.py migrate

python manage.py createsuperuser
-> setting.py LANGUAGE_CODE = 'ko-kr'
-> 'en-us' --> 'ko-kr'
```

- TODO LIST
1. Not Found: /favicon.ico - runserver에서 발생
```text
Not Found: /favicon.ico
[DD/MMM/YYYY HH:MM:SS] "GET /favicon.ico HTTP/1.1" 404 2206
```

2. [CLOSED] Pillow is not installed - models.ImageField를 사용하려고 할 경우 발생
```text
ERRORS: restaurant.Restaurant.image: (fields.E210) Cannot use ImageField because Pillow is not installed. 
        HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".
```