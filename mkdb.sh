mysql -uroot -p -e "
  CREATE DATABASE qa;
  CREATE USER 'qa'@'localhost';
  GRANT ALL PRIVILEGES ON qa.* TO 'qa'@'localhost';
  FLUSH PRIVILEGES;
"
