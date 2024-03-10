from f.get_threads import f as get_threads

# get_last_thread_id
f = lambda service: get_threads(service)[-1]['id']
