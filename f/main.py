def f():
  from f.service.get import f as get_service
  service = get_service()

  from f.get_last_thread_id import f as get_last_thread_id
  last_thread_id = get_last_thread_id(service)

  from f.email_url.get import f as get_email_url
  last_thread_url = get_email_url(last_thread_id)
  
  from f.get_thread_from_thread_id import f as get_thread_from_thread_id
  last_thread = get_thread_from_thread_id(service, last_thread_id)
  print(last_thread.keys())
  print(len(last_thread['messages']))
  print(last_thread['messages'][-1].keys())
  
  from f.html_to_text import f as html_to_text
  _snippet = html_to_text(last_thread['messages'][-1]['snippet'])
  print(f"snippet:                {_snippet}")

  from f.get_dt_of_most_recent_message_in_thread import f as get_dt_of_most_recent_message_in_thread
  _dt = get_dt_of_most_recent_message_in_thread(last_thread)
  print(f'time sent:              {_dt}')
  
  from f.get_most_recent_message_in_thread import f as get_most_recent_message_in_thread
  most_recent_message = get_most_recent_message_in_thread(last_thread)
  from f.get_subject import f as get_subject
  print(f"subject:                {get_subject(most_recent_message)}")
  
  from datetime import datetime
  print(f'now:                    {datetime.now()}')
  print(f'time since sent:        {datetime.now()-_dt}')

  from f.h import f as h
  from f.get_prev_url import f as get_prev_url
  _more_time_needed = h(get_prev_url(), last_thread_url)
  from datetime import timedelta
  _exceeds_day = datetime.now()-_dt > timedelta(days=1)

  if not _exceeds_day:
    from f.foo import f as foo
    _exceeds_day = foo(service)

  return {
    'exceeds_day': _exceeds_day,
    'more_time_needed': _more_time_needed
  }
