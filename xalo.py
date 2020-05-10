print ("kakshell")
print ("xalo software")
import requests
import os
os.system('clear')
print("\033[92m")
os.system('figlet shaho')
e = open('data.txt','w')
r = requests.session()
d='%27'
print ("\033[97m")
sitaka=input('linky siteka bnusa dl')
d = r.get(sitaka+d)
red="\033[91m"
e.write(d.text)
e.close()
t =open('data.txt','r')
for s in t:

         if s==d.text:
                      sqll=str(d)
                      print(red+"[+] sql haya dlm = : "+sitaka)

         else:
             print(red+"sql nia dlm "+sitaka)


t.close()
f=open('sql_haya,txt','w')
f.write(sitaka)

f.close()
