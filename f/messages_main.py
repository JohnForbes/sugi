from f.service.get import f as get_service
from f.results.get import f as get_results
from f.messages.get import f as get_messages
from f.email_url.get import f as get_email_url
from webbrowser import open as open_url

def f():
  service = get_service()
  results = get_results({'service': service})
  messages = get_messages({'results': results})
  
  # url = get_email_url(messages[-1]['id'])

  while 'nextPageToken' in results:
    page_token = results['nextPageToken']
    results = get_results({'service': service, 'page_token': page_token})
    messages = messages + get_messages({'results': results})
  
  print(messages)
  print(len(messages))

  # url = get_email_url(messages[-1]['id'])
  
  # open_url(url)
