from webbrowser import open as open_url
from hak.file.save import f as save_file

# h
def f(previous_url, this_url):
  if previous_url != this_url:
    print(f'url: {this_url}')
    open_url(this_url)
    save_file('last.txt', this_url)
  return previous_url == this_url
