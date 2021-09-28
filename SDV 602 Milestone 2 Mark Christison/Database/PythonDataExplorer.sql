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

-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- Register a User
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DROP PROCEDURE IF EXISTS RegisterUser;
DELIMITER //
CREATE PROCEDURE RegisterUser(username VARCHAR(255), password VARCHAR(255), email VARCHAR(255))
BEGIN
    DECLARE exit handler for sqlexception
        BEGIN
            GET DIAGNOSTICS CONDITION 1
            @P1 = MYSQL_ERRNO, @P2 = MESSAGE_TEXT;
            SELECT "registerUser error", @P1 AS ERROR_NUM, @P2 AS MESSAGE;
            ROLLBACK;
        END;
    START TRANSACTION;
        IF EXISTS (SELECT * FROM tblUser WHERE `username` = username) THEN
            BEGIN
                SELECT "Username already exists" AS `MESSAGE`;
            END;
        ELSE
            BEGIN
                INSERT INTO tblUser(`username` , `password`, `email`) VALUES (username, password, email);
                SELECT concat(pUserName ," has been registered") AS `MESSAGE`;
            END;
        END IF;
    COMMIT;
END//
DELIMITER ;
