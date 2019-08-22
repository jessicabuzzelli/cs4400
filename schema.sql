DROP DATABASE IF EXISTS TripPlanner;
CREATE DATABASE TripPlanner;
USE TripPlanner;

CREATE TABLE USER (  
	Email VARCHAR(50) PRIMARY KEY,
	Name VARCHAR(50),
	isAdmin BOOLEAN NOT NULL,
	isSuspended BOOLEAN NOT NULL
); 

CREATE TABLE CREDIT_CARD (
	CCNumber INT PRIMARY KEY, 
	Expiry INT NOT NULL,
	CVV INT NOT NULL
);

CREATE TABLE ATTRACTION (
	Name VARCHAR(50) PRIMARY KEY,
	Description VARCHAR(500), 
	IsReserved BOOLEAN, 
	Price FLOAT	
);

CREATE TABLE REVIEW (
	Title VARCHAR(25),
	Body VARCHAR(500),
	Date DATE,
	UserEmail VARCHAR(50),
	AttractionName VARCHAR(50),
	FOREIGN KEY (UserEmail) REFERENCES USER(Email),
	FOREIGN KEY (AttractionName) REFERENCES ATTRACTION(Name),
	PRIMARY KEY (UserEmail, AttractionName)
);

CREATE TABLE TRIP (
	City VARCHAR(50), 
	StartDate INT, 
	Booked BOOLEAN, 
	StartDateTime DATETIME, 
	EndDateTime DATETIME, 
	TotalCost FLOAT, 
	UserEmail VARCHAR(50)
	PaidBy INT,
	FOREIGN KEY (UserEmail) REFERENCES USER(Email),
	FOREIGN KEY (PaidBy) REFERENCES CREDIT_CARD(CCNumber),	
	TripID INT PRIMARY KEY, 
);

CREATE TABLE ACTIVITY (
	StartDateTime DATETIME, 
	EndDateTime DATETIME, 
	NumberInParty INT, 
	AttractionName VARCHAR(50),
	TripID INT,
	FOREIGN KEY (AttractionName) REFERENCES ATTRACTION(Name),
	FOREIGN KEY (TripID) REFERENCES TRIP(TripID),
	PRIMARY KEY (StartDateTime, AttractionName)
);

CREATE TABLE TIME_SLOT (
	StartDateTime DATETIME, 
	EndDateTime DATETIME, 
	Quantity INT, 
	ReservationNumber INT, 
	AttractionName VARCHAR(50),
	FOREIGN KEY (AttractionName) REFERENCES ATTRACTION(Name),
	PRIMARY KEY (StartDateTime, EndDateTime, AttractionName, ReservationNumber)
);

CREATE TABLE USER_ADDRESS (
	Number INT,
	Street VARCHAR(50),
	City VARCHAR(50),
	State VARCHAR(50),
	Zip INT,
	Country VARCHAR(50),
	User VARCHAR(50),
	FOREIGN KEY (User) REFERENCES USER(Email), 
	PRIMARY KEY (User)
);



CREATE TABLE ATTRACTION_ADDRESS (
	Number INT,
	Street VARCHAR(50),
	City VARCHAR(50),
	State VARCHAR(50),
	Zip INT,
	Country VARCHAR(50),
	Attraction VARCHAR(50),
	FOREIGN KEY (Attraction) REFERENCES Attraction(Name), 
	PRIMARY KEY (Attraction)

);

CREATE TABLE CCD_ADDRESS (
Number INT,
Street VARCHAR(50),
City VARCHAR(50),
State VARCHAR(50),
Zip INT,
Country VARCHAR(50),
CCD INT,
FOREIGN KEY (CCD) REFERENCES Credit_Card(CCNumber), 
PRIMARY KEY (CCD)

);

CREATE TABLE PT_ADDRESS (
Number INT,
Street VARCHAR(50),
City VARCHAR(50),
State VARCHAR(50),
Zip INT,
Country VARCHAR(50),
PT VARCHAR(150),
PRIMARY KEY (PT)

);

CREATE TABLE HOURS_OF_OPERATION (
	OpenSunday BOOLEAN,
OpenMonday BOOLEAN,
OpenTuesday BOOLEAN,
OpenWednesday BOOLEAN,
OpenThursday BOOLEAN,
OpenFriday BOOLEAN,
OpenSaturday BOOLEAN,
	OpeningTime TIME,
	ClosingTime TIME,
	Attraction VARCHAR(50),
	FOREIGN KEY (Attraction) REFERENCES Attraction(Name)
	
);
