import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationurl():
        url = config.get('common info','baseUrl')
        return url

    @staticmethod
    def getUsername():
        name = config.get('common info','username')
        return name

    @staticmethod
    def getPassword():
        passw = config.get('common info','password')
        return passw