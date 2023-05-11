def f(x):
  with open('token.json', 'w') as token:
    token.write(x.to_json())
