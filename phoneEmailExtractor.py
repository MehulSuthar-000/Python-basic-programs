import re
import pyperclip

text = pyperclip.paste()
matches =[]
#phone number regex
phoneRegex = re.compile(r'''

            (\+\d{2})   #country code e.g. +91
            (\s|-|\.)?  #optional space
            (\d{3})     #three digits of first 10 digit phone number
            (\s|-|\.)   #mandatory separator
            (\d{3})     #three digits of second 10 digit phone number
            (\s|-|\.)   #mandatory separator
            (\d{4})     #four digits of third 10 digit phone number
''',re.VERBOSE)


phoneNumbers = phoneRegex.findall(text)
print(phoneNumbers)
phoneNum =[]
for groups in phoneNumbers:
        phoneNum = '-'.join([groups[0], groups[2], groups[4],groups[6]])
        matches.append(phoneNum)
        
print(phoneNum)

#email regex
emailRegex = re.compile(r'''
        ([a-zA-Z0-9._%+-]+   #username or starting part of the email
        @                   #@ symbol
        [a-zA-Z0-9.-]+      #domain name
        (\.[a-zA-Z]{2,4})
        )
''',re.VERBOSE)


for groups in emailRegex.findall(text):
        matches.append(groups[0])

if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard:')
        print('\n'.join(matches))
else:
        print('No phone numbers or email addresses found.')
