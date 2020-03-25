from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os
from apiclient import errors
import math
import random 

def otp_gen() : 

    digits_in_otp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'
    otp = "" 
    length = len(digits_in_otp)
    for i in range(8) : 
        index = math.floor(random.random() * length)
        otp += list(digits_in_otp)[index] 
    return otp

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/gmail.send']
def send_msg(service,message,user_id='me'):
  try:
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    print('Message Id:',message['id'])
    return message

  except errors.HttpError as error:
    print ('An error occurred:',error)

def create_msg(sender, to, subject, message_text):
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  b64_bytes = base64.urlsafe_b64encode(message.as_bytes())
  b64_string = b64_bytes.decode()
  return {'raw': b64_string}

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    otp = otp_gen()
    print(otp)
    otp_message = 'Please Enter The One Time Password(OTP) On The Registartion Tool.\n'+'Your OTP is :'+otp
    service = build('gmail', 'v1', credentials=creds)
    message = create_msg('sanmeeraj@gmail.com','sanath1002@gmail.com','DPKI One Time Password (OTP)',otp_message)
    x = send_msg(service,message)
    # Call the Gmail API
    


if __name__ == '__main__':
    main()