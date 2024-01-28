from time import sleep
from hak.file.save import f as save_file
from hak.file.load import f as load
from os.path import exists

from src.main import f as main

get_prev_delay = lambda: float(load('delay.txt') if exists('delay.txt') else '5')

delay_seconds = get_prev_delay()

result = {
  'exceeds_day': True,
  'more_time_needed': False
}
while result['exceeds_day']:
  result = main()
  print(result['exceeds_day'])
  delay_seconds += 0.1 if result['more_time_needed'] else -delay_seconds/2
  save_file('delay.txt', f'{delay_seconds:.1f}')
  print(f'delay:                  {delay_seconds:.2f} [seconds]')
  print()
  sleep(delay_seconds)
