--- Creating the user for the database.
DROP USER IF EXISTS 'security_admin'@'localhost';

CREATE USER 'security_admin'@'localhost'
IDENTIFIED BY 'P@ssw0rd'
;

GRANT ALL PRIVILEGES
ON *.* TO 'security_admin'@'localhost'
WITH GRANT OPTION
;

FLUSH PRIVILEGES;


--- mariadb -u security_admin