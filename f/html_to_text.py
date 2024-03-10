from html.parser import HTMLParser

# html_to_text
def f(x):
  class HTMLFilter(HTMLParser):
    text = ""
    def handle_data(self, data):
      self.text += data
  filter = HTMLFilter()
  filter.feed(x)
  return filter.text
