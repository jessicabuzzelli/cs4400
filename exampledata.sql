INSERT into ATTRACTION (Name, Description, isReserved, Price) values
("Eiffel Tower", "The Eiffel Tower is an iron lattice tower built for the World Fair", TRUE, 25),
("The Louvre", "The Louvre is the world's largest and most visited art museum.", TRUE, 15),
("Arc de Triomphe", "A famous monument in Paris, France honoring those who fought and died for France in the French Revolutionary War and Napoleonic War.", FALSE, 9.5),
("Metz Cathedral", "The historic Roman Catholic cathedral in Metz, the capital of Lorraine, France.", FALSE, NULL),
("Centre Pompidou Metz", "The Centre Pompidou Metz is a contemporary art museum.", FALSE, 12),
("Fort de Queuleu", "The Queuleu Fort was a fort used to defend Metz during the 1800s.", FALSE, NULL),
("Cathedral Notre Dame of Strasbourg", "Roman catholic cathedral in Strasbourg, France", FALSE, NULL),
("Petite France", "The historic center of Strasbourg, France containing 16th century buildings linked by cobblestone roads.", FALSE, NULL),
("Palais Rohan", "The Palais Rohan in Strasbourg is the former residence an ancient French noble family, the prince-bishops and cardinals of the House of Rohan. It is a major architectural, historical, and cultural landmark in the city.", FALSE, 12);

INSERT into ATTRACTION_ADDRESS (No, Street, City, State, Zip, Country, Attraction) VALUES
(5, 'Avenue Anatole', 'Paris', NULL , 75007, 'France', 'Eiffel Tower'),
(NULL, 'Rue de Rivoli', 'Paris', NULL , 75001, 'France', 'The Louvre'),
(NULL, 'Place Charles de Gaulle', 'Paris', NULL , 75008, 'France', 'Arc de Triomphe'),
(NULL, 'Place dArmes', 'Metz', NULL , 57000, 'France', 'Metz Cathedral'),
(1, 'Parvis des Droits de lHomme', 'Metz', NULL , 57020, 'France', 'Centre Pompidou Metz'),
(NULL, 'Rue de fort de Queuleu', 'Metz', NULL , 57070, 'France', 'Fort de Queuleu'),
(NULL, 'Place de la Cathedrale', 'Strasbourg', NULL , 67000, 'France', 'Cathedral Notre Dame of Strasbourg'),
(NULL, 'Grand Ile', 'Strasbourg', NULL , 67000, 'France', 'Petite France'),
(2, 'Place du Chateau', 'Strasbourg', NULL , 67000, 'France', 'Palais Rohan');

INSERT into PT_ADDRESS (No, Street, City, State, Zip, Country, PT, ClosestTo) VALUES
(1, "Place Joffre", "Paris", NULL, 75007, "France", "Metro to Champ de Mars / Tour Eiffel", "Eiffel Tower"),
(NULL, "Palais Royal", "Paris", NULL, 75001, "France", "Metro Louvre Rivoli", "The Louvre"),
(NULL, NULL, "Paris", NULL, 75017, "France", "Metro to Charles de Gaulle- Etoile", "Arc de Triomphe"),
(NULL, "Place d'Armes", "Metz", NULL, 57000, "France", "L3 Bus to Place d'Armes", "Metz Cathedral"),
(1, "Parvis des Droits de l'Homme", "Metz", NULL, 57020, "France", "METTIS A or B Bus to Centre Pompidou Metz", "Centre Pompidou Metz"),
(NULL, "Rue du fort de Queuleu", "Metz", NULL, 57070, "France", "C12 bus to Roederer", "Fort de Queuleu"),
(NULL, "Place de la Gare", "Strasbourg", NULL, 67000, "France", "Train to Gare de Strasbourg", "Cathedral Notre Dame of Strasbourg"),
(9, "Place Saint-Pierre-le-Vieux", "Strasbourg", NULL, 67000, "France", "Tram to Alt Winmärik-Vieux Marché aux Vins","Petite France"),
(NULL, NULL, "Strasbourg", NULL, 67000, "France", "Tram to Langstross/Grand Rue","Palais Rohan");

INSERT into HOURS_OF_OPERATION (OpenSunday, OpenMonday, OpenTuesday, OpenWednesday, OpenThursday, OpenFriday, OpenSaturday, OpeningTime, ClosingTime, Attraction) values
(TRUE,TRUE,TRUE,TRUE,TRUE,TRUE,TRUE, '09:00:00', '23:59:59', "Eiffel Tower"),
(TRUE,TRUE,FALSE,TRUE,TRUE,TRUE,TRUE, '09:00:00', '18:00:00', "The Louvre"),
(TRUE,TRUE,TRUE,TRUE,TRUE,TRUE,TRUE, '2018:07:01 00:00:00', '23:59:59', "Arc de Triomphe"),
(TRUE,TRUE,TRUE,TRUE,TRUE,TRUE,TRUE, '2018:07:01 00:00:00', '23:59:59', "Metz Cathedral"),
(TRUE, FALSE, TRUE, TRUE, TRUE, TRUE, TRUE, '10:00:00', '19:00:00', "Centre Pompidou Metz"),
(TRUE,TRUE,TRUE,TRUE,TRUE,TRUE,TRUE, '09:00:00', '17:00:00', "Fort de Queuleu"),
(TRUE,TRUE,TRUE,TRUE,TRUE,TRUE,TRUE, '2018:07:01 00:00:00', '23:59:59', "Cathedral Notre Dame of Strasbourg"),
(TRUE,TRUE,TRUE,TRUE,TRUE,TRUE,TRUE, '09:00:00', '23:59:59', "Petite France"),
(TRUE,TRUE,FALSE,TRUE,TRUE,TRUE,TRUE, '10:00:00', '18:00:00', "Palais Rohan");

INSERT into TIME_SLOT (StartDateTime, EndDateTime, Quantity, ReservationNumber, AttractionName) VALUES
('2018-07-28 09:00:00', '2018-07-28 10:00:00',10,1, 'Eiffel Tower'), ('2018-07-28 10:00:00', '2018-07-28 11:00:00',10,2, 'Eiffel Tower'),
('2018-07-28 11:00:00','2018-07-28 12:00:00',10,3, 'Eiffel Tower'),('2018-07-28 12:00:00','2018-07-28 13:00:00',10,4, 'Eiffel Tower'),
('2018-07-28 13:00:00','2018-07-28 14:00:00',10,5, 'Eiffel Tower'),('2018-07-28 14:00:00','2018-07-28 15:00:00',10,6, 'Eiffel Tower'),
('2018-07-28 15:00:00','2018-07-28 16:00:00',10,7, 'Eiffel Tower'),('2018-07-28 16:00:00','2018-07-28 17:00:00',10,8, 'Eiffel Tower'),
('2018-07-28 17:00:00','2018-07-28 18:00:00',10,9, 'Eiffel Tower'),('2018-07-28 18:00:00','2018-07-28 19:00:00',10,10, 'Eiffel Tower'),
('2018-07-28 19:00:00','2018-07-28 20:00:00',10,11, 'Eiffel Tower'),('2018-07-28 20:00:00','2018-07-28 21:00:00',10,12, 'Eiffel Tower'),
('2018-07-28 21:00:00','2018-07-28 22:00:00',10,13, 'Eiffel Tower'),('2018-07-28 22:00:00','2018-07-28 23:00:00',10,14, 'Eiffel Tower'),
('2018-07-28 23:00:00','2018-07-28 23:59:59',10,15, 'Eiffel Tower'),('2018-07-28 09:00:00','2018-07-28 12:00:00',20,99, 'The Louvre'),
('2018-07-28 10:00:00','2018-07-28 13:00:00',20,98, 'The Louvre'),('2018-07-28 11:00:00','2018-07-28 14:00:00',20,97, 'The Louvre'),
('2018-07-28 12:00:00', '2018-07-28 15:00:00',20,96, 'The Louvre'),('2018-07-28 13:00:00', '2018-07-28 16:00:00',20,95, 'The Louvre'),
('2018-07-28 14:00:00', '2018-07-28 17:00:00',20,94, 'The Louvre'),('2018-07-28 15:00:00', '2018-07-28 18:00:00',20,93, 'The Louvre');

INSERT INTO USER (Email, Name, LastName, FirstName, isAdmin, isSuspended, Password, BirthdayMonth, BirthdayDay, BirthdayYear) VALUES ("exampleuser@gmail.com", "Example User", "User", "Example", FALSE, FALSE, 'password', 12, 13, 1999);
INSERT INTO USER_ADDRESS(No, Street, City, State, Zip, Country, User) VALUES (123, 'Main Street','GTL','Georgia','1234','France','exampleuser@gmail.com');
INSERT INTO CREDIT_CARD (CCNumber, ExpiryMonth, ExpiryYear, CVV, Email) VALUES (12345678910, 11, 22, 123, 'exampleuser@gmail.com');

INSERT INTO TRIP (City, StartDate, Booked, StartDateTime, EndDateTime, TotalCost, UserEmail, PaidBy) VALUES
('Paris', '2018-07-28', TRUE, '2018-07-28 08:00:00', '2018-07-28 21:30:00', 50.0, "exampleuser@gmail.com", 12345678910);

INSERT INTO ACTIVITY (StartDateTime, EndDateTime, NumberInParty, AttractionName, TripID) VALUES
('2018-07-28 09:00:00', '2018-07-28 10:00:00', 1, "Eiffel Tower", 1),
('2018-07-28 15:00:00', '2018-07-28 18:00:00', 1, "The Louvre", 1),
('2018-07-28 22:00:00','2018-07-28 23:00:00', 1, "Arc de Triomphe",1);


UPDATE TIME_SLOT SET Quantity = Quantity - 1 WHERE StartDateTime = '2018-07-28 09:00:00' AND EndDateTime = '2018-07-28 10:00:00' AND AttractionName = "Eiffel Tower" AND ReservationNumber = 1;

UPDATE TIME_SLOT SET Quantity = Quantity - 1 WHERE StartDateTime = '2018-07-28 15:00:00' AND EndDateTime = '2018-07-28 18:00:00' AND AttractionName = "The Louvre" AND ReservationNumber = 20;

INSERT INTO REVIEW (Title, Body, ReviewDate, UserEmail, AttractionName) VALUES ("EF", "I had a fantastic time at the Eiffel Tower. It was very tall and pointy.", '2018-07-28 15:00:00', "exampleuser@gmail.com", "Eiffel Tower");
INSERT INTO USER (Email, Name,FirstName, LastName, isAdmin, isSuspended, Password, BirthdayMonth, BirthdayDay, BirthdayYear) VALUES ("exampleadmin@gmail.com", "Example Admin", "Example", "Admin", TRUE, FALSE,'password',10, 12,1998 );
