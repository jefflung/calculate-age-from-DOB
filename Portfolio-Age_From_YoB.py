#calculate age from year of birth

import datetime

now=datetime.datetime.now()

YoB=int(input("Please enter your year of birth:"))

age=now.year-YoB

print("Your age is ",age)