class VariableHandler():
    def __init__(self):
        self.enviromentVariables()
        self.relativePaths()
        self.readFiles()

    def enviromentVariables(self):
        import getpass
        self.current_user = getpass.getuser()

    def relativePaths(self):
        import os
        from pathlib import Path

        self.db_path = "Z:\\Company_name\\GNOME.db"
        self.local_db_path = os.getenv('APPDATA') + "\\PyRegister\\GNOME.db"

    def readFiles(self):
        import os
        if os.path.isfile('C:\\Users\\' + self.current_user + '\\Documents\\inprogress.txt'):
            with open('C:\\Users\\' + self.current_user + '\\Documents\\inprogress.txt') as contents:
                self.INC_InProgress = []
                for INC in contents.readlines():
                    self.INC_InProgress.append(INC.replace("\n",""))
        
        if os.path.isfile('C:\\Users\\' + self.current_user + '\\Documents\\2nd_ITSM_inprogress.txt'):
            with open('C:\\Users\\' + self.current_user + '\\Documents\\2nd_ITSM_inprogress.txt') as contents:
                self.INC_2nd_ITSM_In_Progress = []
                for INC in contents.readlines():
                    self.INC_2nd_ITSM_In_Progress.append(INC.replace("\n",""))

        with open(str(os.path.dirname(os.path.realpath(__file__))) + "\\templates\\ticket.html","r", encoding="utf-8") as contents:
            self.ticket_temp = contents.read()

        with open(str(os.path.dirname(os.path.realpath(__file__))) + "\\templates\\response.html","r", encoding="utf-8") as contents:
            self.response_temp = contents.read()

        with open(str(os.path.dirname(os.path.realpath(__file__))) + "\\templates\\response_delivery_company.html","r", encoding="utf-8") as contents:
            self.response_delivery_company_temp = contents.read()
        
        with open(str(os.path.dirname(os.path.realpath(__file__))) + "\\templates\\audit.html","r", encoding="utf-8") as contents:
            self.audit_temp = contents.read()
        
        with open(str(os.path.dirname(os.path.realpath(__file__))) + "\\templates\\audit_row.html","r", encoding="utf-8") as contents:
            self.audit_row_temp = contents.read()

        with open(str(os.path.dirname(os.path.realpath(__file__))) + "\\templates\\audit_singular.html","r", encoding="utf-8") as contents:
            self.audit_singular_temp = contents.read()
        
        self.upload_files = []
        upload_dir = 'C:\\Users\\' + self.current_user + '\\Documents\\Upload\\'
        for upload_file in os.listdir(upload_dir):
            filepath = upload_dir + "\\" + upload_file
            import os
            if os.path.getsize(filepath) > 4194304:
                os.remove(filepath)
                #filepath = filepath + " - Przekroczony rozmiar"
                #with open(filepath, "x"):
                    #pass
            self.upload_files.append({"path": filepath, "file_name": upload_file})
        
        
        if os.path.isfile('C:\\Users\\' + self.current_user + '\\Documents\\Resolved\\resolved.txt'):
            with open('C:\\Users\\' + self.current_user + '\\Documents\\Resolved\\resolved.txt') as contents:
                self.INC_resolved = []
                for INC in contents.readlines():
                    self.INC_resolved.append(INC.replace("\n",""))
        
            for INC in self.INC_resolved:
                try:
                    with open('C:\\Users\\' + self.current_user + '\\Documents\\Resolved\\' + INC,'x') as contents:
                        pass
                except(FileExistsError):
                    pass
            os.remove('C:\\Users\\' + self.current_user + '\\Documents\\Resolved\\resolved.txt')

        self.resolve_files = []
        resolved_dir = 'C:\\Users\\' + self.current_user + '\\Documents\\Resolved\\'
        for resolve_file in os.listdir(resolved_dir):
            self.resolve_files.append({"path": resolved_dir + resolve_file, "file_name": resolve_file})
        

        
        

