# find all the links inside a HTML page
from HTMLParser import HTMLParser
from urlparse import urlparse

class LinkFinder(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag


    def error(self, message):
        pass


finder = LinkFinder()
finder.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')