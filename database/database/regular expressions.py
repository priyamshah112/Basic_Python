Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: C:/Users/CEC-07/Desktop/pooja/database/db1.py ===========
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/database/db1.py", line 3, in <module>
    cars=( (1,mercedes,745612),(2,audi,747534),(3,bugatti,74561200),(4,nano,45612),(5,tesla,74561211),(6,nexa,7456122))
NameError: name 'mercedes' is not defined
>>> 
=========== RESTART: C:/Users/CEC-07/Desktop/pooja/database/db1.py ===========
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/database/db1.py", line 7, in <module>
    cur.execute("DROP TABLE IF EXITS cars")
sqlite3.OperationalError: near "EXITS": syntax error
>>> 
=========== RESTART: C:/Users/CEC-07/Desktop/pooja/database/db1.py ===========
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/database/db1.py", line 12, in <module>
    cur.commit()
AttributeError: 'sqlite3.Cursor' object has no attribute 'commit'
>>> 
=========== RESTART: C:/Users/CEC-07/Desktop/pooja/database/db1.py ===========
>>> 
=========== RESTART: C:/Users/CEC-07/Desktop/pooja/database/db1.py ===========
>>> 
=========== RESTART: C:/Users/CEC-07/Desktop/pooja/database/db2.py ===========
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/database/db2.py", line 13, in <module>
    print(row)
NameError: name 'row' is not defined
>>> 
=========== RESTART: C:/Users/CEC-07/Desktop/pooja/database/db2.py ===========
(1, 'mercedes', 745612)
(2, 'audii', 747534)
(3, 'bugatti', 74561200)
(4, 'nano', 45612)
(5, 'tesla', 74561211)
(6, 'nexa', 7456122)
>>> 
=========== RESTART: C:/Users/CEC-07/Desktop/pooja/database/db3.py ===========
enter car id - 123456
enter car name kj
car rate -  45612
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/database/db3.py", line 10, in <module>
    cur.executemany("UPDATE cars SET(?,?,? )",cars)
sqlite3.OperationalError: near "(": syntax error
>>> import Exception
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import Exception
ModuleNotFoundError: No module named 'Exception'
>>> import Exceptions
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import Exceptions
ModuleNotFoundError: No module named 'Exceptions'
>>> import exxception
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import exxception
ModuleNotFoundError: No module named 'exxception'
>>> help(exception)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    help(exception)
NameError: name 'exception' is not defined
>>> raise Exception
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    raise Exception
Exception
>>> raise AttributError
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    raise AttributError
NameError: name 'AttributError' is not defined
>>> raise AttributeError
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    raise AttributeError
AttributeError
>>> raise IOError
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    raise IOError
OSError
>>> raise IndexError
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    raise IndexError
IndexError
>>> raise KeyError
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    raise KeyError
KeyError
>>> raise NameError
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    raise NameError
NameError
>>> 
=========== RESTART: C:/Users/CEC-07/Desktop/pooja/database/db3.py ===========
enter car id - 1221
enter car name fddf
car rate -  123
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/database/db3.py", line 10, in <module>
    cur.executemany("UPDATE cars SET x,y,z=(?,?,?)")
TypeError: function takes exactly 2 arguments (1 given)
>>> 
=========== RESTART: C:/Users/CEC-07/Desktop/pooja/database/db3.py ===========
enter car id - 11213
enter car name fgfg
car rate -  22
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/database/db3.py", line 10, in <module>
    cur.executemany("UPDATE cars SET x,y,z=(?,?,?) WHERE x=0")
TypeError: function takes exactly 2 arguments (1 given)
>>> 
=========== RESTART: C:/Users/CEC-07/Desktop/pooja/database/db3.py ===========
enter car id - 123
enter car name gf
car rate -  23
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/database/db3.py", line 10, in <module>
    cur.executemany("UPDATE cars SET id=? WHERE name=? OR rate=?",x,y,z)
TypeError: function takes exactly 2 arguments (4 given)
>>> 
=========== RESTART: C:/Users/CEC-07/Desktop/pooja/database/db3.py ===========
enter car id - 4524
enter car name hjhj
car rate -  122
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/database/db3.py", line 10, in <module>
    cur.executemany("UPDATE cars SET id=? WHERE name=? OR rate=?",x,y,z)
TypeError: function takes exactly 2 arguments (4 given)
>>> 
=========== RESTART: C:/Users/CEC-07/Desktop/pooja/database/db3.py ===========
enter car id - 8
enter car name ui
car rate -  21
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/database/db3.py", line 10, in <module>
    cur.executemany("UPDATE cars SET x=?,y=? WHERE x=8",y,z)
TypeError: function takes exactly 2 arguments (3 given)
>>> 
=========== RESTART: C:/Users/CEC-07/Desktop/pooja/database/db3.py ===========
enter car id - 142
enter car name hj
car rate -  4
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/database/db3.py", line 10, in <module>
    cur.executemany("UPDATE cars SET z=? WHERE y=f",z)
TypeError: 'int' object is not iterable
>>> import re
>>> s=('xx','axa','xas','axc','aax','xxxxxx','xxasds','axcsdax')
>>> x=re.search('devansh','devansh is a bitc..')
>>> print(x)
<_sre.SRE_Match object; span=(0, 7), match='devansh'>
>>> x=re.search('d','devansh jha2')
>>> print(k)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(k)
NameError: name 'k' is not defined
>>> print(x)
<_sre.SRE_Match object; span=(0, 1), match='d'>
>>> a=re.search('xxx',s)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a=re.search('xxx',s)
  File "C:\Users\CEC-07\AppData\Local\Programs\Python\Python36-32\lib\re.py", line 182, in search
    return _compile(pattern, flags).search(string)
TypeError: expected string or bytes-like object
>>> a=filter((lambda s: re.match(r"xxxx",s)),s)
>>> print(*a)
xxxxxx
>>> s=('xx','axa','xas','axc','aax','xxxxxx','xxasds','axcsdax','xxxa')
>>> a=filter((lambda s: re.match(r"xxxx",s)),s)
>>> print(*a)
xxxxxx
>>>  a=filter((lambda s: re.match(r"xx",s)),s)
 
SyntaxError: unexpected indent
>>> a=filter((lambda s: re.match(r"xx",s)),s)
>>> print(*a)
xx xxxxxx xxasds xxxa
>>> a=filter((lambda s: re.search(r"xx",s)),s)
>>> print(*a)
xx xxxxxx xxasds xxxa
>>> a=filter((lambda s: re.search(r"ax",s)),s)
>>> print(*a)
axa axc aax axcsdax
>>> a=filter((lambda s: re.search(r"a.x",s)),s)
>>> print(*a)
aax
>>> #match - search from start
>>> #search - any thing in between
>>> #  . -wild card for single char it checks first then . then last char
>>> a=filter((lambda s: re.search(r"a\.x",s)),s)
>>> print(*a)

>>> # \ -escape sequal (removes the special meaning of wild card and takes it as value)
>>> s=('xx','axa','xa\s','axc','aa\x','xx\xxxx','xxasds','a\xcsdax','xxxa')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \xXX escape
>>> s=('xx','a\\xa','x\\as','a\\xc','aa\\x','xxxxxx','xxasds','axcsdax','xxxa')
>>> a=filter((lambda s: re.search(r"a\.x",s)),s)
>>> print(*a)

>>> # \\ now slash itself got slash value while it was just \ it took it as escape sequal
>>>  a=filter((lambda s: re.search(r"a\\x",s)),s)
 
SyntaxError: unexpected indent
>>> a=filter((lambda s: re.search(r"a\\x",s)),s)
>>> print(*a)
a\xa a\xc aa\x
>>> * - any number many
SyntaxError: invalid syntax
>>> #  * - any number many
>>> a=filter((lambda s: re.search(r"a.*x",s)),s)
>>> print(*a)
a\xa a\xc aa\x axcsdax
>>> a=filter((lambda s: re.search(r"a.*",s)),s)
>>> print(*a)
a\xa x\as a\xc aa\x xxasds axcsdax xxxa
>>> # + - it checks in between
>>> a=filter((lambda s: re.search(r"a+x",s)),s)
>>> print(*a)
axcsdax
>>> a=filter((lambda s: re.match(r"a+x",s)),s)
>>> print(*a)
axcsdax
>>> a=filter((lambda s: re.match(r"a*x",s)),s)
>>> print(*a)
xx x\as xxxxxx xxasds axcsdax xxxa
>>> a=filter((lambda s: re.match(r"a.*x",s)),s)
>>> print(*a)
a\xa a\xc aa\x axcsdax
>>> a=filter((lambda s: re.match(r"[^a]",s)),s)
>>> print(*a)
xx x\as xxxxxx xxasds xxxa
>>> a=filter((lambda s: re.match(r"[^a]**",s)),s)
>>> print(*a)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print(*a)
  File "<pyshell#64>", line 1, in <lambda>
    a=filter((lambda s: re.match(r"[^a]**",s)),s)
  File "C:\Users\CEC-07\AppData\Local\Programs\Python\Python36-32\lib\re.py", line 172, in match
    return _compile(pattern, flags).match(string)
  File "C:\Users\CEC-07\AppData\Local\Programs\Python\Python36-32\lib\re.py", line 301, in _compile
    p = sre_compile.compile(pattern, flags)
  File "C:\Users\CEC-07\AppData\Local\Programs\Python\Python36-32\lib\sre_compile.py", line 562, in compile
    p = sre_parse.parse(p, flags)
  File "C:\Users\CEC-07\AppData\Local\Programs\Python\Python36-32\lib\sre_parse.py", line 856, in parse
    p = _parse_sub(source, pattern, flags & SRE_FLAG_VERBOSE, False)
  File "C:\Users\CEC-07\AppData\Local\Programs\Python\Python36-32\lib\sre_parse.py", line 415, in _parse_sub
    itemsappend(_parse(source, state, verbose))
  File "C:\Users\CEC-07\AppData\Local\Programs\Python\Python36-32\lib\sre_parse.py", line 618, in _parse
    source.tell() - here + len(this))
sre_constants.error: multiple repeat at position 5
>>> e=('c')
>>>  a=filter((lambda e: re.match(r"[^c]",e)),e)
 
SyntaxError: unexpected indent
>>> a=filter((lambda e: re.match(r"[^c]",e)),e)
>>> print(*a)

>>> a=filter((lambda s: re.match(r"[^xa]**",s)),s)
>>> print(*a)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    print(*a)
  File "<pyshell#70>", line 1, in <lambda>
    a=filter((lambda s: re.match(r"[^xa]**",s)),s)
  File "C:\Users\CEC-07\AppData\Local\Programs\Python\Python36-32\lib\re.py", line 172, in match
    return _compile(pattern, flags).match(string)
  File "C:\Users\CEC-07\AppData\Local\Programs\Python\Python36-32\lib\re.py", line 301, in _compile
    p = sre_compile.compile(pattern, flags)
  File "C:\Users\CEC-07\AppData\Local\Programs\Python\Python36-32\lib\sre_compile.py", line 562, in compile
    p = sre_parse.parse(p, flags)
  File "C:\Users\CEC-07\AppData\Local\Programs\Python\Python36-32\lib\sre_parse.py", line 856, in parse
    p = _parse_sub(source, pattern, flags & SRE_FLAG_VERBOSE, False)
  File "C:\Users\CEC-07\AppData\Local\Programs\Python\Python36-32\lib\sre_parse.py", line 415, in _parse_sub
    itemsappend(_parse(source, state, verbose))
  File "C:\Users\CEC-07\AppData\Local\Programs\Python\Python36-32\lib\sre_parse.py", line 618, in _parse
    source.tell() - here + len(this))
sre_constants.error: multiple repeat at position 6
>>> a=filter((lambda s: re.match(r"[^xa]",s)),s)
>>> print(*a)

>>> # ^,~  - it  will not include the given unit
>>>  a=filter((lambda s: re.search(r"[^xa]",s)),('c','a'))
 
SyntaxError: unexpected indent
>>> 
>>> a=filter((lambda s: re.search(r"[^xa]",s)),('c','a'))
>>> print(*a)
c
>>> # ^ - start $- end
>>> a=filter((lambda s: re.search(r"[^xa]*$",s)),s)
>>> print(*a)
xx a\xa x\as a\xc aa\x xxxxxx xxasds axcsdax xxxa
>>> a=filter((lambda s: re.search(r"^[^xa]*$",s)),s)
>>> print(*a)

>>> 
