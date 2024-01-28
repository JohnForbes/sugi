from datetime import datetime
from datetime import timedelta
from hak.file.load import f as load
from hak.file.save import f as save_file
from html.parser import HTMLParser
from os.path import exists
from webbrowser import open as open_url

from src.email_url.get import f as get_email_url
from src.messages.get import f as get_messages
from src.results.get import f as get_results
from src.service.get import f as get_service

def h(previous_url, this_url):
  if previous_url != this_url:
    open_url(this_url)
    save_file('last.txt', this_url)
    return False
  else:
    return True

def get_threads(service):
  result = service.users().threads().list(userId='me').execute()
  threads = result.get('threads', [])  
  while 'nextPageToken' in result:
    page_token = result['nextPageToken']
    _x = {'userId':'me', 'labelIds':['INBOX'], 'pageToken': page_token}
    result = service.users().threads().list(**_x).execute()
    threads = threads + result.get('threads', [])  
  return threads

get_last_thread_id = lambda service: get_threads(service)[-1]['id']

get_prev_url = lambda: load('last.txt') if exists('last.txt') else ''

def get_subject(message):
  payload = message['payload']
  headers = payload['headers']
  for h in headers:
    if h['name'] == 'Subject':
      return h['value']
  return ''

def html_to_text(x):
  class HTMLFilter(HTMLParser):
    text = ""
    def handle_data(self, data):
      self.text += data
  filter = HTMLFilter()
  filter.feed(x)
  return filter.text

def get_dt_of_most_recent_message_in_thread(thread):
  most_recent_message = get_most_recent_message_in_thread(thread)
  return datetime.fromtimestamp(int(most_recent_message['internalDate'])/1000.0)

def get_most_recent_message_in_thread(thread):
  messages = thread['messages']
  messages.sort(key=lambda message: message['internalDate'], reverse=True)
  return messages[0]

def get_thread_from_thread_id(service, thread_id):
  return service.users().threads().get(userId='me', id=thread_id).execute()

def foo(service):
  for thread in get_threads(service):
    _dt = get_dt_of_most_recent_message_in_thread(get_thread_from_thread_id(service, thread['id']))
    _exceeds_day = datetime.now()-_dt > timedelta(days=1)
    print(_dt, _exceeds_day)
    if _exceeds_day:
      return _exceeds_day
  return _exceeds_day

def f():
  service = get_service()

  last_thread_id = get_last_thread_id(service)
  last_thread_url = get_email_url(last_thread_id)
  
  last_thread = get_thread_from_thread_id(service, last_thread_id)
  print(last_thread.keys())
  print(len(last_thread['messages']))
  print(last_thread['messages'][-1].keys())
  
  _snippet = html_to_text(last_thread['messages'][-1]['snippet'])
  print(f"snippet:                {_snippet}")

  _dt = get_dt_of_most_recent_message_in_thread(last_thread)
  print(f'time sent:              {_dt}')
  
  most_recent_message = get_most_recent_message_in_thread(last_thread)
  print(f"subject:                {get_subject(most_recent_message)}")
  
  print(f'now:                    {datetime.now()}')
  print(f'time since sent:        {datetime.now()-_dt}')

  _more_time_needed = h(get_prev_url(), last_thread_url)
  _exceeds_day = datetime.now()-_dt > timedelta(days=1)

  if not _exceeds_day:
    _exceeds_day = foo(service)

  return {
    'exceeds_day': _exceeds_day,
    'more_time_needed': _more_time_needed
  }
