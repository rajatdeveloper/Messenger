import poplib
import time
     
USERNAME = 'USER_NAME'
PASSWORD =  "PASSWARD"
popserver = 'pop.gmail.com' 
pop = poplib.POP3_SSL(popserver)
pop.user(USERNAME)
pop.pass_(PASSWORD)
     
count , total_len = pop.stat()[0],pop.stat()[1]
     
print(" No of unread mail : ",count)
for c in range(count):
   for message in pop.retr(c+1)[1]:
       print(message)
   time.sleep(10)

