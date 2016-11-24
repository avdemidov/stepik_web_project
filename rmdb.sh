mysql -uroot -p -e "
  DROP DATABASE qa;
  DROP USER 'qa'@'localhost';
  FLUSH PRIVILEGES;
"
