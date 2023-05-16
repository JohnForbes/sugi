from src.service.get import f as get_service
from src.results.get import f as get_results
from src.messages.get import f as get_messages
from src.email_url.get import f as get_email_url
from webbrowser import open as open_url

def f():
  service = get_service()
  result = service.users().threads().list(userId='me').execute()
  threads = result.get('threads', [])  
  url = get_email_url(threads[-1]['id'])

  while 'nextPageToken' in result:
    page_token = result['nextPageToken']
    _x = {'userId':'me', 'labelIds':['INBOX'], 'pageToken': page_token}
    result = service.users().threads().list(**_x).execute()
    threads = threads + result.get('threads', [])  

  url = get_email_url(threads[-1]['id'])
  
  open_url(url)
