class SQLiteHandler():
    def __init__(self):
        from sqlite3 import connect
        self.connect = connect

    def connectToDB(self,filename):
        self.sqliteConnection = self.connect(filename)

    def closeConnectionToDB(self):
      self.sqliteConnection.commit()
      self.sqliteConnection.close()

    def insert_query(self, query):
        self.sqliteConnection.cursor().execute(query)

    def select_query(self, query, fetchall):
        cursor = self.sqliteConnection.cursor()
        cursor.execute(query)
        if not fetchall:
           return cursor.fetchone()
        return cursor.fetchall()

    def getColumnNames(self,table_name):
        cursor = self.sqliteConnection.cursor()
        cursor.execute("SELECT name FROM pragma_table_info('" + table_name + "')")
        column_names = []
        for name in cursor.fetchall():
            column_names.append(name[0])
        return column_names

    def selectQueryCreator(self, table_name, field, search_value):
        if not field and not search_value:
            return "SELECT *" + " FROM " + table_name
        return "SELECT *" + " FROM " + table_name + " WHERE " + field + " = '" + search_value + "'"

    def insertQueryCreator(self, table_name, dictionary):
        fields_string = ""
        values_string = "'"
        for key in dictionary:
            fields_string += key + ","
            if dictionary[key] == "NULL":
                values_string = values_string[:-1]
                values_string = values_string + "NULL,'"
            else:
                values_string += dictionary[key] + "','"
        fields_string = fields_string[:-1]
        values_string = values_string[:-2]
        return "INSERT INTO "+ table_name + "\n(" + fields_string + ")\nVALUES\n("+ values_string +")"

    def updateQueryCreator(self, table_name, dictionary, search_field, search_value):
        set_string = ""
        for key in dictionary:
            if dictionary[key] == "NULL":
                set_string += key + " = " + dictionary[key] +", "
            else:
                set_string += key + " = '" + dictionary[key] +"', "
        set_string = set_string[:-2]
        return "UPDATE " + table_name + " SET " + set_string + " WHERE " + search_field + " = " + search_value

    def quickReadWrapper(self, filename, table_name, search_field, search_value, fetchall = False):
        self.connectToDB(filename)
        fetched = self.select_query(self.selectQueryCreator(table_name, search_field, search_value), fetchall)
        if fetchall:
            toreturn = []
            for row in fetched:
                dictionary = {}
                for key, value in zip(self.getColumnNames(table_name),row):
                    dictionary[key] = value
                toreturn.append(dictionary)
        else:
            toreturn = {}
            for key, value in zip(self.getColumnNames(table_name),fetched):
                toreturn[key] = value
        self.closeConnectionToDB()
        return toreturn
    
    def quickWriteWrapper(self, filename, table_name, dictionary):
        self.connectToDB(filename)
        self.insert_query(self.insertQueryCreator(table_name, dictionary))
        self.closeConnectionToDB()

    def quickUpdateWrapper(self, filename, table_name, dictionary, search_field, search_value):
        self.connectToDB(filename)
        self.insert_query(self.updateQueryCreator(table_name, dictionary, search_field, search_value))
        self.closeConnectionToDB()

    def serviceQueryCreator(self, kodpocztowy, AGDRTV):
        if AGDRTV == "Company_name_Awaria_AGD":
            query = "SELECT Serwisy_AGD.SerwisAGD, Serwisant, itsm_name_Popup, Email, Numer, Adres FROM Kody_Pocztowe\nINNER JOIN Powiaty ON Powiaty.Powiat = Kody_Pocztowe.Powiat\nINNER JOIN Serwisy_AGD ON Serwisy_AGD.SerwisAGD = Powiaty.SerwisAGD\nWHERE Kod_Pocztowy = '" + kodpocztowy + "'"
            names = ["Serwis", "Serwisant", "itsm_name_Popup", "Email", "Numer", "Adres"]
            return query, names
        if AGDRTV == "Company_name_Awaria_TV":
            query = "SELECT Serwisy_RTV.SerwisRTV, Serwisant, itsm_name_Popup, Email, Numer, Adres, 2nd_ITSM FROM Kody_Pocztowe\nINNER JOIN Powiaty ON Powiaty.Powiat = Kody_Pocztowe.Powiat\nINNER JOIN Serwisy_RTV ON Serwisy_RTV.SerwisRTV = Powiaty.SerwisRTV\nWHERE Kod_Pocztowy = '" + kodpocztowy + "'"
            names = ["Serwis", "Serwisant", "itsm_name_Popup", "Email", "Numer", "Adres","2nd_ITSM"]
            return query, names

    def serviceQueryWrapper(self,filename,kodpocztowy,AGDRTV):
        if not AGDRTV == "Company_name_Awaria_AGD" and not AGDRTV == "Company_name_Awaria_TV":
            return ["IS_ILW_SD","MAKSYM SYVOKOBYLENKO","True","employer_email"]
        self.connectToDB(filename)
        serviceQuery = self.serviceQueryCreator(kodpocztowy,AGDRTV)
        fetched_row = self.select_query(serviceQuery[0], False)
        toreturn = {}
        for key, value in zip(serviceQuery[1],fetched_row):
            toreturn[key] = value
        self.closeConnectionToDB()
        return toreturn