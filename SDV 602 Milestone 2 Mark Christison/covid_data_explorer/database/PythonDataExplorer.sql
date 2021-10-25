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
          `UserId`   INT(11) NOT NULL AUTO_INCREMENT,
          `username` VARCHAR(255) NOT NULL,
          `password` VARCHAR(255) NOT NULL,
          `email`    VARCHAR(255) NOT NULL,
          PRIMARY KEY (`UserId`));
        CREATE TABLE `Messages` (
          `MessageId`   INT(11) NOT NULL AUTO_INCREMENT,
          `MessageBody` VARCHAR(255) NOT NULL,
          `Timestamp`   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
          PRIMARY KEY (`MessageId`));
        CREATE TABLE `UserMessages` (
          `UserId`    INT(11) NOT NULL,
          `MessageId` INT(11) NOT NULL,
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
        IF EXISTS (SELECT * FROM Users WHERE `username` = username) THEN
            BEGIN
                SELECT "Username already exists" AS `MESSAGE`;
            END;
        ELSE
            BEGIN
                INSERT INTO tblUser(`username` , `password`, `email`) VALUES (username, password, email);
                SELECT concat(username ," has been registered") AS `MESSAGE`;
            END;
        END IF;
    COMMIT;
END//
DELIMITER ;

-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- Send Message
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
DROP PROCEDURE IF EXISTS SendMessage;
DELIMITER //
CREATE PROCEDURE SendMessage(username VARCHAR(255), message VARCHAR(255))
BEGIN
    DECLARE exit handler for sqlexception
        BEGIN
            GET DIAGNOSTICS CONDITION 1
            @P1 = MYSQL_ERRNO, @P2 = MESSAGE_TEXT;
            SELECT "SendMessage error", @P1 AS ERROR_NUM, @P2 AS MESSAGE;
            ROLLBACK;
        END;
    START TRANSACTION;
        BEGIN
            INSERT INTO Messages(`MessageBody`) VAlUES (message);
        END;
    COMMIT;
END//
DELIMITER ;

-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- Get Messages
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DROP PROCEDURE IF EXISTS GetMessages;
DELIMITER //
CREATE PROCEDURE SendMessage()
BEGIN
    DECLARE exit handler for sqlexception
        BEGIN
            GET DIAGNOSTICS CONDITION 1
            @P1 = MYSQL_ERRNO, @P2 = MESSAGE_TEXT;
            SELECT "GetMessages error", @P1 AS ERROR_NUM, @P2 AS MESSAGE;
            ROLLBACK;
        END;
    START TRANSACTION;
        SELECT * from Messages;
    COMMIT;
END//
DELIMITER ;


