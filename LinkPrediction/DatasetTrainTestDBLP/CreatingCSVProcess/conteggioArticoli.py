from xml.sax.handler import ContentHandler
import xml.sax


class countHandler(ContentHandler):
    def __init__(self):
        self.tags = {}

    def startElement(self, name, attr):
        if not self.tags.get(name):
            self.tags[name] = 0
        self.tags[name] += 1


parser = xml.sax.make_parser()
handler = countHandler()
parser.setContentHandler(handler)
parser.parse("../../dblp/dblp.xml")

tags = handler.tags.keys()
for tag in tags:
    print (tag, handler.tags[tag])
