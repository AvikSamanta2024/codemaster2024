import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter0=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter2=chr(random.randint(97,121)) #Generate a random Lowercase letter (based on ASCII code)
digitLetter3 = chr(random.randint(48,56)) #Generate a random Digit (based on ASCII code)
specialLetter4 = chr(random.randint(33,39)) #Generate a random SpecialCharacter (based on ASCII code)
uppercaseLetter5=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter6=chr(random.randint(97,121)) #Generate a random Lowercase letter (based on ASCII code)
digitLetter7 = chr(random.randint(48,56)) #Generate a random Digit (based on ASCII code)
specialLetter8 = chr(random.randint(33,39)) #Generate a random SpecialCharacter (based on ASCII code)
Letter9 = chr(random.randint(97,120)) #Generate a random SpecialCharacter (based on ASCII code)
#Generate more characters here
#....

#Generate password using all the characters, in random order
password = uppercaseLetter1 + lowercaseLetter2  + digitLetter3 + specialLetter4 + uppercaseLetter5 + lowercaseLetter6  + digitLetter7 + specialLetter8
password = shuffle(password)
password = uppercaseLetter0 + password + Letter9
#Ouput
print(password)
