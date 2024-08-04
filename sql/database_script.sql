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