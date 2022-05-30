from re import I
import xml.etree.ElementTree as ET

data = '''
<stuff>
    <users>
        <user serial="1"><name>Mubashshir ali</name><phone>9548902533</phone><email platform="gmail">jssmithsa6516@gmail.com</email></user>
        <user serial="2"><name>Mudassir Ali</name><phone>9639387791</phone><email platform="gmail">mudassirali1297@gmail.com</email></user>
    </users>
</stuff>
'''
hello = open('D:\Coding\Python\Project\Login Project\passwords.txt','r')
Helo = hello.read()
stuff = ET.fromstring(Helo)
lst = stuff.findall('users/user')

# print('User count:',len(lst))

# print(type(lst))

for item in lst:
    print('Username:',item.get('username'))
    print('Name',item.find('name').text)
    print('Email:',item.find('email').text)
    print('Phone:',item.find('phone').text)