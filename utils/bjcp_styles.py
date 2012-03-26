import xml.etree.ElementTree as xml

# Load the BJCP Style Guidelines xml file
bjcpStyles = xml.parse("utils/styleguide2008.xml")

root = bjcpStyles.getroot()

classList = root.findall("class")

if classList != None:
        for styleClass in classList:
            print "Class found:", styleClass

