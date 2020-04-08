# Write a Python program to display the current date and time.

import time
import datetime 

print("Current date and time")
print(datetime.datetime.today())
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))