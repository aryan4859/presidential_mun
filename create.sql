CREATE DATABASE presidential_mun;
CREATE USER 'mun_user'@'localhost' IDENTIFIED BY 'securepassword';
GRANT ALL PRIVILEGES ON presidential_mun.* TO 'mun_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;