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
        CREATE TABLE Category (
          CategoryID   int(10) NOT NULL AUTO_INCREMENT,
          CategoryName varchar(255) NOT NULL,
          Description  varchar(255),
          Image        varchar(100),
          PRIMARY KEY (CategoryID));
        CREATE TABLE Product (
          ProductID        int(10) NOT NULL AUTO_INCREMENT,
          CategoryID       int(10) NOT NULL,
          LastModifiedBy   int(10) NOT NULL,
          ProductName      varchar(255),
          Manufacturer     varchar(255),
          Description      varchar(255),
          QtyInStock       int(10),
          Price            decimal(13, 2),
          MSRP             varchar(255),
          Image            varchar(100),
          LastModifiedDate date NOT NULL,
          IsAvailable      tinyint(1) NOT NULL,
          CONSTRAINT IsAvailable
            PRIMARY KEY (ProductID));
        CREATE TABLE `Order` (
          OrderID        int(10) NOT NULL AUTO_INCREMENT,
          CustomerID     int(10) NOT NULL,
          PaymentID      int(10),
          Status         varchar(255) NOT NULL,
          OrderDate      date,
          ShippedDate    date,
          Comments       varchar(255),
          TrackingNumber varchar(255),
          IsDeleted      tinyint(1) NOT NULL,
          PRIMARY KEY (OrderID));
        CREATE TABLE Payment (
          PaymentID   int(10) NOT NULL AUTO_INCREMENT,
          CustomerID  int(10) NOT NULL,
          PaymentDate date,
          Amount      decimal(13, 2) NOT NULL,
          PRIMARY KEY (PaymentID));
        CREATE TABLE Customer (
          CustomerID int(10) NOT NULL AUTO_INCREMENT,
          PersonID   int(10) NOT NULL,
          PRIMARY KEY (CustomerID));
        CREATE TABLE Order_Product (
          OrderID   int(10) NOT NULL,
          ProductID int(10) NOT NULL,
          Qty       int(10) NOT NULL,
          PriceEach decimal(13, 2) NOT NULL,
          PRIMARY KEY (OrderID,
          ProductID));
        CREATE TABLE Employee (
          EmployeeID int(10) NOT NULL AUTO_INCREMENT,
          PersonID   int(10) NOT NULL,
          Role       varchar(255),
          PRIMARY KEY (EmployeeID));
        CREATE TABLE Person (
          PersonID  int(10) NOT NULL AUTO_INCREMENT,
          FirstName varchar(255) NOT NULL,
          LastName  varchar(255) NOT NULL,
          Email     varchar(255) NOT NULL,
          Phone     varchar(255),
          Address   varchar(255),
          City      varchar(255),
          PostCode  int(4),
          PRIMARY KEY (PersonID));
        CREATE TABLE Users (
          UserId   int(11) NOT NULL AUTO_INCREMENT,
          username varchar(255) NOT NULL,
          password varchar(255) NOT NULL,
          email    varchar(255) NOT NULL,
          PRIMARY KEY (UserId));
        CREATE TABLE Messages (
          MessageId   int(11) NOT NULL AUTO_INCREMENT,
          MessageBody varchar(255) NOT NULL,
          Timestamp   timestamp NOT NULL,
          PRIMARY KEY (MessageId));
        CREATE TABLE UserMessages (
          UserId    int(11) NOT NULL,
          MessageId int(11) NOT NULL,
          PRIMARY KEY (UserId,
          MessageId));
        ALTER TABLE Payment ADD CONSTRAINT FKPayment617515 FOREIGN KEY (CustomerID) REFERENCES Customer (CustomerID);
        ALTER TABLE `Order` ADD CONSTRAINT FKOrder835009 FOREIGN KEY (CustomerID) REFERENCES Customer (CustomerID);
        ALTER TABLE Order_Product ADD CONSTRAINT FKOrder_Prod381299 FOREIGN KEY (OrderID) REFERENCES `Order` (OrderID);
        ALTER TABLE Order_Product ADD CONSTRAINT FKOrder_Prod535307 FOREIGN KEY (ProductID) REFERENCES Product (ProductID);
        ALTER TABLE Product ADD CONSTRAINT FKProduct608764 FOREIGN KEY (CategoryID) REFERENCES Category (CategoryID);
        ALTER TABLE Customer ADD CONSTRAINT FKCustomer415114 FOREIGN KEY (PersonID) REFERENCES Person (PersonID);
        ALTER TABLE Employee ADD CONSTRAINT FKEmployee879888 FOREIGN KEY (PersonID) REFERENCES Person (PersonID);
        ALTER TABLE Product ADD CONSTRAINT FKProduct47824 FOREIGN KEY (LastModifiedBy) REFERENCES Employee (EmployeeID);
        ALTER TABLE `Order` ADD CONSTRAINT FKOrder355972 FOREIGN KEY (PaymentID) REFERENCES Payment (PaymentID);
        ALTER TABLE UserMessages ADD CONSTRAINT FKUserMessag37238 FOREIGN KEY (UserId) REFERENCES Users (UserId);
        ALTER TABLE UserMessages ADD CONSTRAINT FKUserMessag243976 FOREIGN KEY (MessageId) REFERENCES Messages (MessageId);
   END//
DELIMITER ;
CALL makePythonDataExplorerDB();