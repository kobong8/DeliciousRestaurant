- setting.py 파일은 DB 정보를 포함하고 있어 제외됨


- code
```console
python manage.py runserver
python manage.py migrate

python manage.py startapp restaurant
("setting.py" "INSTALLED_APPS"에 추가)
python manage.py runserver
```