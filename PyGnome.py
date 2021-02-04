import seleniumtemplates, tkinterver, tkinter
from outlook import sendEmail, MailAttributes
from SQLModule import SQLiteHandler
from seleniummodule import seleniumHandler
from infohandler import InfoHandler
from tkinter import messagebox
from variablehandler import VariableHandler

global variables
variables = VariableHandler()

global firefox
if variables.current_user == "syvokmak":
    firefox = seleniumHandler("ITSM link")
else:
    firefox = seleniumHandler("ITSM link")

def ver():
    print("Wczytywanie zgłoszeń do Weryfikacji!")
    ticket_list = SQLiteHandler().quickReadWrapper(variables.db_path,"Zgłoszenia","Czy_Zrealizowano","False", fetchall = True)
    print("Wczytywanie Zakończone! Do sprawdzenia: " + str(len(ticket_list)))
    current = 1
    done = []
    for ticket in ticket_list:
        check = tkinterver.initGui(ticket)
        print("Progres: " + str(current) + "/" + str(len(ticket_list)))
        current = current + 1
        if check["Czy_Zrealizowano"] == "verified" or check["Czy_Zrealizowano"] == "declined":
            check["ID"] = str(ticket["ID"])
            done.append(check)
        else:
            check["Czy_Zrealizowano"] = "verified"
            done.append(check)
    print("Zapisywanie!")
    db_connection = SQLiteHandler()
    db_connection.connectToDB(variables.db_path)
    for check in done:
        db_connection.insert_query(db_connection.updateQueryCreator("Zgłoszenia", check, "ID", check["ID"]))
    db_connection.closeConnectionToDB()
  
def reg():
    ticket_list = SQLiteHandler().quickReadWrapper(variables.db_path,"Zgłoszenia","Czy_Zrealizowano","verified", fetchall = True)
    done = []
    current = 0
    print("Do zarejestrowania " + str(len(ticket_list)) +" zgłoszeń.")
    try:
        for ticket in ticket_list:
            service, ticket = InfoHandler().service_assigment(ticket, variables.local_db_path)
            itsm_name_fields = InfoHandler().genitsm_nameFields(ticket,service)
            ticket["INC"] = seleniumtemplates.Company_nameInfoitsm_name(firefox, itsm_name_fields)
            #print("Zarejestrowano: " + ticket["INC"])
            if ticket["Typ_Zgłoszenia"] == "Company_name_Awaria_AGD" or ticket["Typ_Zgłoszenia"] == "Company_name_Awaria_TV":
                sendEmail(service["Email"],"employer_email","employer_email",InfoHandler().emailTicketSubject(ticket["INC"]),InfoHandler().emailTicketBody(ticket,variables.ticket_temp))
                #print("Wysłano zgłoszenie : " + ticket["INC"])
                if InfoHandler().replyEmailValidation(ticket["Mail_Zwrotny"]) != "":
                    if ticket["Czy_Zrealizowano"] == "delivery_company":
                        sendEmail(InfoHandler().replyEmailValidation(ticket["Mail_Zwrotny"]),"employer_email","employer_email",InfoHandler().emailReplySubject(ticket),InfoHandler().emailReplyBody(ticket,service,variables.response_delivery_company_temp))
                    else:
                        sendEmail(InfoHandler().replyEmailValidation(ticket["Mail_Zwrotny"]),"employer_email","employer_email",InfoHandler().emailReplySubject(ticket),InfoHandler().emailReplyBody(ticket,service,variables.response_temp))
                    #print("Wysłano odpowiedź : " + ticket["INC"])
            #print("ready monit ")
            if ticket["Typ_Zgłoszenia"] == "Company_name_Monit":
                monit = SQLiteHandler().quickReadWrapper(variables.local_db_path,"Zgłoszenia","INC",ticket["Dane_Dodatkowe"])
                monit_service, monit = InfoHandler().service_assigment(monit, variables.local_db_path)
                sendEmail(monit_service["Email"],"employer_email","employer_email",InfoHandler().emailMonitSubject(monit["INC"]),InfoHandler().emailMonitBody(monit,monit_service,variables.audit_singular_temp))
                #print("Wysłano monit : " + monit["INC"])
            done.append(ticket)
            current = current + 1
            print( str(current) + "/" + str(len(ticket_list)) + " Dodano do listy : " + ticket["INC"])
        print("Poprawnie zarejestrowano.")
        raise ValueError
    except:
        import traceback
        traceback.print_exc()
        db_connection = SQLiteHandler()
        db_connection.connectToDB(variables.db_path)
        for ticket in done:
            db_connection.insert_query(db_connection.updateQueryCreator("Zgłoszenia", {"Czy_Zrealizowano": ticket["Czy_Zrealizowano"],"INC": ticket["INC"]}, "ID", str(ticket["ID"])))
            print("Dodano do bazy : " + ticket["INC"])
        print("Zapisywanie!")
        db_connection.closeConnectionToDB()

def upl():
    import re, os
    variables.readFiles()
    firefox.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[4]/div/div/div[2]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div[2]/div[2]/div/dl/dd[3]/span[2]/a').click()
    for uploads in variables.upload_files:
        progress = " - Plik " + str(variables.upload_files.index(uploads)+1) + "/" + str(len(variables.upload_files))
        import time
        time.sleep(2)
        try:
            INC = re.findall("INC\d{12}",uploads["file_name"])[0]
        except(IndexError):
            os.remove(uploads["path"])
            print("Brak INC w tytule - "+ uploads["file_name"] + progress)
            continue
        mail_object = MailAttributes(uploads["path"])
        if mail_object.GetSender() in ["* serwisITIS - Detal","employer_email"]:
            summary = "Mail do: " + mail_object.GetRecipient()
        else:
            summary = "Mail od: " + mail_object.GetSender()
        seleniumtemplates.uploadFile(firefox, uploads["path"], INC, summary, mail_object.GetBodyTXT())
        del mail_object
        os.remove(uploads["path"])
        print("Removed a file - " + uploads["file_name"] + progress)
    print("All clear!")
  
def clse():
    import re, os, time
    variables.readFiles()
    for resolved in variables.resolve_files:
        progress = " - Plik " + str(variables.resolve_files.index(resolved)+1) + "/" + str(len(variables.resolve_files))
        try:
            INC = re.findall("INC\d{12}",resolved["file_name"])[0]
        except(IndexError):
            os.remove(resolved["path"])
            print("Brak INC w tytule - "+ resolved["file_name"] + progress)
            continue
        seleniumtemplates.itsm_nameResolve(firefox, INC)
        os.remove(resolved["path"])
        print("Removed a file - " + resolved["file_name"] + progress)
        time.sleep(2)
    print("All clear!")

def qdr():
    import time
    ticket_list = SQLiteHandler().quickReadWrapper(variables.db_path,"Zgłoszenia","Czy_Zrealizowano","2nd_ITSM", fetchall = True)
    if not ticket_list:
        print("All clear!")
        return
    seleniumtemplates.2nd_ITSMLogin(firefox)
    print("Do zarejestrowania: " + str(len(ticket_list)))
    for ticket in ticket_list:
        service = SQLiteHandler().serviceQueryWrapper(variables.local_db_path,ticket["Kod_Pocztowy"],ticket["Typ_Zgłoszenia"])
        seleniumtemplates.2nd_ITSMReg(firefox,ticket,service)
        SQLiteHandler().quickUpdateWrapper(variables.db_path,"Zgłoszenia",{"Czy_Zrealizowano": "True"},"ID",str(ticket["ID"]))
        time.sleep(1)
        firefox.driver.get('2nd ITSM link')
        #messagebox.showinfo(title="2nd_ITSM",message="Zgłoszenie zarejestrowane.")
    firefox.driver.close()
    firefox.driver.switch_to.window(firefox.driver.window_handles[0])   
    print("All clear!")

def stat():
    print("Rozpoczynanie pobierania zgłoszeń. Może to trochę zająć.")
    ticket_list = SQLiteHandler().quickReadWrapper(variables.local_db_path,"Zgłoszenia","Czy_Zrealizowano","True", fetchall = True)
    variables.readFiles()
    done = []
    for ticket in ticket_list:
        if ticket["Status_itsm_name"] in ["In Progress","Not Available"] and ticket["INC"] not in variables.INC_InProgress:
            done.append({"ID": str(ticket["ID"]), "Status_itsm_name": "Resolved"})
        elif ticket["Status_itsm_name"] != "In Progress" and ticket["INC"] in variables.INC_InProgress:
            done.append({"ID": str(ticket["ID"]), "Status_itsm_name": "In Progress"})
    print("Zapisywanie zmian.")
    db_connection = SQLiteHandler()
    db_connection.connectToDB(variables.db_path)
    for check in done:
        db_connection.insert_query(db_connection.updateQueryCreator("Zgłoszenia", check, "ID", check["ID"]))
    db_connection.closeConnectionToDB()

def audit():
    from datetime import datetime
    variables.readFiles()
    ticket_list = SQLiteHandler().quickReadWrapper(variables.local_db_path,"Zgłoszenia","Status_itsm_name","In Progress", fetchall = True)
    AGD_breached = []
    
    excluded = str(datetime.now().year) + "-" + str(datetime.now().month).zfill(2), str(datetime.now().year) + "-" + str(datetime.now().month-1).zfill(2)
    for ticket in ticket_list:
        if excluded[0] in ticket["Czas_Zgłoszenia"] or excluded[1] in ticket["Czas_Zgłoszenia"]:
            continue
        if ticket["Typ_Zgłoszenia"] == "Company_name_Awaria_AGD":
            AGD_breached.append(ticket)
    
    service_list = {}
    
    for ticket in AGD_breached:
        service, x = InfoHandler().service_assigment(ticket, variables.local_db_path)
        if not service["Serwis"] in service_list:
            service_list[service["Serwis"]] = service
            service_list[service["Serwis"]]["tickets"] = []
        service_list[service["Serwis"]]["tickets"].append(ticket)

    for service in service_list:
        if len(service_list[service]['tickets']) > 1:
            sendEmail(service_list[service]["Email"],"employer_email","employer_email",InfoHandler().emailAuditSubject(),InfoHandler().emailAuditBody(variables.audit_temp,variables.audit_row_temp,service_list[service]['tickets']))
        else:
            print("Tylko jedeno zgłoszenie - pomijam: " + service_list[service]['tickets'][0]['INC'])

def 2nd_ITSMStatus():
    variables.readFiles()
    ticket_list = SQLiteHandler().quickReadWrapper(variables.local_db_path,"Zgłoszenia","Status_itsm_name","In Progress", fetchall = True)
    2nd_ITSM_in_progress = []
    for ticket in ticket_list:
        if ticket["Typ_Zgłoszenia"] == "Company_name_Awaria_TV" and ticket["Marka"] != "Toshiba" and ticket["INC"] not in variables.INC_2nd_ITSM_In_Progress:
            2nd_ITSM_in_progress.append(ticket)
    print("Do zamknięcia " + str(len(2nd_ITSM_in_progress)) +" zgłoszeń.")
    for ticket in 2nd_ITSM_in_progress:
        seleniumtemplates.itsm_nameResolve(firefox, ticket["INC"])

def getMikStatus():
    firefox.driver.execute_script("window.open('');")
    firefox.driver.switch_to.window(firefox.driver.window_handles[1])
    firefox.driver.get('https://www.mik.radom.pl/public/status_naprawy')
    messagebox.showinfo(title="Radom mik",message="Wybierz \"Numer telefonu\" z listy opcji.")
    ticket_list = SQLiteHandler().quickReadWrapper(variables.local_db_path,"Zgłoszenia","Marka","Toshiba", fetchall = True)
    for ticket in ticket_list:
        if isinstance(ticket["RMA_MIK"], int) and ticket["Status_itsm_name"] == "In Progress":
            status = seleniumtemplates.radomGetStatus(firefox, ticket["RMA_MIK"], ticket["Numer_Telefonu"])
            try:
                with open('C:\\Users\\' + variables.current_user + '\\Documents\\MIK\\MIK Status - ' + status + "(" + ticket["INC"] + ")",'x') as contents:
                    pass
            except(FileExistsError):
                pass
    firefox.driver.close()
    firefox.driver.switch_to.window(firefox.driver.window_handles[0])