DROP DATABASE IF EXISTS PythonDataExplorerDB;
CREATE DATABASE PythonDataExplorerDB;
USE PythonDataExplorerDB;

-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- Procedure to create the all of the tables in the database
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DROP PROCEDURE IF EXISTS makePythonDataExplorerDB;
DELIMITER //
CREATE PROCEDURE makePythonDataExplorerDB()
	BEGIN
        CREATE TABLE `Users` (
          `UserId`   int(11) NOT NULL AUTO_INCREMENT,
          `username` varchar(255) NOT NULL,
          `password` varchar(255) NOT NULL,
          `email`    varchar(255) NOT NULL,
          PRIMARY KEY (`UserId`));
        CREATE TABLE `Messages` (
          `MessageId`   int(11) NOT NULL AUTO_INCREMENT,
          `MessageBody` varchar(255) NOT NULL,
          `Timestamp`   timestamp NOT NULL,
          PRIMARY KEY (`MessageId`));
        CREATE TABLE `UserMessages` (
          `UserId`    int(11) NOT NULL,
          `MessageId` int(11) NOT NULL,
          PRIMARY KEY (`UserId`, `MessageId`));
        ALTER TABLE `UserMessages` ADD CONSTRAINT FKUserMessag37238 FOREIGN KEY (`UserId`) REFERENCES Users (`UserId`);
        ALTER TABLE `UserMessages` ADD CONSTRAINT FKUserMessag243976 FOREIGN KEY (`MessageId`) REFERENCES Messages (`MessageId`);
   END//
DELIMITER ;
CALL makePythonDataExplorerDB();