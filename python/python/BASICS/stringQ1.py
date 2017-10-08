"""1.	Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String"""
print("program to get a string of the first 2 and the last 2 chars from a given a string.")
def cutter():
    string=str(input("enter a word = "))
    t=len(string)
    if(t>2):
        
        print(string[0]+string[1]+string[:-2])
    elif(t==2):
        print(string*2)
    else:
        print("empty string")
cutter()
