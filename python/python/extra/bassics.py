Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> """salami.py
salami slicer
demonstrate string slicing
16/01/17"""
'salami.py\nsalami slicer\ndemonstrate string slicing\n16/01/17'
>>> print"GUIDE"
SyntaxError: invalid syntax
>>> print "0 1 2 3 4 5"
SyntaxError: Missing parentheses in call to 'print'
>>> print("GUIDE")
GUIDE
>>> print("0 1 2 3 ")
0 1 2 3 
>>>  print "GUIDE"
 
SyntaxError: Missing parentheses in call to 'print'
>>> PRINT
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    PRINT
NameError: name 'PRINT' is not defined
>>> print
<built-in function print>
>>> meat="salami"
>>> print("meat[3:5]",meat[3:5])
meat[3:5] am
>>> print("[2:1]")
[2:1]
>>> print("[2:1]",meat[2:1])
[2:1] 
>>> print("meat[2:1]",meat[2:1])
meat[2:1] 
>>> print("meat[:3]",meat[:3])
meat[:3] sal
>>> print("meat[:-3]",meat[:-3])
meat[:-3] sal
>>> """ interpolation variable.py
            demonstrate variable interpolation"""
' interpolation variable.py\n            demonstrate variable interpolation'
>>> name=raw_input("hi,what is ur name?")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    name=raw_input("hi,what is ur name?")
NameError: name 'raw_input' is not defined
>>> prompt="how old are u,%s"%name
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    prompt="how old are u,%s"%name
NameError: name 'name' is not defined
>>> 
