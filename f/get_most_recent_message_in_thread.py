# get_most_recent_message_in_thread
def f(thread):
  messages = thread['messages']
  messages.sort(key=lambda message: message['internalDate'], reverse=True)
  return messages[0]
