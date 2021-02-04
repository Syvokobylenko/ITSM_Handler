import tkinter
from tkinter import ttk
class formGui:
    def __init__(self, master,ticketinfo):
        self.master = master
        self.ticketinfo = ticketinfo
        self.addFormElements()
        self.positionFormElements()
        self.addandPosLabelElements()
        self.insertDefaultValues()
        self.master.bind("<Control-Return>", self.update)

    def addFormElements(self):
        self.entry0 = tkinter.Entry(self.master, width=40)
        self.entry1 = tkinter.Entry(self.master, width=40)
        self.entry2 = tkinter.Entry(self.master, width=40)
        self.entry3 = tkinter.Entry(self.master, width=40)
        self.entry4 = tkinter.Entry(self.master, width=40)
        self.entry5 = tkinter.Entry(self.master, width=40)
        self.entry6 = tkinter.Entry(self.master, width=40)
        self.entry7 = tkinter.Entry(self.master, width=40)
        self.entry8 = tkinter.Entry(self.master, width=40)
        self.entry9 = tkinter.Entry(self.master, width=40)
        self.entry10 = tkinter.Entry(self.master, width=40)
        self.entry11 = tkinter.Entry(self.master, width=40)
        self.entry12 = tkinter.Entry(self.master, width=40)
        self.entry13 = tkinter.Entry(self.master, width=40)
        self.entry14 = tkinter.Entry(self.master, width=40)
        self.entry15 = tkinter.Entry(self.master, width=40)
        self.entry16 = tkinter.Text(self.master, width=30, height=10)
        self.entry17 = tkinter.Entry(self.master, width=40)
        self.entry18 = tkinter.Entry(self.master, width=40)
        self.entry19 = tkinter.Entry(self.master, width=40)
        self.entry20 = tkinter.Entry(self.master, width=40)
        self.entry21 = tkinter.Entry(self.master, width=40)
        self.FB_Update = tkinter.Button(self.master, text="Update", command=self.update)
        self.FB_Send = tkinter.Button(self.master, text="Zatwierdź", command=self.confirm)
        self.FB_Cancel = tkinter.Button(self.master, text="Odrzuć", command=self.cancel)

    def addandPosLabelElements(self):
        label_names = ["ID","Typ_Zgłoszenia","Czy_Zrealizowano","INC","Osoba_Zgłaszająca","Czas_Zgłoszenia","Imię_Nazwisko","Numer_Telefonu","Ulica","Kod_Pocztowy","Miejscowość","Marka","Model","Urządzenie","Numer_Seryjny","Data_Zakupu","Opis","Dane_Dodatkowe","Mail_Zwrotny","Z_Tytułu","Oczekiwane_Rozwiązanie","Status_itsm_name"]
        tkinter.Label(self.master, text=label_names[0] + ":").grid(column=0, row=0)
        tkinter.Label(self.master, text=label_names[1] + ":").grid(column=0, row=1)
        tkinter.Label(self.master, text=label_names[2] + ":").grid(column=0, row=2)
        tkinter.Label(self.master, text=label_names[3] + ":").grid(column=0, row=3)
        tkinter.Label(self.master, text=label_names[4] + ":").grid(column=0, row=4)
        tkinter.Label(self.master, text=label_names[5] + ":").grid(column=0, row=5)
        tkinter.Label(self.master, text=label_names[6] + ":").grid(column=0, row=6)
        tkinter.Label(self.master, text=label_names[7] + ":").grid(column=0, row=7)
        tkinter.Label(self.master, text=label_names[8] + ":").grid(column=0, row=8)
        tkinter.Label(self.master, text=label_names[9] + ":").grid(column=0, row=9)
        tkinter.Label(self.master, text=label_names[10] + ":").grid(column=0, row=10)
        tkinter.Label(self.master, text=label_names[11] + ":").grid(column=0, row=11)
        tkinter.Label(self.master, text=label_names[12] + ":").grid(column=0, row=12)
        tkinter.Label(self.master, text=label_names[13] + ":").grid(column=0, row=13)
        tkinter.Label(self.master, text=label_names[14] + ":").grid(column=0, row=14)
        tkinter.Label(self.master, text=label_names[15] + ":").grid(column=0, row=15)
        tkinter.Label(self.master, text=label_names[16] + ":").grid(column=0, row=16)
        tkinter.Label(self.master, text=label_names[17] + ":").grid(column=0, row=19)
        tkinter.Label(self.master, text=label_names[18] + ":").grid(column=0, row=20)
        tkinter.Label(self.master, text=label_names[19] + ":").grid(column=0, row=21)
        tkinter.Label(self.master, text=label_names[20] + ":").grid(column=0, row=22)
        tkinter.Label(self.master, text=label_names[21] + ":").grid(column=0, row=23)

    def positionFormElements(self):
        self.entry0.grid(column=1, row=0)
        self.entry1.grid(column=1, row=1)
        self.entry2.grid(column=1, row=2)
        self.entry3.grid(column=1, row=3)
        self.entry4.grid(column=1, row=4)
        self.entry5.grid(column=1, row=5)
        self.entry6.grid(column=1, row=6)
        self.entry7.grid(column=1, row=7)
        self.entry8.grid(column=1, row=8)
        self.entry9.grid(column=1, row=9)
        self.entry10.grid(column=1, row=10)
        self.entry11.grid(column=1, row=11)
        self.entry12.grid(column=1, row=12)
        self.entry13.grid(column=1, row=13)
        self.entry14.grid(column=1, row=14)
        self.entry15.grid(column=1, row=15)
        self.entry16.grid(column=1, row=16)
        self.entry17.grid(column=1, row=19)
        self.entry18.grid(column=1, row=20)
        self.entry19.grid(column=1, row=21)
        self.entry20.grid(column=1, row=22)
        self.entry21.grid(column=1, row=23)
        self.FB_Update.grid(column=1, row=24, sticky=tkinter.NW)
        self.FB_Send.grid(column=1, row=24)
        self.FB_Cancel.grid(column=1, row=24, sticky=tkinter.NE)

    def insertDefaultValues(self):
        if not self.ticketinfo["INC"]:
            self.ticketinfo["INC"] = "NULL"
        self.entry0.insert(0,self.ticketinfo["ID"])
        self.entry1.insert(0,self.ticketinfo["Typ_Zgłoszenia"])
        self.entry2.insert(0,self.ticketinfo["Czy_Zrealizowano"])
        self.entry3.insert(0,self.ticketinfo["INC"])
        self.entry4.insert(0,self.ticketinfo["Osoba_Zgłaszająca"])
        self.entry5.insert(0,self.ticketinfo["Czas_Zgłoszenia"])
        self.entry6.insert(0,self.ticketinfo["Imię_Nazwisko"])
        self.entry7.insert(0,self.ticketinfo["Numer_Telefonu"])
        self.entry8.insert(0,self.ticketinfo["Ulica"])
        self.entry9.insert(0,self.ticketinfo["Kod_Pocztowy"])
        self.entry10.insert(0,self.ticketinfo["Miejscowość"])
        self.entry11.insert(0,self.ticketinfo["Marka"])
        self.entry12.insert(0,self.ticketinfo["Model"])
        self.entry13.insert(0,self.ticketinfo["Urządzenie"])
        self.entry14.insert(0,self.ticketinfo["Numer_Seryjny"])
        self.entry15.insert(0,self.ticketinfo["Data_Zakupu"])
        self.entry16.insert(tkinter.END,self.ticketinfo["Opis"])
        self.entry17.insert(0,self.ticketinfo["Dane_Dodatkowe"])
        self.entry18.insert(0,self.ticketinfo["Mail_Zwrotny"])
        self.entry19.insert(0,self.ticketinfo["Z_Tytułu"])
        self.entry20.insert(0,self.ticketinfo["Oczekiwane_Rozwiązanie"])
        self.entry21.insert(0,self.ticketinfo["Status_itsm_name"])
 
    def getValues(self):
        self.vars = {}
        self.vars["ID"] = self.entry0.get()
        self.vars["Typ_Zgłoszenia"] = self.entry1.get()
        self.vars["Czy_Zrealizowano"] = self.entry2.get()
        self.vars["INC"] = self.entry3.get()
        self.vars["Osoba_Zgłaszająca"] = self.entry4.get()
        self.vars["Czas_Zgłoszenia"] = self.entry5.get()
        self.vars["Imię_Nazwisko"] = self.entry6.get()
        self.vars["Numer_Telefonu"] = self.entry7.get()
        self.vars["Ulica"] = self.entry8.get()
        self.vars["Kod_Pocztowy"] = self.entry9.get()
        self.vars["Miejscowość"] = self.entry10.get()
        self.vars["Marka"] = self.entry11.get()
        self.vars["Model"] = self.entry12.get()
        self.vars["Urządzenie"] = self.entry13.get()
        self.vars["Numer_Seryjny"] = self.entry14.get()
        self.vars["Data_Zakupu"] = self.entry15.get()
        self.vars["Opis"] = self.entry16.get(1.0,tkinter.END)
        self.vars["Dane_Dodatkowe"] = self.entry17.get()
        self.vars["Mail_Zwrotny"] = self.entry18.get()
        self.vars["Z_Tytułu"] = self.entry19.get()
        self.vars["Oczekiwane_Rozwiązanie"] = self.entry20.get()
        self.vars["Status_itsm_name"] = self.entry21.get()


    def update(self):
        self.getValues()
        self.master.destroy()
   
    def confirm(self):
        self.vars = {"Czy_Zrealizowano": "verified"}
        self.master.destroy()
  
    def cancel(self):
        self.vars = {"Czy_Zrealizowano": "declined"}
        self.master.destroy()

def initGui(ticket):
    main_form = tkinter.Tk()
    main_form.geometry("+%d+%d"%(50,50))
    my_gui = formGui(main_form,ticket)
    main_form.mainloop()
    return my_gui.vars