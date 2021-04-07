import xml.etree.ElementTree as ET
# above is elemet tree built in xml parser in python
# used to parse xml from web data import urllib.request import urlopen import parse
#we can use findall without importing re,but here it returns a list of whole tag_base
#and find method of strings returns only single element have parameters i.e what to find
#although get() is dict method but here it will return value of a key(in parameter we write key whose value to return)
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
