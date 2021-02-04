def sendEmail(to,cc,sender,subject,body):
    import win32com.client as win32
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = to
    mail.CC = cc
    mail.SentOnBehalfOfName = sender
    mail.Subject = subject
    mail.HTMLBody = body
    mail.Send()

class MailAttributes():

    def __init__(self, mail_path):
        import win32com.client as win32
        self.mail_object = win32.Dispatch("Outlook.Application").GetNamespace("MAPI").OpenSharedItem(mail_path)

    def GetBodyTXT(self):
        return self.mail_object.Body

    def GetSender(self):
        if self.mail_object.SenderEmailType == "EX":
            return self.mail_object.Sender.GetExchangeUser().PrimarySmtpAddress
        return self.mail_object.SenderEmailAddress

    def GetRecipient(self):
        return self.mail_object.To