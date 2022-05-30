import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Mubashshir</name>
    <phone type="intl">
        +91 9548902533
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))