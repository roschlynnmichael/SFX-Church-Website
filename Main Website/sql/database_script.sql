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

-- Create the mass timings table
CREATE TABLE mass_timings(
    Mass_No int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Mass_Day varchar(255) NOT NULL,
    Mass_Time varchar(255) NOT NULL,
    Mass_Lang varchar(255) NOT NULL
);

-- Create the novenas table
CREATE TABLE novenas(
    Nov_No int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nov_Name varchar(255) NOT NULL,
    Nov_Day varchar(255) NOT NULL
);

-- Create the weekly announcements table
CREATE TABLE weekly_announcements(
    ann_no INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ann longtext NOT NULL
);

-- Create the parish events updates table
CREATE TABLE parish_events_updates(
    Evn_no int PRIMARY KEY NOT NULL AUTO_INCREMENT, 
    Evn_Date DATE NOT NULL, 
    Evn_Time varchar(255) NOT NULL, 
    Evn_Content longtext NOT NULL
);

-- Create the announcement_cards table
CREATE TABLE announcement_cards(
    ann_id int NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    title varchar(255) NOT NULL, 
    content LONGTEXT NOT NULL, 
    image_url LONGTEXT NOT NULL
);

-- Create the list of priests table
CREATE TABLE parish_priests(
    p_id int NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    p_incharge VARCHAR(255) NOT NULL, 
    tenure VARCHAR(255) NOT NULL
);

--Create the gallery table
CREATE TABLE gallery_links(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    title varchar(255) not null, 
    link LONGTEXT NOT NULL
);
