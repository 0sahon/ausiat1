from getpass import getpass
from string import punctuation
#Set First Name
firstName = input( " Input Your first Name: ")
#set Last Name
lastName= input(" Input your Last Name: ")
#set Email
email = char(input(" Input your Email: ")
# set password
def password_validator (password):
# no space
if '' in password:
return "there is a space in your password"
# length of password
if len(password) is not range(7 ,8):
return"password should be b/w 7 and 8 chars"
# special characters
special_chars= true for x in password if x ii
if len(special_chars) ==0:
return"At least a special characters must I
#At least Number
nums= any( x.isdigits( ) for x in password)
return"At least a number should b added"
return ''your password:
{password}is correct"
password= getpass( “Input your Password” )
Login =(firstName + lastName + email + password)
print(Login)
