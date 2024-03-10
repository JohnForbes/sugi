from f.get_most_recent_message_in_thread import f as get_most_recent_message_in_thread
from datetime import datetime

# get_dt_of_most_recent_message_in_thread
def f(thread):
  most_recent_message = get_most_recent_message_in_thread(thread)
  return datetime.fromtimestamp(int(most_recent_message['internalDate'])/1000.0)
