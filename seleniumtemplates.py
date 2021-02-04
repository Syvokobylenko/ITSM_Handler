def Company_nameInfoitsm_name(firefox, itsm_name_fields):
    from selenium.webdriver.common.keys import Keys
    firefox.clickItem('/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[1]/table/tbody/tr/td[2]/a[2]')
    firefox.sendString('//*[@id="arid_WIN_3_1000000018"]',itsm_name_fields["lastname"],"",Keys.RETURN)
    firefox.sendString('//*[@id="arid_WIN_3_1000000000"]',itsm_name_fields["summary"])
    firefox.sendString('//*[@id="arid_WIN_3_1000000151"]',itsm_name_fields["notes"])
    firefox.sendString('//*[@id="arid_WIN_3_1000000001"]',itsm_name_fields["company"],keysBefore=[Keys.CONTROL, 'a'])
    firefox.sendString('//*[@id="arid_WIN_3_1000000063"]',itsm_name_fields["tier1"])
    if itsm_name_fields["tier3"]:
        firefox.sendString('//*[@id="arid_WIN_3_1000000064"]',itsm_name_fields["tier2"])
        firefox.sendString('//*[@id="arid_WIN_3_1000000065"]',itsm_name_fields["tier3"],keysAfter=Keys.RETURN)
    else:
        firefox.sendString('//*[@id="arid_WIN_3_1000000064"]',itsm_name_fields["tier2"],keysAfter=Keys.RETURN)
    firefox.sendString('//*[@id="arid_WIN_3_1000000156"]', itsm_name_fields["resolution"])
    firefox.sendString('//*[@id="arid_WIN_3_1000000217"]',itsm_name_fields["group"])
    firefox.sendString('//*[@id="arid_WIN_3_1000000218"]',itsm_name_fields["assignee"],keysAfter=Keys.RETURN)
    INC = str(firefox.getAtrib('//*[@id="arid_WIN_3_1000000161"]','value'))
    if itsm_name_fields["popup"]:
        firefox.waitForPopup()
        import time
        time.sleep(2)
    if itsm_name_fields["status"]:
        resolve = '/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[4]/div/div/div[3]/fieldset/div/div/div/div/div[2]/fieldset/div/a[5]/div/div'
        firefox.clickBeforePopup(resolve)
        firefox.waitForPopup()
    save = '/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[4]/div/div/div[3]/fieldset/div/div/div/div/div[2]/fieldset/div/a[2]/div/div'
    firefox.clickAfterPopup(save)
    firefox.clickOK("/html/body/div[2]/a",1)
    return INC

def 2nd_ITSMReg(firefox,ticketinfo,service):
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import Select
    firefox.driver.find_element_by_name('order.transactionId').send_keys([Keys.CONTROL, 'a'])
    firefox.driver.find_element_by_name('order.transactionId').send_keys(ticketinfo["Dane_Dodatkowe"])
    firefox.driver.find_element_by_name('order.partnerOrderId').send_keys(ticketinfo["INC"])
    firefox.driver.find_element_by_id('order.customerInformation.custName').send_keys(ticketinfo["Imię_Nazwisko"])
    firefox.driver.find_element_by_id('custMobilePhone').send_keys(ticketinfo["Numer_Telefonu"])
    firefox.driver.find_element_by_name('order.customerInformation.custStreet').send_keys(ticketinfo["Ulica"])
    firefox.driver.find_element_by_name('order.customerInformation.custZip').send_keys(ticketinfo["Kod_Pocztowy"])
    firefox.driver.find_element_by_id('order.customerInformation.custCity').send_keys(ticketinfo["Miejscowość"])
    firefox.driver.find_element_by_id('order.deviceInformation.articleDescription').send_keys(ticketinfo["Model"])
    firefox.driver.find_element_by_name('order.deviceInformation.serialNumber').send_keys(ticketinfo["Model"])
    firefox.driver.find_element_by_name('order.errorInformation.errorDescription').send_keys(ticketinfo["Opis"])
    firefox.driver.find_element_by_name('order.warrantyInformation.guaranteeTypeId').click()
    firefox.driver.find_element_by_id('buyDateAsString').send_keys(ticketinfo["Data_Zakupu"].replace('.','-'))
    if ticketinfo["Z_Tytułu"] == "Przedsprzedaż":
        firefox.driver.find_element_by_id('order.kodNaprawy').send_keys(Keys.DOWN)
    if ticketinfo["Z_Tytułu"] == "Rękojmia":
        firefox.driver.find_element_by_id('order.kodNaprawy').send_keys(Keys.DOWN)
        firefox.driver.find_element_by_id('order.kodNaprawy').send_keys(Keys.DOWN)
    firefox.driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/p/input[1]').click()
    while firefox.driver.title != '2nd_ITSM Logistic - podgląd zlecenia':
        pass
    firefox.driver.execute_script('document.getElementById("orderDiv").getElementsByTagName("ul")[0].getElementsByTagName("li")[0].getElementsByTagName("a")[0].click()')
    firefox.driver.execute_script('document.getElementById("orderData").getElementsByTagName("div")[2].getElementsByTagName("div")[0].getElementsByTagName("div")[0].getElementsByTagName("p")[6].getElementsByTagName("input")[0].click()')
    while True:
        try:
            if firefox.driver.find_element_by_id('serviceId').get_attribute("value") == "0":
                break
        except:
            pass
    import time
    time.sleep(1)
    while True:
        try:
            select = Select(firefox.driver.find_element_by_id('serviceId'))
            select.select_by_visible_text(service['2nd_ITSM'])
            firefox.driver.find_element_by_name('update').click()
            break
        except:
            pass

def 2nd_ITSMLogin(firefox):
    firefox.driver.execute_script("window.open('');")
    firefox.driver.switch_to.window(firefox.driver.window_handles[1])
    firefox.driver.get('https://ql.2nd_ITSM-net.pl/order_new.jsp')
    if firefox.driver.title == '2nd_ITSM Logistic - login':
        firefox.driver.find_element_by_name('login').send_keys("michal.szulecki")
        firefox.driver.find_element_by_name('password').send_keys("LIpiec2019")
        firefox.driver.find_element_by_name('ok').click()

def radomGetStatus(firefox, rma, tel):
    from selenium.webdriver.common.keys import Keys
    firefox.driver.find_element_by_name('orderID').send_keys([Keys.CONTROL, 'a'])
    firefox.driver.find_element_by_name('orderID').send_keys(rma)
    firefox.driver.find_element_by_name('authValue').send_keys([Keys.CONTROL, 'a'])
    firefox.driver.find_element_by_name('authValue').send_keys(tel)
    firefox.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/form/table/tbody/tr[1]/td[3]/input').click()
    firefox.driver.switch_to.frame(firefox.driver.find_elements_by_tag_name('iframe')[0])
    try:
        status = firefox.driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/span").get_attribute("innerHTML")
    except:
        status = "Błąd systemu MIK"
    firefox.driver.switch_to.default_content()
    return status

def itsm_nameResolve(firefox, INC):
    firefox.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[4]/div/div/div[2]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div[2]/div[2]/div/dl/dd[3]/span[2]/a').click()
    firefox.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[1]/table/tbody/tr/td[2]/a[1]').click()
    from selenium.webdriver.common.keys import Keys
    firefox.driver.find_element_by_id('arid_WIN_3_1000000161').send_keys(INC)
    firefox.driver.find_element_by_id('arid_WIN_3_1000000161').send_keys(Keys.RETURN)
    resolve = '/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[4]/div/div/div[3]/fieldset/div/div/div/div/div[2]/fieldset/div/a[5]/div/div'
    while firefox.getAttribute("arid_WIN_3_7","value") == "":
        pass
    if firefox.getAttribute("arid_WIN_3_7","value") == "Resolved" or firefox.getAttribute("arid_WIN_3_7","value") == "Closed":
        return
    if firefox.getAttribute("arid_WIN_3_1000000156","value") == "" or firefox.getAttribute("arid_WIN_3_1000000156","value") == "W trakcie realizacji.":
        firefox.driver.find_element_by_id('arid_WIN_3_1000000156').send_keys([Keys.CONTROL, 'a'])
        firefox.driver.find_element_by_id('arid_WIN_3_1000000156').send_keys("Zgłoszenie zakończone.")
    firefox.clickBeforePopup(resolve)
    firefox.waitForPopup()
    save = '/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[4]/div/div/div[3]/fieldset/div/div/div/div/div[2]/fieldset/div/a[2]/div/div'
    firefox.clickAfterPopup(save)
    firefox.clickOK("/html/body/div[2]/a",2)
    return


def itsm_name_get_status(firefox,INC):
    firefox.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[1]/table/tbody/tr/td[2]/a[1]').click()
    from selenium.webdriver.common.keys import Keys
    firefox.driver.find_element_by_id('arid_WIN_3_1000000161').send_keys(INC)
    firefox.driver.find_element_by_id('arid_WIN_3_1000000161').send_keys(Keys.RETURN)
    resolve = '/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[4]/div/div/div[3]/fieldset/div/div/div/div/div[2]/fieldset/div/a[5]/div/div'
    while firefox.getAttribute("arid_WIN_3_7","value") == "":
        pass
    if firefox.getAttribute("arid_WIN_3_7","value") == "Resolved" or firefox.getAttribute("arid_WIN_3_7","value") == "Closed":
        return "Resolved"
    if firefox.getAttribute("arid_WIN_3_7","value") == "In Progress" or firefox.getAttribute("arid_WIN_3_7","value") == "Assigned":
        return "In Progress"
    return "Unavailable"
 
def uploadFile(firefox, file, INC, summary, notes):
    import time
    #firefox.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[4]/div/div/div[2]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div[2]/div[2]/div/dl/dd[3]/span[2]/a').click()
    firefox.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[1]/table/tbody/tr/td[2]/a[1]').click()
    from selenium.webdriver.common.keys import Keys
    firefox.driver.find_element_by_id('arid_WIN_3_1000000161').send_keys(INC)
    time.sleep(0.2)
    firefox.driver.find_element_by_id('arid_WIN_3_1000000161').send_keys(Keys.RETURN)
    while len(firefox.driver.find_elements_by_tag_name('iframe')) != 2:
        pass
    while len(firefox.driver.find_elements_by_tag_name('iframe')) != 3:
        try:
            while firefox.getAttribute("arid_WIN_3_7","value") not in ["In Progress", "Closed" ,"Resolved", "Assigned"]:
                pass
            if firefox.getAttribute("arid_WIN_3_7","value") == "Closed":
                firefox.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[1]/table/tbody/tr/td[2]/a[1]').click()
                return
            time.sleep(1)
            firefox.jqueryClick('WIN_3_304247100')
        except(KeyboardInterrupt):
            return
        except:
            import traceback
            #traceback.print_exc()
    while True:
        try:
            firefox.driver.switch_to.default_content()
            firefox.driver.switch_to.frame(firefox.driver.find_elements_by_tag_name('iframe')[2])
            firefox.driver.find_element_by_id('PopupAttInput').send_keys(file)
            firefox.driver.find_element_by_xpath('/html/body/div[3]/a[1]').click()
            time.sleep(1)
            try:
                firefox.driver.find_element_by_xpath('/html/body/div[3]/a[1]')
            except:
                firefox.driver.switch_to.default_content()
                break
        except(KeyboardInterrupt):
            return
        except:
            import traceback
            #traceback.print_exc()
    while firefox.getAttribute("arid_WIN_3_304247080","value") == "":
        time.sleep(1)
        firefox.driver.find_element_by_id('arid_WIN_3_304247080').send_keys([Keys.CONTROL, 'a'])
        firefox.driver.find_element_by_id('arid_WIN_3_304247080').send_keys(notes)
        firefox.driver.find_element_by_id('arid_WIN_3_304247080').send_keys(Keys.RETURN)
    while firefox.getAttribute("arid_WIN_3_301398700","value") == "":
        time.sleep(1)
        firefox.driver.find_element_by_id('arid_WIN_3_301398700').send_keys([Keys.CONTROL, 'a'])
        firefox.driver.find_element_by_id('arid_WIN_3_301398700').send_keys(summary)
        firefox.driver.find_element_by_id('arid_WIN_3_301398700').send_keys(Keys.RETURN)
    time.sleep(1)
    firefox.jqueryClick('WIN_3_304247110')
    time.sleep(1)
    save = '/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[4]/div[4]/div/div/div[3]/fieldset/div/div/div/div/div[2]/fieldset/div/a[2]/div/div'
    firefox.clickAfterPopup(save)
    while firefox.getAttribute('arid_WIN_3_1000000161',"value") != "":
        try:
            firefox.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div/div/div[3]/fieldset/div/div/div/div/div[3]/fieldset/div/div/div/div[1]/table/tbody/tr/td[2]/a[1]').click()
        except:
            pass