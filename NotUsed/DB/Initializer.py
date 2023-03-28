"""
CREATE TABLE IF NOT EXISTS User (
    id integer PRIMARY KEY autoincrement NOT NULL,
	userId text,
	chatId text,
	name text,
	surname text,
	username text,
	houseIds text
);

CREATE TABLE IF NOT EXISTS House (
  id integer PRIMARY KEY autoincrement NOT NULL,  
  houseId text PRIMARY KEY,
	userId text,
	deviceList text
);

CREATE TABLE IF NOT EXISTS Device (
    id integer PRIMARY KEY autoincrement NOT NULL,
    deviceId text,
    measureType text,
	deviceName text,
	availableServices text,
    lastUpdate text
);

CREATE TABLE IF NOT EXISTS ServiceDetail (
    id integer PRIMARY KEY autoincrement NOT NULL,
    deviceId text,
    serviceType text,
	topic text
);
"""