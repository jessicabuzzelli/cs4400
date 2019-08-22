from tkinter import *
import mysql.connector


class GUI:

    def __init__(self):
        self.loginPage()

    def loginPage(self):
        self.login = Tk()
        self.login.title("Login")
        self.login.config(bg="white")
        frame = Frame(self.login)
        frame.grid(row=0, column=0, columnspan=6)

        emailLabel = Label(self.login, text="Email:", bg="SkyBlue2")
        emailLabel.grid(column=1, row=0, sticky=W)
        self.emailEntry = Entry(self.login, width=20)
        self.emailEntry.grid(column=2, row=0)
        passwordLabel = Label(self.login, text="Password:", bg="SkyBlue2")
        passwordLabel.grid(column=1, row=1, sticky=W)
        self.passwordEntry = Entry(self.login, width=20)
        self.passwordEntry.grid(column=2, row=1)
        frame2 = Frame(self.login)
        registerButton = Button(frame2, text="Register", width=8, command=self.registerPage)
        registerButton.grid(column=1, row=3, sticky=W)
        loginButton = Button(frame2, text="Login", width=8, command=self.loginCheck)
        loginButton.grid(column=2, row=3, sticky=W)
        frame2.grid(row=3, column=2)
        self.login.mainloop()

    def registerPage(self):
        self.login.withdraw()
        register = Toplevel()
        self.register = register
        register.title("Registration")
        register.config(bg="white")
        frame = Frame(register)

        regemailLabel = Label(frame)
        regemailLabel.pack()
        frame.grid(row=0, column=0, rowspan=6)
        regemailLabel = Label(register, text="Email:", bg="SkyBlue2")
        regemailLabel.grid(row=0, column=1, sticky=W, padx=5)
        regemailEntry = Entry(register, width=15)
        regemailEntry.grid(row=0, column=2)
        self.regemailEntry = regemailEntry
        regconfirmEmailLabel = Label(register, text="Confirm Email:", bg="SkyBlue2")
        regconfirmEmailLabel.grid(row=1, column=1, sticky=W, padx=5)
        regconfirmEmailEntry = Entry(register, width=15)
        regconfirmEmailEntry.grid(row=1, column=2)
        self.regconfirmEmailEntry = regconfirmEmailEntry
        regpasswordLabel = Label(register, text="Password:", bg="SkyBlue2")
        regpasswordLabel.grid(row=2, column=1, sticky=W, padx=5)
        regpasswordEntry = Entry(register, width=15)
        regpasswordEntry.grid(row=2, column=2)
        self.regpasswordEntry = regpasswordEntry
        regconfirmLabel = Label(register, text="Confirm Password:", bg="SkyBlue2")
        regconfirmLabel.grid(row=3, column=1, sticky=W, padx=5)
        regconfirmEntry = Entry(register, width=15)
        regconfirmEntry.grid(row=3, column=2)
        self.regconfirmEntry = regconfirmEntry
        self.regnameLabel = Label(register, text="First Name:", bg="SkyBlue2")
        self.regnameLabel.grid(row=4, column=1, sticky=W, padx=5)
        regnameEntry = Entry(register, width=15)
        regnameEntry.grid(row=4, column=2)
        self.regnameEntry = regnameEntry
        reglastLabel = Label(register, text="Last Name:", bg="SkyBlue2")
        reglastLabel.grid(row=5, column=1, sticky=W, padx=5)
        reglastEntry = Entry(register, width=15)
        reglastEntry.grid(row=5, column=2)
        self.reglastEntry = reglastEntry
        regaddress1Label = Label(register, text="Number", bg="SkyBlue2")
        regaddress1Label.grid(row=6, column=1, sticky=W, padx=5)
        regaddress1Entry = Entry(register, width=15)
        regaddress1Entry.grid(row=6, column=2)
        self.regaddress1Entry = regaddress1Entry
        regaddress2Label = Label(register, text="Street", bg="SkyBlue2")
        regaddress2Label.grid(row=7, column=1, sticky=W, padx=5)
        regaddress2Entry = Entry(register, width=15)
        regaddress2Entry.grid(row=7, column=2)
        self.regaddress2Entry = regaddress2Entry
        regcityLabel = Label(register, text="City:", bg="SkyBlue2")
        regcityLabel.grid(row=8, column=1, sticky=W, padx=5)
        regcityEntry = Entry(register, width=15)
        regcityEntry.grid(row=8, column=2)
        self.regcityEntry = regcityEntry
        regstateLabel = Label(register, text="State:", bg="SkyBlue2")
        regstateLabel.grid(row=9, column=1, sticky=W, padx=5)
        regstateEntry = Entry(register, width=15)
        regstateEntry.grid(row=9, column=2)
        self.regstateEntry = regstateEntry
        regcodeLabel = Label(register, text="Postal Code:", bg="SkyBlue2")
        regcodeLabel.grid(row=10, column=1, sticky=W, padx=5)
        regcodeEntry = Entry(register, width=15)
        regcodeEntry.grid(row=10, column=2)
        self.regcodeEntry = regcodeEntry
        regcountryLabel = Label(register, text="Country:", bg="SkyBlue2")
        regcountryLabel.grid(row=11, column=1, sticky=W, padx=5)

        countryPull = StringVar(register)
        countryPull.set('Country')
        pull = OptionMenu(register, countryPull, 'United States', 'France', 'Germany', 'Spain',
                          command=self.registrationCountryFunc)
        pull.grid(row=11, column=2, sticky=W, padx=5)

        regcardLabel = Label(register, text='Credit Card:', bg='SkyBlue2')
        regcardLabel.grid(row=0, column=3, sticky=W, padx=5)
        regcardEntry = Entry(register, width=25)
        regcardEntry.grid(row=0, column=4)
        self.regcardEntry = regcardEntry
        regexpLabel = Label(register, text='CC Expiry:', bg='SkyBlue2')
        regexpLabel.grid(row=1, column=3, sticky=W, padx=5)

        creditPullMonth = StringVar(register)
        creditPullMonth.set('Month')
        pulling2 = OptionMenu(register, creditPullMonth, '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                              '11', '12', command=self.registrationCCMonth)
        pulling2.grid(row=1, column=4, sticky=W, padx=5)

        creditPull = StringVar(register)
        creditPull.set('Year')
        pulling = OptionMenu(register, creditPull, '2019', '2020', '2021', '2022', '2023', '2024',
                             command=self.registrationCCYear)
        pulling.grid(row=1, column=4, sticky=E, padx=5)

        regbirthdateLabel = Label(register, text='Birthdate:', bg='SkyBlue2')
        regbirthdateLabel.grid(row=2, column=3, sticky=W, padx=5)

        birthdayPullMonth = StringVar(register)
        birthdayPullMonth.set('Month')
        birthdayPulling = OptionMenu(register, birthdayPullMonth, '01', '02', '03', '04', '05', '06', '07', '08', '09',
                                     '10', '11', '12', command=self.registrationBMonth)
        birthdayPulling.grid(row=2, column=4, sticky=W, padx=5)

        birthdayPullDay = StringVar(register)
        birthdayPullDay.set('Day')
        birthdayPulling2 = OptionMenu(register, birthdayPullDay, '01', '02', '03', '04', '05', '06', '07', '08', '09',
                                      '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
                                      '23', '24', '25', '26', '27', '28', '29', '30', '31',
                                      command=self.registrationBDay)
        birthdayPulling2.grid(row=2, column=4, sticky=E, padx=5)

        birthdayPullYear = StringVar(register)
        birthdayPullYear.set('Year')
        birthdayPulling3 = OptionMenu(register, birthdayPullYear, '1990', '1991', '1992', '1993', '1994', '1995',
                                      '1996', '1997', '1998', '1999', '2000', command=self.registrationBYear)
        birthdayPulling3.grid(row=2, column=5, sticky=W, padx=5)

        acceptButton = Button(register, text="Accept Changes", width=15, command=self.registerNew)
        acceptButton.grid(row=12, column=3)
        register.mainloop()

    def registrationCountryFunc(self, value):
        self.registrationCountryVal = value
        print(self.registrationCountryVal)
        return self.registrationCountryVal

    def registrationCCMonth(self, value):
        self.registrationCCMonthVal = value
        return self.registrationCCMonthVal

    def registrationCCYear(self, value):
        self.registrationCCYearVal = value
        return self.registrationCCYearVal

    def registrationBMonth(self, value):
        self.registrationBMonthVal = value
        return self.registrationBMonthVal

    def registrationBDay(self, value):
        self.registrationBDayVal = value
        return self.registrationBDayVal

    def registrationBYear(self, value):
        self.registrationBYearVal = value
        return self.registrationBYearVal

    def editAttractionPage(self):
        self.admindash.withdraw()
        editA = Toplevel()
        self.editA = editA
        editA.title("New/Edit Attraction")
        editA.config(bg="white")
        frame = Frame(editA)

        AttractionLabel = Label(editA, text="Attraction:", bg="SkyBlue2")
        AttractionLabel.grid(row=0, column=1, sticky=W, padx=5)
        AttractionEntry = Entry(editA, width=15)
        AttractionEntry.grid(row=0, column=2)
        self.AttractionEntry = AttractionEntry

        DescriptionLabel = Label(editA, text="Description:", bg="SkyBlue2")
        DescriptionLabel.grid(row=1, column=1, sticky=W, padx=5)
        DescriptionEntry = Entry(editA, width=15)
        DescriptionEntry.grid(row=1, column=2)
        self.DescriptionEntry = DescriptionEntry

        AddressLabel = Label(editA, text="Address Number:", bg="SkyBlue2")
        AddressLabel.grid(row=2, column=1, sticky=W, padx=5)
        AddressEntry = Entry(editA, width=15)
        AddressEntry.grid(row=2, column=2)
        self.AddressEntry = AddressEntry

        Address2Label = Label(editA, text="Street:", bg="SkyBlue2")
        Address2Label.grid(row=3, column=1, sticky=W, padx=5)
        Address2Entry = Entry(editA, width=15)
        Address2Entry.grid(row=3, column=2)
        self.Address2Entry = Address2Entry

        CityLabel = Label(editA, text="City:", bg="SkyBlue2")
        CityLabel.grid(row=4, column=1, sticky=W, padx=5)
        CityEntry = Entry(editA, width=15)
        CityEntry.grid(row=4, column=2)
        self.CityEntry = CityEntry

        StateLabel = Label(editA, text="State:", bg="SkyBlue2")
        StateLabel.grid(row=5, column=1, sticky=W, padx=5)
        StateEntry = Entry(editA, width=15)
        StateEntry.grid(row=5, column=2)
        self.StateEntry = StateEntry

        CountryLabel = Label(editA, text="Country:", bg="SkyBlue2")
        CountryLabel.grid(row=6, column=1, sticky=W, padx=5)
        CountryEntry = Entry(editA, width=15)
        CountryEntry.grid(row=6, column=2)
        self.CountryEntry = CountryEntry

        PostalCodeLabel = Label(editA, text="PostalCode:", bg="SkyBlue2")
        PostalCodeLabel.grid(row=7, column=1, sticky=W, padx=5)
        PostalCodeEntry = Entry(editA, width=15)
        PostalCodeEntry.grid(row=7, column=2)
        self.PostalCodeEntry = PostalCodeEntry

        OpenHoursLabel = Label(editA, text="Opens at:", bg="SkyBlue2")
        OpenHoursLabel.grid(row=8, column=1, sticky=W, padx=5)
        OpenHoursEntry = Entry(editA, width=15)
        OpenHoursEntry.grid(row=8, column=2)
        self.OpenHoursEntry = OpenHoursEntry

        CloseHoursLabel = Label(editA, text="Closes at:", bg="SkyBlue2")
        CloseHoursLabel.grid(row=9, column=1, sticky=W, padx=5)
        CloseHoursEntry = Entry(editA, width=15)
        CloseHoursEntry.grid(row=9, column=2)
        self.CloseHoursEntry = CloseHoursEntry

        NearestTransLabel = Label(editA, text="Nearest Public Transport:", bg="SkyBlue2")
        NearestTransLabel.grid(row=1, column=4, sticky=W, padx=5)
        NearestTransEntry = Entry(editA, width=15)
        NearestTransEntry.grid(row=1, column=5)
        self.NearestTransEntry = NearestTransEntry

        PTNumLabel = Label(editA, text="PT Address #:", bg="SkyBlue2")
        PTNumLabel.grid(row=2, column=4, sticky=W, padx=5)
        PTNumEntry = Entry(editA, width=15)
        PTNumEntry.grid(row=2, column=5)
        self.PTNumEntry = PTNumEntry

        ptStreetLabel = Label(editA, text="PT Street:", bg="SkyBlue2")
        ptStreetLabel.grid(row=3, column=4, sticky=W, padx=5)
        ptStreetEntry = Entry(editA, width=15)
        ptStreetEntry.grid(row=3, column=5)
        self.ptStreetEntry = ptStreetEntry

        ptCityLabel = Label(editA, text="PT City:", bg="SkyBlue2")
        ptCityLabel.grid(row=4, column=4, sticky=W, padx=5)
        ptCityEntry = Entry(editA, width=15)
        ptCityEntry.grid(row=4, column=5)
        self.ptCityEntry = ptCityEntry

        ptStateLabel = Label(editA, text="PT State:", bg="SkyBlue2")
        ptStateLabel.grid(row=5, column=4, sticky=W, padx=5)
        ptStateEntry = Entry(editA, width=15)
        ptStateEntry.grid(row=5, column=5)
        self.ptStateEntry = ptStateEntry

        ptZipLabel = Label(editA, text="PT Postal Code:", bg="SkyBlue2")
        ptZipLabel.grid(row=6, column=4, sticky=W, padx=5)
        ptZipEntry = Entry(editA, width=15)
        ptZipEntry.grid(row=6, column=5)
        self.ptZipEntry = ptZipEntry

        ptCountryLabel = Label(editA, text="PT Country:", bg="SkyBlue2")
        ptCountryLabel.grid(row=7, column=4, sticky=W, padx=5)
        ptCountryEntry = Entry(editA, width=15)
        ptCountryEntry.grid(row=7, column=5)
        self.ptCountryEntry = ptCountryEntry

        PriceLabel = Label(editA, text="Price:", bg="SkyBlue2")
        PriceLabel.grid(row=10, column=1, sticky=W, padx=5)
        PriceEntry = Entry(editA, width=15)
        PriceEntry.grid(row=10, column=2)
        self.PriceEntry = PriceEntry

        ReservedLabel = Label(editA, text="Reservation Needed?:", bg="SkyBlue2")
        ReservedLabel.grid(row=11, column=1, sticky=W, padx=5)
        ReservedEntry = Entry(editA, width=15)
        ReservedEntry.grid(row=11, column=2)
        self.ReservedEntry = ReservedEntry

        acceptButton = Button(editA, text="Accept Changes", width=15, command=self.editAttraction)
        acceptButton.grid(row=12, column=5)
        admindash.mainloop()

    def editAttraction(self):

        attraction = self.AttractionEntry.get()
        description = self.DescriptionEntry.get()
        addnum = int(self.AddressEntry.get())
        street = self.Address2Entry.get()
        city = self.CityEntry.get()
        state = self.StateEntry.get()
        country = self.CountryEntry.get()
        postalcode = int(self.PostalCodeEntry.get())
        openhours = self.OpenHoursEntry.get()
        closehours = self.CloseHoursEntry.get()
        nearestpt = self.NearestTransEntry.get()
        ptnum = int(self.PTNumEntry.get())
        ptstreet = self.ptStreetEntry.get()
        ptcity = self.ptCityEntry.get()
        ptstate = self.ptStateEntry.get()
        ptzip = int(self.ptZipEntry.get())
        ptcountry = self.ptCountryEntry.get()
        price = float(self.PriceEntry.get())
        isreserved = bool(self.ReservedEntry.get())

        self.connect()
        cursor = self.database.cursor()
        sql = "SELECT Name FROM Attraction;"
        cursor.execute(sql)
        existingattractions = []
        for item in cursor:
            if item not in existingattractions:
                existingattractions.append(item)

        if attraction in existingattractions:
            messagebox.showwarning("That Attraction is already in our system. Please try again.")
        elif attraction not in existingattractions:
            sql1 = "INSERT INTO Attraction (Name, Description, isReserved, Price) values (%s, %s, %s, %s);"
            cursor.execute(sql1, (attraction, description, isreserved, price))
            sql2 = "INSERT INTO Attraction_Address (No, Street, City, State, Zip, Country, Attraction) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(sql2, (addnum, street, city, state, postalcode, country, attraction))
            sql3 = "INSERT INTO  PT_ADDRESS (No, Street, City, State, Zip, Country, PT, ClosestTo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(sql3, (ptnum, ptstreet, ptcity, ptstate, ptzip, ptcountry, nearestpt, attraction))
            sql4 = "INSERT INTO Hours_of_Operation (OpeningTime, ClosingTime, Attraction) values (%s, %s, %s);"
            cursor.execute(sql4, (openhours, closehours, attraction))
            self.database.commit()
            messagebox.showwarning("Attraction Added", "You have added a new Attraction!")
            self.admindash.withdraw()

        editA.mainloop()

    def customerDashboard(self):

        self.connect()
        print(self.email)
        cursor = self.database.cursor()
        sql2 = "SELECT * FROM USER"
        cursor.execute(sql2)
        for item in cursor:
            if item[0] == self.email:
                LastName = item[2]
                FirstName = item[3]
                Birthday = str(item[7]) + "/" + str(item[8]) + "/" + str(item[9])
                print(LastName, FirstName, Birthday)

        sql3 = "Select * FROM CREDIT_CARD"
        cursor.execute(sql3)
        for item in cursor:
            if item[4] == self.email:
                CCNumber = item[0]
                Expiry = str(item[1]) + '/' + str(item[2]) + '/' + str(item[3])

        sql4 = "Select * FROM USER_ADDRESS"
        cursor.execute(sql4)
        for item in cursor:
            if item[6] == self.email:
                No = item[0]
                Street = item[1]
                City = item[2]
                State = item[3]
                Zip = item[4]
                Country = item[5]

        custDash = Toplevel()
        self.custDash = custDash
        custDash.title("Customer Dashboard")
        custDash.config(bg="white")
        frame = Frame(custDash)

        regemailLabel = Label(frame)
        regemailLabel.pack()
        frame.grid(row=0, column=0, rowspan=15)

        regProfileLabel = Label(custDash, text="Profile", bg="SkyBlue2")
        regProfileLabel.grid(row=0, column=1, sticky=W, padx=5)

        profileButton = Button(custDash, text='Edit Profile', width=10, command=self.registerPage, bg='SkyBlue2')
        profileButton.grid(row=0, column=2, sticky=W)

        regemailLabel = Label(custDash, text="Email:", bg="SkyBlue2")
        regemailLabel.grid(row=1, column=1, sticky=W, padx=5)
        regemailEntry = Label(custDash, text=self.email)
        regemailEntry.grid(row=1, column=2)

        regLastNameLabel = Label(custDash, text="Last Name:", bg="SkyBlue2")
        regLastNameLabel.grid(row=2, column=1, sticky=W, padx=5)
        regLastNameEntry = Label(custDash, text=LastName)
        regLastNameEntry.grid(row=2, column=2)

        regFirstNameLabel = Label(custDash, text="First Name:", bg="SkyBlue2")
        regFirstNameLabel.grid(row=3, column=1, sticky=W, padx=5)
        regFirstNameEntry = Label(custDash, text=FirstName)
        regFirstNameEntry.grid(row=3, column=2)

        regBirthdayLabel = Label(custDash, text="Birthday:", bg="SkyBlue2")
        regBirthdayLabel.grid(row=4, column=1, sticky=W, padx=5)
        regBirthdayEntry = Label(custDash, text=Birthday)
        regBirthdayEntry.grid(row=4, column=2)

        regcreditCardLabel = Label(custDash, text="Credit Card:", bg="SkyBlue2")
        regcreditCardLabel.grid(row=6, column=1, sticky=W, padx=5)
        regcreditCardEntry = Label(custDash, text=CCNumber)
        regcreditCardEntry.grid(row=6, column=2)

        regExpiryLabel = Label(custDash, text="Expiry:", bg="SkyBlue2")
        regExpiryLabel.grid(row=7, column=1, sticky=W, padx=5)
        regExpiryEntry = Label(custDash, text=Expiry)
        regExpiryEntry.grid(row=7, column=2)

        regaddress1Label = Label(custDash, text="Number:", bg="SkyBlue2")
        regaddress1Label.grid(row=1, column=3, sticky=W, padx=5)
        regaddress1Entry = Label(custDash, text=No)
        regaddress1Entry.grid(row=1, column=4)

        regaddress2Label = Label(custDash, text="Street:", bg="SkyBlue2")
        regaddress2Label.grid(row=2, column=3, sticky=W, padx=5)
        regaddress2Entry = Label(custDash, text=Street)
        regaddress2Entry.grid(row=2, column=4)

        regcityLabel = Label(custDash, text="City:", bg="SkyBlue2")
        regcityLabel.grid(row=3, column=3, sticky=W, padx=5)
        regcityEntry = Label(custDash, text=City)
        regcityEntry.grid(row=3, column=4)

        regstateLabel = Label(custDash, text="State:", bg="SkyBlue2")
        regstateLabel.grid(row=4, column=3, sticky=W, padx=5)
        regstateEntry = Label(custDash, text=State)
        regstateEntry.grid(row=4, column=4)

        regcodeLabel = Label(custDash, text="Postal Code:", bg="SkyBlue2")
        regcodeLabel.grid(row=5, column=3, sticky=W, padx=5)
        regcodeEntry = Label(custDash, text=Zip)
        regcodeEntry.grid(row=5, column=4)

        regcountryLabel = Label(custDash, text="Country:", bg="SkyBlue2")
        regcountryLabel.grid(row=6, column=3, sticky=W, padx=5)
        regcountryEntry = Label(custDash, text=Country)
        regcountryEntry.grid(row=6, column=4)

        tripsLabel = Label(custDash, text="Trips:", bg="SkyBlue2")
        tripsLabel.grid(row=8, column=1, sticky=W, padx=5)

        cursor = self.database.cursor()
        sql = "SELECT * FROM TRIP"
        cursor.execute(sql)
        beginDateList = []
        endDateList = []
        cityList = []
        countryList = []
        for item in cursor:
            if item[6] == self.email:
                beginDateList.append(item[3])
                endDateList.append(item[4])
                cityList.append(item[0])
                countryList.append('France')

        beginDateLabel = Label(custDash, text="Begin Date", bg="SkyBlue2")
        beginDateLabel.grid(row=9, column=1, sticky=W, padx=5)
        beginDatebox = Listbox(custDash)
        beginDatebox.grid(row=10, column=1)
        for item in beginDateList:
            beginDatebox.insert(END, item)

        endDateLabel = Label(custDash, text="End Date", bg="SkyBlue2")
        endDateLabel.grid(row=9, column=2, sticky=W, padx=5)
        endDatebox = Listbox(custDash)
        endDatebox.grid(row=10, column=2)
        for item in endDateList:
            endDatebox.insert(END, item)

        tripCityLabel = Label(custDash, text="City", bg="SkyBlue2")
        tripCityLabel.grid(row=9, column=3, sticky=W, padx=5)
        tripCitybox = Listbox(custDash)
        tripCitybox.grid(row=10, column=3)
        for item in cityList:
            tripCitybox.insert(END, item)

        tripCountryLabel = Label(custDash, text="Country", bg="SkyBlue2")
        tripCountryLabel.grid(row=9, column=4, sticky=W, padx=5)
        tripCountrybox = Listbox(custDash)
        tripCountrybox.grid(row=10, column=4)
        for item in countryList:
            tripCountrybox.insert(END, item)

        tripDetailsButton = Button(custDash, text='Trip Details', width=10, command=self.viewTrip, bg='SkyBlue2')
        tripDetailsButton.grid(row=15, column=1, sticky=E)

        newTripButton = Button(custDash, text='New Trip', width=10, command=self.editTrip, bg='SkyBlue2')
        newTripButton.grid(row=15, column=2, sticky=E)

        reviewButton = Button(custDash, text='Write Review', width=10, command=self.reviewAttraction, bg='SkyBlue2')
        reviewButton.grid(row=15, column=3, sticky=E)

        dismissButton = Button(custDash, text='Logout', width=10, command=self.loginPage, bg='SkyBlue2')
        dismissButton.grid(row=15, column=4, sticky=E)

        self.custDash.mainloop()

    def viewTripPage(self):
        editT = Toplevel()
        self.editT = editT
        editT.title("View")
        editT.config(bg="white")
        frame = Frame(editT)

        cursor = self.database.cursor()
        sql = "SELECT City FROM Attraction_Address"
        cursor.execute(sql)
        cityList = []
        for item in cursor:
            if item not in cityList:
                cityList.append(item)

        cityLabel = Label(editT, text='City:', bg='SkyBlue2')
        cityLabel.grid(row=0, column=1, sticky=W, padx=5)
        cityPull = StringVar(editT)
        cityPull.set('City')
        cityPulling = OptionMenu(editT, cityPull, *cityList, command=self.cityFunc)
        cityPulling.grid(row=0, column=2, sticky=W, padx=5)
        viewInfoButton = Button(editT, text='View Trip', width=20, bg='SkyBlue2', command=self.viewTrip)
        viewInfoButton.grid(row=6, column=2, sticky=W)

        self.viewTrip.mainloop()

    def viewTrip(self):
        editT = Toplevel()
        self.editT = editT
        editT.title("View")
        editT.config(bg="white")
        frame = Frame(editT)

        tripcity = cityPulling.get()
        cityLabel = Label(editT, text='City:', bg='SkyBlue2')
        cityLabel.grid(row=0, column=1, sticky=W, padx=5)

    """
    def editTripPage(self):
        to pull up a page with the trip that was just selected from viewtrip and choose activities from seeAttractions ? to add to it

    def editTrip(self):
        update/trip in database
    """

    def seeAttractions(self):
        self.connect()
        seeAt = Toplevel()
        self.seeAt = seeAt
        seeAt.title("Trip Attractions")
        seeAt.config(bg="white")
        frame = Frame(seeAt)
        cursor = self.database.cursor()
        query = "SELECT (Activity.AttractionName, Activity.StartDateTime, Activity.EndDateTime, Trip.City) FROM Activity JOIN Trip ON(TripID) WHERE City = %s  AND UserEmail = %s; "
        cursor.execute(query, (cityPulling.get(), self.email))
        attractionBox = Listbox(seeAt)
        attractionBox.grid(row=0, column=1)
        for item in cursor:
            attractionBox.insert(END, item)
        self.seeAttractions.mainloop()

    def adminDashboard(self):
        admindash = Toplevel()
        self.admindash = admindash
        admindash.title("Admin Dashboard")
        admindash.config(bg="white")
        frame = Frame(admindash)

        dashattractionsLabel = Label(frame)
        dashattractionsLabel.pack()
        frame.grid(row=0, column=0, rowspan=6)
        dashattractionsLabel = Label(admindash, text='Attractions', bg='white')
        dashattractionsLabel.grid(row=0, column=1, sticky=W, padx=5)

        self.connect()
        cursor = self.database.cursor()
        sql = "SELECT Name FROM Attraction;"
        cursor.execute(sql)
        attractionsListbox = Listbox(admindash)
        attractionsListbox.grid(column=1, row=2)

        for item in cursor:
            attractionsListbox.insert(END, item)

        dashusersLabel = Label(admindash, text='Users', bg='white')
        dashusersLabel.grid(row=5, column=1, sticky=W, padx=5)

        self.connect()
        cursor = self.database.cursor()
        sql2 = "SELECT Email FROM User;"
        cursor.execute(sql2)
        userBox = Listbox(admindash)
        userBox.grid(column=1, row=6)

        for item in cursor:
            userBox.insert(END, item)

        dashnewButton = Button(admindash, text='New', width=20, command=self.editAttractionPage, bg='SkyBlue2')
        dashnewButton.grid(row=1, column=2, sticky=W)
        dasheditButton = Button(admindash, text='Edit', width=20, command=self.editAttractionPage, bg='SkyBlue2')
        dasheditButton.grid(row=2, column=2, sticky=W)
        dashreportsButton = Button(admindash, text='Reports', width=20, command=self.attractionReports, bg='SkyBlue2')
        dashreportsButton.grid(row=3, column=2, sticky=W)

        newUserButton = Button(admindash, text='New', width=20, command=self.editAttractionPage, bg='SkyBlue2')
        newUserButton.grid(row=4, column=2, sticky=W)
        deleteButton = Button(admindash, text='Delete', width=20, command=self.editAttractionPage, bg='SkyBlue2')
        deleteButton.grid(row=5, column=2, sticky=W)
        suspendButton = Button(admindash, text='Suspend', width=20, command=self.attractionReports, bg='SkyBlue2')
        suspendButton.grid(row=6, column=2, sticky=W)

        self.admindash.mainloop()

    def connect(self):
        try:
            self.database = mysql.connector.connect(host="localhost", password="", user="root", database="TripPlanner")
            print("Connection successful")
            return self.database

        except:
            messagebox.showwarning("Cannot Connect", "Check your internet connection")

    def loginCheck(self):
        self.connect()
        cursor = self.database.cursor()
        sql = "SELECT * FROM USER;"
        cursor.execute(sql)
        email = self.emailEntry.get()
        self.email = email
        password = self.passwordEntry.get()
        emails = []
        passes = []
        admin = []
        suspended = []
        for item in cursor:
            emails.append(item[0])
            passes.append(item[6])
            admin.append(item[4])
            suspended.append(item[5])
        if email in emails:
            for item in range(len(emails)):
                if emails[item] == email:
                    if passes[item] == password:
                        messagebox.showwarning("Login Successful!", "You have successfully logged in.")
                        if admin[item] == TRUE:
                            self.adminDashboard()
                        if admin[item] == FALSE:
                            self.customerDashboard()
                    if passes[item] != password:
                        messagebox.showwarning("Not a valid password",
                                               "That password is invalid or doesn't match the given email. Please try again.")
        else:
            messagebox.showwarning("Not a valid email.",
                                   "That email is not in our system. Please try again or register an account.")

        return self.email

    def registerNew(self):
        self.connect()
        cursor = self.database.cursor()

        email = self.regemailEntry.get()
        confirmEmail = self.regconfirmEmailEntry.get()
        password = self.regpasswordEntry.get()
        passwordConfirm = self.regconfirmEntry.get()
        firstName = self.regnameEntry.get()
        lastName = self.reglastEntry.get()
        address1 = self.regaddress1Entry.get()
        address2 = self.regaddress2Entry.get()
        city = self.regcityEntry.get()
        state = self.regstateEntry.get()
        zipcode = int(self.regcodeEntry.get())
        creditCard = int(self.regcardEntry.get())
        country = self.registrationCountryVal
        expiryMonth = int(self.registrationCCMonthVal)
        expiryYear = int(self.registrationCCYearVal)
        birthMonth = int(self.registrationBMonthVal)
        birthDay = int(self.registrationBDayVal)
        birthYear = int(self.registrationBYearVal)
        Name = str(firstName) + ' ' + str(lastName)

        self.connect()
        cursor = self.database.cursor()
        sql = "SELECT Email FROM USER;"
        cursor.execute(sql)
        emails = []
        for item in cursor:
            if item not in emails:
                emails.append(item)
        if password != passwordConfirm:
            messagebox.showwarning("Passwords", "Your passwords don't match!")
        if email != confirmEmail:
            messagebox.showwarning("Emails", "Emails don't match!")
        if email == '':
            messagebox.showwarning("Emails", "You must enter an email!")

        if email in emails:
            messagebox.showwarning("Email Not Available", "That email is already in use. Please login.")
        elif email not in emails:
            newsql = "INSERT INTO USER (Email,Name,LastName,FirstName,isAdmin,isSuspended,Password,BirthdayMonth,BirthdayDay,BirthdayYear) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(newsql,
                           (email, Name, lastName, firstName, '0', '0', password, birthMonth, birthDay, birthYear))
            self.database.commit()
            newsql2 = "INSERT INTO CREDIT_CARD (CCNumber,ExpiryMonth,ExpiryYear,CVV,Email) VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(newsql2, (creditCard, expiryMonth, expiryYear, '333', email))
            self.database.commit()
            messagebox.showwarning("Registered", "You are now registered!")
            self.register.withdraw()

    def attractionReports(self):
        cursor = self.database.cursor()
        sql = "SELECT Name FROM ATTRACTION;"
        cursor.execute(sql)
        attreports = Toplevel()
        self.attreports = attreports
        attreports.title("Attraction Reports")
        attreports.config(bg="white")
        frame = Frame(attreports)
        attLabel = Label(attreports, text='Attraction:', bg='SkyBlue2')
        attLabel.grid(row=0, column=1, sticky=W, padx=5)

        attractionList = []
        for item in cursor:
            attractionList.append(item)

        attPulldown = StringVar(attreports)
        attPulldown.set('Attraction')
        attPulling = OptionMenu(attreports, attPulldown, *attractionList)
        attPulling.grid(row=0, column=2, sticky=W, padx=5)
        # value = attPulldown.get()

        repdateLabel = Label(attreports, text='Date:', bg='SkyBlue2')
        repdateLabel.grid(row=0, column=3, sticky=W, padx=5)

        repdatePullday = StringVar(attreports)
        repdatePullday.set('Day')
        daypulling = OptionMenu(attreports, repdatePullday, '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                                '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
                                '25', '26', '27', '28', '29', '30', '31')
        daypulling.grid(row=0, column=4, sticky=W, padx=5)

        repdatePullmonth = StringVar(attreports)
        repdatePullmonth.set('Month')
        monthpulling = OptionMenu(attreports, repdatePullmonth, '01', '02', '03', '04', '05', '06', '07', '08', '09',
                                  '10', '11', '12')
        monthpulling.grid(row=0, column=5, sticky=W, padx=5)

        repdatePullyear = StringVar(attreports)
        repdatePullyear.set('Year')
        yearpulling = OptionMenu(attreports, repdatePullyear, '2018', '2019', '2020', '2021', '2022', '2023', '2024',
                                 '2025')
        yearpulling.grid(row=0, column=6, sticky=E, padx=5)

        tslotLabel = Label(attreports, text='Time Slots', bg='SkyBlue2')
        tslotLabel.grid(row=2, column=1, sticky=W, padx=5)

        cursor = self.database.cursor()
        sql0 = "SELECT * FROM Attraction"
        cursor.execute(sql0)

        tslotsListbox = Listbox(attreports, width=80)
        tslotsListbox.grid(columnspan=6, row=3)

        for item in cursor:
            tslotsListbox.insert(END, item)

        rosterLabel = Label(attreports, text='Roster', bg='SkyBlue2')
        rosterLabel.grid(row=10, column=1)
        rosterBox = Listbox(attreports, width=80)
        rosterBox.grid(columnspan=6, row=11)

    def reviewAttraction(self):
        review = Toplevel()
        self.review = review
        review.title("Review Attractions")
        review.config(bg='White')
        frame = Frame(review)
        frame.grid(row=0, column=0, rowspan=15)

        cityLabel = Label(review, text='City:', bg='SkyBlue2')
        cityLabel.grid(row=0, column=0, sticky=W, padx=5)

        cursor = self.database.cursor()
        sql = "SELECT City FROM TRIP"
        cursor.execute(sql)
        cityList = []
        for item in cursor:
            if item not in cityList:
                cityList.append(item)

        cPull = StringVar(review)
        cPull.set('Attraction')
        cPulling = OptionMenu(review, cPull, *cityList)
        cPulling.grid(row=0, column=1, sticky=W, padx=5)

        aLabel = Label(review, text='Atraction:', bg='SkyBlue2')
        aLabel.grid(row=1, column=0, sticky=W, padx=5)

        attractionPull = StringVar(review)
        attractionPull.set('Attraction')
        attractionPulling = OptionMenu(review, attractionPull, *cityList)
        attractionPulling.grid(row=1, column=1, sticky=W, padx=5)

        starsPull = StringVar(review)
        starsPull.set('Number of Stars')
        starsPulling = OptionMenu(review, starsPull, "One", "Two", "Three", "Four", "Five")
        starsPulling.grid(row=3, column=1, sticky=W, padx=5)

    def editTrip(self):
        editT = Toplevel()
        self.editT = editT
        editT.title("New Trip")
        editT.config(bg="white")
        frame = Frame(editT)

        cursor = self.database.cursor()
        sql = "SELECT City FROM Attraction_Address"
        cursor.execute(sql)
        cityList = []
        for item in cursor:
            if item not in cityList:
                cityList.append(item)

        cityLabel = Label(editT, text='City:', bg='SkyBlue2')
        cityLabel.grid(row=0, column=1, sticky=W, padx=5)
        cityPull = StringVar(editT)
        cityPull.set('City')
        cityPulling = OptionMenu(editT, cityPull, *cityList, command=self.cityFunc)
        cityPulling.grid(row=0, column=2, sticky=W, padx=5)

        dateDayLabel = Label(editT, text='Day', bg='SkyBlue2')
        dateDayLabel.grid(row=0, column=3, sticky=W, padx=5)
        repdatePullday = StringVar(editT)
        repdatePullday.set('Day')
        daypulling = OptionMenu(editT, repdatePullday, '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11',
                                '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25',
                                '26', '27', '28', '29', '30', '31')
        daypulling.grid(row=0, column=4, sticky=W, padx=5)

        dateMonthLabel = Label(editT, text='Month', bg='SkyBlue2')
        dateMonthLabel.grid(row=0, column=5, sticky=W, padx=5)
        repdatePullmonth = StringVar(editT)
        repdatePullmonth.set('Month')
        monthpulling = OptionMenu(editT, repdatePullmonth, '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                                  '11', '12')
        monthpulling.grid(row=0, column=6, sticky=W, padx=5)

        dateYearLabel = Label(editT, text='Year', bg='SkyBlue2')
        dateYearLabel.grid(row=0, column=7, sticky=W, padx=5)
        repdatePullyear = StringVar(editT)
        repdatePullyear.set('Year')
        yearpulling = OptionMenu(editT, repdatePullyear, '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025')
        yearpulling.grid(row=0, column=8, sticky=E, padx=5)

        viewInfoButton = Button(editT, text='Add Trip', width=20, bg='SkyBlue2', command=self.AddActivity)
        viewInfoButton.grid(row=6, column=2, sticky=W)

        self.editTrip.mainloop()

    def AddActivity(self):
        AddA = Toplevel()
        self.AddA = AddA
        AddA.title("Add Activities to your Trip")
        AddA.config(bg="white")
        frame = Frame(AddA)
        cursor = self.database.cursor()
        sql = "SELECT (Name, Description) from "
        cursor.execute(sql)

    def cityFunc(self, value):
        self.editCityVal = value
        print(self.editCityVal)
        return self.editCityVal


def AddActivity(self):
    AddA = Toplevel()
    self.AddA = AddA
    AddA.title("Add Activities to your Trip")
    AddA.config(bg="white")
    frame = Frame(AddA)
    cursor = self.database.cursor()
    sql = "SELECT (Name, Description) from "
    cursor.execute(sql)

    ActivityStartLabel = Label(AddA, text='Start Date Time:', bg='SkyBlue2')
    ActivityStartLabel.grid(row=0, column=1, sticky=W, padx=5)
    ActivityStartPull = StringVar(AddA)
    ActivityStartPull.set('Activity Start Times')
    ActivityStartPulling = OptionMenu(AddA, ActivityStartPull, *cityList, command=self)
    ActivityStartPulling.grid(row=0, column=2, sticky=W, padx=5)

    ActivityEndLabel = Label(AddA, text='End Date Time:', bg='SkyBlue2')
    ActivityEndLabel.grid(row=1, column=1, sticky=W, padx=5)
    ActivityEndPull = StringVar(AddA)
    ActivityEndPull.set('Activity End Times')
    ActivityEndPulling = OptionMenu(AddA, ActivityEndPull, *cityList, command=self)
    ActivityEndPulling.grid(row=1, column=2, sticky=W, padx=5)

    PartyNumLabel = Label(AddA, text='Number in party', bg='SkyBlue2')
    PartyNumLabel.grid(row=2, column=1, sticky=W, padx=5)
    PartyNumEntry = Entry(AddA, width=15)
    PartyNumEntry.grid(row=2, column=2, sticky=W, padx=5)
    self.PartyNumEntry = PartyNumEntry

    ActvNameLabel = Label(AddA, text='Activity Name', bg='SkyBlue2')
    ActvNameLabel.grid(row=3, column=1, sticky=W, padx=5)
    ActvNamePull = StringVar(AddA)
    ActvNamePull.set('Activity Names')
    ActvNamePulling = OptionMenu(AddA, ActvNamePull, *cityList, command=self)
    ActvNamePulling.grid(row=3, column=2, sticky=W, padx=5)


app = GUI()
