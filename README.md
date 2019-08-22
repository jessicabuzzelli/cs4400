# cs4400
A command-line GUI made with Tkinter for CS 4400 at Georgia Tech Lorraine in Summer 2018 to create trip itineraries by booking timeslots at various attractions loaded from a MySQL database or write/read reviews of selected attractions. 

* gui.py pulls from a MySQL database constructed by schema.sql and populated by exampledata.sql. 
* When ran, a login window will pop up -- you can either login or register as a New User. 
* If the account used is designated as an admin, an admin dashboard will appear where you can create users, add new attractions, and suspend users. 
* Otherwise, a customer dashboard will ope after creating an account/signing in where you can edit the account's profile, view a selected trip, edit/create a new trip, write reviews, read reviews, and log out. 
