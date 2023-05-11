from google.oauth2.credentials import Credentials
from os.path import exists
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from src.creds.save import f as save_creds

def f(x):
  creds = (
    Credentials.from_authorized_user_file('token.json', x['scopes'])
    if exists('token.json') else
    None
  )
  
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      creds = (
        InstalledAppFlow
          .from_client_secrets_file('credentials.json', x['scopes'])
          .run_local_server(port=0)
      )
    
    # Save the credentials for the next run
    save_creds(creds)
  
  return creds
