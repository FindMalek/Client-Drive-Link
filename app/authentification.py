from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def authentification():
    gauth = GoogleAuth()
    gauth.settings['client_config_file'] = 'data/client_secrets.json'
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)