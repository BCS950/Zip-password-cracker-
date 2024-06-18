#AUTHOR: EASIN HOSSAIN
#zip password cracker 
from termcolor import colored
import pyfiglet
import zipfile
text = ("ZIP CRACKER")
print(pyfiglet.figlet_format(text))
print("_______________________________________")
print(colored("Tool Name: Zip password cracker","green"))
print(colored("Author   : Easin Hossain","red"))
print(colored("Github   : BCS_950","blue")
print(colored("Facebook : EASIN HOSSAIN","yellow"))
print("••••••••••••••••••••••••••••••••••••••••")

def shawon_crack(password_list, obj):
  bcs=0
  with open (password_list, 'rb') as file:
    for line in file:
      for word in line,split():
        try:
          bcs+=1
          obj.extractall(pwd=word)



          print("PASSWORD FOUND AT LINE", bcs)
          print("PASSWORD IS", word.decode())
          return True

        except:
          continue

  return False

if __name__ == '__main__':
  zip_file = input(">Enter zip file to extract: ")
  password_list = input(">Provide list of passwords to use: ")

  obj = zipfile.ZipFile(zip_file)
  cnt = len(list(open(password_list, 'rb')))
  print("There are total", cnt, "number of passwords to test.")
  if shawon_crack(password_list, obj) == False:
    print(">Password not found in the list provided.")
    
