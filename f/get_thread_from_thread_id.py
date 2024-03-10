# get_thread_from_thread_id
def f(service, thread_id):
  return service.users().threads().get(userId='me', id=thread_id).execute()
