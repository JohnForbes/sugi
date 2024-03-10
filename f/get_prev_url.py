from hak.file.load import f as load
from os.path import exists

# get_prev_url
f = lambda: load('last.txt') if exists('last.txt') else ''
