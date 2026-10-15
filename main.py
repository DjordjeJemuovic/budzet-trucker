# 1.Budzet
# 2.Dodaje troskove
#3.Beisanje troskova
#4.Loguje troskove
import json
import sys
import time
from tarfile import data_filter

user = None

with open('data/user.json', 'r') as file:
    user = json.load(file)

my_budzet = user["budzet"]+ user["credit"]
expens = 0
max_budzet = 10000
print(my_budzet)
if my_budzet>= max_budzet or my_budzet <= 0:
    print("Va budzet nije u dozvoljenom iznosu")
    sys.exit()

expens = 0

while expens <= 0 or expens > my_budzet:
    expens = int(input("Umolim vas unesite vas trosak: \n"))
log = None

current_budzet = my_budzet - expens
with open("expens_log.txt","a") as log_file:
    mesage = f"\n\nAmmount: {expens}\nUser ID: {user["id"]}\nDataTime {time.strftime('%d/%m/%Y %H:%M:%S')}\nTrenutni budzet: {my_budzet}\nPreostali budzet:{current_budzet} "
    log_file.write(mesage)





