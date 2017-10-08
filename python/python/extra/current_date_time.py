#1.	Write a Python program to display the current date and time

import time
 
now = time.strftime("%c")
## date and time representation
print ("Current date & time " + time.strftime("%c"))
 
## Only date representation
print ("Current date "  + time.strftime("%x"))
 
## Only time representation
print ("Current time " + time.strftime("%X"))
 
## Display current date and time from now variable 
print ("Current time %s"  % now )
