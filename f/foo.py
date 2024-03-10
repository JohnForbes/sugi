from f.get_threads import f as get_threads
from f.get_dt_of_most_recent_message_in_thread import f as get_dt_of_most_recent_message_in_thread
from f.get_thread_from_thread_id import f as get_thread_from_thread_id
from datetime import datetime
from datetime import timedelta

# foo
def f(service) -> bool:
  for thread in get_threads(service):
    _dt = get_dt_of_most_recent_message_in_thread(
      get_thread_from_thread_id(service, thread['id'])
    )
    _exceeds_day = datetime.now()-_dt > timedelta(days=1)
    print(_dt, _exceeds_day)
    if _exceeds_day:
      return _exceeds_day
  return _exceeds_day

t = lambda: 1 # TODO: Fix this test
