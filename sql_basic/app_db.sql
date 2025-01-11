--"c:\Program Files\MySQL\MySQL Server 8.4\bin\mysql.exe" -uroot -p
SHOW DATABASES;
CREATE DATABASE app_db;
CREATE USER 'user'@'%' IDENTIFIED BY '{password}';
GRANT ALL PRIVILEGES ON app_db.* TO 'user'@'%';
FLUSH PRIVILEGES;