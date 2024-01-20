-- creates the MySQL server user user_0d_2
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- creates the database hbtn_0d_2
CREATE DATABASE hbtn_0d_2;

-- grants select privileges on the hbtn_0d_2 database to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

