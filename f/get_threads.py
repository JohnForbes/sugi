# get_threads
def f(service):
  result = service.users().threads().list(userId='me').execute()
  threads = result.get('threads', [])  
  while 'nextPageToken' in result:
    page_token = result['nextPageToken']
    _x = {'userId':'me', 'labelIds':['INBOX'], 'pageToken': page_token}
    result = service.users().threads().list(**_x).execute()
    threads = threads + result.get('threads', [])  
  return threads
