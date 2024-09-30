--- Creating the database.
DROP DATABASE IF EXISTS security_app;

CREATE DATABASE security_app;

-- import the tables.
source tables.sql;
source procedures.sql;