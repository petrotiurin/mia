CREATE TABLE weather(
 id INTEGER PRIMARY KEY,
 weather TEXT NOT NULL,
 write_datetime datetime,
 temp_max REAL,
 temp_min REAL,
 temp REAL,
 visibility REAL,
 name TEXT
);

CREATE TABLE driver_info(
 id INTEGER PRIMARY KEY ,
 phone TEXT NOT NULL,
 password REAL NOT NULL,
 token TEXT
);