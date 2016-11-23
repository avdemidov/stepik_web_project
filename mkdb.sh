mysql -uroot -p -e "
  CREATE DATABASE qa;
  CREATE USER 'qa'@'localhos';
  GRANT ALL PRIVILEGES ON qa.* TO 'qa'@'localhost';
  FLUSH PRIVILEGES;
"
