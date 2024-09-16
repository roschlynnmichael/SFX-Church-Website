-- Create the database
CREATE DATABASE church_db;

-- Use the newly created database
USE church_db;

-- Create the communities table
CREATE TABLE communities(
    Comm_No int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Comm_Name varchar(255) NOT NULL,
    Rep_Name varchar(255) NOT NULL
);

-- Create the religious associations table
CREATE TABLE associations(
    Ass_No int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Ass_Name varchar(255) NOT NULL,
    Rep_Name varchar(255) NOT NULL
);

