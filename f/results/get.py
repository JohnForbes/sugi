def f(x):
  s = x['service']
  messages = s.users().messages()
  _x = {'userId':'me', 'labelIds':['INBOX']}
  if 'page_token' in x: _x['pageToken'] = x['page_token']
  return messages.list(**_x).execute()
