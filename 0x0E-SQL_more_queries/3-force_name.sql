-- A script that creates the table force_name on your MySQL server.
-- and attribute 'name' in force_name can't be NULL

CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL
);
