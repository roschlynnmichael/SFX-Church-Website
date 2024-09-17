-- Use the current church db
USE church_db;

-- Create the announcement_cards table
CREATE TABLE announcement_cards(
    ann_id int NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    title varchar(255) NOT NULL, 
    content LONGTEXT NOT NULL, 
    image_url LONGTEXT NOT NULL
);

-- Create the admin table
CREATE TABLE admin_user(
    a_id int NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    a_name varchar(128) NOT NULL, 
    a_pass varchar(128) NOT NULL
);