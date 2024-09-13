-- Create the database
CREATE DATABASE church_db;

-- Use the newly created database
USE church_db;

-- Create the mass_timings table
CREATE TABLE mass_timings (
    mass_day VARCHAR(255) NOT NULL,
    mass_time TIME NOT NULL,
    mass_type VARCHAR(255) NOT NULL
);

-- Create the novenas table
CREATE TABLE novenas (
    novena_name VARCHAR(255) NOT NULL,
    novena_day VARCHAR(255) NOT NULL
);

-- Create the confessions table
CREATE TABLE confessions (
    confession_day VARCHAR(255) NOT NULL,
    confession_time TIME NOT NULL
);

-- Create the parish_updates_events table
CREATE TABLE parish_updates_events (
    event_name VARCHAR(255) NOT NULL,
    event_date VARCHAR(255) NOT NULL,
    event_time TIME NOT NULL
);

-- Create the admin users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the priests table
CREATE TABLE priests (
    name VARCHAR(255) NOT NULL,
    date_served_from DATE NOT NULL,
    date_served_to DATE NOT NULL,
    is_current_parish_priest TINYINT(1) NOT NULL
);

CREATE TABLE weekly_announcements (
    ID int(10) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    announcement VARCHAR(1500) NOT NULL
);