import tkinter, threading
from shutil import copyfile
from tkinter import ttk
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
if os.path.getsize(dir_path+"\\logo.gif") != 2904:
  exit()
print("Wczytywanie bazy danych...")
appdata = os.getenv('APPDATA')
try:
  os.remove(appdata+"\\PyRegister\\GNOME.db")
except(FileNotFoundError):
  try:
    os.mkdir(appdata+"\\PyRegister")
  except(FileExistsError):
    pass
except(PermissionError):
  pass
try:
  copyfile(dir_path+"\\GNOME.db", appdata+"\\PyRegister\\GNOME.db")
except:
  pass

print("Otwieranie kopii bazy danych.")

def downloadBrowser():
 import os
 appdata = os.getenv('APPDATA')
 if os.path.isfile(appdata + '\\PyRegister\\DBbrowser\\sqlitebrowser.exe'):
  os.system('%appdata%\\PyRegister\\DBbrowser\\sqlitebrowser.exe  -R -t Zgłoszenia "%appdata%\\PyRegister\\GNOME.DB"')
  return
 from shutil import copyfile
 copyfile(dir_path+"\\DBbrowser.zip", appdata+"\\PyRegister\\DBbrowser.zip")
 from zipfile import ZipFile
 with ZipFile(appdata + '\\PyRegister\\DBbrowser.zip', 'r') as zipObj:
  zipObj.extractall(appdata+"\\PyRegister\\")
 os.system('%appdata%\\PyRegister\\DBbrowser\\sqlitebrowser.exe  -R -t Zgłoszenia "%appdata%\\PyRegister\\GNOME.DB"')
thread = threading.Thread(target=downloadBrowser, args=())
thread.daemon = True
thread.start()

print("Gotowe!")

class formGui:
 def __init__(self, main_window):
  main_window.title("Company_Name v1.23")
  self.master = tkinter.Frame(main_window)
  self.master.grid(pady=20, padx=20)
  import os
  dir_path = os.path.dirname(os.path.realpath(__file__))
  self.logo = tkinter.PhotoImage(file=dir_path+"\logo.gif")
  self.initElements()

 def initElements(self):
  self.initVariables()
  self.addFormElements()
  self.addLabelElements()
  self.setPositions()
  self.FE_PostCodeVar.trace("w",self.postCodeUpdate)
  self.FE_DeviceVar.trace("w",self.postCodeUpdate)
  self.FE_BrandVar.trace("w",self.postCodeUpdate)
  self.FE_TypeVar.trace("w",self.ticketTypeUpdate)
  self.FE_RegexVar.trace("w",self.regexInfill)
  self.FE_TelVar.trace("w",self.phonechange)
  self.FE_SNVar.trace("w",self.SNChange)
  self.FE_ModelVar.trace("w",self.ModelChange)
  self.FE_TelValue = ""
  self.master.update()


 def setPositions(self):
  self.positionFormElements()
  self.positionLabelElements()

 def initVariables(self):
  self.FE_TypeVar = tkinter.StringVar()
  self.FE_DeviceVar = tkinter.StringVar()
  self.FE_MoreInfoVar = tkinter.StringVar()
  self.FE_ClientMailVar = tkinter.StringVar()
  self.FE_LegalVar = tkinter.StringVar()
  self.FE_ClaimVar = tkinter.StringVar()
  self.FE_TelVar =  tkinter.StringVar()
  self.FE_NameVar = tkinter.StringVar()
  self.FE_StreetVar = tkinter.StringVar()
  self.FE_PostCodeVar = tkinter.StringVar()
  self.FE_CityVar = tkinter.StringVar()
  self.FE_BrandVar = tkinter.StringVar()
  self.FE_ModelVar =   tkinter.StringVar()
  self.FE_SNVar = tkinter.StringVar()
  self.FE_DayVar = tkinter.StringVar() 
  self.FE_MonthVar = tkinter.StringVar() 
  self.FE_YearVar = tkinter.StringVar()
  self.FE_DescriptionVar = tkinter.StringVar()
  self.FE_RegexVar = tkinter.StringVar()
  self.L_ValidationVar = tkinter.StringVar()
  self.L_CheckboxVar = tkinter.BooleanVar()
  self.FE_ServiceNameVar = tkinter.StringVar()
  self.FE_ServiceNumberVar = tkinter.StringVar()
  self.FE_ServiceMailVar = tkinter.StringVar()
  self.FE_ServiceAddressVar = tkinter.StringVar()

 def addFormElements(self):
  self.FE_Type = ttk.Combobox(self.master, textvariable=self.FE_TypeVar, width=17, state="readonly", values=["Company_Name_Awaria_AGD","Company_Name_Awaria_TV","Company_Name_Udzielenie Informacji","Company_Name_Monit"])
  self.FE_Device = ttk.Combobox(self.master, textvariable=self.FE_DeviceVar, width=17, state="readonly")
  self.FE_MoreInfo = tkinter.Entry(self.master, textvariable=self.FE_MoreInfoVar)
  self.FE_ClientMail = tkinter.Entry(self.master, textvariable=self.FE_ClientMailVar)
  self.FE_Legal = ttk.Combobox(self.master, textvariable=self.FE_LegalVar, width=17, state="readonly", values=["Gwarancja","Gwarancja ze Sklepu","Rękojmia","Przedsprzedaż"])
  self.FE_Claim = ttk.Combobox(self.master, textvariable=self.FE_ClaimVar, width=17, state="readonly", values=["Naprawa","Oświadczenie"])
  self.FE_Tel = tkinter.Entry(self.master, textvariable=self.FE_TelVar)
  self.FE_Name = tkinter.Entry(self.master, textvariable=self.FE_NameVar)
  self.FE_Street = tkinter.Entry(self.master, textvariable=self.FE_StreetVar)
  self.FE_PostCode = tkinter.Entry(self.master, textvariable=self.FE_PostCodeVar)
  self.FE_City = tkinter.Entry(self.master, textvariable=self.FE_CityVar)
  self.FB_Send = tkinter.Button(self.master, text="Zatwierdź", bg = "#88ff00", command=self.confirm)
  self.FE_Brand = ttk.Combobox(self.master, textvariable=self.FE_BrandVar, width=17, state="readonly")
  self.FE_Model = ttk.Combobox(self.master, textvariable=self.FE_ModelVar, width=17, values=[])
  self.FE_SN = tkinter.Entry(self.master, textvariable=self.FE_SNVar)
  self.FE_Day = ttk.Combobox(self.master, textvariable=self.FE_DayVar, width=3, height=15, state="readonly", values=[str(i).zfill(2) for i in range(1,32)])
  self.FE_Month = ttk.Combobox(self.master, textvariable=self.FE_MonthVar, width=3, height=12, state="readonly", values=[str(i).zfill(2) for i in range(1,13)])
  self.FE_Year = ttk.Combobox(self.master, textvariable=self.FE_YearVar, width=5, state="readonly", values=["2017","2018","2019","2020","2021"])
  self.FE_Description = tkinter.Text(self.master, width=30, height=10)
  self.FB_Clear = tkinter.Button(self.master, text="Wyczyść", bg = "#ff4040", command=self.initElements)
  self.FE_Regex = tkinter.Entry(self.master, textvariable=self.FE_RegexVar)
  self.FE_ServiceName = tkinter.Entry(self.master, textvariable=self.FE_ServiceNameVar, state="disabled")
  self.FE_ServiceNumber = tkinter.Entry(self.master, textvariable=self.FE_ServiceNumberVar)
  self.FE_ServiceMail = tkinter.Entry(self.master, textvariable=self.FE_ServiceMailVar)
  self.FE_ServiceAddress = tkinter.Entry(self.master, textvariable=self.FE_ServiceAddressVar)

 def addLabelElements(self):
  import getpass
  self.L_Type = tkinter.Label(self.master, text="Typ zgłoszenia:")
  self.L_Device = tkinter.Label(self.master, text="Urządzenie:")
  self.L_MoreInfo = tkinter.Label(self.master, text="INC\RMA:")
  self.L_ClientMail = tkinter.Label(self.master, text="Mail Zwrotny:")
  self.L_Legal = tkinter.Label(self.master, text="Z tytułu:")
  self.L_Claim = tkinter.Label(self.master, text="Roszczenie:")
  self.L_Login = tkinter.Label(self.master, text=getpass.getuser())
  self.L_Tel = tkinter.Label(self.master, text="Numer:")
  self.L_Name = tkinter.Label(self.master, text="Imie Nazwisko:")
  self.L_Street = tkinter.Label(self.master, text="Ulica:")
  self.L_PostCode = tkinter.Label(self.master, text="Kod Pocztowy:")
  self.L_City = tkinter.Label(self.master, text="Miejscowość:")
  self.L_Brand = tkinter.Label(self.master, text="Marka:")
  self.L_Model = tkinter.Label(self.master, text="Model:")
  self.L_SN = tkinter.Label(self.master, text="Numer Seryjny:")
  self.L_Date = tkinter.Label(self.master, text="Data Zakupu:")
  self.L_Description = tkinter.Label(self.master, text="Opis:")
  self.L_Warnings = tkinter.Label(self.master, wraplength=450, justify=tkinter.LEFT, text="W związku z ogłoszeniem stanu epidemii w Polsce proszę o potwierdzenie, że żadna z osób wspólnie zamieszkujących bądź przebywających w miejscu lokalizacji sprzętu nie jest objęta kwarantanną, nie miała kontaktu z osobami zarażonymi Covid19 lub osobą powracającą w ostatnim czasie z zagranicy. Czy powierdza Pan/Pani? \n\nOczyszczacze: Autoryzowany sklep, bez filtrów, tylko XXX.\n\n Pamiętajcie o czytaniu formatki W CAŁOŚCI słowo w słowo oraz przyjęciu zgłoszenia TYLKO po słowach \"Tak\" lub \"Potwierdzam\"")
  self.L_Checkbox = tkinter.Checkbutton(self.master, text="Potwierdzono ", variable=self.L_CheckboxVar)
  self.L_Validation = tkinter.Label(self.master, text="Gotowe!" + "\u00A0" * 310 , wraplength=500, justify=tkinter.LEFT, fg="red", font="Helvetica 9 bold")
  self.L_Logo = tkinter.Label(self.master, image=self.logo)
  self.L_ServiceData = tkinter.Label(self.master, text="Dane Serwisu:")
  self.L_ServiceName = tkinter.Label(self.master, text="Nazwa:")
  self.L_ServiceMail = tkinter.Label(self.master, text="Email:")
  self.L_ServiceNumber = tkinter.Label(self.master, text="Numer:")
  self.L_ServiceAddress = tkinter.Label(self.master, text="Adres:")

 def positionFormElements(self):
  self.FE_Type.grid(column=0, row=1)
  self.FE_Device.grid(column=1, row=1)
  self.FE_MoreInfo.grid(column=2, row=1)
  self.FE_ClientMail.grid(column=3, row=1)
  self.FE_Legal.grid(column=4, row=1, sticky=tkinter.W)
  self.FE_Legal.current(0)
  self.FE_Claim.grid(column=5, row=1, sticky=tkinter.W)
  self.FE_Claim.current(0)
  self.FE_Tel.grid(column=0, row=3)
  self.FE_Name.grid(column=1, row=3)
  self.FE_Street.grid(column=2, row=3)
  self.FE_PostCode.grid(column=3, row=3)
  self.FE_City.grid(column=4, row=3, sticky=tkinter.W)
  self.FB_Send.grid(column=5, row=3)
  self.FE_Brand.grid(column=0, row=5, sticky=tkinter.NW)
  self.FE_Model.grid(column=1, row=5, sticky=tkinter.NW)
  self.FE_SN.grid(column=2, row=5, sticky=tkinter.NW)
  self.FE_Day.grid(column=3, row=5, sticky=tkinter.NW)
  self.FE_Month.grid(column=3, row=5, sticky=tkinter.N)
  self.FE_Year.grid(column=3, row=5, sticky=tkinter.NE)
  self.FE_Description.grid(column=4, row=5, columnspan=2, rowspan=3)
  self.FE_Regex.grid(column=8, row=7, sticky=tkinter.SE)
  self.FB_Clear.grid(column=7, row=7, sticky=tkinter.SW)
  self.FE_ServiceName.grid(column=0, row=7, sticky=tkinter.S)
  self.FE_ServiceMail.grid(column=1, row=7, sticky=tkinter.S)
  self.FE_ServiceNumber.grid(column=2, row=7, sticky=tkinter.S)
  self.FE_ServiceAddress.grid(column=3, row=7, sticky=tkinter.S)

 def positionLabelElements(self):
  self.L_Type.grid(column=0, row=0)
  self.L_Device.grid(column=1, row=0)
  self.L_MoreInfo.grid(column=2, row=0)
  self.L_ClientMail.grid(column=3, row=0)
  self.L_Legal.grid(column=4, row=0, sticky=tkinter.W)
  self.L_Claim.grid(column=5, row=0, sticky=tkinter.W)
  self.L_Login.grid(column=5, row=0, sticky=tkinter.NE)
  self.L_Tel.grid(column=0, row=2)
  self.L_Name.grid(column=1, row=2)
  self.L_Street.grid(column=2, row=2)
  self.L_PostCode.grid(column=3, row=2)
  self.L_City.grid(column=4, row=2, sticky=tkinter.W)
  self.L_Brand.grid(column=0, row=4)
  self.L_Model.grid(column=1, row=4)
  self.L_SN.grid(column=2, row=4)
  self.L_Date.grid(column=3, row=4)
  self.L_Description.grid(column=4, row=4, columnspan=2)
  self.L_Warnings.grid(column=6, row=0, columnspan=6, rowspan=6, sticky=tkinter.NW)
  self.L_Checkbox.grid(column=6, row=6, columnspan=6, sticky=tkinter.NE)
  self.L_Validation.grid(column=0, row=6, sticky=tkinter.NW, columnspan=4, rowspan=2)
  self.L_Logo.grid(column=0, row=5, sticky=tkinter.SE, columnspan=4, rowspan=2)
  self.L_ServiceData.grid(column=0, row=7, sticky=tkinter.NW)
  self.L_ServiceName.grid(column=0, row=7)
  self.L_ServiceMail.grid(column=1, row=7)
  self.L_ServiceNumber.grid(column=2, row=7)
  self.L_ServiceAddress.grid(column=3, row=7)

 def getData(self):
  self.status = "False"
  if self.L_Login["text"] in ["szulemi1","syvokmak"] or self.FE_TypeVar.get() == "Company_Name_Udzielenie Informacji":
   self.status = "verified"
  if self.FE_TypeVar.get() == "Company_Name_Udzielenie Informacji" or self.FE_TypeVar.get() == "Company_Name_Monit":
   self.Status_itsm_name = "Resolved"
  else:
   self.Status_itsm_name = "Not Available"
  self.FE_TypeValue = self.FE_TypeVar.get()
  self.FE_DeviceValue = self.FE_DeviceVar.get()
  self.FE_MoreInfoValue = self.FE_MoreInfoVar.get()
  self.FE_ClientMailValue = self.FE_ClientMailVar.get()
  self.FE_LegalValue = self.FE_LegalVar.get()
  self.FE_ClaimValue = self.FE_ClaimVar.get()
  self.FE_NameValue = self.FE_NameVar.get()
  self.FE_StreetValue = self.FE_StreetVar.get()
  self.FE_PostCodeValue = self.FE_PostCodeVar.get()
  self.FE_CityValue = self.FE_CityVar.get()
  self.FE_BrandValue = self.FE_BrandVar.get()
  self.FE_ModelValue = self.FE_ModelVar.get()
  self.FE_SNValue = self.FE_SNVar.get()
  self.FE_DayValue = self.FE_DayVar.get() 
  self.FE_MonthValue = self.FE_MonthVar.get() 
  self.FE_YearValue = self.FE_YearVar.get()
  self.FE_DescriptionValue = self.FE_Description.get(1.0,tkinter.END)
  self.FE_ServiceNameValue = self.FE_ServiceNameVar.get()
  self.FE_ServiceMailValue = self.FE_ServiceMailVar.get()
  self.FE_ServiceNumberValue = self.FE_ServiceNumberVar.get()
  self.FE_ServiceAddressValue = self.FE_ServiceAddressVar.get()

 def confirm(self):
  import datetime
  self.getData()
  self.isValid = InfoValidation().checkType(self)
  self.fields = ["Typ_Zgłoszenia","Czy_Zrealizowano","INC","Osoba_Zgłaszająca","Czas_Zgłoszenia","Imię_Nazwisko","Numer_Telefonu","Ulica","Kod_Pocztowy","Miejscowość","Marka","Model","Urządzenie","Numer_Seryjny","Data_Zakupu","Opis","Dane_Dodatkowe","Mail_Zwrotny","Z_Tytułu","Oczekiwane_Rozwiązanie","Status_itsm_name"]
  self.values = [self.FE_TypeValue,self.status,"NULL",self.L_Login["text"],str(datetime.datetime.now()),self.FE_NameValue,self.FE_TelValue,self.FE_StreetValue,self.FE_PostCodeValue,self.FE_CityValue,self.FE_BrandValue,self.FE_ModelValue,self.FE_DeviceValue,self.FE_SNValue,self.FE_YearValue + "." + self.FE_MonthValue + "." + self.FE_DayValue  ,self.FE_DescriptionValue,self.FE_MoreInfoValue,self.FE_ClientMailValue,self.FE_LegalValue,self.FE_ClaimValue,self.Status_itsm_name]
  if self.isValid == True:
   import os
   dir_path = os.path.dirname(os.path.realpath(__file__))
   SQLiteHandler().quickSendWrapper(dir_path +"\GNOME.db","Zgłoszenia",self.fields, self.values)
   self.initElements()
   return
  else:
   self.L_Validation["text"] = ""
   self.L_Validation["text"] = "Usupełnij dane: " + self.isValid.replace(":",", ")
   return

 def postCodeUpdate(self,*args):
  if self.FE_TypeVar.get() == "Company_Name_Awaria_AGD":
   if self.FE_BrandVar.get() in ["Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name"]:
    self.FE_BrandVar.set("")
   self.FE_Brand['values'] = ["Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name"]
  if self.FE_TypeVar.get() == "Company_Name_Awaria_TV":
   if self.FE_BrandVar.get() in ["Brand_Name","Brand_Name","Brand_Name","Brand_Name"]:
    self.FE_BrandVar.set("")
   self.FE_Brand['values'] = ["Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name","Brand_Name"]
  self.FE_PostCodeVar.set(self.FE_PostCodeVar.get()[:6])
  import os, re
  if re.search("^\d{2}-\d{3}$",self.FE_PostCodeVar.get()):
   local_db = os.getenv("APPDATA")+"\\PyRegister\\GNOME.db"
   SQLReturn = SQLiteHandler().serviceQueryWrapper(local_db,self.FE_PostCodeVar.get(),self.FE_TypeVar.get())
  else:
   SQLReturn = ["","","","",""]
  if self.FE_DeviceVar.get() == "Oczyszczacz powietrza":
   service = ["Service_Name","Service_Email","phone","Address",SQLReturn[4]]
  elif self.FE_DeviceVar.get() == "Soundbar":
   service = ["Service_Name","Service_Email","phone","Address",SQLReturn[4]]
  elif self.FE_BrandVar.get() == "Brand_Name":
   service = ["Service_Name","Service_Email","Address",SQLReturn[4]]
  else:
   service = SQLReturn
   if service[0] == "Service_Name" and self.FE_DeviceVar.get() == "Lodówka":
    service = ["Service_Name","Service_Email","Address",SQLReturn[4]]
   elif service[0] == "Service_Name" and self.FE_DeviceVar.get() == "":
    service = ["Wybierz","urządzenie","","",SQLReturn[4]]
  self.FE_ServiceNameVar.set(service[0].replace("_"," "))
  self.FE_ServiceMailVar.set(service[1])
  self.FE_ServiceNumberVar.set(service[2])
  self.FE_ServiceAddressVar.set(service[3])
  self.FE_CityVar.set(service[4])

 def ticketTypeUpdate(self,*args):
  if self.FE_TypeVar.get() == "Company_Name_Awaria_AGD":
   if self.FE_DeviceVar.get() == "Telewizor":
    self.FE_DeviceVar.set("")
   self.FE_Device['values'] = ["Lodówka","Pralka","Zmywarka","Mikrofala","Oczyszczacz powietrza","Piekarnik","Klimatyzator","Płyta indukcyjna","Kuchnia","Suszarka","Odkurzacz","Okap","Ekspres","Czajnik","Blender"]
  if self.FE_TypeVar.get() == "Company_Name_Awaria_TV":
   self.FE_Device['values'] = ["Telewizor","Soundbar"]
   self.FE_Device.current(0)
  
 def regexInfill(self,*args):
  import re
  regexVar = self.FE_RegexVar.get()
  if re.search("TV",regexVar):
   self.FE_Type.current(1)
  else:
   self.FE_Type.current(0)
  if re.search("Rękojmia",regexVar):
   pass
  self.FE_MoreInfoVar.set(re.search("(?<=ZGŁOSZENIE REKLAMACYJNE NR )(\d{10})", regexVar).group())
  if re.search("company name",regexVar):
   self.FE_ClientMailVar.set("return email")
  if re.search("sender name",regexVar):
   self.FE_ClientMailVar.set("return email")
  if re.search("sender name",regexVar):
   self.FE_ClientMailVar.set("return email")
  if re.search("sender name",regexVar):
   self.FE_ClientMailVar.set("return email")
  if re.search("sender name",regexVar):
   self.FE_ClientMailVar.set("return email")
  if re.search("sender name",regexVar):
   self.FE_ClientMailVar.set("return email")
  if re.search("Gwarancja Zgodnie z warunkami Gwarancji",regexVar):
   self.FE_Legal.current(1)
  elif re.search("R.kojmia",regexVar):
   self.FE_Legal.current(2)
   if re.search("Wymiana",regexVar) or re.search("Zwrot got.wki",regexVar):
    self.FE_Claim.current(1)
  self.FE_TelVar.set(re.search("(?<=Telefon )((.|\n)*?)(?=DOKUMENT)",regexVar).group())
  self.FE_NameVar.set(re.search("(?<=Imi. i nazwisko )(.*?)(?= Adres e-mail)",regexVar).group())
  address = (re.search("(?<=ADRES, POD KT.RYM ZNAJDUJE SI. REKLAMOWANY TOWAR\nAdres )((.|\n)*?)(?=PODSTAWA PRAWNA)",regexVar).group()).replace("\n"," ")
  self.FE_StreetVar.set(re.search("(.*)(?=\d{2}-\d{3})",address).group())
  self.FE_PostCodeVar.set(re.search("\d{2}-\d{3}",address).group())
  self.FE_Description.delete('1.0',tkinter.END)
  try:
   self.FE_Description.insert('1.0',re.search("(?<=Opis wady Opis Klienta)((.|\n)*?)(?=Data stwierdzenia)",regexVar).group())
  except(AttributeError):
   self.FE_Description.insert('1.0',re.search("(?<=Opis wady )((.|\n)*?)(?=Data stwierdzenia)",regexVar).group())
  self.FE_SNVar.set(re.search("(?<=IMEI )(.*?\s)",regexVar).group())
  self.FE_ModelVar.set(re.search("(?<=\s)(.*)", re.search("(?<=Nazwa towaru )(.*?\s.*?)(?=\s)",regexVar).group()).group())
  self.FE_Day.current(self.FE_Day.cget("values").index(re.search("(?<=Data Sprzeda.y )(\d{2})",regexVar).group()))
  self.FE_Month.current(self.FE_Month.cget("values").index(re.search("(?<=Data Sprzeda.y \d{2}.)(\d{2})",regexVar).group()))
  self.FE_Year.current(self.FE_Year.cget("values").index(re.search("(?<=Data Sprzeda.y \d{2}.\d{2}.)(\d{4})",regexVar).group()))

 def phonechange(self, *args):
  self.FE_TelValue = ""
  r = ""
  for e in self.FE_TelVar.get():
   if e in "1234567890":
    r += e
  if len(r) == 9:
    self.FE_TelVar.set(r[0:3] + "-" + r[3:6] + "-" + r[6:9])
    self.FE_Tel.icursor(11)
    self.FE_TelValue = r


 def SNChange(self, *args):
  r = ""
  for e in self.FE_SNVar.get():
   if e in "1234567890Jj-":
    r += e
  self.FE_SNVar.set(r)

 def ModelChange(self, *args):
  self.FE_ModelVar.set(self.FE_ModelVar.get().upper())
  
class SQLiteHandler():
 def __init__(self):
  from sqlite3 import connect
  self.connect = connect

 def connectToDB(self,filename):
  self.sqliteConnection = self.connect(filename)

 def insert_query(self, query):
  self.sqliteConnection.cursor().execute(query)

 def select_query(self, query):
  cursor = self.sqliteConnection.cursor()
  cursor.execute(query)
  toreturn = cursor.fetchone()
  self.sqliteConnection.commit()
  self.sqliteConnection.close()
  return toreturn

 def closeConnectiontoDB(self):
  self.sqliteConnection.commit()
  self.sqliteConnection.close()

 def serviceQueryWrapper(self,filename,kodpocztowy,AGDRTV):
  self.connectToDB(filename)
  toreturn = self.select_query(self.serviceQueryCreator(kodpocztowy,AGDRTV))
  if not AGDRTV == "Company_Name_Awaria_AGD" and not AGDRTV == "Company_Name_Awaria_TV":
   return ["Brak","Brak","Brak","Brak",toreturn[4]]
  if toreturn:
   return toreturn
  else:
   return ["Brak","Brak","Brak","Brak","Brak"]

 def serviceQueryCreator(self, kodpocztowy,AGDRTV):
  if AGDRTV == "Company_Name_Awaria_AGD":
   return "SELECT Serwisy_AGD.SerwisAGD, Email, Numer, Adres, Miejscowość FROM Kody_Pocztowe\nINNER JOIN Powiaty ON Powiaty.Powiat = Kody_Pocztowe.Powiat\nINNER JOIN Serwisy_AGD ON Serwisy_AGD.SerwisAGD = Powiaty.SerwisAGD\nWHERE Kod_Pocztowy = '" + kodpocztowy + "'"
  else:
   return "SELECT Serwisy_RTV.SerwisRTV, Email, Numer, Adres, Miejscowość FROM Kody_Pocztowe\nINNER JOIN Powiaty ON Powiaty.Powiat = Kody_Pocztowe.Powiat\nINNER JOIN Serwisy_RTV ON Serwisy_RTV.SerwisRTV = Powiaty.SerwisRTV\nWHERE Kod_Pocztowy = '" + kodpocztowy + "'"

 def insert_query_creator(self, table_name, fields_list, values_list):

  fields_string = ""
  for field in fields_list:
   fields_string += field + ","
  fields_string = fields_string[:-1]

  values_string = "'"
  for value in values_list:
   if value == "NULL":
    values_string = values_string[:-1]
    values_string = values_string + "NULL,'"
   else:
    values_string += value + "','"
  values_string = values_string[:-2]
  return "INSERT INTO "+ table_name + "\n(" + fields_string + ")\nVALUES\n("+ values_string +")"

 def quickSendWrapper(self, filename, table_name, fields_list, values_list):
  self.connectToDB(filename)
  self.insert_query(self.insert_query_creator(table_name,fields_list,values_list))
  self.closeConnectiontoDB()

 def selectQueryCreator(self, column, table_name, field, search_value):
  return "SELECT " + column + " FROM " + table_name + " WHERE " + field + " = '" + search_value + "'"

 def quickReadWrapper(self, filename, column, table_name, field, search_value):
  self.connectToDB(filename)
  return self.select_query(self.selectQueryCreator(column,table_name, field, search_value))

class InfoValidation():
 def checkType(self, guiobject):
  if guiobject.FE_TypeValue == "Company_Name_Awaria_AGD":
   return self.Company_NameTicket(guiobject)
  if guiobject.FE_TypeValue == "Company_Name_Awaria_TV":
   return self.Company_NameTicket(guiobject)
  if guiobject.FE_TypeValue == "Company_Name_Monit":
   return self.Company_NameMonit(guiobject)
  if guiobject.FE_TypeValue == "Company_Name_Udzielenie Informacji":
   return self.Company_NameINFO(guiobject)
  if guiobject.FE_TypeValue == "COSMO_Udzielenie_Info":
   return self.CosmoINFO(guiobject)
  return guiobject.L_Type.cget("text")

 def Company_NameTicket(self, guiobject):
  isValid = ""
  if guiobject.FE_NameValue == "":
   isValid += guiobject.L_Name.cget("text")
  if guiobject.FE_TelValue == "":
   isValid += guiobject.L_Tel.cget("text")
  if guiobject.FE_StreetValue == "":
   isValid += guiobject.L_Street.cget("text")
  if guiobject.FE_PostCodeValue == "":
   isValid += guiobject.L_PostCode.cget("text")
  if guiobject.FE_CityValue == "" or guiobject.FE_CityValue == "Brak":
   isValid += guiobject.L_City.cget("text")
  if guiobject.FE_ServiceNameValue == "" or guiobject.FE_ServiceNameValue == "Brak":
   isValid += guiobject.FE_ServiceName.cget("text")
  if guiobject.FE_BrandValue == "":
   isValid += guiobject.L_Brand.cget("text")
  if guiobject.FE_ModelValue == "":
   isValid += guiobject.L_Model.cget("text")
  if guiobject.FE_DeviceValue == "":
   isValid += guiobject.L_Device.cget("text")
  if guiobject.FE_TypeValue == "Company_Name_Awaria_TV" and len(guiobject.FE_SNValue) != 13 and guiobject.FE_LegalValue == "Gwarancja" and not guiobject.FE_BrandValue == "Brand_Name":
    isValid += "Długość SN = 13 cyfr."
  elif guiobject.FE_SNValue == "":
    isValid += guiobject.L_SN.cget("text")
  if guiobject.FE_DayValue == "":
   isValid += "Dzień:"
  if guiobject.FE_MonthValue == "":
   isValid += "Miesiąc:"
  if guiobject.FE_YearValue == "":
   isValid += "Rok:"
  if guiobject.FE_DescriptionValue == "":
   isValid += guiobject.L_Description.cget("text")
  if guiobject.L_CheckboxVar.get() == False:
   isValid += guiobject.L_Checkbox.cget("text")
  if isValid == "":
   return True
  return isValid


 def Company_NameINFO(self, guiobject):
  isValid = ""
  if guiobject.FE_DescriptionValue == "":
   isValid += guiobject.L_Description.cget("text")
  if isValid == "":
   return True
  return isValid


 def Company_NameMonit(self, guiobject):
  import os
  ticket = SQLiteHandler().quickReadWrapper(os.getenv('APPDATA') + "\\PyRegister\\GNOME.db","*","Zgłoszenia","INC",guiobject.FE_MoreInfoValue)
  if not ticket:
   return guiobject.L_MoreInfo.cget("text")
  print(ticket)
  return True

 def CosmoINFO(self, guiobject):
  isValid = ""
  if isValid == "":
   return "Work in Progress"
  return isValid

main_form = tkinter.Tk()
my_gui = formGui(main_form)
main_form.mainloop()
