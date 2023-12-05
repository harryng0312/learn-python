class PasswordFormModel:
    def __init__(self, client_pubkey: str="", server_pubkey:str = "", session_id:str="", random_no:str="", enc_passwd:str="") -> None:
        self.client_pubkey = client_pubkey
        self.server_pubkey = server_pubkey
        self.session_id = session_id
        self.random_no = random_no
        self.enc_passwd = enc_passwd
        pass

    @property
    def client_pubkey(self) -> str:
        return self.__client_pubkey

    @client_pubkey.setter
    def client_pubkey(self, val: str):
        self.__client_pubkey = val
        return
    
    @property
    def server_pubkey(self) -> str:
        return self.__server_pubkey
    
    @server_pubkey.setter
    def server_pubkey(self, val: str):
        self.__server_pubkey = val
        return
    
    @property
    def session_id(self) -> str:
        return self.__session_id
    
    @session_id.setter
    def session_id(self, val: str):
        self.__session_id = val
        return
    
    @property
    def random_no(self) -> str:
        return self.__random_no
    
    @random_no.setter
    def random_no(self, val: str):
        self.__random_no = val
        return
    
    @property
    def enc_passwd(self) -> str:
        return self.__enc_passwd

    @enc_passwd.setter
    def enc_passwd(self, val: str):
        self.__enc_passwd = val
        return

    # end class
    pass