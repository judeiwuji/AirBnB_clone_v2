-- Database
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

USE `hbnb_dev_db`;

-- Create a DB User
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privilege
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
