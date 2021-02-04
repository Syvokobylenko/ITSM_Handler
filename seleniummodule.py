class seleniumHandler():
 def __init__(self,link):
  from selenium import webdriver
  self.driver = webdriver.Firefox(executable_path="C:\\Program Files (x86)\\Python37-32\\Scripts\\geckodriver")
  self.driver.get(link)

 def injectValue(self,ID,value):
  self.driver.execute_script("document.getElementById('"+ ID +"').value ='" + value + "'")

 def getAttribute(self,ID,attribute):
  return self.driver.find_element_by_id(ID).get_attribute(attribute)

 def jqueryClick(self,ID):
  self.driver.execute_script("document.getElementById('"+ ID +"').click()")

 def sendString(self, xpath, string, keysBefore=False, keysAfter=False):
  from selenium.webdriver.common.keys import Keys
  item = self.driver.find_element_by_xpath(xpath)
  if keysBefore:
   item.send_keys(*keysBefore)
  item.send_keys(string)
  if keysAfter:
   item.send_keys(*keysAfter)

 def getAtrib(self,xpath,attribute):
   return self.driver.find_element_by_xpath(xpath).get_attribute(attribute)

 def clickItem(self,xpath):
  self.driver.find_element_by_xpath(xpath).click()

 def clickItemByID(self,ID):
  self.driver.find_element_by_xpath(xpath).click()

 def clickAfterPopup(self, xpath):
  while True:
   try:
    self.clickItem(xpath)
    break
   except(KeyboardInterrupt):
    return
   except:
    pass

 def clickBeforePopup(self, xpath):
  while len(self.driver.window_handles) == 1:
   try:
    self.clickItem(xpath)
   except(KeyboardInterrupt):
    return
   except:
    pass

 def checkForPopup(self):
  while True:
   if len(self.driver.window_handles) == 1:
    return True

 def waitForPopup(self):
  while len(self.driver.window_handles) == 1:
   pass
  self.popupHandler()

 def popupHandler(self):
  try:
   self.driver.switch_to.window(self.driver.window_handles[1])
  except(IndexError):
   return
  while True:
   if self.driver.title == 'Incident Creation' or self.driver.title == 'Incident Modification':
    from selenium.webdriver.common.keys import Keys
    self.driver.find_element_by_id('arid_WIN_0_1000000881').send_keys([Keys.CONTROL, 'a'],"Rozwiązane",Keys.RETURN)
    self.injectValue("arid_WIN_0_1000000881","Rozwiązane")
    self.driver.find_element_by_id('arid_WIN_0_1000000881').click()
    self.driver.find_element_by_id('arid_WIN_0_1000000881').send_keys(Keys.RETURN)
    self.driver.find_element_by_id('arid_WIN_0_1000000881').click()
    self.driver.find_element_by_id('arid_WIN_0_1000000881').send_keys(Keys.RETURN)
    if self.driver.title == 'Incident Creation':
     self.closePopup('/html/body/div[1]/div[5]/a[5]/div/div')
    elif self.driver.title == 'Incident Modification':
     self.closePopup('/html/body/div[1]/div[5]/a[3]/div/div')
    if len(self.driver.window_handles) == 1:
     break
   elif self.driver.title == 'Support Staff Search':
    self.closePopup('/html/body/div[1]/div[5]/a[3]/div/div', waitfor="/html/body/div[1]/div[5]/div[10]/div[2]/div/div/table/tbody/tr[2]/td[1]/nobr/span")
    break
 def closePopup(self, xpath, waitfor=False):
  self.driver.switch_to.window(self.driver.window_handles[1])
  while len(self.driver.window_handles) != 1:
   try:
    if waitfor:
     while self.getAtrib(waitfor,"innerText") == "":
      pass
    self.driver.find_element_by_xpath(xpath).click()
   except(KeyboardInterrupt):
    return
   except:
    pass
  self.driver.switch_to.window(self.driver.window_handles[0])
  
 def clickOK(self, xpath, iframenum):
  while True:
   try:
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(self.driver.find_elements_by_tag_name('iframe')[iframenum])
    self.driver.find_element_by_xpath(xpath).click()
    self.driver.switch_to.default_content()
    break
   except(KeyboardInterrupt):
    return
   except:
    pass