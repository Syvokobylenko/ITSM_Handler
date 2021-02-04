class InfoHandler():

    def __init__(self):
        self.itsm_nameFields = {
        "Company_name_Awaria_AGD": {
            "lastname": "5272717654",
            "company": "SD - Integrated Solutions",
            "summary": "Zgłoszenie Awarii: ",
            "tier1": "Company_name_Awaria_AGD",
            "tier2": "SHARP - AGD - 22 272 74 44",
            "tier3": False,
            "group": False,
            "assignee": False,
            "status": False,
            "reason": False,
            "resolution": "W trakcie realizacji."
        },

        "Company_name_Awaria_TV": {
            "lastname": "5272717654",
            "company": "SD - Integrated Solutions",
            "summary": "Zgłoszenie Awarii: ",
            "tier1": "Company_name_Awaria_TV",
            "tier2": "Toshiba",
            "tier3": False,
            "group": False,
            "assignee": False,
            "status": False,
            "reason": False,
            "resolution": "W trakcie realizacji."
        },

        "Company_name_Udzielenie Informacji": {
            "lastname": "5272717654",
            "company": "SD - Integrated Solutions",
            "summary": "Udzielenie informacji Company_name",
            "tier1": "Company_name_Udzielenie Informacji",
            "tier2": "SHARP - AGD - 22 272 74 44",
            "tier3": "Troubleshooting",
            "group": "IS_ILW_SD",
            "assignee": "MAKSYM SYVOKOBYLENKO",
            "popup": True,
            "status": "Resolved",
            "reason": "Rozwiązane",
            "resolution": "Udzielono informacji."
        },

        "Company_name_Monit": {
            "lastname": "5272717654",
            "company": "SD - Integrated Solutions",
            "summary": "Monit zgłoszenia Company_name",
            "tier1": "Company_name_Udzielenie Informacji",
            "tier2": "SHARP - AGD - 22 272 74 44",
            "tier3": "Troubleshooting",
            "group": "IS_ILW_SD",
            "assignee": "MAKSYM SYVOKOBYLENKO",
            "popup": True,
            "status": "Resolved",
            "reason": "Rozwiązane",
            "resolution": "Wysłano monit drogą mailową."
        }}

        self.special_service = {
        "toshiba": {
            "Serwis": "RADOM_MIK_TOSHIBA",
            "Serwisant": "NORBERT WIERZGAŁA",
            "itsm_name_Popup": "False",
            "Email": "toshiba@mik.radom.pl",
            "Numer": "48 362 27 20",
            "Adres": "ul. Chrobrego 22, Radom",
        },

        "oczyszczacz": {
            "Serwis": "WARSZAWA_ATV_VIDEO",
            "Serwisant": "SŁAWOMIR OSTROWSKI",
            "itsm_name_Popup": "False",
            "Email": "biuro@atv-video.pl",
            "Numer": "22 818 64 28; 22 620 12 54",
            "Adres": "ul. Jagiellońska 2, 03-721 Warszawa",
        },

        "klasen": {
            "Serwis": "IS_ILW_SD",
            "Serwisant": "MAKSYM SYVOKOBYLENKO",
            "itsm_name_Popup": "True",
            "Email": "bkedra@ciarko.pl; Serwis@ciarko.pl; mbilanski@ciarko.pl",
            "Numer": "-",
            "Adres": "-",
        },

        "mgm": {
            "Serwis": "ŁÓDŹ_ZUH_MGM_SERVICE",
            "Serwisant": "MIECZYSŁAW POLEWCZAK",
            "itsm_name_Popup": "False",
            "Email": "mgm@ceti.com.pl",
            "Numer": "46 874 28 30",
            "Adres": "ul. Pomorska 94, Łódź",
        }}


    def ticketSummary(self,ticket):
        if ticket["Typ_Zgłoszenia"] == "Company_name_Awaria_AGD" or ticket["Typ_Zgłoszenia"] == "Company_name_Awaria_TV":
            ticket["summary"] += ticket["Imię_Nazwisko"]
    
    def ticketNotes(self, ticket, service):
        notes = "Zgłoszenie z tytułu: \"" + ticket["Z_Tytułu"] + "\", oczekiwany sposób rozwiązania:\"" + ticket["Oczekiwane_Rozwiązanie"] + "\"\n\n"
        notes += "Typ urządzenia: " + ticket["Urządzenie"] + "\n\n"
        notes += "Model: " + ticket["Model"] + "\n"
        notes += "SN: " + ticket["Numer_Seryjny"] + "\n"
        notes += "Data zakupu: " + ticket["Data_Zakupu"] + "\n"
        notes += "Lokalizacja urządzenia: " + self.address(ticket["Ulica"],ticket["Kod_Pocztowy"],ticket["Miejscowość"]) + "\n"
        notes += "Opis usterki (opis klienta): " + ticket["Opis"] + "\n"
        notes += "Imię i nazwisko klienta: " + ticket["Imię_Nazwisko"] + "\n"
        notes += "Telefon kontaktowy: " + ticket["Numer_Telefonu"] + "\n"
        notes += "Email Klienta: " + self.replyEmailValidation(ticket["Mail_Zwrotny"]) + "\n"
        if ticket["Typ_Zgłoszenia"] == "Company_name_Awaria_AGD" or ticket["Typ_Zgłoszenia"] == "Company_name_Awaria_TV":
            notes += "Najbliższy serwis: " + service["Email"]
        return notes

    def emailTicketSubject(self, INC):
        return INC + " - zgłoszenie serwisowe Company_name"

    def emailTicketBody(self, ticket, template):
        template = template.replace("[WARRANTY_RETURN]",ticket["Z_Tytułu"])
        template = template.replace("[DEMAND]",ticket["Oczekiwane_Rozwiązanie"])
        template = template.replace("[BRAND]",ticket["Marka"])
        template = template.replace("[MODEL]",ticket["Model"])
        template = template.replace("[DEVICE]",ticket["Urządzenie"])
        template = template.replace("[SN]",ticket["Numer_Seryjny"])
        template = template.replace("[PURCHASE_DATE]",ticket["Data_Zakupu"])
        template = template.replace("[ADDRESS]",self.address(ticket["Ulica"],ticket["Kod_Pocztowy"],ticket["Miejscowość"]))
        template = template.replace("[DESCRIPTION]",ticket["Opis"])
        template = template.replace("[CLIENT_NAME]",ticket["Imię_Nazwisko"])
        template = template.replace("[CLIENT_PHONE]",ticket["Numer_Telefonu"])
        template = template.replace("[CLIENT_MAIL]",ticket["Mail_Zwrotny"])
        template = template.replace("[INC]",ticket["INC"])
        return template

    def emailReplySubject(self, ticket):
        if ticket["Dane_Dodatkowe"] != "":
            return str(ticket["Dane_Dodatkowe"]) + ": Zgłoszenie serwisowe Company_name - " + ticket["INC"]
        return "Zgłoszenie serwisowe Company_name - " + ticket["INC"]
    
    def emailReplyBody(self, ticket, service, template):
        if ticket["Dane_Dodatkowe"] != "":
            template = template.replace("[CLIENT_RMA]"," - " + str(ticket["Dane_Dodatkowe"]))
        else:
            template = template.replace("[CLIENT_RMA]","")
        template = template.replace("[WARRANTY_RETURN]",ticket["Z_Tytułu"])
        template = template.replace("[DEMAND]",ticket["Oczekiwane_Rozwiązanie"])
        template = template.replace("[S_NAME]",service["Serwis"])
        template = template.replace("[S_MAIL]",service["Email"])
        template = template.replace("[S_PHONE]",service["Numer"])
        template = template.replace("[S_ADDRESS]",service["Adres"])
        template = template.replace("[INC]",ticket["INC"])
        return template

    def emailMonitSubject(self, INC):
        return "Monit:" + INC + " - prosimy o kontakt z klientem"
    
    def emailMonitBody(self, ticket, service, template):
        template = template.replace("[INC]",ticket["INC"])        
        template = template.replace("[CLIENT_NAME]",ticket["Imię_Nazwisko"])
        template = template.replace("[CLIENT_PHONE]",ticket["Numer_Telefonu"])
        template = template.replace("[CLIENT_ADDRESS]",self.address(ticket["Ulica"],ticket["Kod_Pocztowy"],ticket["Miejscowość"]))
        template = template.replace("[REPORTED_ON]",ticket["Czas_Zgłoszenia"][:10])
        return template

    def emailAuditSubject(self):
        return "Statusy zgłoszeń Company_name po terminie - Proszę o uzupełnienie, lub zamknięcie zgłoszeń na ZPSD"

    def emailAuditBody(self,audit_temp,audit_row_temp,ticket_list):
        html_rows = ""
        for ticket in ticket_list:
            html_current = audit_row_temp.replace("[INC]",ticket["INC"])
            html_current = html_current.replace("[CLIENT_NAME]",ticket["Imię_Nazwisko"])
            html_current = html_current.replace("[CLIENT_PHONE]",ticket["Numer_Telefonu"])
            html_rows += html_current
        return audit_temp.replace("[AUDIT_ROWS]",html_rows)

    def address(self, street, postcode, city):
        return street + ", " + postcode + " " + city

    def number(self, value):
        #Code that changes phone number into universal value.
        return value

    def postCode(self, value):
        #Code that searches for postcode (eg. regex).
        return value

    def service_assigment(self,ticket,db_path):
        from SQLModule import SQLiteHandler
        if ticket["Urządzenie"] == "Oczyszczacz powietrza" and ticket["Typ_Zgłoszenia"] == "Company_name_Awaria_AGD":
            ticket["Czy_Zrealizowano"] = "delivery_company"
            if ticket["Miejscowość"] == "Warszawa":
                ticket["Czy_Zrealizowano"] = "True"  
            service = self.special_service["oczyszczacz"].copy()
        elif ticket["Marka"] == "Toshiba" and ticket["Typ_Zgłoszenia"] == "Company_name_Awaria_TV":
            ticket["Czy_Zrealizowano"] = "True"
            service = self.special_service["toshiba"].copy()
        elif ticket["Marka"] == "Klasen":
            ticket["Czy_Zrealizowano"] = "True"
            service = self.special_service["klasen"].copy()
        else:
            ticket["Czy_Zrealizowano"] = "True"
            service = SQLiteHandler().serviceQueryWrapper(db_path,ticket["Kod_Pocztowy"],ticket["Typ_Zgłoszenia"])
            if ticket["Typ_Zgłoszenia"] == "Company_name_Awaria_TV" and not service["Serwis"] == "ZDUŃSKA WOLA_SERIWS AGD":
                ticket["Czy_Zrealizowano"] = "2nd_ITSM"
            elif ticket["Typ_Zgłoszenia"] == "Company_name_Awaria_AGD" and service["Serwis"] == "ŁÓDŹ_SKLEEP" and ticket["Urządzenie"] == "Lodówka":
                ticket["Czy_Zrealizowano"] = "True"
                service = self.special_service["mgm"].copy()
        return service, ticket
    
    def genitsm_nameFields(self, ticket, service):
        itsm_name_fields = self.itsm_nameFields[ticket["Typ_Zgłoszenia"]].copy()
        itsm_name_fields["notes"] = self.ticketNotes(ticket,service)
        if ticket["Typ_Zgłoszenia"] == "Company_name_Awaria_AGD" or ticket["Typ_Zgłoszenia"] == "Company_name_Awaria_TV":
            itsm_name_fields["summary"] += ticket["Imię_Nazwisko"]
        if not itsm_name_fields["group"]:
            itsm_name_fields["group"] = service["Serwis"]
            itsm_name_fields["assignee"] = service["Serwisant"]
            itsm_name_fields["popup"] = service["itsm_name_Popup"] in ("True")
        return itsm_name_fields

    def replyEmailValidation(self, emails):
        import re
        emails_list = re.findall(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)",emails)
        emails = ""
        for email in emails_list:
            emails += email + "; "
        return emails