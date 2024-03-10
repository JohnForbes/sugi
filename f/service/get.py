from googleapiclient.discovery import build
from f.creds.get import f as get_credentials

f = lambda: build(
  'gmail',
  'v1',
  credentials=get_credentials({
    'scopes': ['https://www.googleapis.com/auth/gmail.readonly']
  })
)
