# get_subject
def f(message):
  payload = message['payload']
  headers = payload['headers']
  for h in headers:
    if h['name'] == 'Subject':
      return h['value']
  return ''
