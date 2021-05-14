#Birth day checker

import datetime  #library

from datetime import *

#Todays date
today = date.today()

#Get users Birthday
dob_str = input ("what is your DOB  DD/MM/YYYY?")

#conver input to data
dob_data = dob_str.split("/")
dob_day = int(dob_data[0])
dob_month = int(dob_data[1])
dob_year = int(dob_data[2])

#Is itthere birthday
dob = date(dob_year,dob_month,dob_day)

this_year = today.year
next_birthday = date(this_year,dob_month,dob_day)

if today ==  next_birthday:
    print ("Happy Birthday")
else:
    print ("today is not your birthday.")




