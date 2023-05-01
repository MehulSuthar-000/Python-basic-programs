import re
def strongPasswordChecker(regexList,password):
    for regex in regexList:
        if(regex.search(password) == None):
            print("The entered password is not strong")
            return
        else:
            print("The entered password is strong")
            return
        
lengthRegex =  re.compile(r'.{8,}')
lowerCaseRegex = re.compile(r'[a-z]+')   #lower case and should occur atleast once
upperCaseRegex = re.compile(r'[A-Z]+')   #upper case and should occur atleast once
digitRegex = re.compile(r'[0-9]+')       # checks digit and should occur atleast once
specialCharRegex = re.compile(r'[!@#$%^&*()_+{}|:\"<>?/~`-]') 

regexList = [lengthRegex,lowerCaseRegex,upperCaseRegex,digitRegex,specialCharRegex]

print("Enter the password")
password = input()

strongPasswordChecker(regexList , password)
