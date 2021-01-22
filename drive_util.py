from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from gmail_util import send_email
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def upload_file(filename, recipient):

    gauth = GoogleAuth()
    # try to load saved client credentials
    # this is specific to computer/user account
    gauth.LoadCredentialsFile(f"{DIR_PATH}/mycreds.txt")
    if gauth.credentials is None:
        # authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # refresh them if expired
        gauth.Refresh()
    else:
        # initialize the saved creds
        gauth.Authorize()
    # save the current credentials to a file
    gauth.SaveCredentialsFile(f"{DIR_PATH}/mycreds.txt")

    drive = GoogleDrive(gauth)

    # Demo Videos: Folder ID = 1NlxuZwt12g54JjL6Unr01h6DauOJQvOW
    myfile = drive.CreateFile({'parents': [{'id': '1NlxuZwt12g54JjL6Unr01h6DauOJQvOW'}]})
    myfile.SetContentFile(filename)  # reference file name to be uploaded
    name = filename[filename.rindex('/')+1:]
    myfile['title'] = name  # update file name
    myfile.Upload()  # upload file
    print("File uploaded!")

    # send email
    subject = "Your video is ready to view"
    msg = '''Thanks so much for donating!\nYour video is ready to view. Go to the link below to view your video.\n'''
    # Google Drive File link format
    # https://drive.google.com/file/d/FILE_ID
    link = f"https://drive.google.com/file/d/{myfile['id']}"
    body = msg + link
    send_email(recipient, subject, body)
    print(f"Email sent to {recipient}")
