Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: C:/Users/CEC-07/Desktop/pooja/file/basicfileop.py =========
hello priyam

>>> help(open)
Help on built-in function open in module io:

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a stream.  Raise IOError upon failure.
    
    file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)
    
    mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending (which on some Unix systems, means that all writes
    append to the end of the file regardless of the current seek position).
    In text mode, if encoding is not specified the encoding used is platform
    dependent: locale.getpreferredencoding(False) is called to get the
    current locale encoding. (For reading and writing raw bytes use binary
    mode and leave encoding unspecified.) The available modes are:
    
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
    
    The default mode is 'rt' (open for reading text). For binary random
    access, the mode 'w+b' opens and truncates the file to 0 bytes, while
    'r+b' opens the file without truncation. The 'x' mode implies 'w' and
    raises an `FileExistsError` if the file already exists.
    
    Python distinguishes between files opened in binary and text modes,
    even when the underlying operating system doesn't. Files opened in
    binary mode (appending 'b' to the mode argument) return contents as
    bytes objects without any decoding. In text mode (the default, or when
    't' is appended to the mode argument), the contents of the file are
    returned as strings, the bytes having been first decoded using a
    platform-dependent encoding or using the specified encoding if given.
    
    'U' mode is deprecated and will raise an exception in future versions
    of Python.  It has no effect in Python 3.  Use newline to control
    universal newlines mode.
    
    buffering is an optional integer used to set the buffering policy.
    Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
    line buffering (only usable in text mode), and an integer > 1 to indicate
    the size of a fixed-size chunk buffer.  When no buffering argument is
    given, the default buffering policy works as follows:
    
    * Binary files are buffered in fixed-size chunks; the size of the buffer
      is chosen using a heuristic trying to determine the underlying device's
      "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
      On many systems, the buffer will typically be 4096 or 8192 bytes long.
    
    * "Interactive" text files (files for which isatty() returns True)
      use line buffering.  Other text files use the policy described above
      for binary files.
    
    encoding is the name of the encoding used to decode or encode the
    file. This should only be used in text mode. The default encoding is
    platform dependent, but any encoding supported by Python can be
    passed.  See the codecs module for the list of supported encodings.
    
    errors is an optional string that specifies how encoding errors are to
    be handled---this argument should not be used in binary mode. Pass
    'strict' to raise a ValueError exception if there is an encoding error
    (the default of None has the same effect), or pass 'ignore' to ignore
    errors. (Note that ignoring encoding errors can lead to data loss.)
    See the documentation for codecs.register or run 'help(codecs.Codec)'
    for a list of the permitted encoding error strings.
    
    newline controls how universal newlines works (it only applies to text
    mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
    follows:
    
    * On input, if newline is None, universal newlines mode is
      enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
      these are translated into '\n' before being returned to the
      caller. If it is '', universal newline mode is enabled, but line
      endings are returned to the caller untranslated. If it has any of
      the other legal values, input lines are only terminated by the given
      string, and the line ending is returned to the caller untranslated.
    
    * On output, if newline is None, any '\n' characters written are
      translated to the system default line separator, os.linesep. If
      newline is '' or '\n', no translation takes place. If newline is any
      of the other legal values, any '\n' characters written are translated
      to the given string.
    
    If closefd is False, the underlying file descriptor will be kept open
    when the file is closed. This does not work when a file name is given
    and must be True in that case.
    
    A custom opener can be used by passing a callable as *opener*. The
    underlying file descriptor for the file object is then obtained by
    calling *opener* with (*file*, *flags*). *opener* must return an open
    file descriptor (passing os.open as *opener* results in functionality
    similar to passing None).
    
    open() returns a file object whose type depends on the mode, and
    through which the standard file operations such as reading and writing
    are performed. When open() is used to open a file in a text mode ('w',
    'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
    a file in a binary mode, the returned class varies: in read binary
    mode, it returns a BufferedReader; in write binary and append binary
    modes, it returns a BufferedWriter, and in read/write mode, it returns
    a BufferedRandom.
    
    It is also possible to use a string or bytearray as a file for both
    reading and writing. For strings StringIO can be used like a file
    opened in a text mode, and for bytes a BytesIO can be used like a file
    opened in a binary mode.

>>> 
========== RESTART: C:/Users/CEC-07/Desktop/pooja/file/anotherop.py ==========
hello priyam

>>> 
========= RESTART: C:/Users/CEC-07/Desktop/pooja/file/testcase X.py =========
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/file/testcase X.py", line 7, in <module>
    file1()
  File "C:/Users/CEC-07/Desktop/pooja/file/testcase X.py", line 2, in file1
    with open('priyam.txt' ,'x') as file:
FileExistsError: [Errno 17] File exists: 'priyam.txt'
>>> 
========= RESTART: C:/Users/CEC-07/Desktop/pooja/file/testcase X.py =========
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/file/testcase X.py", line 7, in <module>
    file1()
  File "C:/Users/CEC-07/Desktop/pooja/file/testcase X.py", line 3, in file1
    content = file.read()
io.UnsupportedOperation: not readable
>>> 
========= RESTART: C:/Users/CEC-07/Desktop/pooja/file/testcase X.py =========
the first chars are -  hello priyam  devans
the rest chars are -  h _|_

>>> 
========= RESTART: C:/Users/CEC-07/Desktop/pooja/file/testcase X.py =========
the first chars are -  hello priyam  devansh _|_

the rest chars are -  
>>> 
========= RESTART: C:/Users/CEC-07/Desktop/pooja/file/testcase X.py =========
the first chars are -  hello priyam -> GAMERX welcome
the rest chars are -  11:17 11-03-2017

>>> 
========== RESTART: C:/Users/CEC-07/Desktop/pooja/file/readline.py ==========
the first chars are -  ['hello priyam -> GAMERX welcome11:17 11-03-2017\n']
the rest chars are -  
>>> 
======== RESTART: C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py ========
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py", line 8, in <module>
    for priyam in reversed(priyam):
NameError: name 'priyam' is not defined
>>> 
======== RESTART: C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py ========
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py", line 8, in <module>
    for file in reversed(priyam):
NameError: name 'priyam' is not defined
>>> 
======== RESTART: C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py ========
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py", line 8, in <module>
    for file in reversed(file):
NameError: name 'file' is not defined
>>> 
======== RESTART: C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py ========
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py", line 8, in <module>
    for file in reversed(priyam):
NameError: name 'priyam' is not defined
>>> 
======== RESTART: C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py ========
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py", line 8, in <module>
    for file in reversed(priyam):
NameError: name 'priyam' is not defined
>>> 
======== RESTART: C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py ========
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py", line 5, in <module>
    for file in reversed(priyam):
NameError: name 'priyam' is not defined
>>> 
======== RESTART: C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py ========
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py", line 5, in <module>
    for file in reversed(file):
NameError: name 'file' is not defined
>>> 
============= RESTART: C:/Users/CEC-07/Desktop/pooja/file/len.py =============
>>> 
============= RESTART: C:/Users/CEC-07/Desktop/pooja/file/len.py =============
47
>>> 
======== RESTART: C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py ========
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py", line 5, in <module>
    for file in reversed(file):
NameError: name 'file' is not defined
>>> 
======== RESTART: C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py ========
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py", line 5, in <module>
    for file in reversed(priyam):
NameError: name 'priyam' is not defined
>>> 
======== RESTART: C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py ========
hello priyam -> GAMERX welcome11:17 11-03-2017

Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py", line 9, in <module>
    file1()
  File "C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py", line 5, in file1
    for file in reversed(priyam):
NameError: name 'priyam' is not defined
>>> 
======== RESTART: C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py ========
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py", line 9, in <module>
    file1()
  File "C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py", line 3, in file1
    p = file.readline()
UnboundLocalError: local variable 'file' referenced before assignment
>>> 
======== RESTART: C:/Users/CEC-07/Desktop/pooja/file/stripreverse.py ========
hello priyam -> GAMERX welcome11:17 11-03-2017


7
1
0
2
-
3
0
-
1
1

7
1
:
1
1
e
m
o
c
l
e
w

X
R
E
M
A
G

>
-

m
a
y
i
r
p

o
l
l
e
h
>>> 
============= RESTART: C:/Users/CEC-07/Desktop/pooja/file/url.py =============
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en-IN"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script>(function(){window.google={kEI:'05fDWNu-JcnQ0ATqhp5A',kEXPI:'1352992,3700062,3700285,3700347,4028875,4029815,4031109,4032677,4036527,4038012,4039268,4043492,4045840,4048347,4065786,4067342,4071842,4072364,4072776,4073405,4075963,4076096,4076999,4078430,4078763,4079894,4081039,4081164,4083030,4089338,4090550,4090806,4090893,4091352,4092475,4092479,4092827,4092897,4092934,4093133,4093313,4093499,4093808,4093947,4094251,4094544,4094768,4094878,4095381,4095787,4095998,4096052,4096324,4096392,4096742,4097153,4097203,4097517,4097865,4097922,4097929,4097951,4098048,4098050,4098098,4098733,4098740,4098752,4099305,4099382,4100320,4100380,4100671,4100817,4100844,4101224,4101229,4101301,4101651,4101681,4102098,4102234,4102545,4102658,4102694,8503585,8505259,8506340,8507380,8507420,8507940,8508229,8508931,8509037,8509373,8509870,8510787,10200083,10202230,16200027,19001698,19001893,19001897,41027340',authuser:0,kscs:'c9c918f0_24'};google.kHL='en-IN';})();(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||google.kEI};google.getLEI=function(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b};google.https=function(){return"https:"==window.location.protocol};google.ml=function(){return null};google.wl=function(a,b){try{google.ml(Error(a),!1,b)}catch(c){}};google.time=function(){return(new Date).getTime()};google.log=function(a,b,c,d,g){a=google.logUrl(a,b,c,d,g);if(""!=a){b=new Image;var e=google.lc,f=google.li;e[f]=b;b.onerror=b.onload=b.onabort=function(){delete e[f]};window.google&&window.google.vel&&window.google.vel.lu&&window.google.vel.lu(a);b.src=a;google.li=f+1}};google.logUrl=function(a,b,c,d,g){var e="",f=google.ls||"";c||-1!=b.search("&ei=")||(e="&ei="+google.getEI(d),-1==b.search("&lei=")&&(d=google.getLEI(d))&&(e+="&lei="+d));a=c||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+b+e+f+"&zx="+google.time();/^http:/i.test(a)&&google.https()&&(google.ml(Error("a"),!1,{src:a,glmm:1}),a="");return a};google.y={};google.x=function(a,b){google.y[a.id]=[a,b];return!1};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};}).call(this);var a=window.location,b=a.href.indexOf("#");if(0<=b){var c=a.href.substring(b+1);/(^|&)q=/.test(c)&&-1==c.indexOf("#")&&a.replace("/search?"+c.replace(/(^|&)fp=[^&]*/g,"")+"&cad=h")};</script><style>#gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}
</style><style>body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#36c}.q{color:#00c}.ts td{padding:0}.ts{border-collapse:collapse}em{font-weight:bold;font-style:normal}.lst{height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0 4px;margin-left:4px}input{font-family:inherit}a.gb1,a.gb2,a.gb3,a.gb4{color:#11c !important}body{background:#fff;color:black}a{color:#11c;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#36c}a:visited{color:#551a8b}a.gb1,a.gb4{text-decoration:underline}a.gb3:hover{text-decoration:none}#ghead a.gb2:hover{color:#fff !important}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px}.lsbb{background:#eee;border:solid 1px;border-color:#ccc #999 #999 #ccc;height:30px}.lsbb{display:block}.ftl,#fll a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;border:none;color:#000;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#ccc}.lst:focus{outline:none}</style><script></script><link href="/images/branding/product/ico/googleg_lodp.ico" rel="shortcut icon"></head><body bgcolor="#fff"><script>(function(){var src='/images/nav_logo229.png';var iesg=false;document.body.onload = function(){window.n && window.n();if (document.images){new Image().src=src;}
if (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}
}
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/file/url.py", line 9, in <module>
    internet()
  File "C:/Users/CEC-07/Desktop/pooja/file/url.py", line 7, in internet
    l2 = l.decode("utf-8")
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 5206: invalid start byte
>>> 
============= RESTART: C:/Users/CEC-07/Desktop/pooja/file/url.py =============
<META HTTP-EQUIV=Refresh CONTENT="0; URL=http://www.newbostonfund.com/">
>>> 
============= RESTART: C:/Users/CEC-07/Desktop/pooja/file/url.py =============
b'<META HTTP-EQUIV=Refresh CONTENT="0; URL=http://www.newbostonfund.com/">'
>>> 
============= RESTART: C:/Users/CEC-07/Desktop/pooja/file/url.py =============
b'<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en-IN"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script>(function(){window.google={kEI:\'PJjDWN2zAcWa0gSN8au4BA\',kEXPI:\'1352993,3700332,3700347,3700405,4028875,4029815,4031109,4032677,4036527,4038012,4039268,4043492,4045841,4048347,4063220,4065787,4071842,4072126,4072364,4072774,4073405,4075963,4076096,4076998,4077776,4079894,4081038,4081165,4083030,4084029,4085628,4085685,4089914,4090550,4090553,4090806,4090893,4091028,4091352,4092182,4092475,4092479,4092897,4092934,4093134,4093808,4093943,4093947,4094104,4094251,4094544,4094767,4095381,4095997,4096052,4096323,4096742,4096768,4096828,4097153,4097204,4097467,4097517,4097624,4097922,4097929,4097951,4098047,4098721,4098728,4098752,4099381,4100150,4100169,4100380,4100671,4100817,4101151,4101225,4101230,4101875,4102020,4102097,4102099,4102194,4102233,4102400,4102542,4102544,4102658,4102681,4102691,8503585,8505259,8506340,8507380,8507420,8507940,8508229,8508931,8509037,8509373,8509871,8510786,10200083,10202231,16200027,19001698,19001893,19001897,41027342\',authuser:0,kscs:\'c9c918f0_24\'};google.kHL=\'en-IN\';})();(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||google.kEI};google.getLEI=function(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b};google.https=function(){return"https:"==window.location.protocol};google.ml=function(){return null};google.wl=function(a,b){try{google.ml(Error(a),!1,b)}catch(c){}};google.time=function(){return(new Date).getTime()};google.log=function(a,b,c,d,g){a=google.logUrl(a,b,c,d,g);if(""!=a){b=new Image;var e=google.lc,f=google.li;e[f]=b;b.onerror=b.onload=b.onabort=function(){delete e[f]};window.google&&window.google.vel&&window.google.vel.lu&&window.google.vel.lu(a);b.src=a;google.li=f+1}};google.logUrl=function(a,b,c,d,g){var e="",f=google.ls||"";c||-1!=b.search("&ei=")||(e="&ei="+google.getEI(d),-1==b.search("&lei=")&&(d=google.getLEI(d))&&(e+="&lei="+d));a=c||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+b+e+f+"&zx="+google.time();/^http:/i.test(a)&&google.https()&&(google.ml(Error("a"),!1,{src:a,glmm:1}),a="");return a};google.y={};google.x=function(a,b){google.y[a.id]=[a,b];return!1};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};}).call(this);var a=window.location,b=a.href.indexOf("#");if(0<=b){var c=a.href.substring(b+1);/(^|&)q=/.test(c)&&-1==c.indexOf("#")&&a.replace("/search?"+c.replace(/(^|&)fp=[^&]*/g,"")+"&cad=h")};</script><style>#gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}'
b'</style><style>body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#36c}.q{color:#00c}.ts td{padding:0}.ts{border-collapse:collapse}em{font-weight:bold;font-style:normal}.lst{height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0 4px;margin-left:4px}input{font-family:inherit}a.gb1,a.gb2,a.gb3,a.gb4{color:#11c !important}body{background:#fff;color:black}a{color:#11c;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#36c}a:visited{color:#551a8b}a.gb1,a.gb4{text-decoration:underline}a.gb3:hover{text-decoration:none}#ghead a.gb2:hover{color:#fff !important}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px}.lsbb{background:#eee;border:solid 1px;border-color:#ccc #999 #999 #ccc;height:30px}.lsbb{display:block}.ftl,#fll a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;border:none;color:#000;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#ccc}.lst:focus{outline:none}</style><script></script><link href="/images/branding/product/ico/googleg_lodp.ico" rel="shortcut icon"></head><body bgcolor="#fff"><script>(function(){var src=\'/images/nav_logo229.png\';var iesg=false;document.body.onload = function(){window.n && window.n();if (document.images){new Image().src=src;}'
b'if (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}'
b'}'
b'})();</script><div id="mngb"> <div id=gbar><nobr><b class=gb1>Search</b> <a class=gb1 href="http://www.google.co.in/imghp?hl=en&tab=wi">Images</a> <a class=gb1 href="http://maps.google.co.in/maps?hl=en&tab=wl">Maps</a> <a class=gb1 href="https://play.google.com/?hl=en&tab=w8">Play</a> <a class=gb1 href="http://www.youtube.com/?gl=IN&tab=w1">YouTube</a> <a class=gb1 href="http://news.google.co.in/nwshp?hl=en&tab=wn">News</a> <a class=gb1 href="https://mail.google.com/mail/?tab=wm">Gmail</a> <a class=gb1 href="https://drive.google.com/?tab=wo">Drive</a> <a class=gb1 style="text-decoration:none" href="https://www.google.co.in/intl/en/options/"><u>More</u> &raquo;</a></nobr></div><div id=guser width=100%><nobr><span id=gbn class=gbi></span><span id=gbf class=gbf></span><span id=gbe></span><a href="http://www.google.co.in/history/optout?hl=en" class=gb4>Web History</a> | <a  href="/preferences?hl=en" class=gb4>Settings</a> | <a target=_top id=gb_70 href="https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=http://www.google.co.in/%3Fgfe_rd%3Dcr%26ei%3DO5jDWOjSOqPy8AfznZq4Aw" class=gb4>Sign in</a></nobr></div><div class=gbh style=left:0></div><div class=gbh style=right:0></div> </div><center><br clear="all" id="lgpd"><div id="lga"><div style="padding:28px 0 3px"><div style="height:110px;width:276px;background:url(/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png) no-repeat" title="Google" align="left" id="hplogo" onload="window.lol&&lol()"><div style="color:#777;font-size:16px;font-weight:bold;position:relative;top:70px;left:218px" nowrap="">India</div></div></div><br></div><form action="/search" name="f"><table cellpadding="0" cellspacing="0"><tr valign="top"><td width="25%">&nbsp;</td><td align="center" nowrap=""><input name="ie" value="ISO-8859-1" type="hidden"><input value="en-IN" name="hl" type="hidden"><input name="source" type="hidden" value="hp"><input name="biw" type="hidden"><input name="bih" type="hidden"><div class="ds" style="height:32px;margin:4px 0"><input style="color:#000;margin:0;padding:5px 8px 0 6px;vertical-align:top" autocomplete="off" class="lst" value="" title="Google Search" maxlength="2048" name="q" size="57"></div><br style="line-height:0"><span class="ds"><span class="lsbb"><input class="lsb" value="Google Search" name="btnG" type="submit"></span></span><span class="ds"><span class="lsbb"><input class="lsb" value="I\'m Feeling Lucky" name="btnI" onclick="if(this.form.q.value)this.checked=1; else top.location=\'/doodles/\'" type="submit"></span></span></td><td class="fl sblc" align="left" nowrap="" width="25%"><a href="/advanced_search?hl=en-IN&amp;authuser=0">Advanced search</a><a href="/language_tools?hl=en-IN&amp;authuser=0">Language tools</a></td></tr></table><input id="gbv" name="gbv" type="hidden" value="1"></form><div id="gac_scont"></div><div style="font-size:83%;min-height:3.5em"><br><div id="als"><style>#als{font-size:small;margin-bottom:24px}#_eEe{display:inline-block;line-height:28px;}#_eEe a{padding:0 3px;}._lEe{display:inline-block;margin:0 2px;white-space:nowrap}._PEe{display:inline-block;margin:0 2px}</style><div id="_eEe">Google.co.in offered in: <a href="http://www.google.co.in/setprefs?sig=0_2dPaac0hw0oFwruErYLFtJ6SvLU%3D&amp;hl=hi&amp;source=homepage" data-ved="0ahUKEwjdwafN6M3SAhVFjZQKHY34CkcQ2ZgBCAU">&#2361;&#2367;&#2344;&#2381;&#2342;&#2368;</a>  <a href="http://www.google.co.in/setprefs?sig=0_2dPaac0hw0oFwruErYLFtJ6SvLU%3D&amp;hl=bn&amp;source=homepage" data-ved="0ahUKEwjdwafN6M3SAhVFjZQKHY34CkcQ2ZgBCAY">&#2476;&#2494;&#2434;&#2482;&#2494;</a>  <a href="http://www.google.co.in/setprefs?sig=0_2dPaac0hw0oFwruErYLFtJ6SvLU%3D&amp;hl=te&amp;source=homepage" data-ved="0ahUKEwjdwafN6M3SAhVFjZQKHY34CkcQ2ZgBCAc">&#3108;&#3142;&#3122;&#3137;&#3095;&#3137;</a>  <a href="http://www.google.co.in/setprefs?sig=0_2dPaac0hw0oFwruErYLFtJ6SvLU%3D&amp;hl=mr&amp;source=homepage" data-ved="0ahUKEwjdwafN6M3SAhVFjZQKHY34CkcQ2ZgBCAg">&#2350;&#2352;&#2366;&#2336;&#2368;</a>  <a href="http://www.google.co.in/setprefs?sig=0_2dPaac0hw0oFwruErYLFtJ6SvLU%3D&amp;hl=ta&amp;source=homepage" data-ved="0ahUKEwjdwafN6M3SAhVFjZQKHY34CkcQ2ZgBCAk">&#2980;&#2990;&#3007;&#2996;&#3021;</a>  <a href="http://www.google.co.in/setprefs?sig=0_2dPaac0hw0oFwruErYLFtJ6SvLU%3D&amp;hl=gu&amp;source=homepage" data-ved="0ahUKEwjdwafN6M3SAhVFjZQKHY34CkcQ2ZgBCAo">&#2711;&#2753;&#2716;&#2736;&#2750;&#2724;&#2752;</a>  <a href="http://www.google.co.in/setprefs?sig=0_2dPaac0hw0oFwruErYLFtJ6SvLU%3D&amp;hl=kn&amp;source=homepage" data-ved="0ahUKEwjdwafN6M3SAhVFjZQKHY34CkcQ2ZgBCAs">&#3221;&#3240;&#3277;&#3240;&#3233;</a>  <a href="http://www.google.co.in/setprefs?sig=0_2dPaac0hw0oFwruErYLFtJ6SvLU%3D&amp;hl=ml&amp;source=homepage" data-ved="0ahUKEwjdwafN6M3SAhVFjZQKHY34CkcQ2ZgBCAw">&#3374;&#3378;&#3375;&#3390;&#3379;&#3330;</a>  <a href="http://www.google.co.in/setprefs?sig=0_2dPaac0hw0oFwruErYLFtJ6SvLU%3D&amp;hl=pa&amp;source=homepage" data-ved="0ahUKEwjdwafN6M3SAhVFjZQKHY34CkcQ2ZgBCA0">&#2602;&#2672;&#2588;&#2622;&#2604;&#2624;</a> </div></div></div><span id="footer"><div style="font-size:10pt"><div style="margin:19px auto;text-align:center" id="fll"><a href="/intl/en/ads/">Advertising\xa0Programs</a><a href="http://www.google.co.in/services/">Business Solutions</a><a href="https://plus.google.com/104205742743787718296" rel="publisher">+Google</a><a href="/intl/en/about.html">About Google</a><a href="http://www.google.co.in/setprefdomain?prefdom=US&amp;sig=__B9gehYn9c5C_OwKMovdTO0SP1-k%3D" id="fehl">Google.com</a></div></div><p style="color:#767676;font-size:8pt">&copy; 2017 - <a href="/intl/en/policies/privacy/">Privacy</a> - <a href="/intl/en/policies/terms/">Terms</a></p></span></center><script>(function(){window.google.cdo={height:0,width:0};(function(){var a=window.innerWidth,b=window.innerHeight;if(!a||!b)var c=window.document,d="CSS1Compat"==c.compatMode?c.documentElement:c.body,a=d.clientWidth,b=d.clientHeight;a&&b&&(a!=google.cdo.width||b!=google.cdo.height)&&google.log("","","/client_204?&atyp=i&biw="+a+"&bih="+b+"&ei="+google.kEI);}).call(this);})();</script><div id="xjsd"></div><div id="xjsi"><script>(function(){function c(b){window.setTimeout(function(){var a=document.createElement("script");a.src=b;document.getElementById("xjsd").appendChild(a)},0)}google.dljp=function(b,a){google.xjsu=b;c(a)};google.dlj=c;}).call(this);(function(){window.google.xjsrm=[];})();if(google.y)google.y.first=[];if(!google.xjs){window._=window._||{};window._._DumpException=function(e){throw e};if(google.timers&&google.timers.load.t){google.timers.load.t.xjsls=new Date().getTime();}google.dljp(\'/xjs/_/js/k\\x3dxjs.hp.en_US.qWyNDPmYk0M.O/m\\x3dsb_he,d/am\\x3dgA/rt\\x3dj/d\\x3d1/t\\x3dzcms/rs\\x3dACT90oGnFhl0DdMldEWigofsiaiPa94Ciw\',\'/xjs/_/js/k\\x3dxjs.hp.en_US.qWyNDPmYk0M.O/m\\x3dsb_he,d/am\\x3dgA/rt\\x3dj/d\\x3d1/t\\x3dzcms/rs\\x3dACT90oGnFhl0DdMldEWigofsiaiPa94Ciw\');google.xjs=1;}google.pmc={"sb_he":{"agen":true,"cgen":true,"client":"heirloom-hp","dh":true,"dhqt":true,"ds":"","fl":true,"host":"google.co.in","isbh":28,"jam":0,"jsonp":true,"msgs":{"cibl":"Clear Search","dym":"Did you mean:","lcky":"I\\u0026#39;m Feeling Lucky","lml":"Learn more","oskt":"Input tools","psrc":"This search was removed from your \\u003Ca href=\\"/history\\"\\u003EWeb History\\u003C/a\\u003E","psrl":"Remove","sbit":"Search by image","srch":"Google Search"},"nds":true,"ovr":{},"pq":"","refpd":true,"rfs":[],"sbpl":24,"sbpr":24,"scd":10,"sce":5,"stok":"KbFEGuirMG9kgqN_AFytD43NvbE"},"d":{},"YFCs/g":{}};google.y.first.push(function(){if(google.med){google.med(\'init\');google.initHistory();google.med(\'history\');}});if(google.j&&google.j.en&&google.j.xi){window.setTimeout(google.j.xi,0);}'
b'</script></div></body></html>'
>>> 
============= RESTART: C:/Users/CEC-07/Desktop/pooja/file/url.py =============
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en-IN"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script>(function(){window.google={kEI:'WJjDWKjZA8TN0ASfyKWoDA',kEXPI:'1352992,3700290,3700347,3700405,4028875,4029815,4031109,4032677,4036527,4038012,4039268,4043492,4045841,4048347,4063220,4065786,4066195,4072364,4072775,4073405,4075963,4076096,4076999,4077777,4078760,4079444,4079601,4079894,4081038,4081164,4083030,4085336,4085682,4088341,4090550,4090806,4090877,4090893,4092183,4092475,4092479,4092897,4092934,4093808,4093948,4094251,4094544,4094769,4095381,4095787,4095998,4096052,4096323,4096742,4097153,4097204,4097517,4097922,4097929,4097951,4098047,4098733,4098740,4098752,4099381,4099913,4100380,4100671,4100826,4101151,4101224,4101229,4101317,4101369,4101644,4101651,4101681,4102020,4102090,4102096,4102099,4102658,8503585,8505259,8506340,8507181,8507380,8507420,8507940,8508229,8508607,8508931,8509037,8509373,8509871,8510787,10200083,19001698,19001893,19001897,41027342',authuser:0,kscs:'c9c918f0_24'};google.kHL='en-IN';})();(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||google.kEI};google.getLEI=function(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b};google.https=function(){return"https:"==window.location.protocol};google.ml=function(){return null};google.wl=function(a,b){try{google.ml(Error(a),!1,b)}catch(c){}};google.time=function(){return(new Date).getTime()};google.log=function(a,b,c,d,g){a=google.logUrl(a,b,c,d,g);if(""!=a){b=new Image;var e=google.lc,f=google.li;e[f]=b;b.onerror=b.onload=b.onabort=function(){delete e[f]};window.google&&window.google.vel&&window.google.vel.lu&&window.google.vel.lu(a);b.src=a;google.li=f+1}};google.logUrl=function(a,b,c,d,g){var e="",f=google.ls||"";c||-1!=b.search("&ei=")||(e="&ei="+google.getEI(d),-1==b.search("&lei=")&&(d=google.getLEI(d))&&(e+="&lei="+d));a=c||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+b+e+f+"&zx="+google.time();/^http:/i.test(a)&&google.https()&&(google.ml(Error("a"),!1,{src:a,glmm:1}),a="");return a};google.y={};google.x=function(a,b){google.y[a.id]=[a,b];return!1};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};}).call(this);var a=window.location,b=a.href.indexOf("#");if(0<=b){var c=a.href.substring(b+1);/(^|&)q=/.test(c)&&-1==c.indexOf("#")&&a.replace("/search?"+c.replace(/(^|&)fp=[^&]*/g,"")+"&cad=h")};</script><style>#gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}
</style><style>body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#36c}.q{color:#00c}.ts td{padding:0}.ts{border-collapse:collapse}em{font-weight:bold;font-style:normal}.lst{height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0 4px;margin-left:4px}input{font-family:inherit}a.gb1,a.gb2,a.gb3,a.gb4{color:#11c !important}body{background:#fff;color:black}a{color:#11c;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#36c}a:visited{color:#551a8b}a.gb1,a.gb4{text-decoration:underline}a.gb3:hover{text-decoration:none}#ghead a.gb2:hover{color:#fff !important}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px}.lsbb{background:#eee;border:solid 1px;border-color:#ccc #999 #999 #ccc;height:30px}.lsbb{display:block}.ftl,#fll a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;border:none;color:#000;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#ccc}.lst:focus{outline:none}</style><script></script><link href="/images/branding/product/ico/googleg_lodp.ico" rel="shortcut icon"></head><body bgcolor="#fff"><script>(function(){var src='/images/nav_logo229.png';var iesg=false;document.body.onload = function(){window.n && window.n();if (document.images){new Image().src=src;}
if (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}
}
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/file/url.py", line 10, in <module>
    internet()
  File "C:/Users/CEC-07/Desktop/pooja/file/url.py", line 8, in internet
    l2 = l.decode("utf-8")
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 5206: invalid start byte
>>> 
============= RESTART: C:/Users/CEC-07/Desktop/pooja/file/url.py =============
<script>window.googleJavaScriptRedirect=1</script><script>var n={navigateTo:function(b,a,d){if(b!=a&&b.google){if(b.google.r){b.google.r=0;b.location.href=d;a.location.replace("about:blank");}}else{a.location.replace(d);}}};n.navigateTo(window.parent,window,"https://www.youtube.com/");
</script><noscript><META http-equiv="refresh" content="0;URL='https://www.youtube.com/'"></noscript>
>>> 
============= RESTART: C:/Users/CEC-07/Desktop/pooja/file/url.py =============
<!DOCTYPE html><html lang="en" data-cast-api-enabled="true"><head><style name="www-roboto">@font-face{font-family:'Roboto';font-style:normal;font-weight:500;src:local('Roboto Medium'),local('Roboto-Medium'),url(//fonts.gstatic.com/s/roboto/v15/RxZJdnzeo3R5zSexge8UUaCWcynf_cDxXwCLxiixG1c.ttf)format('truetype');}@font-face{font-family:'Roboto';font-style:normal;font-weight:400;src:local('Roboto Regular'),local('Roboto-Regular'),url(//fonts.gstatic.com/s/roboto/v15/zN7GBFwfMP4uA6AR0HCoLQ.ttf)format('truetype');}@font-face{font-family:'Roboto';font-style:italic;font-weight:400;src:local('Roboto Italic'),local('Roboto-Italic'),url(//fonts.gstatic.com/s/roboto/v15/W4wDsBUluyw0tK3tykhXEfesZW2xOQ-xsNqO47m55DA.ttf)format('truetype');}@font-face{font-family:'Roboto';font-style:italic;font-weight:500;src:local('Roboto Medium Italic'),local('Roboto-MediumItalic'),url(//fonts.gstatic.com/s/roboto/v15/OLffGBTaF0XFOW1gnuHF0Z0EAVxt0G0biEntp43Qt6E.ttf)format('truetype');}</style><script name="www-roboto">if (document.fonts && document.fonts.load) {document.fonts.load("400 10pt Roboto", "E");document.fonts.load("500 10pt Roboto", "E");}</script><script>var ytcsi = {gt: function(n) {n = (n || '') + 'data_';return ytcsi[n] || (ytcsi[n] = {tick: {},info: {}});},now: window.performance && window.performance.timing &&window.performance.now ? function() {return window.performance.timing.navigationStart + window.performance.now();} : function() {return (new Date()).getTime();},tick: function(l, t, n) {ticks = ytcsi.gt(n).tick;var v = t || ytcsi.now();if (ticks[l]) {ticks['_' + l] = (ticks['_' + l] || [ticks[l]]);ticks['_' + l].push(v);}ticks[l] = v;},info: function(k, v, n) {ytcsi.gt(n).info[k] = v;},setStart: function(s, t, n) {ytcsi.info('yt_sts', s, n);ytcsi.tick('_start', t, n);}};(function(w, d) {ytcsi.setStart('dhs', w.performance ? w.performance.timing.responseStart : null);var isPrerender = (d.visibilityState || d.webkitVisibilityState) == 'prerender';var vName = d.webkitVisibilityState ? 'webkitvisibilitychange' : 'visibilitychange';if (isPrerender) {ytcsi.info('prerender', 1);var startTick = function() {ytcsi.setStart('dhs');d.removeEventListener(vName, startTick);};d.addEventListener(vName, startTick, false);}if (d.addEventListener) {d.addEventListener(vName, function() {ytcsi.tick('vc');}, false);}var slt = function(el, t) {setTimeout(function() {var n = ytcsi.now();el.loadTime = n;if (el.slt) {el.slt();}}, t);};w.__ytRIL = function(el) {if (!el.getAttribute('data-thumb')) {if (w.requestAnimationFrame) {w.requestAnimationFrame(function() {slt(el, 0);});} else {slt(el, 16);}}};})(window, document);</script><script>var ytcfg = {d: function() {return (window.yt && yt.config_) || ytcfg.data_ || (ytcfg.data_ = {});},get: function(k, o) {return (k in ytcfg.d()) ? ytcfg.d()[k] : o;},set: function() {var a = arguments;if (a.length > 1) {ytcfg.d()[a[0]] = a[1];} else {for (var k in a[0]) {ytcfg.d()[k] = a[0][k];}}}};</script>





<script>
(function(){var b={a:"content-snap-width-1",b:"content-snap-width-2",c:"content-snap-width-3"};function f(){var a=[],c;for(c in b)a.push(b[c]);return a}
function h(a){var c=f().concat(["guide-pinned","show-guide"]),e=c.length,g=[];a.replace(/\S+/g,function(a){for(var d=0;d<e;d++)if(a==c[d])return;g.push(a)});
return g}
;function k(a,c,e){var g=document.getElementsByTagName("html")[0],d=h(g.className);a&&1251<=(window.innerWidth||document.documentElement.clientWidth)&&(d.push("guide-pinned"),c&&d.push("show-guide"));e&&(e=(window.innerWidth||document.documentElement.clientWidth)-21-50,1251<=(window.innerWidth||document.documentElement.clientWidth)&&a&&c&&(e-=230),d.push(1262<=e?"content-snap-width-3":1056<=e?"content-snap-width-2":"content-snap-width-1"));g.className=d.join(" ")}
var l=["yt","www","masthead","sizing","runBeforeBodyIsReady"],m=this;l[0]in m||!m.execScript||m.execScript("var "+l[0]);for(var n;l.length&&(n=l.shift());)l.length||void 0===k?m[n]&&m[n]!==Object.prototype[n]?m=m[n]:m=m[n]={}:m[n]=k;}).call(this);

try {window.ytbuffer = {};ytbuffer.handleClick = function(e) {var element = e.target || e.srcElement;while (element.parentElement) {if (/(^| )yt-can-buffer( |$)/.test(element.className)) {window.ytbuffer = {bufferedClick: e};element.className += ' yt-is-buffered';break;}element = element.parentElement;}};if (document.addEventListener) {document.addEventListener('click', ytbuffer.handleClick);} else {document.attachEvent('onclick', ytbuffer.handleClick);}} catch(e) {}

yt.www.masthead.sizing.runBeforeBodyIsReady(true,true,true);
</script>

<script src="/yts/jsbin/scheduler-vfl166vaM/scheduler.js" type="text/javascript" name="scheduler/scheduler"></script>



<link rel="stylesheet" href="/yts/cssbin/www-core-vflb9kFrb.css" name="www-core">
<link rel="stylesheet" href="/yts/cssbin/www-spacecast-vflvydAHe.css" name="www-spacecast">
<link rel="stylesheet" href="/yts/cssbin/www-home-c4-vflRkK6kq.css" name="www-home-c4">

<link rel="stylesheet" href="/yts/cssbin/www-pageframe-vflnlJjDX.css" name="www-pageframe">
<link rel="stylesheet" href="/yts/cssbin/www-guide-vflzcam_P.css" name="www-guide">


<title>YouTube</title><link rel="canonical" href="https://www.youtube.com/"><link rel="alternate" media="handheld" href="https://m.youtube.com/"><link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.youtube.com/"><meta name="description" content="Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube."><meta name="keywords" content="video, sharing, camera phone, video phone, free, upload"><link rel="manifest" href="/manifest.json"><link rel="search" type="application/opensearchdescription+xml" href="https://www.youtube.com/opensearch?locale=en_US" title="YouTube Video Search"><link rel="shortcut icon" href="https://s.ytimg.com/yts/img/favicon-vflz7uhzw.ico" type="image/x-icon">     <link rel="icon" href="/yts/img/favicon_32-vfl8NGn4k.png" sizes="32x32"><link rel="icon" href="/yts/img/favicon_48-vfl1s0rGh.png" sizes="48x48"><link rel="icon" href="/yts/img/favicon_96-vfldSA3ca.png" sizes="96x96"><link rel="icon" href="/yts/img/favicon_144-vflWmzoXw.png" sizes="144x144"><meta name="theme-color" content="#e62117">  <meta property="og:image" content="/yts/img/yt_1200-vfl4C3T0K.png">
<meta property="fb:app_id" content="87741124305">
<link rel="publisher" href="https://plus.google.com/115229808208707341778">
<link rel="alternate" href="android-app://com.google.android.youtube/http/www.youtube.com/">
<link rel="alternate" href="ios-app://544007664/vnd.youtube/www.youtube.com/">
<style>.yt-uix-button-primary, .yt-uix-button-primary[disabled], .yt-uix-button-primary[disabled]:hover, .yt-uix-button-primary[disabled]:active, .yt-uix-button-primary[disabled]:focus { background-color: #167ac6; }</style></head>
<body dir="ltr" id="body" class="  ltr    exp-responsive exp-scrollable-guide exp-search-big-thumbs exp-search-big-thumbs246 exp-search-font-18 exp-wn-big-thumbs exp-wn-big-thumbs-v3 exp-wn-font-14   site-center-aligned site-as-giant-card guide-pinning-enabled    visibility-logging-enabled   not-nirvana-dogfood  not-yt-legacy-css    flex-width-enabled      flex-width-enabled-snap    delayed-frame-styles-not-in  " data-spf-name="other">

<div id="early-body"></div>
<div id="body-container"><div id="a11y-announcements-container" role="alert"><div id="a11y-announcements-message"></div></div><form name="logoutForm" method="POST" action="/logout"><input type="hidden" name="action_logout" value="1"></form><div id="masthead-positioner">  <div id="ticker-content">


</div>
<div id="yt-masthead-container" class="clearfix yt-base-gutter">  <button id="a11y-skip-nav" class="skip-nav" data-target-id="main" tabindex="3">
Skip navigation
</button>
<div id="yt-masthead"><div class="yt-masthead-logo-container ">  <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-text yt-uix-button-empty yt-uix-button-has-icon appbar-guide-toggle appbar-guide-clickable-ancestor" type="button" onclick=";return false;" id="appbar-guide-button" aria-label="Guide" aria-controls="appbar-guide-menu"><span class="yt-uix-button-icon-wrapper"><span class="yt-uix-button-icon yt-uix-button-icon-appbar-guide yt-sprite"></span></span></button>
<div id="appbar-main-guide-notification-container"></div>
<span id="yt-masthead-logo-fragment"><a href="/" class="masthead-logo-renderer yt-uix-sessionlink      spf-link " data-sessionlink="itct=CAUQsV4iEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4"  id="logo-container" title="YouTube Home">  <span class="logo masthead-logo-renderer-logo yt-sprite" title="YouTube Home"></span>
<span class="content-region">IN</span></a></span></div><div id="yt-masthead-signin"><a href="//www.youtube.com/upload" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-opacity yt-uix-button-size-default yt-uix-button-has-icon yt-uix-tooltip yt-uix-button-empty" data-sessionlink="ei=EZnDWKSfFI_qoAOR9Zv4CA&amp;feature=mhsb" id="upload-btn" title="Upload"><span class="yt-uix-button-icon-wrapper"><span class="yt-uix-button-icon yt-uix-button-icon-material-upload yt-sprite"></span></span></a><div class="signin-container "><button class="yt-uix-button yt-uix-button-size-default yt-uix-button-primary" type="button" onclick=";window.location.href=this.getAttribute(&#39;href&#39;);return false;" role="link" href="https://accounts.google.com/ServiceLogin?service=youtube&amp;hl=en&amp;uilel=3&amp;passive=true&amp;continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fapp%3Ddesktop%26hl%3Den%26feature%3Dsign_in_button%26action_handle_signin%3Dtrue%26next%3D%252F"><span class="yt-uix-button-content">Sign in</span></button></div></div><div id="yt-masthead-content"><form id="masthead-search" class="  search-form consolidated-form  vve-check" action="/results" onsubmit="if (document.getElementById(&#39;masthead-search-term&#39;).value == &#39;&#39;) return false;" data-clicktracking="CAIQ7VAiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" data-visibility-tracking="CAIQ7VAiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4"><button class="yt-uix-button yt-uix-button-size-default yt-uix-button-default search-btn-component search-button" type="submit" onclick="if (document.getElementById(&#39;masthead-search-term&#39;).value == &#39;&#39;) return false; document.getElementById(&#39;masthead-search&#39;).submit(); return false;;return true;" dir="ltr" tabindex="2" id="search-btn"><span class="yt-uix-button-content">Search</span></button><div id="masthead-search-terms" class="masthead-search-terms-border" dir="ltr"><input id="masthead-search-term" autocomplete="off" autofocus onkeydown="if (!this.value &amp;&amp; (event.keyCode == 40 || event.keyCode == 32 || event.keyCode == 34)) {this.onkeydown = null; this.blur();}" class="search-term masthead-search-renderer-input yt-uix-form-input-bidi" name="search_query" value="" type="text" tabindex="1" placeholder="Search" title="Search" aria-label="Search"></div></form></div></div></div>
<div id="masthead-appbar-container" class="clearfix"><div id="masthead-appbar"><div id="appbar-content" class="">      <div id="appbar-nav" class="appbar-content-hidable">
<ul class="appbar-nav-menu"><li>    <h2 class="epic-nav-item-heading " aria-selected="true">
Home
</h2>
</li><li>    <a href="/feed/trending" class="yt-uix-button   spf-link yt-uix-sessionlink yt-uix-button-epic-nav-item yt-uix-button-size-default" data-sessionlink="ei=EZnDWKSfFI_qoAOR9Zv4CA&amp;ved=CK0BEMMtGAEiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" aria-selected="false"><span class="yt-uix-button-content">Trending</span></a>
</li></ul>  </div>

</div></div></div>

</div><div id="masthead-positioner-height-offset"></div><div id="page-container"><div id="page" class="  home     branded-page-v2-masthead-ad-header  clearfix"><div id="guide" class="yt-scrollbar">      <div id="appbar-guide-menu" class="appbar-menu appbar-guide-menu-layout appbar-guide-clickable-ancestor yt-uix-scroller yt-uix-tdl" role="navigation">
<div id="guide-container">
<div class="guide-module-content yt-scrollbar">
<ul class="guide-toplevel">
<li class="guide-section vve-check"
data-visibility-tracking="">
<div class="guide-item-container personal-item">

<ul class="guide-user-links yt-uix-tdl yt-box" role="menu">

<li class="vve-check guide-channel guide-notification-item overflowable-list-item " id="what_to_watch-guide-item"
data-visibility-tracking="" role="menuitem">

<a class="guide-item yt-uix-sessionlink yt-valign spf-link  guide-item-selected   "
href="/"
title="Home"
data-external-id="what_to_watch" data-serialized-endpoint="0qDduQEREg9GRXdoYXRfdG9fd2F0Y2g%3D" data-visibility-tracking="" data-sessionlink="ei=EZnDWKSfFI_qoAOR9Zv4CA&amp;feature=g-system&amp;ved=CJsBELUsGAAiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4"
>
<span class="yt-valign-container">
<span class="thumb guide-what-to-watch-icon yt-sprite"></span>
<span class="display-name  no-count">
<span>
Home
</span>
</span>
</span>
</a>

</li>


<li class="vve-check guide-channel guide-notification-item overflowable-list-item " id="trending-guide-item"
data-visibility-tracking="" role="menuitem">

<a class="guide-item yt-uix-sessionlink yt-valign spf-link    "
href="/feed/trending"
title="Trending"
data-external-id="trending" data-serialized-endpoint="0qDduQEMEgpGRXRyZW5kaW5n" data-visibility-tracking="" data-sessionlink="ei=EZnDWKSfFI_qoAOR9Zv4CA&amp;feature=g-trending&amp;ved=CJwBELUsGAEiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4"
>
<span class="yt-valign-container">
<span class="thumb guide-trending-icon yt-sprite"></span>
<span class="display-name  no-count">
<span>
Trending
</span>
</span>
</span>
</a>

</li>


<li class="vve-check guide-channel guide-notification-item overflowable-list-item " id="history-guide-item"
data-visibility-tracking="" role="menuitem">

<a class="guide-item yt-uix-sessionlink yt-valign spf-link    "
href="/feed/history"
title="History"
data-external-id="history" data-serialized-endpoint="0qDduQELEglGRWhpc3Rvcnk%3D" data-visibility-tracking="" data-sessionlink="ei=EZnDWKSfFI_qoAOR9Zv4CA&amp;feature=g-personal&amp;ved=CJ0BELUsGAIiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4"
>
<span class="yt-valign-container">
<span class="thumb guide-history-icon yt-sprite"></span>
<span class="display-name  no-count">
<span>
History
</span>
</span>
</span>
</a>

</li>

</ul>
</div>
<hr class="guide-section-separator">
</li>

<li class="guide-section vve-check"
data-visibility-tracking="">
<div class="guide-item-container personal-item">
<h3>
Best of YouTube
</h3>

<ul class="guide-user-links yt-uix-tdl yt-box" role="menu">

<li class="vve-check guide-channel guide-notification-item overflowable-list-item " id="UC-9-kyTW8ZkZNDHQJ6FgpwQ-guide-item"
data-visibility-tracking="" role="menuitem">

<a class="guide-item yt-uix-sessionlink yt-valign spf-link    "
href="/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ"
title="Music"
data-external-id="UC-9-kyTW8ZkZNDHQJ6FgpwQ" data-serialized-endpoint="0qDduQEaEhhVQy05LWt5VFc4WmtaTkRIUUo2Rmdwd1E%3D" data-visibility-tracking="" data-sessionlink="ei=EZnDWKSfFI_qoAOR9Zv4CA&amp;feature=g-channel&amp;ved=CJ8BELUsGAAiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4"
>
<span class="yt-valign-container">
<span class="thumb">  <span class="video-thumb  yt-thumb yt-thumb-20"
>
<span class="yt-thumb-square">
<span class="yt-thumb-clip">

<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="20" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="//i.ytimg.com/i/-9-kyTW8ZkZNDHQJ6FgpwQ/1.jpg" alt="" aria-hidden="true" width="20" data-ytimg="1" >

<span class="vertical-align"></span>
</span>
</span>
</span>
</span>
<span class="display-name  no-count">
<span>
Music
</span>
</span>
</span>
</a>

</li>


<li class="vve-check guide-channel guide-notification-item overflowable-list-item " id="UCEgdi0XIXXZ-qJOFPf4JSKw-guide-item"
data-visibility-tracking="" role="menuitem">

<a class="guide-item yt-uix-sessionlink yt-valign spf-link    "
href="/channel/UCEgdi0XIXXZ-qJOFPf4JSKw"
title="Sports"
data-external-id="UCEgdi0XIXXZ-qJOFPf4JSKw" data-serialized-endpoint="0qDduQEaEhhVQ0VnZGkwWElYWFotcUpPRlBmNEpTS3c%3D" data-visibility-tracking="" data-sessionlink="ei=EZnDWKSfFI_qoAOR9Zv4CA&amp;feature=g-channel&amp;ved=CKABELUsGAEiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4"
>
<span class="yt-valign-container">
<span class="thumb">  <span class="video-thumb  yt-thumb yt-thumb-20"
>
<span class="yt-thumb-square">
<span class="yt-thumb-clip">

<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="20" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="//i.ytimg.com/i/Egdi0XIXXZ-qJOFPf4JSKw/1.jpg" alt="" aria-hidden="true" width="20" data-ytimg="1" >

<span class="vertical-align"></span>
</span>
</span>
</span>
</span>
<span class="display-name  no-count">
<span>
Sports
</span>
</span>
</span>
</a>

</li>


<li class="vve-check guide-channel guide-notification-item overflowable-list-item " id="UCOpNcN46UbXVtpKMrmU4Abg-guide-item"
data-visibility-tracking="" role="menuitem">

<a class="guide-item yt-uix-sessionlink yt-valign spf-link    "
href="/channel/UCOpNcN46UbXVtpKMrmU4Abg"
title="Gaming"
data-external-id="UCOpNcN46UbXVtpKMrmU4Abg" data-serialized-endpoint="0qDduQEaEhhVQ09wTmNONDZVYlhWdHBLTXJtVTRBYmc%3D" data-visibility-tracking="" data-sessionlink="ei=EZnDWKSfFI_qoAOR9Zv4CA&amp;feature=g-channel&amp;ved=CKEBELUsGAIiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4"
>
<span class="yt-valign-container">
<span class="thumb">  <span class="video-thumb  yt-thumb yt-thumb-20"
>
<span class="yt-thumb-square">
<span class="yt-thumb-clip">

<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="20" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="//i.ytimg.com/i/OpNcN46UbXVtpKMrmU4Abg/1.jpg" alt="" aria-hidden="true" width="20" data-ytimg="1" >

<span class="vertical-align"></span>
</span>
</span>
</span>
</span>
<span class="display-name  no-count">
<span>
Gaming
</span>
</span>
</span>
</a>

</li>


<li class="vve-check guide-channel guide-notification-item overflowable-list-item " id="UClgRkhTL3_hImCAmdLfDE4g-guide-item"
data-visibility-tracking="" role="menuitem">

<a class="guide-item yt-uix-sessionlink yt-valign spf-link    "
href="/channel/UClgRkhTL3_hImCAmdLfDE4g"
title="Movies"
data-external-id="UClgRkhTL3_hImCAmdLfDE4g" data-serialized-endpoint="0qDduQEaEhhVQ2xnUmtoVEwzX2hJbUNBbWRMZkRFNGc%3D" data-visibility-tracking="" data-sessionlink="ei=EZnDWKSfFI_qoAOR9Zv4CA&amp;feature=g-channel&amp;ved=CKIBELUsGAMiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4"
>
<span class="yt-valign-container">
<span class="thumb">  <span class="video-thumb  yt-thumb yt-thumb-20"
>
<span class="yt-thumb-square">
<span class="yt-thumb-clip">

<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="20" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="//i.ytimg.com/i/lgRkhTL3_hImCAmdLfDE4g/1.jpg" alt="" aria-hidden="true" width="20" data-ytimg="1" >

<span class="vertical-align"></span>
</span>
</span>
</span>
</span>
<span class="display-name  no-count">
<span>
Movies
</span>
</span>
</span>
</a>

</li>


<li class="vve-check guide-channel guide-notification-item overflowable-list-item " id="UCY9Jh3SK0N1SAVJi-U--Rwg-guide-item"
data-visibility-tracking="" role="menuitem">

<a class="guide-item yt-uix-sessionlink yt-valign spf-link    "
href="/channel/UCY9Jh3SK0N1SAVJi-U--Rwg"
title="TV Shows"
data-external-id="UCY9Jh3SK0N1SAVJi-U--Rwg" data-serialized-endpoint="0qDduQEaEhhVQ1k5SmgzU0swTjFTQVZKaS1VLS1Sd2c%3D" data-visibility-tracking="" data-sessionlink="ei=EZnDWKSfFI_qoAOR9Zv4CA&amp;feature=g-channel&amp;ved=CKMBELUsGAQiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4"
>
<span class="yt-valign-container">
<span class="thumb">  <span class="video-thumb  yt-thumb yt-thumb-20"
>
<span class="yt-thumb-square">
<span class="yt-thumb-clip">

<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="20" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://yt3.ggpht.com/-QVxMDQG3JIQ/AAAAAAAAAAI/AAAAAAAAAAA/iuuJM6sO36E/s88-c-k-no-mo-rj-c0xffffff/photo.jpg" alt="" aria-hidden="true" width="20" data-ytimg="1" >

<span class="vertical-align"></span>
</span>
</span>
</span>
</span>
<span class="display-name  no-count">
<span>
TV Shows
</span>
</span>
</span>
</a>

</li>


<li class="vve-check guide-channel guide-notification-item overflowable-list-item " id="UCYfdidRxbB8Qhf0Nx7ioOYw-guide-item"
data-visibility-tracking="" role="menuitem">

<a class="guide-item yt-uix-sessionlink yt-valign spf-link    "
href="/channel/UCYfdidRxbB8Qhf0Nx7ioOYw"
title="News"
data-external-id="UCYfdidRxbB8Qhf0Nx7ioOYw" data-serialized-endpoint="0qDduQEaEhhVQ1lmZGlkUnhiQjhRaGYwTng3aW9PWXc%3D" data-visibility-tracking="" data-sessionlink="ei=EZnDWKSfFI_qoAOR9Zv4CA&amp;feature=g-channel&amp;ved=CKQBELUsGAUiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4"
>
<span class="yt-valign-container">
<span class="thumb">  <span class="video-thumb  yt-thumb yt-thumb-20"
>
<span class="yt-thumb-square">
<span class="yt-thumb-clip">

<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="20" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="//i.ytimg.com/i/YfdidRxbB8Qhf0Nx7ioOYw/1.jpg" alt="" aria-hidden="true" width="20" data-ytimg="1" >

<span class="vertical-align"></span>
</span>
</span>
</span>
</span>
<span class="display-name  no-count">
<span>
News
</span>
</span>
</span>
</a>

</li>


<li class="vve-check guide-channel guide-notification-item overflowable-list-item " id="UC4R8DWoMoI7CAwX8_LjQHig-guide-item"
data-visibility-tracking="" role="menuitem">

<a class="guide-item yt-uix-sessionlink yt-valign spf-link    "
href="/channel/UC4R8DWoMoI7CAwX8_LjQHig"
title="Live"
data-external-id="UC4R8DWoMoI7CAwX8_LjQHig" data-serialized-endpoint="0qDduQEaEhhVQzRSOERXb01vSTdDQXdYOF9MalFIaWc%3D" data-visibility-tracking="" data-sessionlink="ei=EZnDWKSfFI_qoAOR9Zv4CA&amp;feature=g-channel&amp;ved=CKUBELUsGAYiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4"
>
<span class="yt-valign-container">
<span class="thumb">  <span class="video-thumb  yt-thumb yt-thumb-20"
>
<span class="yt-thumb-square">
<span class="yt-thumb-clip">

<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="20" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="//i.ytimg.com/i/4R8DWoMoI7CAwX8_LjQHig/1.jpg" alt="" aria-hidden="true" width="20" data-ytimg="1" >

<span class="vertical-align"></span>
</span>
</span>
</span>
</span>
<span class="display-name  no-count">
<span>
Live
</span>
</span>
</span>
</a>

</li>


<li class="vve-check guide-channel guide-notification-item overflowable-list-item " id="UCvScgo6mAvbMEjszK4sSj6g-guide-item"
data-visibility-tracking="" role="menuitem">

<a class="guide-item yt-uix-sessionlink yt-valign spf-link    "
href="/channel/UCvScgo6mAvbMEjszK4sSj6g"
title="Spotlight"
data-external-id="UCvScgo6mAvbMEjszK4sSj6g" data-serialized-endpoint="0qDduQEaEhhVQ3ZTY2dvNm1BdmJNRWpzeks0c1NqNmc%3D" data-visibility-tracking="" data-sessionlink="ei=EZnDWKSfFI_qoAOR9Zv4CA&amp;feature=g-channel&amp;ved=CKYBELUsGAciEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4"
>
<span class="yt-valign-container">
<span class="thumb">  <span class="video-thumb  yt-thumb yt-thumb-20"
>
<span class="yt-thumb-square">
<span class="yt-thumb-clip">

<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="20" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://yt3.ggpht.com/-_fOHTgyA2Og/AAAAAAAAAAI/AAAAAAAAAAA/mrENVma0Tyc/s88-c-k-no-mo-rj-c0xffffff/photo.jpg" alt="" aria-hidden="true" width="20" data-ytimg="1" >

<span class="vertical-align"></span>
</span>
</span>
</span>
</span>
<span class="display-name  no-count">
<span>
Spotlight
</span>
</span>
</span>
</a>

</li>


<li class="vve-check guide-channel guide-notification-item overflowable-list-item " id="UCzuqhhs6NWbgTzMuM09WKDQ-guide-item"
data-visibility-tracking="" role="menuitem">

<a class="guide-item yt-uix-sessionlink yt-valign spf-link    "
href="/channel/UCzuqhhs6NWbgTzMuM09WKDQ"
title="360° Video"
data-external-id="UCzuqhhs6NWbgTzMuM09WKDQ" data-serialized-endpoint="0qDduQEaEhhVQ3p1cWhoczZOV2JnVHpNdU0wOVdLRFE%3D" data-visibility-tracking="" data-sessionlink="ei=EZnDWKSfFI_qoAOR9Zv4CA&amp;feature=g-channel&amp;ved=CKcBELUsGAgiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4"
>
<span class="yt-valign-container">
<span class="thumb">  <span class="video-thumb  yt-thumb yt-thumb-20"
>
<span class="yt-thumb-square">
<span class="yt-thumb-clip">

<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="20" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="//i.ytimg.com/i/zuqhhs6NWbgTzMuM09WKDQ/1.jpg" alt="" aria-hidden="true" width="20" data-ytimg="1" >

<span class="vertical-align"></span>
</span>
</span>
</span>
</span>
<span class="display-name  no-count">
<span>
360° Video
</span>
</span>
</span>
</a>

</li>

</ul>
</div>
<hr class="guide-section-separator">
</li>

<li class="guide-section vve-check"
data-visibility-tracking="">
<div class="guide-item-container personal-item">

<ul class="guide-user-links yt-uix-tdl yt-box" role="menu">

<li class="vve-check guide-channel guide-notification-item overflowable-list-item " id="guide_builder-guide-item"
data-visibility-tracking="" role="menuitem">

<a class="guide-item yt-uix-sessionlink yt-valign spf-nolink    "
href="/channels"
title="Browse channels"
data-external-id="guide_builder" data-serialized-endpoint="0qPduQECCAE%3D" data-visibility-tracking="" data-sessionlink="ei=EZnDWKSfFI_qoAOR9Zv4CA&amp;feature=g-manage&amp;ved=CKkBELUsGAAiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4"
>
<span class="yt-valign-container">
<span class="thumb guide-builder-icon yt-sprite"></span>
<span class="display-name  no-count">
<span>
Browse channels
</span>
</span>
</span>
</a>

</li>

</ul>
</div>
<hr class="guide-section-separator">
</li>

<li class="guide-section guide-header signup-promo">
<p>
Sign in now to see your channels and recommendations!
</p>
<div id="guide-builder-promo-buttons" class="signed-out clearfix">
<a href="https://accounts.google.com/ServiceLogin?service=youtube&amp;hl=en&amp;uilel=3&amp;passive=true&amp;continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fapp%3Ddesktop%26hl%3Den%26feature%3Dsign_in_promo%26action_handle_signin%3Dtrue%26next%3D%252F" class="yt-uix-button   yt-uix-sessionlink yt-uix-button-primary yt-uix-button-size-default" data-sessionlink="ei=EZnDWKSfFI_qoAOR9Zv4CA"><span class="yt-uix-button-content">Sign in</span></a>
</div>
</li>

</ul>
</div>

</div>
</div>
<div id="appbar-guide-notifications" class="hid">
<div id="appbar-guide-notification-watch-later-video-added">
<!--
<div class="appbar-guide-notification " role="alert"><span class="appbar-guide-notification-content-wrapper yt-valign"><span class="appbar-guide-notification-icon yt-sprite"></span><span class="appbar-guide-notification-text-content" >Added to Watch Later</span></span></div>
-->
</div>


<div id="appbar-guide-notification-watch-later-video-removed">
<!--
<div class="appbar-guide-notification " role="alert"><span class="appbar-guide-notification-content-wrapper yt-valign"><span class="appbar-guide-notification-icon yt-sprite"></span><span class="appbar-guide-notification-text-content" >Removed from Watch Later</span></span></div>
-->
</div>


<div id="appbar-guide-notification-subscription">
<!--
<div class="appbar-guide-notification " role="alert"><span class="appbar-guide-notification-content-wrapper yt-valign"><span class="appbar-guide-notification-icon yt-sprite"></span><span class="appbar-guide-notification-text-content" >Subscription added</span></span></div>
-->
</div>


<div id="appbar-guide-notification-unsubscription">
<!--
<div class="appbar-guide-notification " role="alert"><span class="appbar-guide-notification-content-wrapper yt-valign"><span class="appbar-guide-notification-icon yt-sprite"></span><span class="appbar-guide-notification-text-content" >Subscription removed</span></span></div>
-->
</div>


<div id="appbar-guide-notification-playlist-like">
<!--
<div class="appbar-guide-notification " role="alert"><span class="appbar-guide-notification-content-wrapper yt-valign"><span class="appbar-guide-notification-icon yt-sprite"></span><span class="appbar-guide-notification-text-content" >Saved to Playlists</span></span></div>
-->
</div>


<div id="appbar-guide-notification-playlist-unlike">
<!--
<div class="appbar-guide-notification " role="alert"><span class="appbar-guide-notification-content-wrapper yt-valign"><span class="appbar-guide-notification-icon yt-sprite"></span><span class="appbar-guide-notification-text-content" >Removed from Playlists</span></span></div>
-->
</div>


<div id="appbar-guide-notification-playlist-video-added">
<!--
<div class="appbar-guide-notification " role="alert"><span class="appbar-guide-notification-content-wrapper yt-valign"><span class="appbar-guide-notification-icon yt-sprite"></span><span class="appbar-guide-notification-text-content" >Added to playlist</span></span></div>
-->
</div>


<div id="appbar-guide-notification-playlist-video-removed">
<!--
<div class="appbar-guide-notification " role="alert"><span class="appbar-guide-notification-content-wrapper yt-valign"><span class="appbar-guide-notification-icon yt-sprite"></span><span class="appbar-guide-notification-text-content" >Removed from playlist</span></span></div>
-->
</div>


<div id="appbar-guide-notification-video-like">
<!--
<div class="appbar-guide-notification " role="alert"><span class="appbar-guide-notification-content-wrapper yt-valign"><span class="appbar-guide-notification-icon yt-sprite"></span><span class="appbar-guide-notification-text-content" >Added to Liked videos</span></span></div>
-->
</div>


<div id="appbar-guide-notification-video-unlike">
<!--
<div class="appbar-guide-notification " role="alert"><span class="appbar-guide-notification-content-wrapper yt-valign"><span class="appbar-guide-notification-icon yt-sprite"></span><span class="appbar-guide-notification-text-content" >Removed from Liked videos</span></span></div>
-->
</div>


<div id="appbar-guide-notification-event-reminder-set">
<!--
<div class="appbar-guide-notification " role="alert"><span class="appbar-guide-notification-content-wrapper yt-valign"><span class="appbar-guide-notification-icon yt-sprite"></span><span class="appbar-guide-notification-text-content" >You'll be reminded about this event</span></span></div>
-->
</div>


<div id="appbar-guide-notification-event-reminder-removed">
<!--
<div class="appbar-guide-notification " role="alert"><span class="appbar-guide-notification-content-wrapper yt-valign"><span class="appbar-guide-notification-icon yt-sprite"></span><span class="appbar-guide-notification-text-content" >Event reminder removed</span></span></div>
-->
</div>


</div>
<div id="appbar-guide-item-templates" class="hid">
<div id="appbar-guide-item-template-playlist">
<!--

<li class="vve-check guide-channel guide-notification-item overflowable-list-item show-insertion-notification " id="__ID__-guide-item"
data-visibility-tracking="" role="menuitem">

<a class="guide-item yt-uix-sessionlink yt-valign spf-nolink    "
href="__URL__"
title="__TITLE__"
data-external-id="__ID__" data-serialized-endpoint="" data-visibility-tracking="" data-sessionlink="ei=EZnDWKSfFI_qoAOR9Zv4CA&amp;feature=g-playlists"
>
<span class="yt-valign-container">
<span class="thumb guide-playlists-icon yt-sprite"></span>
<span class="display-name  no-count">
<span>
__TITLE__
</span>
</span>
</span>
</a>

<div class="appbar-guide-notification guide-item-insertion-notification" role="alert"><span class="appbar-guide-notification-content-wrapper yt-valign"><span class="appbar-guide-notification-icon yt-sprite"></span><span class="appbar-guide-notification-text-content" aria-label="Saved to Playlists">__NOTIFICATION_OVERLAY_MESSAGE__</span></span></div>
</li>

-->
</div>
<div id="appbar-guide-item-template-mix">
<!--

<li class="vve-check guide-channel guide-notification-item overflowable-list-item show-insertion-notification " id="__ID__-guide-item"
data-visibility-tracking="" role="menuitem">

<a class="guide-item yt-uix-sessionlink yt-valign spf-nolink    "
href="__URL__"
title="__TITLE__"
data-external-id="__ID__" data-serialized-endpoint="" data-visibility-tracking="" data-sessionlink="ei=EZnDWKSfFI_qoAOR9Zv4CA&amp;feature=g-playlists"
>
<span class="yt-valign-container">
<span class="thumb guide-mix-icon yt-sprite"></span>
<span class="display-name  no-count">
<span>
__TITLE__
</span>
</span>
</span>
</a>

<div class="appbar-guide-notification guide-item-insertion-notification" role="alert"><span class="appbar-guide-notification-content-wrapper yt-valign"><span class="appbar-guide-notification-icon yt-sprite"></span><span class="appbar-guide-notification-text-content" aria-label="Saved to Playlists">__NOTIFICATION_OVERLAY_MESSAGE__</span></span></div>
</li>

-->
</div>
<div id="appbar-guide-item-template-channel">
<!--

<li class="vve-check guide-channel guide-notification-item overflowable-list-item show-insertion-notification " id="__ID__-guide-item"
data-visibility-tracking="" role="menuitem">

<a class="guide-item yt-uix-sessionlink yt-valign spf-nolink    "
href="__URL__"
title="__TITLE__"
data-external-id="__ID__" data-serialized-endpoint="" data-visibility-tracking="" data-sessionlink="ei=EZnDWKSfFI_qoAOR9Zv4CA&amp;feature=g-channel"
>
<span class="yt-valign-container">
<span class="thumb">  <span class="video-thumb  yt-thumb yt-thumb-20"
>
<span class="yt-thumb-square">
<span class="yt-thumb-clip">

<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="20" src="__THUMBNAIL_URL__" alt="" aria-hidden="true" width="20" data-ytimg="1" >

<span class="vertical-align"></span>
</span>
</span>
</span>
</span>
<span class="display-name  no-count">
<span>
__TITLE__
</span>
</span>
</span>
</a>

<div class="appbar-guide-notification guide-item-insertion-notification" role="alert"><span class="appbar-guide-notification-content-wrapper yt-valign"><span class="appbar-guide-notification-icon yt-sprite"></span><span class="appbar-guide-notification-text-content" aria-label="Subscription added">__NOTIFICATION_OVERLAY_MESSAGE__</span></span></div>
</li>

-->
</div>

</div>

</div><div class="alerts-wrapper"><div id="alerts" class="content-alignment">
</div></div><div id="header">


<div id="ad_creative_1" class="ad-div mastad" style="z-index: 1;">
<script>(function() {var loaded = function() {return window.yt && yt.www && yt.www.feed && yt.www.feed.ui && yt.www.feed.ui.ads;};window.masthead_ad_creative_iframe_1_workaround = function() {if (loaded()) {yt.www.feed.ui.ads.workaroundIE(this);}};window.masthead_ad_creative_iframe_1_onload = function() {if (!loaded()) {setTimeout(masthead_ad_creative_iframe_1_onload, 50);return;}yt.www.feed.ui.ads.workaroundLoad();};})();</script>
<script>(function() {function tagMpuIframe() {var containerEl = document.getElementById('ad_creative_1');if (!containerEl) {return;}var iframeEl = document.createElement('iframe');var iframeSrc = "https:\/\/pubads.g.doubleclick.net\/gampad\/ads?ad_rule=0\u0026d_imp=1\u0026gdfp_req=1\u0026impl=ifr\u0026iu=%2F4061%2Fcom.ythome\u0026scp=dc_yt%3D1%26kbsg%3DHPIN170311%26kga%3D-1%26kgg%3D-1%26klg%3Den%26kmyd%3Dad_creative_1%26ssl%3D1%26ytdevice%3D1%26ytexp%3D9456628%252C9451827%252C9434289%252C9428398%252C9431012%252C9422596%252C9446054%252C9454909%252C9458240%252C9453077%252C9457114%252C9462855%252C9454899%252C9433221%252C9461757%252C9460350%252C9442074%252C9460073\u0026sz=970x250\u0026ytdevice=1" + '&correlator=' +Math.floor(Math.random() * 10000000000000000);iframeEl.id = 'ad_creative_iframe_1';iframeEl.width = '970';iframeEl.height = '250';iframeEl.style.cssText = 'z-index:1;';iframeEl.onload = window.masthead_ad_creative_iframe_1_onload;iframeEl.onmouseover = window.masthead_ad_creative_iframe_1_workaround;iframeEl.onfocus = window.masthead_ad_creative_iframe_1_workaround;iframeEl.setAttribute('allowFullScreen', '');iframeEl.scrolling = 'no';iframeEl.frameBorder = '0';containerEl.appendChild(iframeEl);iframeEl.src = iframeSrc;}tagMpuIframe();if (window.ytcsi) {window.ytcsi.info("yt_ad", "1", '');}})();</script>
</div>



<div id="ad_creative_expand_btn_1" class="masthead-ad-control open content-alignment masthead-ad-control-header hid">
<a onclick="masthead.expand_ad(); return false;" class="yt-valign">
<span class="yt-valign-container">Show ad</span>
<img src="/yts/img/pixel-vfl3z5WfW.gif" alt="" class="yt-valign-container">
</a>
</div>

</div><div id="player" class="  off-screen " role="complementary"><div id="theater-background" class="player-height"></div>  <div id="player-mole-container">
<div id="player-unavailable" class="  hid  ">

</div>

<div id="player-api" class="player-width player-height off-screen-target player-api" tabIndex="-1"></div>
<script>if (window.ytcsi) {window.ytcsi.tick("cfg", null, '');}</script>
<script>var ytplayer = ytplayer || {};ytplayer.config = {"url":"https:\/\/s.ytimg.com\/yts\/swfbin\/player-vflk-b1gu\/watch_as3.swf","args":{"innertube_api_key":"AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8","innertube_context_client_version":"1.20170307","player_error_log_fraction":"1.0","c":"WEB","fflags":"html5_min_upgrade_health=0\u0026enable_audio_cast=true\u0026html5_min_buffer_to_resume=6\u0026desktop_cleanup_companion_on_instream_begin=true\u0026autoplay_time=8000\u0026html5_tight_max_buffer_allowed_bandwidth_stddevs=0.0\u0026kids_enable_spain_lp=true\u0026disable_html5_size_check=true\u0026kids_enable_server_side_assets=true\u0026high_res_timestamps=true\u0026html5_request_sizing_multiplier=0.8\u0026html5_ad_no_buffer_abort_after_skippable=true\u0026html5_vp9_live_whitelist=false\u0026html5_local_max_byterate_lookahead=15\u0026enable_playlist_multi_season=true\u0026html5_min_vss_watchtime_to_cut_secs=0.0\u0026enable_pla_desktop_shelf=true\u0026html5_variability_no_discount_thresh=1.0\u0026kids_enable_latam_lp=true\u0026request_mpu_on_unfilled_ad_break=true\u0026html5_repredict_interval_secs=0.0\u0026html5_get_video_info_promiseajax=true\u0026html5_pause_manifest_ended=true\u0026android_min_bitrate_kbs_sd=200\u0026android_enable_thumbnail_overlay_side_panel=false\u0026html5_live_4k_more_buffer=true\u0026interaction_log_delayed_event_batch_size=200\u0026html5_tight_max_buffer_allowed_impaired_time=0.0\u0026enable_live_state_auth=true\u0026html5_report_conn=true\u0026playready_on_borg=true\u0026html5_spherical_bicubic_mode=0\u0026desktop_fsi_promo=style_masthead_ad\u0026doubleclick_gpt_retagging=true\u0026mweb_blacklist_progressive_chrome_mobile=true\u0026html5_trust_platform_bitrate_limits=true\u0026html5_live_pin_to_tail=true\u0026mweb_adsense_instreams_disabled_for_android_tablets=true\u0026html5_min_readbehind_secs=0\u0026flex_theater_mode=true\u0026html5_min_secs_between_format_selections=8.0\u0026html5_streaming_response_mediastream_rewrite=true\u0026mpu_visible_threshold_count=2\u0026html5_live_disable_dg_pacing=true\u0026kids_enable_columbia_lp=true\u0026enable_mweb_ypc_promotion_renderer=true\u0026chrome_promo_enabled=true\u0026send_html5_api_stats_ads_abandon=true\u0026log_it_display_tree=true\u0026html5_min_readbehind_cap_secs=0\u0026html5_enable_embedded_player_visibility_signals=true\u0026dynamic_ad_break_pause_threshold_sec=0\u0026html5_idle_time_msec=0\u0026log_js_exceptions_fraction=0.20\u0026html5_request_size_min_secs=0.0\u0026ad_video_end_renderer_duration_milliseconds=7000\u0026html5_max_readahead_bandwidth_cap=0\u0026disable_html5_cast_hdcp_filter=true\u0026king_crimson_player=false\u0026html5_audio_preload_duration=2.0\u0026ios_disable_notification_preprompt=true\u0026lugash_header_by_service=true\u0026html5_retry_media_element_errors_delay=0\u0026html5_long_term_bandwidth_window_size=0\u0026html5_background_cap_idle_secs=60\u0026android_min_bitrate_kbs_hd=200\u0026use_fast_fade_in_0s=true\u0026pla_shelf_hovercard=true\u0026html5_max_buffer_duration=0\u0026king_crimson_player_redux=true\u0026live_chunk_readahead=3\u0026kids_enable_privacy_notice=true\u0026html5_background_quality_cap=360\u0026dash_manifest_version=4\u0026live_readahead_seconds_multiplier=0.8\u0026html5_post_interrupt_readahead=0\u0026json_serialize_shut_off=true\u0026enable_android_encoder_constant_bitrate=true\u0026html5_allowable_liveness_drift_chunks=2\u0026enable_fmp4_defrag=true\u0026dynamic_ad_break_seek_threshold_sec=0\u0026yto_feature_hub_channel=false\u0026html5_min_startup_smooth_target=0.0\u0026html5_bandwidth_window_size=0\u0026mweb_pu_android_chrome_54_above=true\u0026html5_reseek_on_infinite_buffer=true\u0026sidebar_renderers=true\u0026yt_unlimited_pts_skip_ads_promo_desktop_always=true\u0026variable_load_timeout_ms=0\u0026disable_mediasession=true\u0026html5_variability_full_discount_thresh=3.0\u0026html5_connect_timeout_secs=7.0\u0026kids_enable_post_onboarding_red_flow=true\u0026stop_using_ima_sdk_gpt_request_activity=true\u0026html5_variability_discount=0.5\u0026html5_stale_dash_manifest_retry_factor=1.0\u0026html5_max_buffer_health_for_downgrade=0\u0026polymer_report_missing_web_navigation_endpoint=false\u0026html5_multicam=true\u0026fixed_padding_skip_button=true\u0026ios_notifications_disabled_subs_tab_promoted_item_promo=true\u0026feeds_on_innertube=true\u0026lugash_header_warmup=true\u0026enable_ccs_buy_flow_for_chirp=true\u0026yto_enable_watch_offer_module=true\u0026html5_deadzone_multiplier=1.1\u0026launch_new_wallet_api=true\u0026show_countdown_on_bumper=true\u0026html5_default_quality_cap=0\u0026ios_enable_mixin_accessibility_custom_actions=true\u0026html5_max_vss_watchtime_ratio=0.0\u0026enable_offer_restricts_for_watch_page_offers=true\u0026html5_new_preloading=true\u0026html5_throttle_rate=0.0\u0026enable_yt_music_lp=true\u0026html5_strip_emsg=true\u0026html5_burst_less_for_no_bw_data=true\u0026html5_get_video_info_timeout_ms=0\u0026html5_use_adaptive_live_readahead=true\u0026html5_timeupdate_readystate_check=true\u0026website_actions_throttle_percentage=1.0\u0026html5_idle_preload_secs=1\u0026spherical_on_android_iframe=true\u0026html5_progressive_signature_reload=true\u0026disable_search_mpu=true\u0026vss_dni_delayping=0\u0026enable_red_carpet_p13n_shelves=true\u0026html5_max_av_sync_drift=50\u0026use_new_skip_icon=true\u0026sdk_wrapper_levels_allowed=0\u0026yto_enable_ytr_promo_refresh_assets=true\u0026show_thumbnail_on_standard=true\u0026enable_mrm_channel_approve=true\u0026legacy_autoplay_flag=true\u0026html5_playing_event_buffer_underrun=true\u0026yto_enable_unlimited_landing_page_yto_features=true\u0026ad_duration_threshold_for_showing_endcap_seconds=15\u0026enable_get_offers_for_item_list_for_get_cart=true\u0026disable_new_pause_state3=true\u0026html5_check_for_reseek=true\u0026kids_enable_brazil_lp=true\u0026kids_enable_terms_servlet=true\u0026disable_html5_manifest_namespace=true\u0026html5_always_reload_on_403=true\u0026forced_brand_precap_duration_ms=2000\u0026use_web_player_gestures=true\u0026enable_local_channel=true\u0026use_push_for_desktop_live_chat=true\u0026use_new_style=true\u0026html5_reduce_startup_rebuffers=true\u0026kids_enable_block_servlet=true\u0026kids_asset_theme=server_side_assets\u0026html5_serverside_biscotti_id_wait_ms=1000\u0026html5_adjust_effective_request_size=true\u0026native_controls_assume_media_volume=true\u0026rendering_is_optimized_scrolling_enabled=false\u0026html5_min_vss_watchtime_to_cut_secs_redux=0.0\u0026fix_gpt_pos_params=true\u0026music_tastebuilder_p13n=true","ssl":"1","host_language":"en","fexp":"9419452,9422596,9428398,9431012,9433221,9434046,9434289,9436843,9442074,9443436,9446054,9446364,9449034,9449243,9450059,9450862,9453077,9456362,9456640,9457141,9458230,9459457,9459959,9460073,9460160,9461561,9461757,9461807,9461887,9462013,9462016,9462191,9463496,9464098,9464547,9464642,9464791,9465068,9465534,9465639,9465797,9465925,9465974,9466112","hl":"en_US","apiary_host_firstparty":"","cr":"IN","apiary_host":"","autoplay":"0","cver":"1.20170307","enablejsapi":"1","gapi_hint_params":"m;\/_\/scs\/abc-static\/_\/js\/k=gapi.gapi.en.-QXB_U8R8Eg.O\/m=__features__\/rt=j\/d=1\/rs=AHpOoo8PUrmM-10GgMhjxf52iM2kLRUicg","innertube_api_version":"v1"},"url_v8":"https:\/\/s.ytimg.com\/yts\/swfbin\/player-vflk-b1gu\/cps.swf","params":{"allowfullscreen":"true","allowscriptaccess":"always","bgcolor":"#000000"},"attrs":{"id":"movie_player"},"sts":17229,"html5":true,"messages":{"player_fallback":["Adobe Flash Player or an HTML5 supported browser is required for video playback.\u003cbr\u003e\u003ca href=\"https:\/\/get.adobe.com\/flashplayer\/\"\u003eGet the latest Flash Player \u003c\/a\u003e\u003cbr\u003e\u003ca href=\"\/html5\"\u003eLearn more about upgrading to an HTML5 browser\u003c\/a\u003e"]},"url_v9as2":"","min_version":"8.0.0","assets":{"css":"\/yts\/cssbin\/www-player-vflNfFvAf.css","js":"\/yts\/jsbin\/player-en_US-vflOnuOF-\/base.js"}};ytplayer.load = function() {yt.player.Application.create("player-api", ytplayer.config);ytplayer.config.loaded = true;};</script>


<div id="watch-queue-mole" class="video-mole mole-collapsed hid"><div id="watch-queue" class="watch-playlist player-height"><div class="main-content"><div class="watch-queue-header"><div class="watch-queue-info"><div class="watch-queue-info-icon"><span class="tv-queue-list-icon yt-sprite"></span></div><h3 class="watch-queue-title">Watch Queue</h3><h3 class="tv-queue-title">Queue</h3><span class="tv-queue-details"></span></div><div class="watch-queue-control-bar control-bar-button"><div class="watch-queue-mole-info"><div class="watch-queue-control-bar-icon"><span class="watch-queue-icon yt-sprite"></span></div><div class="watch-queue-title-container"><span class="watch-queue-count"></span><span class="watch-queue-title">Watch Queue</span><span class="tv-queue-title">Queue</span></div></div>  <span class="dark-overflow-action-menu">


<button type="button" aria-label="Actions for the queue" onclick=";return false;" aria-haspopup="true" class="flip control-bar-button yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" aria-expanded="false" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid" role="menu" aria-haspopup="true"><li role="menuitem"><span class="watch-queue-menu-choice overflow-menu-choice yt-uix-button-menu-item" onclick=";return false;" data-action="remove-all" >Remove all</span></li><li role="menuitem"><span class="watch-queue-menu-choice overflow-menu-choice yt-uix-button-menu-item" onclick=";return false;" data-action="disconnect" >Disconnect</span></li></ul></button>
</span>
<div class="watch-queue-controls">
<button class="yt-uix-button yt-uix-button-size-default yt-uix-button-empty yt-uix-button-has-icon control-bar-button prev-watch-queue-button yt-uix-button-opacity yt-uix-tooltip yt-uix-tooltip" type="button" onclick=";return false;" title="Previous video"><span class="yt-uix-button-icon-wrapper"><span class="yt-uix-button-icon yt-uix-button-icon-watch-queue-prev yt-sprite"></span></span></button>

<button class="yt-uix-button yt-uix-button-size-default yt-uix-button-empty yt-uix-button-has-icon control-bar-button play-watch-queue-button yt-uix-button-opacity yt-uix-tooltip yt-uix-tooltip" type="button" onclick=";return false;" title="Play"><span class="yt-uix-button-icon-wrapper"><span class="yt-uix-button-icon yt-uix-button-icon-watch-queue-play yt-sprite"></span></span></button>

<button class="yt-uix-button yt-uix-button-size-default yt-uix-button-empty yt-uix-button-has-icon control-bar-button pause-watch-queue-button yt-uix-button-opacity yt-uix-tooltip hid yt-uix-tooltip" type="button" onclick=";return false;" title="Pause"><span class="yt-uix-button-icon-wrapper"><span class="yt-uix-button-icon yt-uix-button-icon-watch-queue-pause yt-sprite"></span></span></button>

<button class="yt-uix-button yt-uix-button-size-default yt-uix-button-empty yt-uix-button-has-icon control-bar-button next-watch-queue-button yt-uix-button-opacity yt-uix-tooltip yt-uix-tooltip" type="button" onclick=";return false;" title="Next video"><span class="yt-uix-button-icon-wrapper"><span class="yt-uix-button-icon yt-uix-button-icon-watch-queue-next yt-sprite"></span></span></button>
</div>
</div><div class="autoplay-dismiss-bar fade-out"><span class="autoplay-dismiss-title-label">The next video is starting</span><span><button class="yt-uix-button yt-uix-button-size-default autoplay-dismiss-button yt-uix-tooltip" type="button" onclick=";return false;" title="stop"><span class="yt-uix-button-content">stop</span></button></span></div></div><div class="watch-queue-items-container yt-scrollbar-dark yt-scrollbar"><div class="yt-uix-scroller playlist-videos-list"><ol class="watch-queue-items-list" data-scroll-action="yt.www.watchqueue.loadThumbnails">  <p class="yt-spinner ">
<span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>

<span class="yt-spinner-message">
Loading...
</span>
</p>
</ol><div class="autoplay-control-container yt-uix-scroller-scroll-unit hid">  <div class="autoplay-control-bar">
<label class="autoplay-label" for=autoplay-toggle-id></label>
<label class="yt-uix-form-input-checkbox-container yt-uix-form-input-container yt-uix-form-input-paper-toggle-container "><input class="yt-uix-form-input-checkbox" type="checkbox" id="autoplay-toggle-id"/><div class="yt-uix-form-input-paper-toggle-bg yt-uix-form-input-paper-toggle-bar"></div><div class="yt-uix-form-input-paper-toggle-bg yt-uix-form-input-paper-toggle-button"></div></label>
</div>
</div><div class="up-next-item-container hid"></div></div></div></div>  <div class="hid">
<div id="watch-queue-title-msg">
Watch Queue
</div>

<div id="tv-queue-title-msg">Queue</div>

<div id="watch-queue-count-msg">
__count__/__total__
</div>

<div id="watch-queue-loading-template">
<!--
<p class="yt-spinner ">
<span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>

<span class="yt-spinner-message">
Loading...
</span>
</p>

-->
</div>
</div>
</div></div>

<div id="player-playlist" class="  hid  ">

</div>

</div>

<div class="clear"></div>
</div><div id="content" class="  content-alignment" role="main">


<div class="branded-page-v2-container branded-page-base-bold-titles branded-page-v2-container-flex-width branded-page-v2-secondary-column-hidden" >

<div class="branded-page-v2-col-container">
<div class="branded-page-v2-col-container-inner">
<div class="branded-page-v2-primary-col">
<div class="   yt-card  clearfix">
<div class="branded-page-v2-primary-col-header-container branded-page-v2-primary-column-content">

</div>
<div class="branded-page-v2-body branded-page-v2-primary-column-content" id="">
<div id="feed" class="">
<div id="feed-main-what_to_watch" class="individual-feed" data-feed-name="what_to_watch" data-feed-type="main">

<ol id="section-list-739917" class="section-list">
<li>
<ol id="item-section-529934" class="item-section">
<li><div class="feed-item-container browse-list-item-container yt-section-hover-container compact-shelf shelf-item branded-page-box vve-check clearfix " data-visibility-tracking="CIgBENwcGAAiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4="><div class="feed-item-dismissable"><div class="shelf-title-table"><div class="shelf-title-row"><h2 class="branded-page-module-title shelf-title-cell"><a href="/feed/trending" class="branded-page-module-title-link yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIgBENwcGAAiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" ><span class="branded-page-module-title-text">Trending</span></a></h2><div class="menu-container shelf-title-cell"></div></div></div><div class="compact-shelf yt-uix-shelfslider yt-uix-shelfslider-at-head"><div class="yt-uix-shelfslider-body yt-viewport"><ul class="yt-uix-shelfslider-list"><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="F1qFB4n9K6Q" data-visibility-tracking="CJgBEJQ1GAAiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5ApNf0z_igoa0X"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=F1qFB4n9K6Q" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CJgBEJQ1GAAiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="https://i.ytimg.com/vi/F1qFB4n9K6Q/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=r9yr0TUjqcV4ka4PdYnSahrjsUQ" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">6:41</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="F1qFB4n9K6Q"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="F1qFB4n9K6Q"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="F1qFB4n9K6Q"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="F1qFB4n9K6Q"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=F1qFB4n9K6Q" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CJgBEJQ1GAAiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA"  title="BB Ki Vines- | Group Study |" aria-describedby="description-id-769057" dir="ltr">BB Ki Vines- | Group Study |</a><span class="accessible-description" id="description-id-769057"> - Duration: 6:41.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/channel/UCqwUrj10mAEsqezcItqvwEw" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCqwUrj10mAEsqezcItqvwEw" data-sessionlink="itct=CJgBEJQ1GAAiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >BB Ki Vines</a>&nbsp;<span class="yt-uix-tooltip yt-channel-title-icon-verified yt-sprite" title="Verified"></span></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>3,757,013 views</li><li>1 day ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="cDpWv7MAHqM" data-visibility-tracking="CJcBEJQ1GAEiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5Ao72AmPvXlZ1w"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=cDpWv7MAHqM" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CJcBEJQ1GAEiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="https://i.ytimg.com/vi/cDpWv7MAHqM/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=GNDacJt2WzMpmWsO8M5MepOUkuY" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">14:36</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="cDpWv7MAHqM"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="cDpWv7MAHqM"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="cDpWv7MAHqM"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="cDpWv7MAHqM"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=cDpWv7MAHqM" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CJcBEJQ1GAEiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA"  title="Live: Exit Polls Result For UP, Punjab, Goa, And Uttarakhand Elections 2017" aria-describedby="description-id-216583" dir="ltr">Live: Exit Polls Result For UP, Punjab, Goa, And Uttarakhand Elections 2017</a><span class="accessible-description" id="description-id-216583"> - Duration: 14:36.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/aajtaktv" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCt4t-jeY85JegMlZ-E5UWtA" data-sessionlink="itct=CJcBEJQ1GAEiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >Aaj Tak</a>&nbsp;<span class="yt-uix-tooltip yt-channel-title-icon-verified yt-sprite" title="Verified"></span></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>150,202 views</li><li>1 day ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="jdLRjBhngJs" data-visibility-tracking="CJYBEJQ1GAIiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5Am4Gew8GxtOmNAQ=="><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=jdLRjBhngJs" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CJYBEJQ1GAIiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="https://i.ytimg.com/vi/jdLRjBhngJs/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=ewf2hUklBWVQEYca49awA-WANa0" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">10:43</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="jdLRjBhngJs"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="jdLRjBhngJs"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="jdLRjBhngJs"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="jdLRjBhngJs"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=jdLRjBhngJs" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CJYBEJQ1GAIiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA"  title="Dad At Your Office" aria-describedby="description-id-746203" dir="ltr">Dad At Your Office</a><span class="accessible-description" id="description-id-746203"> - Duration: 10:43.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/TheViralFeverVideos" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCNJcSUSzUeFm8W9P7UUlSeQ" data-sessionlink="itct=CJYBEJQ1GAIiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >TheViralFeverVideos</a>&nbsp;<span class="yt-uix-tooltip yt-channel-title-icon-verified yt-sprite" title="Verified"></span></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>364,240 views</li><li>18 hours ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="431fmhWOb-E" data-visibility-tracking="CJUBEJQ1GAMiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5A4d-5rKHz177jAQ=="><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=431fmhWOb-E" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CJUBEJQ1GAMiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="https://i.ytimg.com/vi/431fmhWOb-E/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=NIZEMY9CB8Tc7V3adD7OSFI8vII" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">20:32</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="431fmhWOb-E"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="431fmhWOb-E"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="431fmhWOb-E"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="431fmhWOb-E"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=431fmhWOb-E" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CJUBEJQ1GAMiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA"  title="Tuzyat Jeev Rangla Episode 138 9th march full hd (1080)p" aria-describedby="description-id-658787" dir="ltr">Tuzyat Jeev Rangla Episode 138 9th march full hd (1080)p</a><span class="accessible-description" id="description-id-658787"> - Duration: 20:32.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/channel/UCy3KHzuYrUHz6tu3MaGgrew" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCy3KHzuYrUHz6tu3MaGgrew" data-sessionlink="itct=CJUBEJQ1GAMiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >Zee Tube</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>78,528 views</li><li>1 day ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="37jSVy-9FOs" data-visibility-tracking="CJQBEJQ1GAQiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5A66n0_fLKtNzfAQ=="><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=37jSVy-9FOs" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CJQBEJQ1GAQiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="https://i.ytimg.com/vi/37jSVy-9FOs/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=jASwGd-2JTcgflmUCRdBWaGPY0s" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">3:22</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="37jSVy-9FOs"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="37jSVy-9FOs"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="37jSVy-9FOs"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="37jSVy-9FOs"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=37jSVy-9FOs" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CJQBEJQ1GAQiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA"  title="Rinku Bhabhi : Mere Husband Mujhko Piyar Nahin Karte | Sunil Grover" aria-describedby="description-id-37974" dir="ltr">Rinku Bhabhi : Mere Husband Mujhko Piyar Nahin Karte | Sunil Grover</a><span class="accessible-description" id="description-id-37974"> - Duration: 3:22.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/channel/UCWsHWYlQH94H9VE3q6gLQmA" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCWsHWYlQH94H9VE3q6gLQmA" data-sessionlink="itct=CJQBEJQ1GAQiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >Elephant Company</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>1,358,535 views</li><li>2 days ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="kwffx3OshHM" data-visibility-tracking="CJMBEJQ1GAUiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5A84iynff494OTAQ=="><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=kwffx3OshHM" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CJMBEJQ1GAUiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="https://i.ytimg.com/vi/kwffx3OshHM/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=Nkk3neAWmmKlU7HnghhisFtWsn0" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">7:37</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="kwffx3OshHM"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="kwffx3OshHM"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="kwffx3OshHM"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="kwffx3OshHM"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=kwffx3OshHM" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CJMBEJQ1GAUiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA"  title="Most Shocking LAST OVER in ODI Cricket  History" aria-describedby="description-id-795122" dir="ltr">Most Shocking LAST OVER in ODI Cricket  History</a><span class="accessible-description" id="description-id-795122"> - Duration: 7:37.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/channel/UCd7rEDpfcW5dWFwUkWKA0lQ" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCd7rEDpfcW5dWFwUkWKA0lQ" data-sessionlink="itct=CJMBEJQ1GAUiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >Euro Sport</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>502,696 views</li><li>1 day ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="Qq0B0NVKghA" data-visibility-tracking="CJIBEJQ1GAYiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5AkISqqo26wNZC"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=Qq0B0NVKghA" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CJIBEJQ1GAYiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/Qq0B0NVKghA/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=wEzLO9Q9wqLmEgnhqKtUkrF-ajE" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">1:30</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="Qq0B0NVKghA"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="Qq0B0NVKghA"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="Qq0B0NVKghA"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="Qq0B0NVKghA"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=Qq0B0NVKghA" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CJIBEJQ1GAYiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA"  title="Game of Thrones Season 7: Official Tease: Sigils" aria-describedby="description-id-250289" dir="ltr">Game of Thrones Season 7: Official Tease: Sigils</a><span class="accessible-description" id="description-id-250289"> - Duration: 1:30.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/GameofThrones" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCQzdMyuz0Lf4zo4uGcEujFw" data-sessionlink="itct=CJIBEJQ1GAYiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >GameofThrones</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>2,561,774 views</li><li>1 day ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="xZS21vNdUyQ" data-visibility-tracking="CJEBEJQ1GAciEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5ApKb1mu_arcrFAQ=="><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=xZS21vNdUyQ" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CJEBEJQ1GAciEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/xZS21vNdUyQ/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=ETNuZkxnrQgzI2BSL8HkUJv3N_Q" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">1:32</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="xZS21vNdUyQ"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="xZS21vNdUyQ"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="xZS21vNdUyQ"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="xZS21vNdUyQ"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=xZS21vNdUyQ" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CJEBEJQ1GAciEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA"  title="Kaatru Veliyidai - Trailer | Mani Ratnam, AR Rahman | Karthi, Aditi" aria-describedby="description-id-92969" dir="ltr">Kaatru Veliyidai - Trailer | Mani Ratnam, AR Rahman | Karthi, Aditi</a><span class="accessible-description" id="description-id-92969"> - Duration: 1:32.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/SonyMusicSouthVEVO" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCTNtRdBAiZtHP9w7JinzfUg" data-sessionlink="itct=CJEBEJQ1GAciEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >SonyMusicSouthVEVO</a>&nbsp;<span class="yt-uix-tooltip yt-channel-title-icon-verified yt-sprite" title="Verified"></span></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>1,387,600 views</li><li>1 day ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="5elgLOGyzBk" data-visibility-tracking="CJABEJQ1GAgiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5AmZjLjc6F2PTlAQ=="><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=5elgLOGyzBk" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CJABEJQ1GAgiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/5elgLOGyzBk/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=o8rVO9je5QAkfYo_UgrOTn1ZFug" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">4:33</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="5elgLOGyzBk"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="5elgLOGyzBk"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="5elgLOGyzBk"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="5elgLOGyzBk"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=5elgLOGyzBk" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CJABEJQ1GAgiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA"  title="Misbah Ul Haq Blast 6 Sixes In 6 Balls | Hongkong T20 Blitz 2017" aria-describedby="description-id-548876" dir="ltr">Misbah Ul Haq Blast 6 Sixes In 6 Balls | Hongkong T20 Blitz 2017</a><span class="accessible-description" id="description-id-548876"> - Duration: 4:33.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/channel/UCJIGuX67XfDFbX1RgeeDStg" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCJIGuX67XfDFbX1RgeeDStg" data-sessionlink="itct=CJABEJQ1GAgiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >Cricket De Zone HD</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>1,501,245 views</li><li>2 days ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="bo5zd82fh2w" data-visibility-tracking="CI8BEJQ1GAkiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5A7I7-7PzunMdu"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=bo5zd82fh2w" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CI8BEJQ1GAkiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/bo5zd82fh2w/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=zjMY9mxiyuzXbAO3_ohAvNzYAyU" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">7:41</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="bo5zd82fh2w"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="bo5zd82fh2w"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="bo5zd82fh2w"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="bo5zd82fh2w"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=bo5zd82fh2w" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CI8BEJQ1GAkiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA"  title="15 Deadliest Gangsters and Dons Of India And Unknown Facts About Them|in Hindi/Urdu|PointPlay PK" aria-describedby="description-id-252124" dir="ltr">15 Deadliest Gangsters and Dons Of India And Unknown Facts About Them|in Hindi/Urdu|PointPlay PK</a><span class="accessible-description" id="description-id-252124"> - Duration: 7:41.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/channel/UCv09wodVl6bHAf_Qj1V5YmQ" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCv09wodVl6bHAf_Qj1V5YmQ" data-sessionlink="itct=CI8BEJQ1GAkiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >PointPlay PK</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>286,433 views</li><li>1 day ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="1_mCqObGG4s" data-visibility-tracking="CI4BEJQ1GAoiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5Ai7eYto7V4PzXAQ=="><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=1_mCqObGG4s" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CI4BEJQ1GAoiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/1_mCqObGG4s/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=abDVNoDqAoKiiB8X5PbPByOn-Ic" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">5:45</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="1_mCqObGG4s"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="1_mCqObGG4s"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="1_mCqObGG4s"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="1_mCqObGG4s"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=1_mCqObGG4s" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CI4BEJQ1GAoiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA"  title="Dil Ka Haal | Full Video Song | Jubin Nautiyal | Shayadshah Shahebdin | New Indipop 2017" aria-describedby="description-id-255026" dir="ltr">Dil Ka Haal | Full Video Song | Jubin Nautiyal | Shayadshah Shahebdin | New Indipop 2017</a><span class="accessible-description" id="description-id-255026"> - Duration: 5:45.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/timesmusicindia" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCo07fumrTn1w4AxcU4j_uDw" data-sessionlink="itct=CI4BEJQ1GAoiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >Times Music</a>&nbsp;<span class="yt-uix-tooltip yt-channel-title-icon-verified yt-sprite" title="Verified"></span></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>359,983 views</li><li>20 hours ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="DHuM6C6EyXE" data-visibility-tracking="CI0BEJQ1GAsiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5A8ZKT9IKd470M"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=DHuM6C6EyXE" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CI0BEJQ1GAsiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/DHuM6C6EyXE/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=gxExUdBY771a-eGiooREJh8IFg0" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">2:21</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="DHuM6C6EyXE"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="DHuM6C6EyXE"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="DHuM6C6EyXE"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="DHuM6C6EyXE"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=DHuM6C6EyXE" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CI0BEJQ1GAsiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA"  title="Noor Official Trailer | Sonakshi Sinha | Sunhil Sippy | Releasing on 21 April 2017 | T-Series" aria-describedby="description-id-741916" dir="ltr">Noor Official Trailer | Sonakshi Sinha | Sunhil Sippy | Releasing on 21 April 2017 | T-Series</a><span class="accessible-description" id="description-id-741916"> - Duration: 2:21.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/tseries" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCq-Fj5jknLsUf-MWSy4_brA" data-sessionlink="itct=CI0BEJQ1GAsiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >T-Series</a>&nbsp;<span class="yt-uix-tooltip yt-channel-title-icon-verified yt-sprite" title="Verified"></span></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>9,383,950 views</li><li>3 days ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="ke4jcUPFcrY" data-visibility-tracking="CIwBEJQ1GAwiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5AtuWVnpTuiPeRAQ=="><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=ke4jcUPFcrY" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIwBEJQ1GAwiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/ke4jcUPFcrY/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=BgJXGVBYYdUKBex0teQ2Q3QKlfY" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">3:01</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="ke4jcUPFcrY"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="ke4jcUPFcrY"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="ke4jcUPFcrY"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="ke4jcUPFcrY"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=ke4jcUPFcrY" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIwBEJQ1GAwiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA"  title="Rabb Da Radio (TRAILER) Tarsem Jassar | Mandy Takhar | Simi Chahal | Releasing On 31 March 2017" aria-describedby="description-id-273809" dir="ltr">Rabb Da Radio (TRAILER) Tarsem Jassar | Mandy Takhar | Simi Chahal | Releasing On 31 March 2017</a><span class="accessible-description" id="description-id-273809"> - Duration: 3:01.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/VehliJantaRecords" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCyXTmEh_ftszgyO3FTe4-jA" data-sessionlink="itct=CIwBEJQ1GAwiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >VehliJantaRecords</a>&nbsp;<span class="yt-uix-tooltip yt-channel-title-icon-verified yt-sprite" title="Verified"></span></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>1,277,340 views</li><li>1 day ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="4-6SxN3uPkw" data-visibility-tracking="CIsBEJQ1GA0iEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5AzPy4783YpPfjAQ=="><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=4-6SxN3uPkw" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIsBEJQ1GA0iEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/4-6SxN3uPkw/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=L8DGloGEYZPSmOTRcGzbBZielEg" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">4:03</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="4-6SxN3uPkw"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="4-6SxN3uPkw"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="4-6SxN3uPkw"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="4-6SxN3uPkw"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=4-6SxN3uPkw" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIsBEJQ1GA0iEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA"  title="GAGAN KOKRI : Berukhiyan (Full Video) | Jassi Katyal | New Punjabi Songs 2017 | Saga Music" aria-describedby="description-id-747407" dir="ltr">GAGAN KOKRI : Berukhiyan (Full Video) | Jassi Katyal | New Punjabi Songs 2017 | Saga Music</a><span class="accessible-description" id="description-id-747407"> - Duration: 4:03.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/sagahits" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCuFwzKrS0wE43CSkyaHBGiQ" data-sessionlink="itct=CIsBEJQ1GA0iEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >SagaHits</a>&nbsp;<span class="yt-uix-tooltip yt-channel-title-icon-verified yt-sprite" title="Verified"></span></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>2,778,445 views</li><li>2 days ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="_XOp8llQ3yk" data-visibility-tracking="CIoBEJQ1GA4iEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5Aqb7DyqW-6rn9AQ=="><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=_XOp8llQ3yk" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIoBEJQ1GA4iEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/_XOp8llQ3yk/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=iVv0C_RzSZBoREcKMFuv0cc0_v4" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">3:26</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="_XOp8llQ3yk"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="_XOp8llQ3yk"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="_XOp8llQ3yk"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="_XOp8llQ3yk"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=_XOp8llQ3yk" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIoBEJQ1GA4iEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC10cnZaD0ZFd2hhdF90b193YXRjaA"  title="Breakup Celebrations (Full Song) | Amardeep Maana | Latest Punjabi Songs | White Hill Music" aria-describedby="description-id-94536" dir="ltr">Breakup Celebrations (Full Song) | Amardeep Maana | Latest Punjabi Songs | White Hill Music</a><span class="accessible-description" id="description-id-94536"> - Duration: 3:26.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/WHBBP" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCopY0NAzASqmD6eVaRj2TFQ" data-sessionlink="itct=CIoBEJQ1GA4iEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >White Hill Music</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>400,620 views</li><li>1 day ago</li></ul></div></div></div></div></li></ul></div><button class="yt-uix-button yt-uix-button-size-default yt-uix-button-shelf-slider-pager yt-uix-shelfslider-prev" type="button" onclick=";return false;"><span class="yt-uix-button-content"><span data-tooltip-text="Previous" class="yt-uix-shelfslider-prev-arrow yt-uix-tooltip yt-sprite" aria-label="Previous"></span></span></button><button class="yt-uix-button yt-uix-button-size-default yt-uix-button-shelf-slider-pager yt-uix-shelfslider-next" type="button" onclick=";return false;"><span class="yt-uix-button-content"><span data-tooltip-text="Next" class="yt-uix-shelfslider-next-arrow yt-uix-tooltip yt-sprite" aria-label="Next"></span></span></button></div></div><div class="feed-item-dismissal-notices"></div></div></li>
</ol>
</li>

<li>
<ol id="item-section-449112" class="item-section">
<li><div class="feed-item-container browse-list-item-container yt-section-hover-container compact-shelf shelf-item branded-page-box vve-check clearfix " data-visibility-tracking="CHQQ3BwYACITCOTrgrPpzdICFQ81aAodkfoGjyiOHg=="><div class="feed-item-dismissable"><div class="shelf-title-table"><div class="shelf-title-row"><h2 class="branded-page-module-title shelf-title-cell"><a href="/channel/UCDbM8yVukVKPWUQSODaw_Mw" class="branded-page-module-title-link g-hovercard yt-uix-sessionlink      spf-link " data-ytid="UCDbM8yVukVKPWUQSODaw_Mw" data-sessionlink="itct=CHQQ3BwYACITCOTrgrPpzdICFQ81aAodkfoGjyiOHg" ><div class="yt-lockup-thumbnail"><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="20" src="//yt3.ggpht.com/3z8YGOIp0FMWX8SVY4j_xGQM19UBuR5iWGSKU4CaI5jCbLDf2cph9OIQKj-jbSeTTdgwOJionHtbVXCRBg=s88-nd-c-c0xffffffff-rj-k-no" alt="" width="20" data-ytimg="1" >
</span></div></div>&nbsp;<span class="branded-page-module-title-text">Comedy Movies - Topic</span></a>&nbsp;<span class="shelf-annotation shelf-title-annotation">Recommended channel</span></h2><div class="menu-container shelf-title-cell"><div class="shelf-action-container"><span class="shelf-subscription-button yt-uix-button-subscription-container"><span class="unsubscribe-confirmation-overlay-container">
<div class="yt-uix-overlay "  data-overlay-style="primary" data-overlay-shape="tiny">

<div class="yt-dialog hid ">
<div class="yt-dialog-base">
<span class="yt-dialog-align"></span>
<div class="yt-dialog-fg" role="dialog">
<div class="yt-dialog-fg-content">
<div class="yt-dialog-loading">
<div class="yt-dialog-waiting-content">
<p class="yt-spinner ">
<span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>

<span class="yt-spinner-message">
Loading...
</span>
</p>

</div>

</div>
<div class="yt-dialog-content">
<div class="unsubscribe-confirmation-overlay-content-container">
<div class="unsubscribe-confirmation-overlay-content">
<div class="unsubscribe-confirmation-message">
Unsubscribe from Comedy Movies - Topic?
</div>
</div>

<div class="yt-uix-overlay-actions">
<button class="yt-uix-button yt-uix-button-size-default yt-uix-button-default yt-uix-overlay-close" type="button" onclick=";return false;"><span class="yt-uix-button-content">Cancel</span></button>
<button class="yt-uix-button yt-uix-button-size-default yt-uix-button-primary overlay-confirmation-unsubscribe-button yt-uix-overlay-close" type="button" onclick=";return false;"><span class="yt-uix-button-content">Unsubscribe</span></button>
</div>
</div>

</div>
<div class="yt-dialog-working">
<div class="yt-dialog-working-overlay"></div>
<div class="yt-dialog-working-bubble">
<div class="yt-dialog-waiting-content">
<p class="yt-spinner ">
<span class="yt-spinner-img  yt-sprite" title="Loading icon"></span>

<span class="yt-spinner-message">
Working...
</span>
</p>

</div>
</div>

</div>
</div>
<div class="yt-dialog-focus-trap" tabindex="0"></div>
</div>
</div>
</div>


</div>

</span><button class="yt-uix-button yt-uix-button-size-default yt-uix-button-subscribe-branded yt-uix-button-has-icon no-icon-markup yt-uix-subscription-button yt-can-buffer" type="button" onclick=";return false;" aria-busy="false" aria-live="polite" data-show-unsub-confirm-dialog="true" data-clicktracking="itct=CHUQmysiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCGhvbWVwYWdl" data-show-unsub-confirm-time-frame="always" data-channel-external-id="UCDbM8yVukVKPWUQSODaw_Mw" data-subscribed-timestamp="0" data-style-type="branded" data-href="https://accounts.google.com/ServiceLogin?service=youtube&amp;hl=en&amp;uilel=3&amp;passive=true&amp;continue=http%3A%2F%2Fwww.youtube.com%2Fsignin%3Fapp%3Ddesktop%26continue_action%3DQUFFLUhqbVZqMmFFNHhpZjVOZmJsN2VId3hua1ItalV1QXxBQ3Jtc0tsUUdubnBtVm1VdlpUTVh1bG5nUnhiX0F6VVRrSXlpMmRIa09xa1VMb3F6anBXd29aa1BXWHM3WUNKR2JwV2FaVVduUzBLUU53T3djdDFYZXlVSkNBd0tTa2Y4Zmo2UVg2YUFDR3BkRks1ejhnemFRV3pMeXR4MVk0WDBHZTAzcE1ranE0Q2hTUWY1eUJtMkM5Ul9qakRNOGZQLU9WeVdVcWhHN1R2cjkyRk5rUWVFZ3BaNk1QMklUeTFmS0pwRnpQa1hmSWZQaHEzUkticUR1Uk1STE9pOG00TVNn%26hl%3Den%26feature%3Dsubscribe%26action_handle_signin%3Dtrue%26next%3D%252Fchannel%252FUCDbM8yVukVKPWUQSODaw_Mw"><span class="yt-uix-button-content"><span class="subscribe-label" aria-label="Subscribe">Subscribe</span><span class="subscribed-label" aria-label="Unsubscribe">Subscribed</span><span class="unsubscribe-label" aria-label="Unsubscribe">Unsubscribe</span></span></button><span class="yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count" title="504,430" aria-label="504,430" tabindex="0">504,430</span><span class="yt-subscription-button-subscriber-count-branded-horizontal yt-short-subscriber-count" title="504K" aria-label="504K" tabindex="0">504K</span></span></div></div></div></div><div class="compact-shelf yt-uix-shelfslider yt-uix-shelfslider-at-head"><div class="yt-uix-shelfslider-body yt-viewport"><ul class="yt-uix-shelfslider-list"><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="1EROaOmxnbk" data-visibility-tracking="CIYBEJQ1GAAiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5AubvGzY7Nk6LUAQ=="><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=1EROaOmxnbk" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIYBEJQ1GAAiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC1yY2haD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="https://i.ytimg.com/vi/1EROaOmxnbk/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=R94fjQjHJBSyfbvKamhwBrMgHM4" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">4:18</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="1EROaOmxnbk"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="1EROaOmxnbk"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="1EROaOmxnbk"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="1EROaOmxnbk"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=1EROaOmxnbk" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIYBEJQ1GAAiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC1yY2haD0ZFd2hhdF90b193YXRjaA"  title="Hotest Actress on Kapil Sharma Show" aria-describedby="description-id-349137" dir="ltr">Hotest Actress on Kapil Sharma Show</a><span class="accessible-description" id="description-id-349137"> - Duration: 4:18.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/channel/UCH0CrAaxlG8kronH5GLHOHQ" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCH0CrAaxlG8kronH5GLHOHQ" data-sessionlink="itct=CIYBEJQ1GAAiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >Amazing World</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>5,168,492 views</li><li>3 months ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="tdE2-xI3VNE" data-visibility-tracking="CIUBEJQ1GAEiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5A0andkbHfzei1AQ=="><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=tdE2-xI3VNE" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIUBEJQ1GAEiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC1yY2haD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="https://i.ytimg.com/vi/tdE2-xI3VNE/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=87VB_HEJDkhZuMEqBrK0Qj8Wbfo" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">1:11:59</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="tdE2-xI3VNE"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="tdE2-xI3VNE"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="tdE2-xI3VNE"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="tdE2-xI3VNE"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=tdE2-xI3VNE" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIUBEJQ1GAEiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC1yY2haD0ZFd2hhdF90b193YXRjaA"  title="Mr bean 1 hour full episode Best of Mr bean" aria-describedby="description-id-818282" dir="ltr">Mr bean 1 hour full episode Best of Mr bean</a><span class="accessible-description" id="description-id-818282"> - Duration: 1:11:59.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/channel/UCuSEyt2JYfrX93r_jYt5cxg" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCuSEyt2JYfrX93r_jYt5cxg" data-sessionlink="itct=CIUBEJQ1GAEiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >faizan</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>4,907,721 views</li><li>6 months ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="1FPbmsY7WNk" data-visibility-tracking="CIQBEJQ1GAIiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5A2bHtsazz9qnUAQ=="><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=1FPbmsY7WNk" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIQBEJQ1GAIiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC1yY2haD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="https://i.ytimg.com/vi/1FPbmsY7WNk/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=z8C_ZM29Kman2Iq-ErnMZn8Nt08" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">37:22</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="1FPbmsY7WNk"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="1FPbmsY7WNk"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="1FPbmsY7WNk"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="1FPbmsY7WNk"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=1FPbmsY7WNk" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIQBEJQ1GAIiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC1yY2haD0ZFd2hhdF90b193YXRjaA"  title="Comedy Circus Ke Ajoobe - Ep 2 - Kareena Kapoor as Special Guest" aria-describedby="description-id-160871" dir="ltr">Comedy Circus Ke Ajoobe - Ep 2 - Kareena Kapoor as Special Guest</a><span class="accessible-description" id="description-id-160871"> - Duration: 37:22.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/setindia" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCpEhnqL0y41EpW2TvWAHD7Q" data-sessionlink="itct=CIQBEJQ1GAIiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >SET India</a>&nbsp;<span class="yt-uix-tooltip yt-channel-title-icon-verified yt-sprite" title="Verified"></span></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>1,564,701 views</li><li>1 month ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="eLIKkCrV1G4" data-visibility-tracking="CIMBEJQ1GAMiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5A7qjX1oLSgtl4"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=eLIKkCrV1G4" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIMBEJQ1GAMiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC1yY2haD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="https://i.ytimg.com/vi/eLIKkCrV1G4/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=MV-zG7-BsqIoM447cFO8mj_A-sI" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">2:08:32</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="eLIKkCrV1G4"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="eLIKkCrV1G4"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="eLIKkCrV1G4"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="eLIKkCrV1G4"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=eLIKkCrV1G4" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIMBEJQ1GAMiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC1yY2haD0ZFd2hhdF90b193YXRjaA"  title="Jolly LLB 2013 movie HD" aria-describedby="description-id-813275" dir="ltr">Jolly LLB 2013 movie HD</a><span class="accessible-description" id="description-id-813275"> - Duration: 2:08:32.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/channel/UCdTfAWwLD4-sVkDFUHyh7pA" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCdTfAWwLD4-sVkDFUHyh7pA" data-sessionlink="itct=CIMBEJQ1GAMiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >movies world</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>1,548,265 views</li><li>3 weeks ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="U-Xk4CrG-oY" data-visibility-tracking="CIIBEJQ1GAQiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5AhvWb1oKc-fJT"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=U-Xk4CrG-oY" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIIBEJQ1GAQiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC1yY2haD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="https://i.ytimg.com/vi/U-Xk4CrG-oY/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=jOe1SE6ntIlq5d-udn2ZvilBXIc" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">1:23</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="U-Xk4CrG-oY"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="U-Xk4CrG-oY"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="U-Xk4CrG-oY"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="U-Xk4CrG-oY"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=U-Xk4CrG-oY" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIIBEJQ1GAQiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC1yY2haD0ZFd2hhdF90b193YXRjaA"  title="AMERICAN PIE: EL REENCUENTRO -Las parejas de American Pie" aria-describedby="description-id-587602" dir="ltr">AMERICAN PIE: EL REENCUENTRO -Las parejas de American Pie</a><span class="accessible-description" id="description-id-587602"> - Duration: 1:23.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/UniversalSpain" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UC6Raldd8iIExwu5BNS_hzvw" data-sessionlink="itct=CIIBEJQ1GAQiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >UniversalSpain</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>61,327,877 views</li><li>4 years ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="dOpqkO9xWBc" data-visibility-tracking="CIEBEJQ1GAUiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5Al7DF-47SmvV0"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=dOpqkO9xWBc" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIEBEJQ1GAUiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC1yY2haD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="https://i.ytimg.com/vi/dOpqkO9xWBc/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=cfsMPMU5VMYqMlRgHzLzc1KE_60" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">2:15:38</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="dOpqkO9xWBc"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="dOpqkO9xWBc"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="dOpqkO9xWBc"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="dOpqkO9xWBc"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=dOpqkO9xWBc" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIEBEJQ1GAUiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC1yY2haD0ZFd2hhdF90b193YXRjaA"  title="NEW FULL MOVIES 2016 HD || NEERU BAJWA , DILJIT DOSANJH || LATEST FILMS 2016 HD" aria-describedby="description-id-979791" dir="ltr">NEW FULL MOVIES 2016 HD || NEERU BAJWA , DILJIT DOSANJH || LATEST FILMS 2016 HD</a><span class="accessible-description" id="description-id-979791"> - Duration: 2:15:38.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/punjaabitadka" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCYLwXIJgRSA9kjEzXJrRNxA" data-sessionlink="itct=CIEBEJQ1GAUiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >Punjabi Tadka</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>2,178,961 views</li><li>5 months ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="EocHhTd6fqI" data-visibility-tracking="CIABEJQ1GAYiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh5Aov3pu9PwwcMS"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=EocHhTd6fqI" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIABEJQ1GAYiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC1yY2haD0ZFd2hhdF90b193YXRjaA" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/EocHhTd6fqI/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=pSLIcyUeEcQvwyZ0w7C1cTngSnA" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">6:21</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="EocHhTd6fqI"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="EocHhTd6fqI"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="EocHhTd6fqI"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="EocHhTd6fqI"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=EocHhTd6fqI" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CIABEJQ1GAYiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4yCmctaGlnaC1yY2haD0ZFd2hhdF90b193YXRjaA"  title="Dhamaal - Aeroplane scene - Sanjay Dutt | Ritesh Deshmukh | Vijay Raaz" aria-describedby="description-id-692516" dir="ltr">Dhamaal - Aeroplane scene - Sanjay Dutt | Ritesh Deshmukh | Vijay Raaz</a><span class="accessible-description" id="description-id-692516"> - Duration: 6:21.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/indiancomedy" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UC0PKLLmL8pIJLjOI1gBH_pA" data-sessionlink="itct=CIABEJQ1GAYiEwjk64Kz6c3SAhUPNWgKHZH6Bo8ojh4" >Indian comedy</a>&nbsp;<span class="yt-uix-tooltip yt-channel-title-icon-verified yt-sprite" title="Verified"></span></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>12,472,653 views</li><li>7 years ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="iCy-biKcgLs" data-visibility-tracking="CH8QlDUYByITCOTrgrPpzdICFQ81aAodkfoGjyiOHkC7gfKU4s2vlogB"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=iCy-biKcgLs" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CH8QlDUYByITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIKZy1oaWdoLXJjaFoPRkV3aGF0X3RvX3dhdGNo" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/iCy-biKcgLs/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=Obh-dAaTxT1xam9tWBAmeDpyImQ" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">57:24</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="iCy-biKcgLs"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="iCy-biKcgLs"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="iCy-biKcgLs"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="iCy-biKcgLs"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=iCy-biKcgLs" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CH8QlDUYByITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIKZy1oaWdoLXJjaFoPRkV3aGF0X3RvX3dhdGNo"  title="Kapil Sharma and Sumona&#39;s Rib-Tickling Perfomance" aria-describedby="description-id-390570" dir="ltr">Kapil Sharma and Sumona&#39;s Rib-Tickling Perfomance</a><span class="accessible-description" id="description-id-390570"> - Duration: 57:24.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/setindia" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCpEhnqL0y41EpW2TvWAHD7Q" data-sessionlink="itct=CH8QlDUYByITCOTrgrPpzdICFQ81aAodkfoGjyiOHg" >SET India</a>&nbsp;<span class="yt-uix-tooltip yt-channel-title-icon-verified yt-sprite" title="Verified"></span></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>6,288,974 views</li><li>1 year ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="bB84H0syPi4" data-visibility-tracking="CH4QlDUYCCITCOTrgrPpzdICFQ81aAodkfoGjyiOHkCu_MjZ9IPOj2w="><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=bB84H0syPi4" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CH4QlDUYCCITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIKZy1oaWdoLXJjaFoPRkV3aGF0X3RvX3dhdGNo" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/bB84H0syPi4/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=zqRDf_e6hnjA5TyB8FWiYLXykRA" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">2:20:18</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="bB84H0syPi4"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="bB84H0syPi4"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="bB84H0syPi4"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="bB84H0syPi4"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=bB84H0syPi4" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CH4QlDUYCCITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIKZy1oaWdoLXJjaFoPRkV3aGF0X3RvX3dhdGNo"  title="Bade Miyan Chote Miyan (1998) HD Full Comedy Movie  - Amitabh Bachchan - Govinda" aria-describedby="description-id-38452" dir="ltr">Bade Miyan Chote Miyan (1998) HD Full Comedy Movie  - Amitabh Bachchan - Govinda</a><span class="accessible-description" id="description-id-38452"> - Duration: 2:20:18.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/indiancomedy" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UC0PKLLmL8pIJLjOI1gBH_pA" data-sessionlink="itct=CH4QlDUYCCITCOTrgrPpzdICFQ81aAodkfoGjyiOHg" >Indian comedy</a>&nbsp;<span class="yt-uix-tooltip yt-channel-title-icon-verified yt-sprite" title="Verified"></span></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>6,801,555 views</li><li>1 year ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="TeTraJKgX-Y" data-visibility-tracking="CH0QlDUYCSITCOTrgrPpzdICFQ81aAodkfoGjyiOHkDmv4GVie268k0="><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=TeTraJKgX-Y" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CH0QlDUYCSITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIKZy1oaWdoLXJjaFoPRkV3aGF0X3RvX3dhdGNo" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/TeTraJKgX-Y/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=AJeJbXt9zsrcl9KZVDXp7Ycvikw" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">2:09:50</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="TeTraJKgX-Y"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="TeTraJKgX-Y"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="TeTraJKgX-Y"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="TeTraJKgX-Y"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=TeTraJKgX-Y" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CH0QlDUYCSITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIKZy1oaWdoLXJjaFoPRkV3aGF0X3RvX3dhdGNo"  title="Dirty Politics Full Movie (2015) | HD | Mallika Sherawat, Om Puri | Latest Bollywood Hindi Movie" aria-describedby="description-id-315880" dir="ltr">Dirty Politics Full Movie (2015) | HD | Mallika Sherawat, Om Puri | Latest Bollywood Hindi Movie</a><span class="accessible-description" id="description-id-315880"> - Duration: 2:09:50.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/rajshri" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCEKWXRsfUHkan-D_ljU8Asw" data-sessionlink="itct=CH0QlDUYCSITCOTrgrPpzdICFQ81aAodkfoGjyiOHg" >Rajshri</a>&nbsp;<span class="yt-uix-tooltip yt-channel-title-icon-verified yt-sprite" title="Verified"></span></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>20,119,459 views</li><li>1 year ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="3nOzDNZ5m9E" data-visibility-tracking="CHwQlDUYCiITCOTrgrPpzdICFQ81aAodkfoGjyiOHkDRt-azzeHsud4B"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=3nOzDNZ5m9E" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CHwQlDUYCiITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIKZy1oaWdoLXJjaFoPRkV3aGF0X3RvX3dhdGNo" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/3nOzDNZ5m9E/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=XwZxCsRNWoLgFJPNvGZF8fgeZsY" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">2:02:05</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="3nOzDNZ5m9E"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="3nOzDNZ5m9E"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="3nOzDNZ5m9E"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="3nOzDNZ5m9E"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=3nOzDNZ5m9E" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CHwQlDUYCiITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIKZy1oaWdoLXJjaFoPRkV3aGF0X3RvX3dhdGNo"  title="NEW PUNJABI FILM - PARMISH VERMA || Latest Punjabi Movies 2017 Full HD" aria-describedby="description-id-709751" dir="ltr">NEW PUNJABI FILM - PARMISH VERMA || Latest Punjabi Movies 2017 Full HD</a><span class="accessible-description" id="description-id-709751"> - Duration: 2:02:05.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/channel/UC-lNHm45-1hH9bnOYecdfuA" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UC-lNHm45-1hH9bnOYecdfuA" data-sessionlink="itct=CHwQlDUYCiITCOTrgrPpzdICFQ81aAodkfoGjyiOHg" >Ballewood - Punjabi Movies Library</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>416,704 views</li><li>1 week ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="qAW2XwrIyac" data-visibility-tracking="CHsQlDUYCyITCOTrgrPpzdICFQ81aAodkfoGjyiOHkCnk6PW8MvtgqgB"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=qAW2XwrIyac" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CHsQlDUYCyITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIKZy1oaWdoLXJjaFoPRkV3aGF0X3RvX3dhdGNo" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/qAW2XwrIyac/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=kkzOt3TyIS_nnNwrq1bQSvQYRFs" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">15:31</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="qAW2XwrIyac"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="qAW2XwrIyac"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="qAW2XwrIyac"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="qAW2XwrIyac"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=qAW2XwrIyac" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CHsQlDUYCyITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIKZy1oaWdoLXJjaFoPRkV3aGF0X3RvX3dhdGNo"  title="Salman Khan and Aishwarya Rai Bachchan in Best of Undekha | The Kapil Sharma Show | Sony LIV | HD" aria-describedby="description-id-349380" dir="ltr">Salman Khan and Aishwarya Rai Bachchan in Best of Undekha | The Kapil Sharma Show | Sony LIV | HD</a><span class="accessible-description" id="description-id-349380"> - Duration: 15:31.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/sonyliv" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCOQNJjhXwvAScuELTT_i7cQ" data-sessionlink="itct=CHsQlDUYCyITCOTrgrPpzdICFQ81aAodkfoGjyiOHg" >SonyLIV</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>3,471,928 views</li><li>3 weeks ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="PlzN8x2fBZU" data-visibility-tracking="CHoQlDUYDCITCOTrgrPpzdICFQ81aAodkfoGjyiOHkCVi_zssb6zrj4="><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=PlzN8x2fBZU" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CHoQlDUYDCITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIKZy1oaWdoLXJjaFoPRkV3aGF0X3RvX3dhdGNo" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/PlzN8x2fBZU/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=kRg5BAAGYyyHeVMwBiIfqUYZ7hU" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">39:50</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="PlzN8x2fBZU"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="PlzN8x2fBZU"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="PlzN8x2fBZU"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="PlzN8x2fBZU"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=PlzN8x2fBZU" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CHoQlDUYDCITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIKZy1oaWdoLXJjaFoPRkV3aGF0X3RvX3dhdGNo"  title="The Angrez 2 Comedy Scenes Back to Back | Ismail Bhai, Saleem Pheku | Sri Balaji Video" aria-describedby="description-id-869330" dir="ltr">The Angrez 2 Comedy Scenes Back to Back | Ismail Bhai, Saleem Pheku | Sri Balaji Video</a><span class="accessible-description" id="description-id-869330"> - Duration: 39:50.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/SriBalajiMovies" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCoy3dQzEdq1y2zMnT4pdj3Q" data-sessionlink="itct=CHoQlDUYDCITCOTrgrPpzdICFQ81aAodkfoGjyiOHg" >SriBalajiMovies</a>&nbsp;<span class="yt-uix-tooltip yt-channel-title-icon-verified yt-sprite" title="Verified"></span></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>2,831,421 views</li><li>1 year ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="WEmxQyTx8NU" data-visibility-tracking="CHkQlDUYDSITCOTrgrPpzdICFQ81aAodkfoGjyiOHkDV4censqjspFg="><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=WEmxQyTx8NU" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CHkQlDUYDSITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIKZy1oaWdoLXJjaFoPRkV3aGF0X3RvX3dhdGNo" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/WEmxQyTx8NU/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=n1ZthV-kqbCPLloC41ksAk1p_xE" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">2:43</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="WEmxQyTx8NU"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="WEmxQyTx8NU"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="WEmxQyTx8NU"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="WEmxQyTx8NU"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=WEmxQyTx8NU" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CHkQlDUYDSITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIKZy1oaWdoLXJjaFoPRkV3aGF0X3RvX3dhdGNo"  title="Grand Masti | HD Hindi Movie Hot Trailer [2013] - Riteish Deshmukh,Vivek Oberoi,Aftab Shivdasani." aria-describedby="description-id-870189" dir="ltr">Grand Masti | HD Hindi Movie Hot Trailer [2013] - Riteish Deshmukh,Vivek Oberoi,Aftab Shivdasani.</a><span class="accessible-description" id="description-id-870189"> - Duration: 2:43.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/MoviesHDFull2012" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UC2RQWb519Sx6qnHqS10mGtA" data-sessionlink="itct=CHkQlDUYDSITCOTrgrPpzdICFQ81aAodkfoGjyiOHg" >Hindi Movies Trailer</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>8,132,574 views</li><li>3 years ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="y18s1NAUKy8" data-visibility-tracking="CHgQlDUYDiITCOTrgrPpzdICFQ81aAodkfoGjyiOHkCv1tCAzZrLr8sB"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=y18s1NAUKy8" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CHgQlDUYDiITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIKZy1oaWdoLXJjaFoPRkV3aGF0X3RvX3dhdGNo" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/y18s1NAUKy8/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=qVqqtE2hhP7r2RlbYDLLKn2GxuY" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">2:44:49</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="y18s1NAUKy8"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="y18s1NAUKy8"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="y18s1NAUKy8"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="y18s1NAUKy8"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=y18s1NAUKy8" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CHgQlDUYDiITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIKZy1oaWdoLXJjaFoPRkV3aGF0X3RvX3dhdGNo"  title="Ziddi Super Hit Full Bhojpuri Movie 2017  Pawan Singh Bhojpuri Full Film...ily" aria-describedby="description-id-512243" dir="ltr">Ziddi Super Hit Full Bhojpuri Movie 2017  Pawan Singh Bhojpuri Full Film...ily</a><span class="accessible-description" id="description-id-512243"> - Duration: 2:44:49.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/channel/UC8LdHrDQA1eMIx1i0F_mqTQ" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UC8LdHrDQA1eMIx1i0F_mqTQ" data-sessionlink="itct=CHgQlDUYDiITCOTrgrPpzdICFQ81aAodkfoGjyiOHg" >Raja yadav</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>826,300 views</li><li>1 month ago</li></ul></div></div></div></div></li></ul></div><button class="yt-uix-button yt-uix-button-size-default yt-uix-button-shelf-slider-pager yt-uix-shelfslider-prev" type="button" onclick=";return false;"><span class="yt-uix-button-content"><span data-tooltip-text="Previous" class="yt-uix-shelfslider-prev-arrow yt-uix-tooltip yt-sprite" aria-label="Previous"></span></span></button><button class="yt-uix-button yt-uix-button-size-default yt-uix-button-shelf-slider-pager yt-uix-shelfslider-next" type="button" onclick=";return false;"><span class="yt-uix-button-content"><span data-tooltip-text="Next" class="yt-uix-shelfslider-next-arrow yt-uix-tooltip yt-sprite" aria-label="Next"></span></span></button></div></div><div class="feed-item-dismissal-notices"></div></div></li>
</ol>
</li>

<li>
<ol id="item-section-388084" class="item-section">
<li><div class="feed-item-container browse-list-item-container yt-section-hover-container compact-shelf shelf-item branded-page-box vve-check clearfix " data-visibility-tracking="CGcQ3BwYACITCOTrgrPpzdICFQ81aAodkfoGjyiOHg=="><div class="feed-item-dismissable"><div class="shelf-title-table"><div class="shelf-title-row"><h2 class="branded-page-module-title shelf-title-cell"><a href="/playlist?list=PL_yIBWagYVjyvcAQFvq4AoOcD6oJwOOZq" class="branded-page-module-title-link yt-uix-sessionlink      spf-link " data-sessionlink="itct=CGcQ3BwYACITCOTrgrPpzdICFQ81aAodkfoGjyiOHg" ><div class="yt-lockup-thumbnail"><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="20" src="//yt3.ggpht.com/giJxJZmi9-thsLNLCQ_uMjtwcLg3CcI3guGNgQBHyJj0zyidJ9phV186dqrajBKRAxCxcYabQ1FZcDOVYQ=s88-nd-c-c0xffffffff-rj-k-no" alt="" width="20" data-ytimg="1" >
</span></div></div>&nbsp;<span class="branded-page-module-title-text">Sports</span></a>&nbsp;<span class="shelf-annotation shelf-title-annotation">by <b><a href="/channel/UCAh9DbAZny_eoGFsYlH2JZw" class="g-hovercard yt-uix-sessionlink      spf-link " data-ytid="UCAh9DbAZny_eoGFsYlH2JZw" data-sessionlink="ei=EZnDWKSfFI_qoAOR9Zv4CA" >Popular on YouTube - India</a></b></span></h2><div class="menu-container shelf-title-cell"></div></div></div><div class="compact-shelf yt-uix-shelfslider yt-uix-shelfslider-at-head"><div class="yt-uix-shelfslider-body yt-viewport"><ul class="yt-uix-shelfslider-list"><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="k500CJruYjE" data-visibility-tracking="CHIQlDUYACITCOTrgrPpzdICFQ81aAodkfoGjyiOHkCxxLnXiYHNzpMB"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=k500CJruYjE" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CHIQlDUYACITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIGZy1oaWdoWg9GRXdoYXRfdG9fd2F0Y2g" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="https://i.ytimg.com/vi/k500CJruYjE/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=Qo0mv_qW7LvWy5ovXiWajrTYW5A" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">2:37</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="k500CJruYjE"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="k500CJruYjE"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="k500CJruYjE"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="k500CJruYjE"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=k500CJruYjE" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CHIQlDUYACITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIGZy1oaWdoWg9GRXdoYXRfdG9fd2F0Y2g"  title="Virat Kohli-Steve Smith DRS spat triggered after this incident in Bangalore" aria-describedby="description-id-935799" dir="ltr">Virat Kohli-Steve Smith DRS spat triggered after this incident in Bangalore</a><span class="accessible-description" id="description-id-935799"> - Duration: 2:37.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/ht" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCm7lHFkt2yB_WzL67aruVBQ" data-sessionlink="itct=CHIQlDUYACITCOTrgrPpzdICFQ81aAodkfoGjyiOHg" >Hindustan Times</a>&nbsp;<span class="yt-uix-tooltip yt-channel-title-icon-verified yt-sprite" title="Verified"></span></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>1,375,454 views</li><li>2 days ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="S5Hqk0upD6g" data-visibility-tracking="CHEQlDUYASITCOTrgrPpzdICFQ81aAodkfoGjyiOHkCon6TdtNL6yEs="><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=S5Hqk0upD6g" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CHEQlDUYASITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIGZy1oaWdoWg9GRXdoYXRfdG9fd2F0Y2g" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="https://i.ytimg.com/vi/S5Hqk0upD6g/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=BEr_9fuYDNABMeg4uvn9sCIiXLY" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">3:45</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="S5Hqk0upD6g"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="S5Hqk0upD6g"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="S5Hqk0upD6g"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="S5Hqk0upD6g"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=S5Hqk0upD6g" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CHEQlDUYASITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIGZy1oaWdoWg9GRXdoYXRfdG9fd2F0Y2g"  title="Top Fastest Run-outs In Cricket History By MS Dhoni" aria-describedby="description-id-592423" dir="ltr">Top Fastest Run-outs In Cricket History By MS Dhoni</a><span class="accessible-description" id="description-id-592423"> - Duration: 3:45.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/channel/UC3_pyg9NWzKQKYKzT5ET93g" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UC3_pyg9NWzKQKYKzT5ET93g" data-sessionlink="itct=CHEQlDUYASITCOTrgrPpzdICFQ81aAodkfoGjyiOHg" >Cricket CountDown</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>1,079,984 views</li><li>1 day ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="5elgLOGyzBk" data-visibility-tracking="CHAQlDUYAiITCOTrgrPpzdICFQ81aAodkfoGjyiOHkCZmMuNzoXY9OUB"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=5elgLOGyzBk" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CHAQlDUYAiITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIGZy1oaWdoWg9GRXdoYXRfdG9fd2F0Y2g" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="https://i.ytimg.com/vi/5elgLOGyzBk/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=o8rVO9je5QAkfYo_UgrOTn1ZFug" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">4:33</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="5elgLOGyzBk"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="5elgLOGyzBk"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="5elgLOGyzBk"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="5elgLOGyzBk"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=5elgLOGyzBk" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CHAQlDUYAiITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIGZy1oaWdoWg9GRXdoYXRfdG9fd2F0Y2g"  title="Misbah Ul Haq Blast 6 Sixes In 6 Balls | Hongkong T20 Blitz 2017" aria-describedby="description-id-221952" dir="ltr">Misbah Ul Haq Blast 6 Sixes In 6 Balls | Hongkong T20 Blitz 2017</a><span class="accessible-description" id="description-id-221952"> - Duration: 4:33.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/channel/UCJIGuX67XfDFbX1RgeeDStg" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCJIGuX67XfDFbX1RgeeDStg" data-sessionlink="itct=CHAQlDUYAiITCOTrgrPpzdICFQ81aAodkfoGjyiOHg" >Cricket De Zone HD</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>1,501,245 views</li><li>2 days ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="JZmku4XbFj0" data-visibility-tracking="CG8QlDUYAyITCOTrgrPpzdICFQ81aAodkfoGjyiOHkC9rOyuuJfpzCU="><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=JZmku4XbFj0" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CG8QlDUYAyITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIGZy1oaWdoWg9GRXdoYXRfdG9fd2F0Y2g" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="https://i.ytimg.com/vi/JZmku4XbFj0/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=D1XE6NHCLw4B9HWiSCIEy0M89iw" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">2:35</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="JZmku4XbFj0"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="JZmku4XbFj0"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="JZmku4XbFj0"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="JZmku4XbFj0"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=JZmku4XbFj0" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CG8QlDUYAyITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIGZy1oaWdoWg9GRXdoYXRfdG9fd2F0Y2g"  title="INDIA VS PAKISTAN | Super Over | Unforgettable Victory | Must Watch !!!" aria-describedby="description-id-164256" dir="ltr">INDIA VS PAKISTAN | Super Over | Unforgettable Victory | Must Watch !!!</a><span class="accessible-description" id="description-id-164256"> - Duration: 2:35.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/channel/UCAzRzJtnSOsR-VE2H6dRrjA" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCAzRzJtnSOsR-VE2H6dRrjA" data-sessionlink="itct=CG8QlDUYAyITCOTrgrPpzdICFQ81aAodkfoGjyiOHg" >SiMSiM</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>230,710 views</li><li>2 days ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="gDAhsgMOVWA" data-visibility-tracking="CG4QlDUYBCITCOTrgrPpzdICFQ81aAodkfoGjyiOHkDgqrmYoLaImIAB"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=gDAhsgMOVWA" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CG4QlDUYBCITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIGZy1oaWdoWg9GRXdoYXRfdG9fd2F0Y2g" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="https://i.ytimg.com/vi/gDAhsgMOVWA/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=c7nd9yTeiar0eENITk2bW_maIYA" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">4:39</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="gDAhsgMOVWA"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="gDAhsgMOVWA"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="gDAhsgMOVWA"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="gDAhsgMOVWA"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=gDAhsgMOVWA" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CG4QlDUYBCITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIGZy1oaWdoWg9GRXdoYXRfdG9fd2F0Y2g"  title="Barcelona vs Paris Saint Germain 6-1 All Goals &amp; Highlights  UCL 08.03.2017 HD" aria-describedby="description-id-903018" dir="ltr">Barcelona vs Paris Saint Germain 6-1 All Goals &amp; Highlights  UCL 08.03.2017 HD</a><span class="accessible-description" id="description-id-903018"> - Duration: 4:39.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/channel/UCdEoGvgIF50jbvzbQ9kmkqg" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCdEoGvgIF50jbvzbQ9kmkqg" data-sessionlink="itct=CG4QlDUYBCITCOTrgrPpzdICFQ81aAodkfoGjyiOHg" >ARIZUNA</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>826,854 views</li><li>2 days ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="wRahbtEeUQc" data-visibility-tracking="CG0QlDUYBSITCOTrgrPpzdICFQ81aAodkfoGjyiOHkCHovmI7a2oi8EB"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=wRahbtEeUQc" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CG0QlDUYBSITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIGZy1oaWdoWg9GRXdoYXRfdG9fd2F0Y2g" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="https://i.ytimg.com/vi/wRahbtEeUQc/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=gi4iZPAiHEHBfkpwGgNWYJbEdTs" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">1:21</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="wRahbtEeUQc"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="wRahbtEeUQc"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="wRahbtEeUQc"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="wRahbtEeUQc"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=wRahbtEeUQc" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CG0QlDUYBSITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIGZy1oaWdoWg9GRXdoYXRfdG9fd2F0Y2g"  title="MS Dhoni Preparations for India-Australia third Test |&#39;தல&#39;தோனி இவ்வளவு  நல்லவரா? - Oneindia Tamil" aria-describedby="description-id-98382" dir="ltr">MS Dhoni Preparations for India-Australia third Test |&#39;தல&#39;தோனி இவ்வளவு  நல்லவரா? - Oneindia Tamil</a><span class="accessible-description" id="description-id-98382"> - Duration: 1:21.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/OneindiaTamil" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCpZBvTbjam0yTrD4HUUWTZw" data-sessionlink="itct=CG0QlDUYBSITCOTrgrPpzdICFQ81aAodkfoGjyiOHg" >Oneindia Tamil | ஒன்இந்தியா தமிழ்</a>&nbsp;<span class="yt-uix-tooltip yt-channel-title-icon-verified yt-sprite" title="Verified"></span></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>64,972 views</li><li>1 day ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="jMt6OW6WnPo" data-visibility-tracking="CGwQlDUYBiITCOTrgrPpzdICFQ81aAodkfoGjyiOHkD6udr0lsfe5YwB"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=jMt6OW6WnPo" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CGwQlDUYBiITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIGZy1oaWdoWg9GRXdoYXRfdG9fd2F0Y2g" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/jMt6OW6WnPo/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=IJ-aIMGVajqY6_S734bGZ5eJbJc" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">1:17</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="jMt6OW6WnPo"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="jMt6OW6WnPo"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="jMt6OW6WnPo"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="jMt6OW6WnPo"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=jMt6OW6WnPo" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CGwQlDUYBiITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIGZy1oaWdoWg9GRXdoYXRfdG9fd2F0Y2g"  title="R Ashwin takes revenge to Mitchel Starc | India Beat australia by 75 Runs | 2nd Test" aria-describedby="description-id-997490" dir="ltr">R Ashwin takes revenge to Mitchel Starc | India Beat australia by 75 Runs | 2nd Test</a><span class="accessible-description" id="description-id-997490"> - Duration: 1:17.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/user/aman051988" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UC3_9Tz8c_MLDuPAKwgjiK7Q" data-sessionlink="itct=CGwQlDUYBiITCOTrgrPpzdICFQ81aAodkfoGjyiOHg" >AmanJakz News</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>241,203 views</li><li>2 days ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="szDjAY2hP0c" data-visibility-tracking="CGsQlDUYByITCOTrgrPpzdICFQ81aAodkfoGjyiOHkDH_oTtmOC4mLMB"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=szDjAY2hP0c" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CGsQlDUYByITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIGZy1oaWdoWg9GRXdoYXRfdG9fd2F0Y2g" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/szDjAY2hP0c/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=3ozxJZ3wN_ctVV-oCC3CSqL3dVs" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">1:01</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="szDjAY2hP0c"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="szDjAY2hP0c"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="szDjAY2hP0c"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="szDjAY2hP0c"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch?v=szDjAY2hP0c" class=" yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link " data-sessionlink="itct=CGsQlDUYByITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIGZy1oaWdoWg9GRXdoYXRfdG9fd2F0Y2g"  title="Chennai adayar bike accident" aria-describedby="description-id-52843" dir="ltr">Chennai adayar bike accident</a><span class="accessible-description" id="description-id-52843"> - Duration: 1:01.</span></h3><div class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"><a href="/channel/UCHDP82Pp1k9JlqhGYu1AsGw" class="g-hovercard yt-uix-sessionlink       spf-link " data-ytid="UCHDP82Pp1k9JlqhGYu1AsGw" data-sessionlink="itct=CGsQlDUYByITCOTrgrPpzdICFQ81aAodkfoGjyiOHg" >tamil seithikal</a></div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>5,738 views</li><li>1 day ago</li></ul></div></div></div></div></li><li class="yt-shelf-grid-item yt-uix-shelfslider-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video vve-check clearfix" data-context-item-id="5MFZ9dLfua8" data-visibility-tracking="CGoQlDUYCCITCOTrgrPpzdICFQ81aAodkfoGjyiOHkCv8_6W3b7W4OQB"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto"><a aria-hidden="true"  href="/watch?v=5MFZ9dLfua8" class=" yt-uix-sessionlink      spf-link " data-sessionlink="itct=CGoQlDUYCCITCOTrgrPpzdICFQ81aAodkfoGjyiOHjIGZy1oaWdoWg9GRXdoYXRfdG9fd2F0Y2g" ><div class="yt-thumb video-thumb"><span class="yt-thumb-simple">
<img onload=";window.__ytRIL &amp;&amp; __ytRIL(this)" height="110" src="/yts/img/pixel-vfl3z5WfW.gif" data-thumb="https://i.ytimg.com/vi/5MFZ9dLfua8/hqdefault.jpg?custom=true&amp;w=196&amp;h=110&amp;stc=true&amp;jpg444=true&amp;jpgq=90&amp;sp=68&amp;sigh=0BAfnlzd9EraZHAE98nyKUfqavA" alt="" width="196" data-ytimg="1" >
<span class="video-time" aria-hidden="true">6:06</span></span></div></a>  <span class="thumb-menu dark-overflow-action-menu video-actions">
<button type="button" aria-expanded="false" class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" onclick=";return false;" aria-haspopup="true" ><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;"  data-video-ids="5MFZ9dLfua8"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;"  data-video-ids="5MFZ9dLfua8"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
</span>


<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button-sign-in yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-button-menu-id="shared-addto-watch-later-login" data-video-ids="5MFZ9dLfua8"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-style="tv-queue" data-video-ids="5MFZ9dLfua8"></button>
Traceback (most recent call last):
  File "C:/Users/CEC-07/Desktop/pooja/file/url.py", line 11, in <module>
    internet()
  File "C:/Users/CEC-07/Desktop/pooja/file/url.py", line 10, in internet
    print(l2)
UnicodeEncodeError: 'UCS-2' codec can't encode characters in position 341-341: Non-BMP character not supported in Tk
>>> 
============= RESTART: C:/Users/CEC-07/Desktop/pooja/file/url.py =============

<html lang="en"    class="version-d platform-desktop">
<head>
<meta charset="UTF-8">
<title>WhatsApp</title>



<meta property="og:title" content="WhatsApp"/>
<meta property="og:image" content="https://www.cdn.whatsapp.net/img/v4/whatsapp-promo.png?v=32fe13a"/>
<meta property="og:site_name" content="WhatsApp.com"/>

<meta name="description" content="WhatsApp Messenger: More than 1 billion people in over 180 countries use WhatsApp to stay in touch with friends and family, anytime and anywhere. WhatsApp is free and offers simple, secure, reliable messaging and calling, available on phones all over the world.">
<meta property="og:description" content="WhatsApp Messenger: More than 1 billion people in over 180 countries use WhatsApp to stay in touch with friends and family, anytime and anywhere. WhatsApp is free and offers simple, secure, reliable messaging and calling, available on phones all over the world."/>

<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />
<meta http-equiv="X-UA-Compatible" content="IE=9">

<meta name="theme-color" content="#1BA691">
<meta name="msapplication-navbutton-color" content="#1BA691">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="#1BA691">

<link id="favicon" rel="shortcut icon" href="https://whatsapp.com/favicon.png" type="image/png">

<meta name="google-site-verification" content="Cusl-1G4lInGd7xZ55vzhKEF4l3O11umoaqQ-RxTf2w" />

<script>
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-8707243-1', {
'cookieName' : 'whatsapp_cookie',
'cookieDomain' : 'www.whatsapp.com',
'cookieExpires' : 60 * 60 * 24 * 365 * 2
});
ga('send', 'pageview');
// delete old cookies
document.cookie = '__utma=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
document.cookie = '__utmc=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
document.cookie = '__utmz=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
</script>

<link rel="stylesheet" href="https://www.cdn.whatsapp.net/css/v4/style.build.css?v=32fe13a">

<script type="text/javascript" src="https://www.cdn.whatsapp.net/js/v4/jquery-1.12.2.min.js"></script>

</head>
<body class="page page--index" id="top">
<div class="header page-header--index">
<header class="page-header page-header--index">
<div class="page-header__inner">
<a class="page-header__logo" href="https://www.whatsapp.com"></a>

<div class="page-header__title">
<a href="https://www.whatsapp.com/">WhatsApp<a/>
</div>

<div class="page-header__menu" onclick="toggle_menu()">

<svg version="1.1" id="icon-menu" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="37px" height="37px" viewBox="0 0 37 37" style="enable-background:new 0 0 37 37;" xml:space="preserve">
<path class="icon_white" d="M8,26h21v-1.8H8V26z M8,11v1.8h21V11H8z M8,19.2h21v-1.8H8V19.2z"/>
</svg>

</div>


<div class="page-header__language">

<div id="lng" onclick="toggle_lng_menu()">

<svg version="1.1" id="icon-language" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
y="0px" width="19px" height="19px" viewBox="0 0 19 19" style="enable-background:new 0 0 19 19;" xml:space="preserve">
<style type="text/css">
.icon_language_1{fill:#FFFFFF;}
</style>
<path class="icon_language_1" d="M9.5,2C5.4,2,2,5.4,2,9.5S5.4,17,9.5,17c4.1,0,7.5-3.4,7.5-7.5S13.6,2,9.5,2z M14.7,6.5h-2.2
c-0.2-1-0.6-1.8-1.1-2.7C12.8,4.3,14,5.2,14.7,6.5z M9.5,3.5c0.6,0.9,1.1,1.9,1.4,3H8.1C8.4,5.4,8.9,4.4,9.5,3.5z M3.7,11
c-0.2-0.5-0.2-1-0.2-1.5C3.5,9,3.5,8.4,3.7,8h2.6C6.2,8.5,6.2,9,6.2,9.5c0,0.5,0.1,1,0.1,1.5H3.7z M4.3,12.5h2.2
c0.2,1,0.6,1.8,1.1,2.7C6.2,14.7,5,13.8,4.3,12.5z M6.5,6.5H4.3c0.8-1.3,1.9-2.2,3.2-2.7C7.1,4.7,6.7,5.5,6.5,6.5z M9.5,15.5
c-0.6-0.9-1.1-1.9-1.4-3h2.9C10.6,13.6,10.1,14.6,9.5,15.5z M11.2,11H7.8c-0.1-0.5-0.2-1-0.2-1.5c0-0.5,0.1-1,0.2-1.5h3.5
c0.1,0.5,0.2,1,0.2,1.5C11.5,10,11.3,10.5,11.2,11z M11.5,15.2c0.5-0.8,0.8-1.7,1.1-2.7h2.2C14,13.8,12.8,14.7,11.5,15.2z M12.8,11
c0.1-0.5,0.1-1,0.1-1.5c0-0.5-0.1-1-0.1-1.5h2.6c0.2,0.5,0.2,1,0.2,1.5c0,0.5-0.1,1.1-0.2,1.5H12.8z"/>
</svg>

<span class="lng-id" dir="auto">en<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="lng-dropdown" x="0px" y="0px" width="9px" height="20px" viewBox="0 0 9 20" style="enable-background:new 0 0 9 20;" xml:space="preserve"><polygon fill="#ffffff" points="1,9 4.5,12.5 8,9 "/></svg>
</span>
</div>

<div id="lng_open">
<div id="select" onclick="toggle_lng_menu()">
<span class="dropdown">&#9662;</span>
<span class="icon"></span>
Select your language	</div>
<div id="popular">
<li ><a class="lng-link" data-lng="az" href="?l=az" dir="auto">Azərbaycanca</a></li><li ><a class="lng-link" data-lng="id" href="?l=id" dir="auto">Bahasa Indonesia</a></li><li ><a class="lng-link" data-lng="ms" href="?l=ms" dir="auto">Bahasa Melayu</a></li><li ><a class="lng-link" data-lng="ca" href="?l=ca" dir="auto">Català</a></li><li ><a class="lng-link" data-lng="cs" href="?l=cs" dir="auto">Česky</a></li><li ><a class="lng-link" data-lng="da" href="?l=da" dir="auto">Dansk</a></li><li ><a class="lng-link" data-lng="de" href="?l=de" dir="auto">Deutsch</a></li><li ><a class="lng-link" data-lng="et" href="?l=et" dir="auto">Eesti</a></li><li class="active"><a class="lng-link" data-lng="en" href="?l=en" dir="auto">English</a></li><li ><a class="lng-link" data-lng="es" href="?l=es" dir="auto">Español</a></li><li ><a class="lng-link" data-lng="fr" href="?l=fr" dir="auto">Français</a></li><li ><a class="lng-link" data-lng="hr" href="?l=hr" dir="auto">Hrvatski</a></li><li ><a class="lng-link" data-lng="it" href="?l=it" dir="auto">Italiano</a></li><li ><a class="lng-link" data-lng="sw" href="?l=sw" dir="auto">Kiswahili</a></li><li ><a class="lng-link" data-lng="lv" href="?l=lv" dir="auto">Latviešu</a></li><li ><a class="lng-link" data-lng="lt" href="?l=lt" dir="auto">Lietuviškai</a></li><li ><a class="lng-link" data-lng="hu" href="?l=hu" dir="auto">Magyar</a></li><li ><a class="lng-link" data-lng="nl" href="?l=nl" dir="auto">Nederlands</a></li><li ><a class="lng-link" data-lng="nb" href="?l=nb" dir="auto">Norsk</a></li><li ><a class="lng-link" data-lng="uz" href="?l=uz" dir="auto">Oʻzbekcha</a></li><li ><a class="lng-link" data-lng="fil" href="?l=fil" dir="auto">Pilipino</a></li><li ><a class="lng-link" data-lng="pl" href="?l=pl" dir="auto">Polski</a></li><li ><a class="lng-link" data-lng="pt_br" href="?l=pt_br" dir="auto">Português (BR)</a></li><li ><a class="lng-link" data-lng="pt_pt" href="?l=pt_pt" dir="auto">Português (PT)</a></li><li ><a class="lng-link" data-lng="ro" href="?l=ro" dir="auto">Română</a></li><li ><a class="lng-link" data-lng="sq" href="?l=sq" dir="auto">Shqip</a></li><li ><a class="lng-link" data-lng="sk" href="?l=sk" dir="auto">Slovenčina</a></li><li ><a class="lng-link" data-lng="sl" href="?l=sl" dir="auto">Slovenščina</a></li><li ><a class="lng-link" data-lng="fi" href="?l=fi" dir="auto">Suomi</a></li><li ><a class="lng-link" data-lng="sv" href="?l=sv" dir="auto">Svensk</a></li><li ><a class="lng-link" data-lng="vi" href="?l=vi" dir="auto">Tiếng Việt</a></li><li ><a class="lng-link" data-lng="tr" href="?l=tr" dir="auto">Türkçe</a></li><li ><a class="lng-link" data-lng="el" href="?l=el" dir="auto">Ελληνικά</a></li><li ><a class="lng-link" data-lng="bg" href="?l=bg" dir="auto">Български</a></li><li ><a class="lng-link" data-lng="kk" href="?l=kk" dir="auto">Қазақша</a></li><li ><a class="lng-link" data-lng="mk" href="?l=mk" dir="auto">Македонски</a></li><li ><a class="lng-link" data-lng="ru" href="?l=ru" dir="auto">Pусский</a></li><li ><a class="lng-link" data-lng="sr" href="?l=sr" dir="auto">Српски</a></li><li ><a class="lng-link" data-lng="uk" href="?l=uk" dir="auto">Українська</a></li><li ><a class="lng-link" data-lng="he" href="?l=he" dir="auto">‏עברית‏</a></li><li ><a class="lng-link" data-lng="ar" href="?l=ar" dir="auto">العربية</a></li><li ><a class="lng-link" data-lng="fa" href="?l=fa" dir="auto">فارسی</a></li><li ><a class="lng-link" data-lng="ur" href="?l=ur" dir="auto">اردو</a></li><li ><a class="lng-link" data-lng="bn" href="?l=bn" dir="auto">বাংলা </a></li><li ><a class="lng-link" data-lng="hi" href="?l=hi" dir="auto">हिंदी</a></li><li ><a class="lng-link" data-lng="gu" href="?l=gu" dir="auto">ગુજરાતી</a></li><li ><a class="lng-link" data-lng="kn" href="?l=kn" dir="auto">ಕನ್ನಡ</a></li><li ><a class="lng-link" data-lng="mr" href="?l=mr" dir="auto">मराठी</a></li><li ><a class="lng-link" data-lng="ta" href="?l=ta" dir="auto">தமிழ்</a></li><li ><a class="lng-link" data-lng="te" href="?l=te" dir="auto">తెలుగు</a></li><li ><a class="lng-link" data-lng="ml" href="?l=ml" dir="auto">മലയാളം</a></li><li ><a class="lng-link" data-lng="th" href="?l=th" dir="auto">ภาษาไทย</a></li><li ><a class="lng-link" data-lng="zh_cn" href="?l=zh_cn" dir="auto">简体中文</a></li><li ><a class="lng-link" data-lng="zh_tw" href="?l=zh_tw" dir="auto">繁體中文</a></li><li ><a class="lng-link" data-lng="ja" href="?l=ja" dir="auto">日本語</a></li><li ><a class="lng-link" data-lng="ko" href="?l=ko" dir="auto">한국어</a></li>		<div class="clear"></div>
</div>
<div id="helptranslate">
<li><a href="https://translate.whatsapp.com" target="_blank">Help translate WhatsApp into your language</a></li>
<div class="clear"></div>
</div>

</div>                </div>

<nav class="page-header__nav">
<ul class="sitenav">
<li class="sitenav-item">
<a href="https://web.whatsapp.com/">
WhatsApp Web                                </a>
</li>
<li class="sitenav-item">
<a href="https://www.whatsapp.com/features/">
Features                                </a>
</li>
<li class="sitenav-item">
<a href="https://www.whatsapp.com/download/">
Download                                </a>
</li>
<li class="sitenav-item">
<a href="https://www.whatsapp.com/security/">
Security                                </a>
</li>
<li class="sitenav-item">
<a href="https://www.whatsapp.com/faq/">
FAQ                                </a>
</li>
</ul>
</nav>
</div>

<nav class="page-header__drawer drawer">
<div class="drawer__inner">
<div class="drawer__close" onclick="toggle_menu()">

<svg version="1.1" id="icon-close" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
width="37px" height="37px" viewBox="0 0 37 37" style="enable-background:new 0 0 37 37;" xml:space="preserve">
<polygon class="icon_white" points="26.7,11.6 25.4,10.3 18.5,17.2 11.6,10.3 10.3,11.6 17.2,18.5 10.3,25.4 11.6,26.7 18.5,19.8
25.4,26.7 26.7,25.4 19.8,18.5 "/>
</svg>

</div>

<div class="drawer__icon">
<svg version="1.1" id="whatsapp-logo-notext" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
x="0px" y="0px" width="39px" height="39px" viewBox="0 0 39 39" style="enable-background:new 0 0 39 39;" xml:space="preserve">
<style type="text/css">
.logo_white{fill:#FFFFFF;}
.logo_green{fill:#00E676;}
</style>
<path class="logo_green" d="M10.7,32.8l0.6,0.3c2.5,1.5,5.3,2.2,8.1,2.2l0,0c8.8,0,16-7.2,16-16c0-4.2-1.7-8.3-4.7-11.3
s-7-4.7-11.3-4.7c-8.8,0-16,7.2-15.9,16.1c0,3,0.9,5.9,2.4,8.4l0.4,0.6l-1.6,5.9L10.7,32.8z"/>
<path class="logo_white" d="M32.4,6.4C29,2.9,24.3,1,19.5,1C9.3,1,1.1,9.3,1.2,19.4c0,3.2,0.9,6.3,2.4,9.1L1,38l9.7-2.5
c2.7,1.5,5.7,2.2,8.7,2.2l0,0c10.1,0,18.3-8.3,18.3-18.4C37.7,14.4,35.8,9.8,32.4,6.4z M19.5,34.6L19.5,34.6c-2.7,0-5.4-0.7-7.7-2.1
l-0.6-0.3l-5.8,1.5L6.9,28l-0.4-0.6c-4.4-7.1-2.3-16.5,4.9-20.9s16.5-2.3,20.9,4.9s2.3,16.5-4.9,20.9C25.1,33.8,22.3,34.6,19.5,34.6
z M28.3,23.5L27.2,23c0,0-1.6-0.7-2.6-1.2c-0.1,0-0.2-0.1-0.3-0.1c-0.3,0-0.5,0.1-0.7,0.2l0,0c0,0-0.1,0.1-1.5,1.7
c-0.1,0.2-0.3,0.3-0.5,0.3h-0.1c-0.1,0-0.3-0.1-0.4-0.2l-0.5-0.2l0,0c-1.1-0.5-2.1-1.1-2.9-1.9c-0.2-0.2-0.5-0.4-0.7-0.6
c-0.7-0.7-1.4-1.5-1.9-2.4L15,18.4c-0.1-0.1-0.1-0.2-0.2-0.4c0-0.2,0-0.4,0.1-0.5c0,0,0.4-0.5,0.7-0.8c0.2-0.2,0.3-0.5,0.5-0.7
c0.2-0.3,0.3-0.7,0.2-1c-0.1-0.5-1.3-3.2-1.6-3.8c-0.2-0.3-0.4-0.4-0.7-0.5h-0.3c-0.2,0-0.5,0-0.8,0c-0.2,0-0.4,0.1-0.6,0.1
l-0.1,0.1c-0.2,0.1-0.4,0.3-0.6,0.4c-0.2,0.2-0.3,0.4-0.5,0.6c-0.7,0.9-1.1,2-1.1,3.1l0,0c0,0.8,0.2,1.6,0.5,2.3l0.1,0.3
c0.9,1.9,2.1,3.6,3.7,5.1l0.4,0.4c0.3,0.3,0.6,0.5,0.8,0.8c2.1,1.8,4.5,3.1,7.2,3.8c0.3,0.1,0.7,0.1,1,0.2l0,0c0.3,0,0.7,0,1,0
c0.5,0,1.1-0.2,1.5-0.4c0.3-0.2,0.5-0.2,0.7-0.4l0.2-0.2c0.2-0.2,0.4-0.3,0.6-0.5s0.4-0.4,0.5-0.6c0.2-0.4,0.3-0.9,0.4-1.4
c0-0.2,0-0.5,0-0.7C28.6,23.7,28.5,23.6,28.3,23.5z"/>
</svg>
</div>

<ul class="menu menu--drawer">
<li class="menu__item">
<a href="https://www.whatsapp.com/download/" class="menu__link">
Download                                </a>
</li>
<li class="menu__item">
<a href="https://www.whatsapp.com/features/" class="menu__link">
Features                                </a>
</li>
<li class="menu__item">
<a href="https://www.whatsapp.com/security/" class="menu__link">
Security                                </a>
</li>
<li class="menu__item">
<a href="https://www.whatsapp.com/faq/" class="menu__link">
FAQ                                </a>
</li>
<li class="menu__item">
<a href="https://www.whatsapp.com/contact/" class="menu__link">
Get in touch                                </a>
</li>
<li class="menu__item menu__item--language">
<select onchange="window.location = this.options[this.selectedIndex].value;"><option  value="?l=az">Azərbaycanca</option><option  value="?l=id">Bahasa Indonesia</option><option  value="?l=ms">Bahasa Melayu</option><option  value="?l=ca">Català</option><option  value="?l=cs">Česky</option><option  value="?l=da">Dansk</option><option  value="?l=de">Deutsch</option><option  value="?l=et">Eesti</option><option selected="selected" value="?l=en">English</option><option  value="?l=es">Español</option><option  value="?l=fr">Français</option><option  value="?l=hr">Hrvatski</option><option  value="?l=it">Italiano</option><option  value="?l=sw">Kiswahili</option><option  value="?l=lv">Latviešu</option><option  value="?l=lt">Lietuviškai</option><option  value="?l=hu">Magyar</option><option  value="?l=nl">Nederlands</option><option  value="?l=nb">Norsk</option><option  value="?l=uz">Oʻzbekcha</option><option  value="?l=fil">Pilipino</option><option  value="?l=pl">Polski</option><option  value="?l=pt_br">Português (BR)</option><option  value="?l=pt_pt">Português (PT)</option><option  value="?l=ro">Română</option><option  value="?l=sq">Shqip</option><option  value="?l=sk">Slovenčina</option><option  value="?l=sl">Slovenščina</option><option  value="?l=fi">Suomi</option><option  value="?l=sv">Svensk</option><option  value="?l=vi">Tiếng Việt</option><option  value="?l=tr">Türkçe</option><option  value="?l=el">Ελληνικά</option><option  value="?l=bg">Български</option><option  value="?l=kk">Қазақша</option><option  value="?l=mk">Македонски</option><option  value="?l=ru">Pусский</option><option  value="?l=sr">Српски</option><option  value="?l=uk">Українська</option><option  value="?l=he">‏עברית‏</option><option  value="?l=ar">العربية</option><option  value="?l=fa">فارسی</option><option  value="?l=ur">اردو</option><option  value="?l=bn">বাংলা </option><option  value="?l=hi">हिंदी</option><option  value="?l=gu">ગુજરાતી</option><option  value="?l=kn">ಕನ್ನಡ</option><option  value="?l=mr">मराठी</option><option  value="?l=ta">தமிழ்</option><option  value="?l=te">తెలుగు</option><option  value="?l=ml">മലയാളം</option><option  value="?l=th">ภาษาไทย</option><option  value="?l=zh_cn">简体中文</option><option  value="?l=zh_tw">繁體中文</option><option  value="?l=ja">日本語</option><option  value="?l=ko">한국어</option></select>                        </li>
</ul>
</div>

</nav>

</header>
</div>

<div class="section section--hero">
<div class="block block--hero">
<div class="block__inner">
<h1 class="block__title">
Simple. Secure.<br>Reliable messaging.            </h1>
<div class="block__body">
With WhatsApp, you'll get fast, simple, secure messaging and calling for <span class='nowrap'>free<sup>*</sup>,</span> available on phones all over the world.            </div>

<a href="https://www.whatsapp.com/download/" class="button button--primary button--s block__action">Download now</a>

<div class="block__hint">
<sup>*</sup> Data charges may apply. Contact your provider for details.            </div>

<div class="block__action actions">
<ul>
<li>
<a href="https://play.google.com/store/apps/details?id=com.whatsapp">
<img src="https://www.cdn.whatsapp.net/img/v4/icon-android.svg" alt="">
Android                        </a>
</li>
<li>
<a href="http://itunes.apple.com/us/app/whatsapp-messenger/id310633997?mt=8">
<img src="https://www.cdn.whatsapp.net/img/v4/icon-iphone.svg" alt="">
iPhone                        </a>
</li>
<li>
<a href="/download">
<img src="https://www.cdn.whatsapp.net/img/v4/icon-desktop.svg" alt="">
Mac or Windows PC                        </a>
</li>
<li>
<a href="/wp/">
<img src="https://www.cdn.whatsapp.net/img/v4/icon-wp.svg" alt="">
Windows Phone                        </a>
</li>
</ul>

</div>
</div>
<div class="block__img">
<div class="hero-phone"></div>
</div>
</div>

</div>

<div class="section section--features">
<div class="section__inner">
<div class="feature feature--dark feature--calls section__item">
<div class="feature__inner">
<h3 class="feature__intro">
WhatsApp Voice and Video Calls                </h3>
<h1 class="feature__title">
Speak Freely                </h1>
<div class="feature__text">
With voice calls, you can talk to your friends and family for <span class='nowrap'>free<sup>*</sup>,</span> even if they're in another country. And with <span class='nowrap'>free<sup>*</sup></span> video calls, you can have face-to-face conversations for when voice or text just isn't enough.                    WhatsApp voice and video calls use your phone's Internet connection, instead of your cell plan's voice minutes, so you don't have to worry about expensive calling charges.                </div>

<!-- <div class="feature__hint">
<sup>*</sup> Data charges may apply. Contact your provider for details.                </div> -->
</div>
<div class="feature__img"></div>
</div>
<div class="section__divider"></div>
<div class="feature feature--dimmed feature--security section__item">

<div class="feature__inner">
<div class="feature__img">
<iframe src="https://www.whatsapp.com/img/v4/animation/security/security_localized.html?v=32fe13a&amp;l=en" class="feature__embed" frameborder="0" width="272" height="272"></iframe>
</div>
<h3 class="feature__intro">
End-to-end encryption                </h3>
<h1 class="feature__title">
Security by Default                </h1>
<div class="feature__text">
Some of your most personal moments are shared on WhatsApp, which is why we built end-to-end encryption into the latest versions of our app. When end-to-end encrypted, your messages and calls are secured so only you and the person you're communicating with can read or listen to them, and nobody in between, not even WhatsApp.                </div>
</div>

</div>
</div>
</div>

<div class="section section--more">
<a class="button button--outline" href="https://www.whatsapp.com/features/">Explore features</a>
</div>

<footer class="page-footer-container">
<div class="page-footer -primary">
<div class="page-footer__inner">

<div class="four -spaced">
<div class="block block--footer four__item">
<h4 class="block__title">WhatsApp</h4>
<div class="block__body">
<ul class="list list--footer">
<li class="list__item">
<a href="https://www.whatsapp.com/features/" class="list__link">
Features                                            </a>
</li>
<li class="list__item">
<a href="https://www.whatsapp.com/security/" class="list__link">
Security                                            </a>
</li>
<li class="list__item">
<a href="https://www.whatsapp.com/download/" class="list__link">
Download                                            </a>
</li>
<li class="list__item">
<a href="https://web.whatsapp.com/" class="list__link">
WhatsApp Web                                            </a>
</li>
<li class="list__item">
<span class="list__empty"></span>
</li>
</ul>
</div>
</div>
<div class="block block--footer four__item">
<h4 class="block__title">Company</h4>
<div class="block__body">
<ul class="list list--footer">
<li class="list__item">
<a href="https://www.whatsapp.com/about/" class="list__link">
About                                            </a>
</li>
<li class="list__item">
<a href="https://www.whatsapp.com/join/" class="list__link">
Careers                                            </a>
</li>
<li class="list__item">
<a href="https://www.whatsappbrand.com/" class="list__link">
Brand Center                                            </a>
</li>
<li class="list__item">
<a href="https://www.whatsapp.com/contact/" class="list__link">
Get in touch                                            </a>
</li>
<li class="list__item">
<a href="https://blog.whatsapp.com" class="list__link">
Blog                                            </a>
</li>
<li class="list__item">
<span class="list__empty"></span>
</li>
<li class="list__item">
<span class="list__empty"></span>
</li>
</ul>
</div>
</div>
<div class="block block--footer four__item">
<h4 class="block__title">Download</h4>
<div class="block__body">
<ul class="list list--footer">
<li class="list__item">
<a href="https://www.whatsapp.com/download/" class="list__link">
Mac/PC                                            </a>
</li>
<li class="list__item">
<a href="https://www.whatsapp.com/android/" class="list__link">
Android                                            </a>
</li>
<li class="list__item">
<a href="https://www.whatsapp.com/appstore/" class="list__link">
iPhone                                            </a>
</li>
<li class="list__item">
<a href="https://www.whatsapp.com/wp/" class="list__link">
Windows Phone                                            </a>
</li>
<li class="list__item">
<a href="https://www.whatsapp.com/ota/" class="list__link">
BlackBerry                                            </a>
</li>
<li class="list__item">
<a href="https://www.whatsapp.com/nokia/" class="list__link">
Nokia                                            </a>
</li>
</ul>
</div>
</div>
<div class="block block--footer four__item">
<h4 class="block__title">Help</h4>
<div class="block__body">
<ul class="list list--footer">
<li class="list__item">
<a href="https://www.whatsapp.com/faq/" class="list__link">
FAQ                                            </a>
</li>
<li class="list__item">
<a href="https://twitter.com/whatsapp" class="list__link">
Twitter                                            </a>
</li>
<li class="list__item">
<a href="https://www.facebook.com/WhatsApp" class="list__link">
Facebook                                            </a>
</li>
<li class="list__item">
<span class="list__empty"></span>
</li>
<li class="list__item">
<span class="list__empty"></span>
</li>
<li class="list__item">
<span class="list__empty"></span>
</li>
</ul>
</div>
</div>
</div>
</div>
</div>
<div class="page-footer -secondary">
<div class="page-footer__inner">
<div class="four">
<div class="four__item" dir="auto">
2017 &copy; WhatsApp Inc.
</div>
<div class="four__item -span3">
<a href="https://www.whatsapp.com/legal/" class="page-footer__link">Privacy & Terms</a>
</div>
</div>
</div>
</div>
</footer>

<script>
var open = false;
var speed = 200;
function toggle_lng_menu() {
if(open) {
$('#lng_open').slideUp(speed);
$('.header').removeClass('is-expanded');
} else {
$('#lng_open').slideDown(speed);
$('.header').addClass('is-expanded');
}
open = !open;
}

function toggle_menu() {
$('.page-header__drawer').toggleClass('is-visible');
}

function toggle_search() {
$('.page-subheader--search').slideToggle();
}

$(function() {
})
</script>


</body>
</html>
>>> 
============= RESTART: C:/Users/CEC-07/Desktop/pooja/file/url.py =============
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta http-equiv="Content-Script-Type" content="text/javascript">
<script type="text/javascript">
function getCookie(c_name) { // Local function for getting a cookie value
if (document.cookie.length > 0) {
c_start = document.cookie.indexOf(c_name + "=");
if (c_start!=-1) {
c_start=c_start + c_name.length + 1;
c_end=document.cookie.indexOf(";", c_start);

if (c_end==-1)
c_end = document.cookie.length;

return unescape(document.cookie.substring(c_start,c_end));
}
}
return "";
}
function setCookie(c_name, value, expiredays) { // Local function for setting a value of a cookie
var exdate = new Date();
exdate.setDate(exdate.getDate()+expiredays);
document.cookie = c_name + "=" + escape(value) + ((expiredays==null) ? "" : ";expires=" + exdate.toGMTString()) + ";path=/";
}
function getHostUri() {
var loc = document.location;
return loc.toString();
}
setCookie('YPF8827340282Jdskjhfiw_928937459182JAX666', '103.57.70.86', 10);
try {
location.reload(true);
} catch (err1) {
try {
location.reload();
} catch (err2) {
location.href = getHostUri();
}
}
</script>
</head>
<body>
<noscript>This site requires JavaScript and Cookies to be enabled. Please change your browser settings or upgrade your browser.</noscript>
</body>
</html>
>>> 
============= RESTART: C:/Users/CEC-07/Desktop/pooja/file/url.py =============
<!DOCTYPE html>
<html lang="mr" id="facebook" class="no_js">
<head><meta charset="utf-8" /><meta name="referrer" content="default" id="meta_referrer" /><script>function envFlush(a){function b(c){for(var d in a)c[d]=a[d];}if(window.requireLazy){window.requireLazy(['Env'],b);}else{window.Env=window.Env||{};b(window.Env);}}envFlush({"ajaxpipe_token":"AXitrasW6bmPbXE2"});</script><style></style><script>__DEV__=0;CavalryLogger=false;</script><noscript><meta http-equiv="refresh" content="0; URL=/?_fb_noscript=1" /></noscript><title id="pageTitle">Facebook मध्ये आपले स्वागत आहे - लॉग इन करा, साइन अप करा किंवा अधिक जाणून घ्या</title><meta property="og:site_name" content="Facebook" /><meta property="og:url" content="https://www.facebook.com/" /><meta property="og:image" content="https://www.facebook.com/images/fb_icon_325x325.png" /><meta property="og:locale" content="mr_IN" /><meta property="og:locale:alternate" content="www" /><meta property="og:locale:alternate" content="es_LA" /><meta property="og:locale:alternate" content="es_ES" /><meta property="og:locale:alternate" content="fr_FR" /><meta property="og:locale:alternate" content="it_IT" /><meta property="og:locale:alternate" content="id_ID" /><meta property="og:locale:alternate" content="th_TH" /><meta property="og:locale:alternate" content="vi_VN" /><meta property="og:locale:alternate" content="ko_KR" /><meta property="og:locale:alternate" content="ja_JP" /><link rel="search" type="application/opensearchdescription+xml" href="/osd.xml" title="Facebook" /><link rel="canonical" href="https://www.facebook.com/" /><link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.facebook.com/" /><link rel="alternate" media="handheld" href="https://m.facebook.com/" /><link rel="alternate" hreflang="x-default" href="https://www.facebook.com/" /><link rel="alternate" hreflang="en" href="https://www.facebook.com/" /><link rel="alternate" hreflang="ar" href="https://ar-ar.facebook.com/" /><link rel="alternate" hreflang="bg" href="https://bg-bg.facebook.com/" /><link rel="alternate" hreflang="bs" href="https://bs-ba.facebook.com/" /><link rel="alternate" hreflang="ca" href="https://ca-es.facebook.com/" /><link rel="alternate" hreflang="da" href="https://da-dk.facebook.com/" /><link rel="alternate" hreflang="el" href="https://el-gr.facebook.com/" /><link rel="alternate" hreflang="es" href="https://es-la.facebook.com/" /><link rel="alternate" hreflang="es-es" href="https://es-es.facebook.com/" /><link rel="alternate" hreflang="fa" href="https://fa-ir.facebook.com/" /><link rel="alternate" hreflang="fi" href="https://fi-fi.facebook.com/" /><link rel="alternate" hreflang="fr" href="https://fr-fr.facebook.com/" /><link rel="alternate" hreflang="fr-ca" href="https://fr-ca.facebook.com/" /><link rel="alternate" hreflang="hi" href="https://hi-in.facebook.com/" /><link rel="alternate" hreflang="hr" href="https://hr-hr.facebook.com/" /><link rel="alternate" hreflang="id" href="https://id-id.facebook.com/" /><link rel="alternate" hreflang="it" href="https://it-it.facebook.com/" /><link rel="alternate" hreflang="ko" href="https://ko-kr.facebook.com/" /><link rel="alternate" hreflang="mk" href="https://mk-mk.facebook.com/" /><link rel="alternate" hreflang="ms" href="https://ms-my.facebook.com/" /><link rel="alternate" hreflang="pl" href="https://pl-pl.facebook.com/" /><link rel="alternate" hreflang="pt" href="https://pt-br.facebook.com/" /><link rel="alternate" hreflang="pt-pt" href="https://pt-pt.facebook.com/" /><link rel="alternate" hreflang="ro" href="https://ro-ro.facebook.com/" /><link rel="alternate" hreflang="sl" href="https://sl-si.facebook.com/" /><link rel="alternate" hreflang="sr" href="https://sr-rs.facebook.com/" /><link rel="alternate" hreflang="th" href="https://th-th.facebook.com/" /><link rel="alternate" hreflang="vi" href="https://vi-vn.facebook.com/" /><meta name="description" content="Facebook  &#x939;&#x940; &#x90f;&#x915; &#x938;&#x93e;&#x92e;&#x93e;&#x91c;&#x93f;&#x915; &#x909;&#x92a;&#x92f;&#x941;&#x915;&#x94d;&#x924;&#x924;&#x93e; &#x906;&#x939;&#x947; &#x91c;&#x940; &#x932;&#x94b;&#x915;&#x93e;&#x902;&#x928;&#x93e; &#x924;&#x94d;&#x92f;&#x93e;&#x902;&#x91a;&#x94d;&#x92f;&#x93e;&#x938;&#x94b;&#x92c;&#x924; &#x915;&#x93e;&#x930;&#x94d;&#x92f; &#x915;&#x930;&#x923;&#x93e;&#x930;&#x94d;&#x200d;&#x92f;&#x93e;, &#x924;&#x94d;&#x92f;&#x93e;&#x902;&#x91a;&#x94d;&#x92f;&#x93e; &#x92d;&#x94b;&#x935;&#x924;&#x940; &#x905;&#x92d;&#x94d;&#x92f;&#x93e;&#x938; &#x915;&#x930;&#x923;&#x93e;&#x930;&#x94d;&#x200d;&#x92f;&#x93e; &#x906;&#x923;&#x93f; &#x930;&#x93e;&#x939;&#x923;&#x93e;&#x930;&#x94d;&#x200d;&#x92f;&#x93e; &#x92e;&#x93f;&#x924;&#x94d;&#x930;&#x93e;&#x902;&#x938;&#x94b;&#x92c;&#x924; &#x906;&#x923;&#x93f; &#x907;&#x924;&#x930;&#x93e;&#x902;&#x938;&#x94b;&#x92c;&#x924;..." /><meta name="robots" content="noodp,noydir" /><link rel="shortcut icon" href="https://static.xx.fbcdn.net/rsrc.php/yV/r/hzMapiNYYpW.ico" /><link type="text/css" rel="stylesheet" href="https://static.xx.fbcdn.net/rsrc.php/v3/yW/r/46cs9W_wqfX.css" data-bootloader-hash="q3yEk" data-permanent="1" crossorigin="anonymous" />
<link type="text/css" rel="stylesheet" href="https://static.xx.fbcdn.net/rsrc.php/v3/y0/r/PPmSgkSMZ9F.css" data-bootloader-hash="nfKia" data-permanent="1" crossorigin="anonymous" />
<link type="text/css" rel="stylesheet" href="https://static.xx.fbcdn.net/rsrc.php/v3/yH/r/ONdppvuaSOS.css" data-bootloader-hash="4LeXr" data-permanent="1" crossorigin="anonymous" />
<link type="text/css" rel="stylesheet" href="https://static.xx.fbcdn.net/rsrc.php/v3/yq/r/DZrkw4jae2B.css" data-bootloader-hash="P8uBt" data-permanent="1" crossorigin="anonymous" />
<link type="text/css" rel="stylesheet" href="https://static.xx.fbcdn.net/rsrc.php/v3/yE/r/CTLiHfEZFxN.css" data-bootloader-hash="9rG0r" data-permanent="1" crossorigin="anonymous" />
<script src="https://static.xx.fbcdn.net/rsrc.php/v3/yC/r/26RC12d8RE2.js" data-bootloader-hash="hhUgl" crossorigin="anonymous"></script>
<script>require("TimeSlice").guard(function() {(require("ServerJSDefine")).handleDefines([["URLFragmentPreludeConfig",[],{"incorporateQuicklingFragment":true,"hashtagRedirect":true},137],["BootloaderConfig",[],{"maxJsRetries":0,"jsRetries":null,"jsRetryAbortNum":2,"jsRetryAbortTime":5,"payloadEndpointURI":"https:\/\/www.facebook.com\/ajax\/haste-response\/","assumeNotNonblocking":false,"assumePermanent":false},329],["CurrentCommunityInitialData",[],{},490],["CurrentUserInitialData",[],{"USER_ID":"0","ACCOUNT_ID":"0"},270],["DTSGInitialData",[],{},258],["ISB",[],{},330],["LSD",[],{"token":"AVohJnkT"},323],["SiteData",[],{"revision":2885019,"tier":"","push_phase":"V2e","pkg_cohort":"PHASED:DEFAULT","pkg_cohort_key":"__pc","haste_site":"www","be_mode":-1,"be_key":"__be","is_rtl":false,"features":"iw","vip":"31.13.78.35"},317],["SprinkleConfig",[],{"param_name":"ttstamp"},2111],["CSSLoaderConfig",[],{"timeout":5000,"modulePrefix":"BLCSS:"},619],["LinkReactUnsafeHrefConfig",[],{"LinkHrefChecker":null},1182],["LinkshimHandlerConfig",[],{"supports_meta_referrer":false,"default_meta_referrer_policy":"default","switched_meta_referrer_policy":"origin","link_react_default_hash":"ATMucAmu5xDM4p8PF47Howomhecp0IcqGhu-aExSTsX-2tTIeBYAN1EbqSyUPIVAGaQJOor2O7dVuoud0wHkItgduUuiTzNG8paqO-zXNPW9wSsnZxBA6t0F","untrusted_link_default_hash":"ATOq7KYF0B9kp6dIArLVskLkacVkMdxlTjv6EthrejKXPINIHmZxxRXQrWAt7Aiz24n3FSMDTAvUBZfgtHnrLzP2TFt1YB7VgSd43RUgqI__vIkeek9Ln3wz","linkshim_host":"l.facebook.com","use_rel_no_opener":false,"always_use_https":false},27],["CdnAkamaiDomainsConfig",[],{"fbcdnhdsvideo-vh.akamaihd.net":0,"fbcdn-creative-a.akamaihd.net":1,"fbcdn-dragon-a.akamaihd.net":2,"fbcdn-external-a.akamaihd.net":3,"fbcdn-gtvideo-a-a.akamaihd.net":4,"fbcdn-gtvideo-b-a.akamaihd.net":5,"fbcdn-gtvideo-c-a.akamaihd.net":6,"fbcdn-gtvideo-d-a.akamaihd.net":7,"fbcdn-gtvideo-e-a.akamaihd.net":8,"fbcdn-gtvideo-f-a.akamaihd.net":9,"fbcdn-gtvideo-g-a.akamaihd.net":10,"fbcdn-gtvideo-h-a.akamaihd.net":11,"fbcdn-gtvideo-i-a.akamaihd.net":12,"fbcdn-gtvideo-j-a.akamaihd.net":13,"fbcdn-gtvideo-k-a.akamaihd.net":14,"fbcdn-gtvideo-l-a.akamaihd.net":15,"fbcdn-gtvideo-m-a.akamaihd.net":16,"fbcdn-gtvideo-n-a.akamaihd.net":17,"fbcdn-gtvideo-o-a.akamaihd.net":18,"fbcdn-gtvideo-p-a.akamaihd.net":19,"fbcdn-iphotos-a-a.akamaihd.net":20,"fbcdn-iphotos-a.akamaihd.net":21,"fbcdn-iphotos-b-a.akamaihd.net":22,"fbcdn-iphotos-c-a.akamaihd.net":23,"fbcdn-iphotos-d-a.akamaihd.net":24,"fbcdn-iphotos-e-a.akamaihd.net":25,"fbcdn-iphotos-f-a.akamaihd.net":26,"fbcdn-iphotos-g-a.akamaihd.net":27,"fbcdn-iphotos-h-a.akamaihd.net":28,"fbcdn-photos-a-a.akamaihd.net":29,"fbcdn-photos-a.akamaihd.net":30,"fbcdn-photos-b-a.akamaihd.net":31,"fbcdn-photos-c-a.akamaihd.net":32,"fbcdn-photos-d-a.akamaihd.net":33,"fbcdn-photos-e-a.akamaihd.net":34,"fbcdn-photos-f-a.akamaihd.net":35,"fbcdn-photos-g-a.akamaihd.net":36,"fbcdn-photos-h-a.akamaihd.net":37,"fbcdn-profile-a.akamaihd.net":38,"fbcdn-sphotos-a-a.akamaihd.net":39,"fbcdn-sphotos-b-a.akamaihd.net":40,"fbcdn-sphotos-c-a.akamaihd.net":41,"fbcdn-sphotos-d-a.akamaihd.net":42,"fbcdn-sphotos-e-a.akamaihd.net":43,"fbcdn-sphotos-f-a.akamaihd.net":44,"fbcdn-sphotos-g-a.akamaihd.net":45,"fbcdn-sphotos-h-a.akamaihd.net":46,"fbcdn-static-a.akamaihd.net":47,"fbcdn-video-a-a.akamaihd.net":48,"fbcdn-video-a.akamaihd.net":49,"fbcdn-video-b-a.akamaihd.net":50,"fbcdn-video-c-a.akamaihd.net":51,"fbcdn-video-d-a.akamaihd.net":52,"fbcdn-video-e-a.akamaihd.net":53,"fbcdn-video-f-a.akamaihd.net":54,"fbcdn-video-g-a.akamaihd.net":55,"fbcdn-video-h-a.akamaihd.net":56,"fbcdn-video-i-a.akamaihd.net":57,"fbcdn-video-j-a.akamaihd.net":58,"fbcdn-video-k-a.akamaihd.net":59,"fbcdn-video-l-a.akamaihd.net":60,"fbcdn-video-m-a.akamaihd.net":61,"fbcdn-video-n-a.akamaihd.net":62,"fbcdn-video-o-a.akamaihd.net":63,"fbcdn-video-p-a.akamaihd.net":64,"fbcdn-vthumb-a.akamaihd.net":65,"fbexternal-a.akamaihd.net":66,"fbstatic-a.akamaihd.net":67,"lookbackvideo1-a.akamaihd.net":68,"lookbackvideo2-a.akamaihd.net":69,"lookbackvideo3-a.akamaihd.net":70,"lookbackvideo4-a.akamaihd.net":71,"lookbackvideo5-a.akamaihd.net":72,"lookbackvideo6-a.akamaihd.net":73,"lookbackvideo7-a.akamaihd.net":74,"lookbackvideo8-a.akamaihd.net":75,"igexternal-a.akamaihd.net":76,"fbmentionslive-a.akamaihd.net":77,"fblive-a.akamaihd.net":78,"fbcdn-static-a-a.akamaihd.net":79,"fbcdn-static-b-a.akamaihd.net":80,"fb-s-a-a.akamaihd.net":81,"fb-s-b-a.akamaihd.net":82,"fb-s-c-a.akamaihd.net":83,"fb-s-d-a.akamaihd.net":84,"fb-l-a-a.akamaihd.net":85,"fb-l-b-a.akamaihd.net":86,"fb-l-c-a.akamaihd.net":87,"fb-l-d-a.akamaihd.net":88},1634],["CoreWarningGK",[],{"forceWarning":false},725],["BanzaiConfig",[],{"EXPIRY":86400000,"MAX_SIZE":10000,"MAX_WAIT":150000,"RESTORE_WAIT":150000,"blacklist":["time_spent"],"gks":{"boosted_component":true,"boosted_pagelikes":true,"boosted_posts":true,"boosted_website":true,"jslogger":true,"mercury_send_error_logging":true,"pages_client_logging":true,"platform_oauth_client_events":true,"useraction":true,"videos":true,"visibility_tracking":true,"graphexplorer":true,"gqls_web_logging":true,"sticker_search_ranking":true}},7],["UserAgentData",[],{"browserArchitecture":"32","browserFullVersion":null,"browserMinorVersion":null,"browserName":"Unknown","browserVersion":null,"deviceName":"Unknown","engineName":"Unknown","engineVersion":null,"platformArchitecture":"32","platformName":"Unknown","platformVersion":null,"platformFullVersion":null},527],["ZeroRewriteRules",[],{"rewrite_rules":{},"whitelist":{"\/hr\/r":1,"\/hr\/p":1,"\/zero\/unsupported_browser\/":1,"\/zero\/policy\/optin":1,"\/zero\/optin\/write\/":1,"\/zero\/optin\/legal\/":1,"\/zero\/optin\/free\/":1,"\/zero\/toggle\/welcome\/":1,"\/work\/landing":1,"\/work\/login\/":1,"\/work\/email\/":1,"\/ai.php":1,"\/js_dialog_resources\/dialog_descriptions_android.json":1,"\/connect\/jsdialog\/MPlatformAppInvitesJSDialog\/":1,"\/connect\/jsdialog\/MPlatformOAuthShimJSDialog\/":1,"\/connect\/jsdialog\/MPlatformLikeJSDialog\/":1,"\/qp\/interstitial\/":1,"\/qp\/action\/redirect\/":1,"\/qp\/action\/close\/":1,"\/zero\/support\/ineligible\/":1,"\/zero_balance_redirect\/":1,"\/zero_balance_redirect":1,"\/l.php":1,"\/lsr.php":1,"\/ajax\/dtsg\/":1,"\/checkpoint\/block\/":1,"\/exitdsite":1,"\/zero\/balance\/pixel\/":1,"\/zero\/balance\/":1,"\/zero\/balance\/carrier_landing\/":1,"\/tr":1,"\/tr\/":1,"\/sem_campaigns\/sem_pixel_test\/":1,"\/bookmarks\/flyout\/body\/":1,"\/zero\/subno\/":1}},1478],["AsyncFeatureDeployment",[],{},1765],["AsyncRequestConfig",[],{"retryOnNetworkError":"1","logAsyncRequest":false,"immediateDispatch":false},328],["SessionNameConfig",[],{"seed":"1xqj"},757],["ZeroCategoryHeader",[],{},1127],["TrackingConfig",[],{"domain":"https:\/\/pixel.facebook.com"},325],["WebSpeedExperiments",[],{"non_blocking_tracker":false,"non_blocking_logger":false},1160],["CookieCoreConfig",[],{"_ga":{"i":1,"t":63072000},"a11y":{"i":1},"act":{"i":1},"ar":{},"av":{},"bd":{},"bdluid":{},"bdsess":{},"rc":{"t":604800},"bustcache":{"i":1,"t":1},"bva":{},"c_user":{},"campaign_click_url":{"t":2592000},"cavalry_cohort":{},"checkpoint":{},"csm":{"i":1},"csrf":{},"datr":{"i":1,"t":63072000},"dbln":{"p":"\/login\/device-based\/","t":63072000},"dch":{},"ddid":{"p":"\/deferreddeeplink\/","t":2419200},"dnonce":{"i":1},"dpr":{},"employee_login":{"t":2592000},"hckd":{},"i_id":{"i":1},"i_key":{"i":1},"i_user":{},"js_ver":{"t":604800},"locale":{"i":1,"t":604800},"lp":{},"lp3":{},"lu":{"t":63072000},"m_pixel_ratio":{},"m_ts":{"i":1},"m_user":{"i":1,"t":7776000},"mv":{"i":1},"next":{"i":1},"next_path":{"i":1},"noscript":{"i":1},"oo":{"i":1,"t":158284800},"p":{"i":1},"pl":{},"pnl_data":{"i":1},"presence":{},"reg_ext_ref":{},"reg_fb_gate":{},"reg_fb_ref":{},"reg_uniqid":{"i":1},"sW":{},"sb":{"t":63072000},"sfiu":{"i":1},"sfau":{},"smurf":{},"tokbind":{"t":86400},"wd":{},"x-referer":{},"x-src":{"t":1},"xs":{},"xtrn":{"t":63072000},"fr":{"i":1}},2104],["ErrorSignalConfig",[],{"uri":"https:\/\/error.facebook.com\/common\/scribe_endpoint.php"},319],["EventConfig",[],{"sampling":{"bandwidth":0,"play":0,"playing":0,"progress":0,"pause":0,"ended":0,"seeked":0,"seeking":0,"waiting":0,"loadedmetadata":0,"canplay":0,"selectionchange":0,"change":0,"timeupdate":2000000,"adaptation":0,"focus":0,"blur":0,"load":0,"error":0,"message":0,"abort":0,"storage":0,"scroll":10000,"mousemove":20000,"mouseover":10000,"mouseout":10000,"mousewheel":20000,"MSPointerMove":10000,"keydown":0.1,"click":0.01,"__100ms":0.001,"__default":100000,"__min":1000}},1726],["ServerNonce",[],{"ServerNonce":"qawkQMEomK_-PBTautaaL4"},141],["ReactFiberErrorLoggerConfig",[],{"bugNubClickTargetClassName":null},2115],["ReactGK",[],{"logTopLevelRenders":false,"domIsFiber":false,"domIsFiberInUFI":false,"prepareNewChildrenBeforeUnmountInStack":true},998],["PhotoSnowliftActionsGating",[],{"ALLOW_MAKE_PROFILE_PICTURE_BUTTON":false,"skipUnfixed":false},887],["AccessibilityConfig",[],{"a11yLogicalGridComponent":false,"a11yNewsfeedStoryEnumeration":false,"a11yInitialDialogFocusElement":true,"a11yNUXDialog":false},1227],["TimeSliceInteractionCoinflips",[],{"default_rate":1000,"lite_default_rate":100,"interaction_to_lite_coinflip":{"Event":100},"interaction_to_coinflip":{"async_request":0,"video_psr":1,"video_stall":25,"snowlift_open_autoclosed":0,"Event":2,"cms_editor":1,"page_messaging_shortlist":1},"enable_heartbeat":true},1799],["ServiceWorkerBackgroundSyncBanzaiGK",[],{"sw_background_sync_banzai":false},1621],["FbtLogger",[],{"logger":null},288],["FbtResultGK",[],{"shouldReturnFbtResult":true,"inlineMode":"NO_INLINE"},876],["IntlViewerContext",[],{"GENDER":50331648},772],["IntlPhonologicalRules",[],{},1496],["ArtilleryExperiments",[],{"artillery_timeslice_edges":false,"artillery_static_resources_pagelet_attribution":false,"artillery_timeslice_compressed_data":false,"artillery_miny_client_payload":false},1237],["ServiceWorkerBackgroundSyncGK",[],{"background_sync_sw":false},1628],["PageNavigationStageLoggerGK",[],{"gk_check":false},1434],["PageTransitionsConfig",[],{"reloadOnBootloadError":true},1067],["InitialServerTime",[],{"serverTime":1489213892000},204],["UFIReactionTypes",[],{"LIKE":1,"ordering":[1,2,13,11,4,5,3,10,12,7,8,14,15],"NONE":0,"reactions":{"1":{"class_name":"_3j7l","color":"#5890ff","display_name":"\u0906\u0935\u0921\u0932\u0947","is_deprecated":false,"is_visible":true,"name":"like","type":1},"2":{"class_name":"_3j7m","color":"#f25268","display_name":"\u091d\u0915\u093e\u0938","is_deprecated":false,"is_visible":true,"name":"love","type":2},"13":{"class_name":null,"color":"#1d2129","display_name":"\u0938\u0947\u0932\u094d\u092b\u0940","is_deprecated":false,"is_visible":false,"name":"selfie","type":13},"11":{"class_name":"_3rya","color":"#9c87d1","display_name":"\u090b\u0923\u0940","is_deprecated":false,"is_visible":true,"name":"dorothy","type":11},"4":{"class_name":"_3j7o","color":"#f0ba15","display_name":"\u092e\u091c\u0947\u0936\u0940\u0930","is_deprecated":false,"is_visible":true,"name":"haha","type":4},"5":{"class_name":"_3j7p","color":"#f0ba15","display_name":"\u0905\u092d\u093f\u0928\u0902\u0926\u0928","is_deprecated":true,"is_visible":true,"name":"yay","type":5},"3":{"class_name":"_3j7n","color":"#f0ba15","display_name":"\u0935\u094d\u200d\u0935\u093e","is_deprecated":false,"is_visible":true,"name":"wow","type":3},"10":{"class_name":"_3j7s","color":"#f0ba15","display_name":"\u0917\u094b\u0902\u0927\u0933\u0932\u0947\u0932\u0947","is_deprecated":true,"is_visible":true,"name":"confused","type":10},"12":{"class_name":null,"color":"#f0ba15","display_name":"\u0906\u0935\u0921\u0932\u0947","is_deprecated":false,"is_visible":false,"name":"toto","type":12},"7":{"class_name":"_3j7r","color":"#f0ba15","display_name":"\u0909\u0926\u093e\u0938","is_deprecated":false,"is_visible":true,"name":"sorry","type":7},"8":{"class_name":"_3j7q","color":"#f7714b","display_name":"\u0930\u093e\u0917\u0940\u091f","is_deprecated":false,"is_visible":true,"name":"anger","type":8},"14":{"class_name":"_3qr6","color":"#f0ba15","display_name":"\u0906\u0935\u0921\u0932\u0947","is_deprecated":false,"is_visible":false,"name":"flame","type":14},"15":{"class_name":"_4vps","color":"#5890ff","display_name":"\u0906\u0935\u0921\u0932\u0947","is_deprecated":false,"is_visible":false,"name":"plane","type":15}}},911],["MercuryConfig",[],{},35],["NumberFormatConfig",[],{"decimalSeparator":".","numberDelimiter":",","minDigitsForThousandsSeparator":4,"switchImplementationGK":false},54],["NYE2017AnimationTriggerSettings",[],{"shouldTriggerOnPost":false,"shouldTriggerOnComment":false},1992],["NYE2017TriggerStringsLoader",[],{"regex":"(test1|test2|test3|xoxo|love you|i love you)"},1994],["EmojiInputButtonContainer",[],{"EmojiInputButton":null},2057],["UFICommentFileInputAcceptValues",[],{"both":"video\/*,  video\/x-m4v, video\/webm, video\/x-ms-wmv, video\/x-msvideo, video\/3gpp, video\/flv, video\/x-flv, video\/mp4, video\/quicktime, video\/mpeg, video\/ogv, image\/*","photos":"image\/*","videos":"video\/*, video\/x-m4v, video\/webm, video\/x-ms-wmv, video\/x-msvideo, video\/3gpp, video\/flv, video\/x-flv, video\/mp4, video\/quicktime, video\/mpeg, video\/ogv"},1317],["VideoUploadConfig",[],{"videoExtensions":{"mov":1,"qt":1,"wmv":1,"avi":1,"mpe":1,"mpg":1,"mpeg":1,"asf":1,"mp4":1,"m4v":1,"mpeg4":1,"3gpp":1,"3gp":1,"3g2":1,"mkv":1,"flv":1,"vob":1,"ogm":1,"ogv":1,"nsv":1,"mod":1,"tod":1,"dat":1,"mts":1,"m2ts":1,"dv":1,"divx":1,"f4v":1,"ts":1,"tmp":1,"rmvb":1,"webm":1},"allowMultimedia":false,"showMultimediaNUX":false},267],["FileHashWorkerResource",[],{"url":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yD\/r\/QFUi5Mdnwnk.js","name":"FileHashWorkerBundle"},758],["WebWorkerConfig",[],{"logging":{"enabled":false,"config":"WebWorkerLoggerConfig"},"evalWorkerURL":"\/rsrc.php\/v3\/y1\/r\/OCH9Nbs549d.js"},297],["FluxInternalConfig",[],{"logOnPreInitAccess":false,"warnOnPreInitAccess":false},1075],["StickersConfig",[],{"emoticons":{"id":"1471127876485636","name":"\u092d\u093e\u0935\u091a\u093f\u0928\u094d\u0939\u0947","isCommentsCapable":true},"max_mru_stickers":40,"mru_pack":{"id":"599061016853145","name":"\u0905\u0932\u0940\u0915\u0921\u0947","isMRU":true,"isCommentsCapable":true,"isComposerCapable":true,"isMessengerCapable":true,"isPostsCapable":true},"oz_pack":null},1666],["RelayAPIConfigDefaults",["__inst_84473062_0_0","__inst_84473062_0_1"],{"accessToken":null,"actorID":"0","fetchTimeout":30000,"graphBatchURI":{"__m":"__inst_84473062_0_0"},"graphURI":{"__m":"__inst_84473062_0_1"},"retryDelays":[1000,3000],"useXController":true,"xhrEncoding":null},926],["PresenceInitialData",[],{"cookiePollInterval":500,"cookieVersion":3,"serverTime":"1489213892000","shouldSuppress":false,"dictEncode":true},57],["WorkModeConfig",[],{},396],["CurrentEnvironment",[],{"facebookdotcom":true,"messengerdotcom":false},827],["WorkGKs",[],{"work_admin_azure_import":false,"work_admin_disable_gsuite":false,"work_admin_gsuite_1click_import":false,"work_admin_hide_date_claimed_column":false,"work_admin_new_deactivate_users":false,"work_admin_new_setting_design":true,"work_admin_provision_apps_viewer":false,"work_admin_setup_payment_information":false,"work_admin_sidebar_numbers":true,"work_admin_bulk_edit_users":false,"workplace_www_chat_branding":false},1734],["PaddedStickerConfig",[],{},1667],["CanvasToBlobResource",[],{"url":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yy\/r\/hSCwcG2ckQh.js","name":"CanvasToBlobBundle"},864],["VideoThumbnailConfig",[],{"defaultThumbnailURL":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yN\/r\/AAqMW82PqGg.gif"},967],["FunnelLoggerConfig",[],{"freq":{"CREATIVE_STUDIO_CREATION_FUNNEL":1,"WWW_CANVAS_AD_CREATION_FUNNEL":1,"WWW_CANVAS_EDITOR_FUNNEL":1,"WWW_LINK_PICKER_DIALOG_FUNNEL":1,"WWW_MEME_PICKER_DIALOG_FUNNEL":1,"WWW_LEAD_GEN_FORM_CREATION_FUNNEL":1,"WWW_LEAD_GEN_DESKTOP_AD_UNIT_FUNNEL":1,"WWW_LEAD_GEN_MSITE_AD_UNIT_FUNNEL":1,"WWW_CAMPFIRE_COMPOSER_UPSELL_FUNNEL":1,"WWW_RECRUITING_SEARCH_FUNNEL":1,"WWW_EXAMPLE_FUNNEL":1,"WWW_REACTIONS_NUX_FUNNEL":1,"WWW_MESSENGER_SHARE_TO_FB_FUNNEL":10,"POLYGLOT_MAIN_FUNNEL":1,"MSITE_EXAMPLE_FUNNEL":10,"WWW_FEED_SHARE_DIALOG_FUNNEL":100,"MSITE_FEED_ALBUM_CTA_FUNNEL":10,"MSITE_FEED_SHARE_DIALOG_FUNNEL":100,"MSITE_COMMENT_TYPING_FUNNEL":500,"MSITE_HASHTAG_PROMPT_FUNNEL":1,"WWW_SEARCH_AWARENESS_LEARNING_NUX_FUNNEL":1,"WWW_CONSTITUENT_TITLE_UPSELL_FUNNEL":1,"MTOUCH_FEED_MISSED_STORIES_FUNNEL":10,"WWW_UFI_SHARE_LINK_FUNNEL":1,"WWW_CMS_SEARCH_FUNNEL":1,"GAMES_QUICKSILVER_FUNNEL":1,"SOCIAL_SEARCH_CONVERSION_WWW_FUNNEL":1,"SOCIAL_SEARCH_DASHBOARD_WWW_FUNNEL":1,"SRT_USER_FLOW_FUNNEL":1,"MSITE_PPD_FUNNEL":1,"WWW_PAGE_CREATION_FUNNEL":1,"NT_EXAMPLE_FUNNEL":1,"WWW_LIVE_VIEWER_TIPJAR_FUNNEL":1,"FACECAST_BROADCASTER_FUNNEL":1,"WWW_FUNDRAISER_CREATION_FUNNEL":1,"WWW_FUNDRAISER_EDIT_FUNNEL":1,"WWW_OFFERS_SIMPLE_COMPOSE_FUNNEL":1,"default":1000}},1271],["MarauderConfig",[],{"app_version":2885019,"gk_enabled":false},31],["GroupsProductDetailGating",[],{"tuzi_dialog":null},1461],["WWWBase",[],{"uri":"https:\/\/www.facebook.com\/"},318],["PhotoSnowliftLoggingConfig",[],{"logOnInit":true},2078],["VideoPlayerAbortLoadingExperiment",[],{"canAbort":false,"delayedAbortLoading":0},824],["TypeaheadMetricsConfig",[],{"gkResults":false},263],["EmojiConfig",[],{"aliases":{},"hasFBEmoji":true,"hasFBEmojiInComposer":false,"pixelRatio":"1","schemaAuth":"https:\/\/static.xx.fbcdn.net\/images\/emoji.php\/v7"},1421],["FamilyMentionsData",[],{"allowFamilyNames":false,"hasAcceptedNUX":false},708],["NYE2017CommentSettings",[],{"shouldAnimate":false,"shouldHighlight":false},1986],["UFISpamCountImpl",[],{"module":null},72],["BigPipeExperiments",[],{"preparse_content":"","link_images_to_pagelets":false,"enable_bigpipe_plugins":false},907],["FbtQTOverrides",[],{"overrides":{}},551],["UFIConfig",[],{"commentVPVD":{"debug_console":false,"debug_html":false,"idle_timeout":5000,"locations":["permalink","newsstand"],"everywhere":true,"min_duration_to_log":100,"min_visible_size":200},"enableCommentListVisibilityTracking":false,"defaultPageSize":50,"renderEmoji":true,"renderEmoticons":true,"shouldShowStickerNUX":false,"shouldShowVideosInCommentsNux":false,"shouldShowMarkdownCommentNUX":false,"shouldShowHideConstituentTitleNUX":false,"shouldShowOwnerConstituentTitleNUX":false,"vpvLoggingTimeout":1000,"facecastWWWCommentQueueThreshold":3,"canPublishLive":false,"logChangeOrderingModeUsageSampleRate":1,"logCommentsTimespent":true,"logWhetherUFISeen":false,"showHashtagTypeahead":false,"reshareedu":true,"logCommentPost":false,"logCommentLoad":false,"reactionsHasDirectReactTokens":false,"reactionsHasDirectReactTokensCounts":false,"reactionsDirectReactTokensModule":null,"reactionsFunnelLogger":null,"reactionsHasFunnelLogger":false,"reactionsHasCommentFunnelLogger":false,"reactionsHasCommentsNux":false,"reactionsHasTooltipBreakdown":false,"reactionsHasMegaDock":false,"reactionsPopupDockAnimationDuration":700,"reactionsHasAnimatedVectorDock":false,"reactionsHasAnimatedIconsOnHover":false,"reactionsHasStaticVectorDock":false,"reactionsHasStaticFileVectorDock":false,"reactionsHasThemes":false,"reactionsTheme":null,"reactionsHasSuggestedReaction":false,"reactionsHasReactionsRollback":true,"reactionsHasCommentReactionsRollback":true,"reactionsHasReactionsRetry":true,"reactionsHasCommentReactionsRetry":true,"reactionsHasCompactCommentBling":false,"reactionsHasSharedCommentBlingTooltip":false,"reactionsHasShorterCommentDockHotspot":false,"reactionsHasCommentDockBelow":false,"reactionsHasReactionLinkPerfFixes":false,"hasBounceOnLikeOrReaction":false,"showCommentEmbedOption":true,"showLiveVideoAnnoucements":false,"alwaysPreviewSticker":false,"publicConversationsUnicornWhitelist":false,"typingIndicator":{"subscribe":false,"showInline":false,"showPill":false,"fromEveryone":false},"maxSubscriptionLiveCommentsQueueLength":10,"showChooseLoveAnimation":false,"feedfocusWrapperModule":null,"shouldTranslationsReplaceContent":true,"shouldLogFacecastStreamingCommentDelay":false,"showUFICrowdsource":false,"flushEventQueueBeforeRenderTimeout":0,"flushEventQueueBeforeRenderUseIdleCallback":false,"hasFaceliftCommentComposerIcons":false,"prefetchTextTriggerAnimation":false,"UFICommentFilterFallbackWarning":null},71]]);new (require("ServerJS"))().setServerFeatures("iw").handle({"instances":[["__inst_84473062_0_0",["URI"],["\/api\/graphqlbatch\/"],1],["__inst_84473062_0_1",["URI"],["\/api\/graphql\/"],1]],"require":[["TimeSlice"],["markJSEnabled"],["lowerDomain"],["URLFragmentPrelude"],["Primer"],["BigPipe"],["Bootloader"],["TimeSlice","disablePageHeartbeat",[],[],[]]]});}, "ServerJS define", {"root":true})();</script></head><body class="fbIndex UIPage_LoggedOut b_c3pyn-ahh x1 Locale_mr_IN" dir="ltr"><div class="_li"><div id="pagelet_bluebar" data-referrer="pagelet_bluebar"><div id="blueBarDOMInspector"><div class="_53jh"><div class="loggedout_menubar_container"><div class="clearfix loggedout_menubar"><div class="lfloat _ohe"><h1><a href="https://www.facebook.com/" title="Facebook &#x91a;&#x94d;&#x92f;&#x93e; &#x92e;&#x941;&#x916;&#x92a;&#x943;&#x937;&#x94d;&#x920;&#x93e;&#x935;&#x930; &#x91c;&#x93e;"><i class="fb_logo img sp_Mlxwn39jCAE sx_896ebb"><u>Facebook</u></i></a></h1></div><div class="menu_login_container rfloat _ohf"><form id="login_form" action="https://www.facebook.com/login.php?login_attempt=1&amp;lwv=110" method="post" novalidate="1" onsubmit="return window.Event &amp;&amp; Event.__inlineSubmit &amp;&amp; Event.__inlineSubmit(this,event)"><input type="hidden" name="lsd" value="AVohJnkT" autocomplete="off" /><table cellspacing="0" role="presentation"><tr><td class="html7magic"><label for="email">ईमेल किंवा फोन</label></td><td class="html7magic"><label for="pass">पासवर्ड</label></td></tr><tr><td><input type="email" class="inputtext" name="email" id="email" value="" tabindex="1" /></td><td><input type="password" class="inputtext" name="pass" id="pass" tabindex="2" /></td><td><label class="uiButton uiButtonConfirm" style="" id="loginbutton" for="u_0_q"><input value="&#x932;&#x949;&#x917; &#x907;&#x928;" tabindex="4" type="submit" id="u_0_q" /></label></td></tr><tr><td class="login_form_label_field"></td><td class="login_form_label_field"><div><a href="https://www.facebook.com/recover/initiate?lwv=110" data-testid="forgot_account_link">खाते विसरलात?</a></div></td></tr></table><input type="hidden" autocomplete="off" name="timezone" value="" id="u_0_r" /><input type="hidden" autocomplete="off" name="lgndim" value="" id="u_0_s" /><input type="hidden" name="lgnrnd" value="223132_pqq1" /><input type="hidden" id="lgnjs" name="lgnjs" value="n" /><input type="hidden" autocomplete="off" name="ab_test_data" value="" /><input type="hidden" autocomplete="off" id="locale" name="locale" value="mr_IN" /><input type="hidden" autocomplete="off" name="next" value="https://www.facebook.com/" /></form></div></div></div></div></div></div><div id="globalContainer" class="uiContextualLayerParent"><div class="fb_content clearfix " id="content" role="main"><div><div class="gradient"><div class="gradientContent"><div class="clearfix"><div class="lfloat _ohe"><div class="_5iyy"><div class="_5iyx">Facebook  आपल्याला आपल्या जीवनातील लोकांशी संपर्क साधण्यास मदत करते.</div><img class="img" src="https://static.xx.fbcdn.net/rsrc.php/v3/yx/r/pyNVUg5EM0j.png" alt="" width="537" height="195" /></div></div><div class="_5iyz rfloat _ohf"><div class="pvl _52lp _59d-"><div class="mbs _52lq fsl fwb fcb">साइन अप</div><div class="_52lr fsm fwn fcg">हे नि:शुल्क आहे, आणि नेहमीच असणार.</div></div><div id="registration_container"><div><noscript><div id="no_js_box"><h2>आपल्या ब्राउझरवर JavaScript अक्षम केलेले आहे.</h2><p>कृपया आपल्या ब्राउझरवर JavaScript सक्षम करा किंवा Facebook करिता नोंदणी करण्यासाठी एका JavaScript-सक्षम ब्राउझरवर श्रेणीसुधारित करा.</p></div></noscript><div class="_58mf"><div id="reg_box" class="registration_redesign"><div><div id="reg_error" class="hidden_elem _58mn" role="alert"><div class="_58mo" id="reg_error_inner" tabindex="0">त्रुटी आढळली. कृपया पुन्हा प्रयत्न करा.</div></div><form method="post" id="reg" name="reg" action="https://m.facebook.com/reg/" onsubmit="return function(event)&#123;return false;&#125;.call(this,event)!==false &amp;&amp; window.Event &amp;&amp; Event.__inlineSubmit &amp;&amp; Event.__inlineSubmit(this,event)"><input type="hidden" name="lsd" value="AVohJnkT" autocomplete="off" /><div id="reg_form_box" class="large_form"><div id="fullname_field" class="_1ixn"><div class="clearfix _58mh"><div class="mbm _1iy_ _a4y _3-90 lfloat _ohe"><div class="_5dbb" id="u_0_0"><input type="text" class="inputtext _58mg _5dba _2ph-" data-type="text" name="firstname" aria-required="1" placeholder="&#x928;&#x93e;&#x935;" id="u_0_1" aria-label="&#x928;&#x93e;&#x935;" /><i class="_5dbc img sp_CKdQ8U6gnwd sx_c195a4"></i><i class="_5dbd img sp_CKdQ8U6gnwd sx_4c0d6b"></i><i class="_1iz9 img sp_CKdQ8U6gnwd sx_1a9653"></i><div class="_1pc_"></div></div></div><div class="mbm _1iy_ _a4y rfloat _ohf"><div class="_5dbb" id="u_0_2"><input type="text" class="inputtext _58mg _5dba _2ph-" data-type="text" name="lastname" aria-required="1" placeholder="&#x906;&#x921;&#x928;&#x93e;&#x935;" id="u_0_3" aria-label="&#x906;&#x921;&#x928;&#x93e;&#x935;" /><i class="_5dbc img sp_CKdQ8U6gnwd sx_c195a4"></i><i class="_5dbd img sp_CKdQ8U6gnwd sx_4c0d6b"></i><i class="_1iz9 img sp_CKdQ8U6gnwd sx_1a9653"></i><div class="_1pc_"></div></div></div></div><div class="_1pc_" id="fullname_error_msg"></div></div><div class="mbm _a4y" id="u_0_4"><div class="_5dbb" id="u_0_5"><input type="text" class="inputtext _58mg _5dba _2ph-" data-type="text" name="reg_email__" aria-required="1" placeholder="&#x92e;&#x94b;&#x92c;&#x93e;&#x908;&#x932; &#x928;&#x902;&#x92c;&#x930; &#x915;&#x93f;&#x902;&#x935;&#x93e; &#x908;&#x92e;&#x947;&#x932;" id="u_0_6" aria-label="&#x92e;&#x94b;&#x92c;&#x93e;&#x908;&#x932; &#x928;&#x902;&#x92c;&#x930; &#x915;&#x93f;&#x902;&#x935;&#x93e; &#x908;&#x92e;&#x947;&#x932;" /><i class="_5dbc img sp_CKdQ8U6gnwd sx_c195a4"></i><i class="_5dbd img sp_CKdQ8U6gnwd sx_4c0d6b"></i><i class="_1iz9 img sp_CKdQ8U6gnwd sx_1a9653"></i><div class="_1pc_"></div></div></div><div id="u_0_7"><div class="mbm _a4y"><div class="_5dbb" id="u_0_8"><input type="text" class="inputtext _58mg _5dba _2ph-" data-type="text" name="reg_email_confirmation__" aria-required="1" placeholder="&#x92e;&#x94b;&#x92c;&#x93e;&#x908;&#x932; &#x928;&#x902;&#x92c;&#x930; &#x915;&#x93f;&#x902;&#x935;&#x93e; &#x908;&#x92e;&#x947;&#x932; &#x92a;&#x941;&#x928;&#x94d;&#x200d;&#x939;&#x93e;-&#x92a;&#x94d;&#x930;&#x935;&#x93f;&#x937;&#x94d;&#x200d;&#x91f; &#x915;&#x930;&#x93e;" id="u_0_9" aria-label="&#x92e;&#x94b;&#x92c;&#x93e;&#x908;&#x932; &#x928;&#x902;&#x92c;&#x930; &#x915;&#x93f;&#x902;&#x935;&#x93e; &#x908;&#x92e;&#x947;&#x932; &#x92a;&#x941;&#x928;&#x94d;&#x200d;&#x939;&#x93e;-&#x92a;&#x94d;&#x930;&#x935;&#x93f;&#x937;&#x94d;&#x200d;&#x91f; &#x915;&#x930;&#x93e;" /><i class="_5dbc img sp_CKdQ8U6gnwd sx_c195a4"></i><i class="_5dbd img sp_CKdQ8U6gnwd sx_4c0d6b"></i><i class="_1iz9 img sp_CKdQ8U6gnwd sx_1a9653"></i><div class="_1pc_"></div></div></div></div><div class="mbm _registrationForm__inputContainer hidden_elem" id="u_0_a"><input type="text" class="inputtext _58mg _5dba _2ph-" data-type="text" name="reg_second_contactpoint__" placeholder="&#x92e;&#x94b;&#x92c;&#x93e;&#x908;&#x932; &#x928;&#x902;&#x92c;&#x930;" id="u_0_b" aria-label="&#x92e;&#x94b;&#x92c;&#x93e;&#x908;&#x932; &#x928;&#x902;&#x92c;&#x930;" /></div><div class="mbm _registrationForm__inputContainer" id="password_field"><div class="_5dbb" id="u_0_c"><input type="password" class="inputtext _58mg _5dba _2ph-" data-type="text" name="reg_passwd__" aria-required="1" placeholder="&#x928;&#x935;&#x940;&#x928; &#x92a;&#x93e;&#x938;&#x935;&#x930;&#x94d;&#x921;" id="u_0_d" aria-label="&#x928;&#x935;&#x940;&#x928; &#x92a;&#x93e;&#x938;&#x935;&#x930;&#x94d;&#x921;" /><i class="_5dbc img sp_CKdQ8U6gnwd sx_c195a4"></i><i class="_5dbd img sp_CKdQ8U6gnwd sx_4c0d6b"></i><i class="_1iz9 img sp_CKdQ8U6gnwd sx_1a9653"></i><div class="_1pc_"></div></div></div><div class="_58mq _5dbb" id="u_0_e"><div class="mtm mbs _2_68">वाढदिवस</div><div class="_5k_5"><span class="_5k_4" data-type="selectors" data-name="birthday_wrapper" id="u_0_f"><span><select aria-label="&#x926;&#x93f;&#x935;&#x938;" name="birthday_day" id="day" title="&#x926;&#x93f;&#x935;&#x938;" class="_5dba"><option value="0" selected="1">दिवस</option><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option><option value="7">7</option><option value="8">8</option><option value="9">9</option><option value="10">10</option><option value="11">11</option><option value="12">12</option><option value="13">13</option><option value="14">14</option><option value="15">15</option><option value="16">16</option><option value="17">17</option><option value="18">18</option><option value="19">19</option><option value="20">20</option><option value="21">21</option><option value="22">22</option><option value="23">23</option><option value="24">24</option><option value="25">25</option><option value="26">26</option><option value="27">27</option><option value="28">28</option><option value="29">29</option><option value="30">30</option><option value="31">31</option></select><select aria-label="&#x92e;&#x939;&#x93f;&#x928;&#x93e;" name="birthday_month" id="month" title="&#x92e;&#x939;&#x93f;&#x928;&#x93e;" class="_5dba"><option value="0" selected="1">महिना</option><option value="1">जाने</option><option value="2">फेब्रु</option><option value="3">मार्च</option><option value="4">एप्रिल</option><option value="5">मे</option><option value="6">जून</option><option value="7">जुलै</option><option value="8">ऑग</option><option value="9">सप्टें</option><option value="10">ऑक्टो</option><option value="11">नोव्हें</option><option value="12">डिसें</option></select><select aria-label="&#x935;&#x930;&#x94d;&#x937;" name="birthday_year" id="year" title="&#x935;&#x930;&#x94d;&#x937;" class="_5dba"><option value="0" selected="1">वर्ष</option><option value="2017">2017</option><option value="2016">2016</option><option value="2015">2015</option><option value="2014">2014</option><option value="2013">2013</option><option value="2012">2012</option><option value="2011">2011</option><option value="2010">2010</option><option value="2009">2009</option><option value="2008">2008</option><option value="2007">2007</option><option value="2006">2006</option><option value="2005">2005</option><option value="2004">2004</option><option value="2003">2003</option><option value="2002">2002</option><option value="2001">2001</option><option value="2000">2000</option><option value="1999">1999</option><option value="1998">1998</option><option value="1997">1997</option><option value="1996">1996</option><option value="1995">1995</option><option value="1994">1994</option><option value="1993">1993</option><option value="1992">1992</option><option value="1991">1991</option><option value="1990">1990</option><option value="1989">1989</option><option value="1988">1988</option><option value="1987">1987</option><option value="1986">1986</option><option value="1985">1985</option><option value="1984">1984</option><option value="1983">1983</option><option value="1982">1982</option><option value="1981">1981</option><option value="1980">1980</option><option value="1979">1979</option><option value="1978">1978</option><option value="1977">1977</option><option value="1976">1976</option><option value="1975">1975</option><option value="1974">1974</option><option value="1973">1973</option><option value="1972">1972</option><option value="1971">1971</option><option value="1970">1970</option><option value="1969">1969</option><option value="1968">1968</option><option value="1967">1967</option><option value="1966">1966</option><option value="1965">1965</option><option value="1964">1964</option><option value="1963">1963</option><option value="1962">1962</option><option value="1961">1961</option><option value="1960">1960</option><option value="1959">1959</option><option value="1958">1958</option><option value="1957">1957</option><option value="1956">1956</option><option value="1955">1955</option><option value="1954">1954</option><option value="1953">1953</option><option value="1952">1952</option><option value="1951">1951</option><option value="1950">1950</option><option value="1949">1949</option><option value="1948">1948</option><option value="1947">1947</option><option value="1946">1946</option><option value="1945">1945</option><option value="1944">1944</option><option value="1943">1943</option><option value="1942">1942</option><option value="1941">1941</option><option value="1940">1940</option><option value="1939">1939</option><option value="1938">1938</option><option value="1937">1937</option><option value="1936">1936</option><option value="1935">1935</option><option value="1934">1934</option><option value="1933">1933</option><option value="1932">1932</option><option value="1931">1931</option><option value="1930">1930</option><option value="1929">1929</option><option value="1928">1928</option><option value="1927">1927</option><option value="1926">1926</option><option value="1925">1925</option><option value="1924">1924</option><option value="1923">1923</option><option value="1922">1922</option><option value="1921">1921</option><option value="1920">1920</option><option value="1919">1919</option><option value="1918">1918</option><option value="1917">1917</option><option value="1916">1916</option><option value="1915">1915</option><option value="1914">1914</option><option value="1913">1913</option><option value="1912">1912</option><option value="1911">1911</option><option value="1910">1910</option><option value="1909">1909</option><option value="1908">1908</option><option value="1907">1907</option><option value="1906">1906</option><option value="1905">1905</option></select></span></span><a class="mlm _58ms" id="birthday-help" href="#" ajaxify="/help/ajax/reg_birthday/" title="&#x905;&#x927;&#x93f;&#x915; &#x92e;&#x93e;&#x939;&#x93f;&#x924;&#x940;&#x915;&#x930;&#x93f;&#x924;&#x93e; &#x915;&#x94d;&#x932;&#x93f;&#x915; &#x915;&#x930;&#x93e;" rel="async" role="button">मला माझी जन्मतारीख देण्याची गरज का आहे?</a><i class="_5dbc _5k_6 img sp_CKdQ8U6gnwd sx_c195a4"></i><i class="_5dbd _5k_7 img sp_CKdQ8U6gnwd sx_4c0d6b"></i><i class="_1iz9 _3jb- img sp_CKdQ8U6gnwd sx_1a9653"></i><div class="_1pc_"></div></div></div><div class="mtm _5wa2 _5dbb" id="u_0_m"><span class="_5k_3" data-type="radio" data-name="gender_wrapper" id="u_0_n"><span class="_5k_2 _5dba"><input type="radio" name="sex" value="1" id="u_0_k" /><label class="_58mt" for="u_0_k">स्त्री</label></span><span class="_5k_2 _5dba"><input type="radio" name="sex" value="2" id="u_0_l" /><label class="_58mt" for="u_0_l">पुरूष</label></span></span><i class="_5dbc _5k_6 img sp_CKdQ8U6gnwd sx_c195a4"></i><i class="_5dbd _5k_7 img sp_CKdQ8U6gnwd sx_4c0d6b"></i><i class="_1iz9 _3jb- img sp_CKdQ8U6gnwd sx_1a9653"></i><div class="_1pc_"></div></div><div class="_58mu" data-nocookies="1" id="u_0_g"><p class="_58mv">खाते तयार करा क्लिक करण्याने, आमचे <a href="/policies/cookies/" id="cookie-use-link" target="_blank" rel="nofollow">कुकी वापर</a> समाविष्टित तुम्ही आमच्या <a href="/legal/terms" id="terms-link" target="_blank" rel="nofollow">अटी</a> सहमती दर्शवता आणि याचा अर्थ तुम्ही आमची <a href="/about/privacy" id="privacy-link" target="_blank" rel="nofollow">डेटा धोरण</a> वाचलेली आहे. तुम्हाला Facebook कडून SMS सूचना प्राप्त होवू शकतात आणि त्यातून तुम्ही कोणत्याही वेळी बाहेर पडू शकता.</p></div><div class="clearfix"><button type="submit" class="_6j mvm _6wk _6wl _58mi _6o _6v" name="websubmit" id="u_0_h">खाते तयार करा</button><span class="hidden_elem _58ml" id="u_0_o"><img class="img" src="https://static.xx.fbcdn.net/rsrc.php/v3/yb/r/GsNJNwuI-UM.gif" alt="" width="16" height="11" /></span></div></div><input type="hidden" autocomplete="off" id="referrer" name="referrer" value="" /><input type="hidden" autocomplete="off" id="asked_to_login" name="asked_to_login" value="0" /><input type="hidden" autocomplete="off" id="terms" name="terms" value="on" /><input type="hidden" autocomplete="off" id="contactpoint_label" name="contactpoint_label" value="email_or_phone" /><input type="hidden" autocomplete="off" id="ignore" name="ignore" value="reg_second_contactpoint__" /><input type="hidden" autocomplete="off" id="locale" name="locale" value="mr_IN" /><input type="hidden" autocomplete="off" id="reg_instance" name="reg_instance" value="xJnDWD4XakvefQcoLP-pG1Ew" /><div id="reg_captcha" class="_58mw hidden_elem"><div><h2 id="security_check_header">सुरक्षा पडताळणी</h2><div id="outer_captcha_box"><div id="captcha_box"><div class="field_error hidden_elem" id="captcha_response_error">ही माहिती आवश्यक आहे.</div><div id="captcha" class="captcha" data-captcha-class="ReCaptchaCaptcha"><input type="hidden" autocomplete="off" name="captcha_persist_data" id="captcha_persist_data" value="AZmJqzBRh3tUcPpmBDfFXUgpZUJ0k_1KZHGq_Ve3nB9f-Wm-4zW_TrGLOHZdhVg_wqWv_Lusvvg7LXaxkKGBaG5UqitnTtLz3LYm7PYJ1V3Hb1le5GYPtSjmYUXtbim0Ld8wF38Sidhw74zYbE7HzeAhlhtI4F5kIC9JXGUfdPQ50Lc_6aDnotdLDEPU2CgOlkhSzSzOvTyjcpUMFCtaWrDhg4-hQUdBqN7WxFBNVI11isXBcEnkQ-AiIUH8e0BzlXYK5mHbIZASG5mKIZFUZp3xjywPR3nwmj2CXqpstXTLDqiyFcXXSB_8HxF16yswS30Wmis6zxxV4fQP1Wtfeih9IXWt6vnH_plP4KSlfc-5lA" /><div id="recaptcha_scripts" style="display:none"></div><div><input type="hidden" autocomplete="off" id="captcha_session" name="captcha_session" value="Wur7H8DZgZwFPGaLScVKDQ" /><input type="hidden" autocomplete="off" id="extra_challenge_params" name="extra_challenge_params" value="authp=nonce.tt.time.new_audio_default&amp;psig=nzMh71fg3J0DCkUSuFaZOfKjc_E&amp;nonce=Wur7H8DZgZwFPGaLScVKDQ&amp;tt=8FeNdMoUORMQkNSrFTBR-l5eGM8&amp;time=1489213892&amp;new_audio_default=1" /><input type="hidden" autocomplete="off" id="recaptcha_type" name="recaptcha_type" value="password" /></div><div class="recaptcha_text"><div class="recaptcha_only_if_image">खालील शब्द वाचू शकत नाही? <a href="#" id="recaptcha_reload_btn" onclick="Recaptcha.reload(); return false" role="button">वेगवेगळे शब्द वापरून पहा</a></div><div class="recaptcha_only_if_audio" style="display:none">कृपया तुम्हाला ऐकू आलेली अक्षरं किंवा अंक लिहा.<br /><a href="#" id="recaptcha_reload_btn" onclick="Recaptcha.reload(); return false" role="button">वेगळे शब्द वापरून पहा</a> किंवा <a href="#" onclick="Recaptcha.switch_type(&quot;image&quot;);
return false;" role="button">मजकुराकडे परत जा</a>.</div></div><span id="recaptcha_play_audio"></span><div class="audiocaptcha"></div><div id="recaptcha_image" class="captcha_image"></div><div id="recaptcha_loading">लोड होत आहे...<img class="captcha_loading img" src="https://static.xx.fbcdn.net/rsrc.php/v3/yb/r/GsNJNwuI-UM.gif" alt="" width="16" height="11" /></div><div class="captcha_input"><label>आपल्याला वर दिसत असलेला मजकूर प्रविष्ट करा.</label><div class="field_container"><input type="text" class="inputtext" name="captcha_response" id="captcha_response" autocomplete="off" aria-label="&#x915;&#x945;&#x92a;&#x94d;&#x91a;&#x93e; &#x907;&#x928;&#x92a;&#x941;&#x91f;. &#x92a;&#x941;&#x922;&#x947; &#x91a;&#x93e;&#x932;&#x942; &#x920;&#x947;&#x935;&#x923;&#x94d;&#x92f;&#x93e;&#x938;&#x93e;&#x920;&#x940; &#x935;&#x930;&#x940;&#x932; &#x938;&#x942;&#x91a;&#x940;&#x92c;&#x926;&#x94d;&#x927; &#x936;&#x92c;&#x94d;&#x926; &#x91f;&#x93e;&#x907;&#x92a; &#x915;&#x930;&#x93e;. &#x906;&#x92a;&#x923; &#x935;&#x930;&#x940;&#x932; &#x932;&#x93f;&#x902;&#x915; &#x915;&#x94d;&#x932;&#x93f;&#x915; &#x915;&#x930;&#x942;&#x928; &#x911;&#x921;&#x93f;&#x913; &#x915;&#x945;&#x92a;&#x94d;&#x91a;&#x93e; &#x935;&#x93e;&#x92a;&#x930;&#x942; &#x936;&#x915;&#x924;&#x93e;. &#x911;&#x921;&#x93f;&#x913; &#x92a;&#x94d;&#x932;&#x947; &#x915;&#x930;&#x923;&#x94d;&#x92f;&#x93e;&#x938;&#x93e;&#x920;&#x940; &#x915;&#x945;&#x92a;&#x94d;&#x91a;&#x93e; &#x92a;&#x94d;&#x932;&#x947; &#x915;&#x930;&#x93e; &#x92c;&#x91f;&#x923; &#x926;&#x93e;&#x92c;&#x93e; &#x92e;&#x917; &#x92f;&#x93e; &#x92b;&#x940;&#x932;&#x94d;&#x921;&#x92e;&#x927;&#x94d;&#x92f;&#x947; &#x910;&#x915;&#x932;&#x947;&#x932;&#x947; &#x936;&#x92c;&#x94d;&#x926; &#x92a;&#x94d;&#x930;&#x935;&#x93f;&#x937;&#x94d;&#x91f; &#x915;&#x930;&#x93e;." /></div><a class="mlm" href="#" onclick="CSS.show($(&#039;captcha_whats_this&#039;)); return false;" role="button">मला हे का दिसत आहे?</a><div id="captcha_whats_this" class="hidden_elem"><div class="fsl fwb">सुरक्षा पडताळणी</div>खोटी खाती तयार करण्यापासून आणि वापरकर्त्यांना स्पॅमिंग करण्यापासून स्पॅमर्सनां प्रतिबंधित करण्यासाठी आम्ही वापरत असलेली ही एक मानक सुरक्षा तपासणी आहे.</div></div></div></div></div><div id="captcha_buttons" class="_58p2 clearfix hidden_elem"><div class="_58mx _58mm"><div class="_58mz">   </div><a class="_58my" href="#" role="button" id="u_0_i">मागे</a></div><div class="_58mm"><div class="clearfix"><button type="submit" class="_6j mvm _6wk _6wl _58me _58mi _6o _6v" id="u_0_j">साइन अप</button><span class="hidden_elem _58ml" id="u_0_p"><img class="img" src="https://static.xx.fbcdn.net/rsrc.php/v3/yb/r/GsNJNwuI-UM.gif" alt="" width="16" height="11" /></span></div></div></div></div></div></form></div><div id="reg_pages_msg" class="_58mk">सुप्रसिद्ध व्यक्ती ,वाद्यवृंद किंवा व्यवसायासाठी <a href="/pages/create/?ref_type=registration_form">पृष्ठ तयार करा</a></div></div></div></div></div></div></div></div></div></div></div><div><div id="pageFooter" data-referrer="page_footer"><ul class="uiList localeSelectorList _2pid _509- _4ki _6-h _6-j _6-i" data-nocookies="1"><li>मराठी</li><li><a dir="ltr" href="https://hi-in.facebook.com/" onclick="require(&quot;IntlUtils&quot;).setCookieLocale(&quot;hi_IN&quot;, &quot;mr_IN&quot;, &quot;https:\/\/hi-in.facebook.com\/&quot;, &quot;www_list_selector&quot;, 0); return false;" title="Hindi">हिन्दी</a></li><li><a dir="rtl" href="https://ur-pk.facebook.com/" onclick="require(&quot;IntlUtils&quot;).setCookieLocale(&quot;ur_PK&quot;, &quot;mr_IN&quot;, &quot;https:\/\/ur-pk.facebook.com\/&quot;, &quot;www_list_selector&quot;, 1); return false;" title="Urdu">اردو</a></li><li><a dir="ltr" href="https://gu-in.facebook.com/" onclick="require(&quot;IntlUtils&quot;).setCookieLocale(&quot;gu_IN&quot;, &quot;mr_IN&quot;, &quot;https:\/\/gu-in.facebook.com\/&quot;, &quot;www_list_selector&quot;, 2); return false;" title="Gujarati">ગુજરાતી</a></li><li><a dir="ltr" href="https://kn-in.facebook.com/" onclick="require(&quot;IntlUtils&quot;).setCookieLocale(&quot;kn_IN&quot;, &quot;mr_IN&quot;, &quot;https:\/\/kn-in.facebook.com\/&quot;, &quot;www_list_selector&quot;, 3); return false;" title="Kannada">ಕನ್ನಡ</a></li><li><a dir="ltr" href="https://pa-in.facebook.com/" onclick="require(&quot;IntlUtils&quot;).setCookieLocale(&quot;pa_IN&quot;, &quot;mr_IN&quot;, &quot;https:\/\/pa-in.facebook.com\/&quot;, &quot;www_list_selector&quot;, 4); return false;" title="Punjabi">ਪੰਜਾਬੀ</a></li><li><a dir="ltr" href="https://ta-in.facebook.com/" onclick="require(&quot;IntlUtils&quot;).setCookieLocale(&quot;ta_IN&quot;, &quot;mr_IN&quot;, &quot;https:\/\/ta-in.facebook.com\/&quot;, &quot;www_list_selector&quot;, 5); return false;" title="Tamil">தமிழ்</a></li><li><a dir="ltr" href="https://bn-in.facebook.com/" onclick="require(&quot;IntlUtils&quot;).setCookieLocale(&quot;bn_IN&quot;, &quot;mr_IN&quot;, &quot;https:\/\/bn-in.facebook.com\/&quot;, &quot;www_list_selector&quot;, 6); return false;" title="Bengali">বাংলা</a></li><li><a dir="ltr" href="https://te-in.facebook.com/" onclick="require(&quot;IntlUtils&quot;).setCookieLocale(&quot;te_IN&quot;, &quot;mr_IN&quot;, &quot;https:\/\/te-in.facebook.com\/&quot;, &quot;www_list_selector&quot;, 7); return false;" title="Telugu">తెలుగు</a></li><li><a dir="ltr" href="https://ml-in.facebook.com/" onclick="require(&quot;IntlUtils&quot;).setCookieLocale(&quot;ml_IN&quot;, &quot;mr_IN&quot;, &quot;https:\/\/ml-in.facebook.com\/&quot;, &quot;www_list_selector&quot;, 8); return false;" title="Malayalam">മലയാളം</a></li><li><a dir="ltr" href="https://en-gb.facebook.com/" onclick="require(&quot;IntlUtils&quot;).setCookieLocale(&quot;en_GB&quot;, &quot;mr_IN&quot;, &quot;https:\/\/en-gb.facebook.com\/&quot;, &quot;www_list_selector&quot;, 9); return false;" title="English (UK)">English (UK)</a></li><li><a class="_42ft _4jy0 _517i _517h _51sy" role="button" href="#" rel="dialog" ajaxify="/settings/language/language/?uri=https%3A%2F%2Fen-gb.facebook.com%2F&amp;source=www_list_selector_more" title="&#x906;&#x923;&#x916;&#x940; &#x92d;&#x93e;&#x937;&#x93e; &#x926;&#x930;&#x94d;&#x936;&#x935;&#x93e;"><i class="img sp_Mlxwn39jCAE sx_9b333c"></i></a></li></ul><div id="contentCurve"></div><div role="contentinfo" aria-label="Facebook  &#x938;&#x93e;&#x907;&#x91f; &#x932;&#x93f;&#x902;&#x915;"><table class="uiGrid _51mz navigationGrid" cellspacing="0" cellpadding="0"><tbody><tr class="_51mx"><td class="_51m- hLeft plm"><a href="/r.php" title="&#x92b;&#x947;&#x938;&#x92c;&#x941;&#x915;&#x938;&#x93e;&#x920;&#x940; &#x938;&#x93e;&#x907;&#x928; &#x905;&#x92a; &#x915;&#x930;&#x93e;">साइन अप</a></td><td class="_51m- hLeft plm"><a href="/login/" title="Facebook &#x935;&#x930; &#x932;&#x949;&#x917; &#x907;&#x928; &#x915;&#x930;&#x93e;">लॉग इन</a></td><td class="_51m- hLeft plm"><a href="https://messenger.com/" title="&#x92e;&#x947;&#x938;&#x947;&#x902;&#x91c;&#x930; &#x924;&#x92a;&#x93e;&#x938;&#x942;&#x928; &#x92a;&#x939;&#x93e;.">Messenger</a></td><td class="_51m- hLeft plm"><a href="/lite/" title="Android &#x938;&#x93e;&#x920;&#x940; Facebook Lite">Facebook Lite</a></td><td class="_51m- hLeft plm"><a href="/mobile/?ref=pf" title="Facebook  &#x92e;&#x94b;&#x92c;&#x93e;&#x907;&#x932; &#x935;&#x93e;&#x92a;&#x930;&#x941;&#x928; &#x92a;&#x939;&#x93e;.">मोबाईल</a></td><td class="_51m- hLeft plm"><a href="/find-friends?ref=pf" title="&#x915;&#x94b;&#x923;&#x93e;&#x932;&#x93e;&#x939;&#x940; &#x935;&#x947;&#x92c;&#x935;&#x930; &#x936;&#x94b;&#x927;&#x93e;.">मित्र शोधा</a></td><td class="_51m- hLeft plm"><a href="/directory/people/" title="&#x906;&#x92e;&#x91a;&#x940; &#x932;&#x94b;&#x915;&#x93e;&#x902;&#x91a;&#x940; &#x928;&#x93f;&#x930;&#x94d;&#x926;&#x947;&#x936;&#x93f;&#x915;&#x93e; &#x92c;&#x94d;&#x930;&#x93e;&#x909;&#x91d; &#x915;&#x930;&#x93e;.">लोक</a></td><td class="_51m- hLeft plm"><a href="/directory/pages/" title="&#x906;&#x92e;&#x91a;&#x940; &#x92a;&#x943;&#x937;&#x94d;&#x200d;&#x920; &#x926;&#x930;&#x94d;&#x936;&#x93f;&#x915;&#x93e; &#x91a;&#x93e;&#x933;&#x93e;">पृष्ठे</a></td><td class="_51m- hLeft plm"><a href="/places/" title="Facebook  &#x935;&#x930;  &#x932;&#x94b;&#x915;&#x92a;&#x94d;&#x930;&#x93f;&#x92f; &#x920;&#x93f;&#x915;&#x93e;&#x923;&#x947; &#x92a;&#x939;&#x93e;.">ठिकाणे</a></td><td class="_51m- hLeft plm"><a href="/games/" title="Facebook  &#x91a;&#x947; &#x916;&#x947;&#x933; &#x92a;&#x921;&#x924;&#x93e;&#x933;&#x93e;">खेळ</a></td><td class="_51m- hLeft plm _51mw"><a href="/directory/places/" title="&#x906;&#x92e;&#x91a;&#x947; &#x938;&#x94d;&#x925;&#x933;&#x915;&#x94b;&#x936; &#x91a;&#x93e;&#x933;&#x93e;.">स्थाने</a></td></tr><tr class="_51mx"><td class="_51m- hLeft plm"><a href="/directory/celebrities/" title="&#x938;&#x93e;&#x930;&#x94d;&#x935;&#x91c;&#x928;&#x93f;&#x915; &#x906;&#x923;&#x93f; &#x92a;&#x94d;&#x930;&#x938;&#x93f;&#x926;&#x94d;&#x927;  &#x935;&#x94d;&#x92f;&#x915;&#x94d;&#x924;&#x940;&#x902;&#x91a;&#x93e; &#x906;&#x92e;&#x91a;&#x94d;&#x92f;&#x93e; &#x928;&#x93f;&#x930;&#x94d;&#x926;&#x947;&#x936;&#x93f;&#x915;&#x947;&#x924; &#x936;&#x94b;&#x927; &#x918;&#x94d;&#x92f;&#x93e;.">सेलीब्रिटी</a></td><td class="_51m- hLeft plm"><a href="/mkplc/?ref=fb_home" title="Browse our marketplace product directory.">बाजाराचे ठिकाण</a></td><td class="_51m- hLeft plm"><a href="/directory/groups/" title="&#x906;&#x92e;&#x91a;&#x940; &#x938;&#x92e;&#x942;&#x939; &#x928;&#x93f;&#x930;&#x94d;&#x926;&#x947;&#x936;&#x93f;&#x915;&#x93e; &#x92c;&#x94d;&#x930;&#x93e;&#x909;&#x91d; &#x915;&#x930;&#x93e;.">समूह</a></td><td class="_51m- hLeft plm"><a href="http://l.facebook.com/l.php?u=http%3A%2F%2Fmomentsapp.com%2F&amp;h=ATPgN-c1s4jHUQlPgiA6mc2rTCbxpaKc-Y04A0fLuiZgKLC9WkjVmS3biIAvXEyr__YSw_WuC6newwJ0ipPrngz6sDJB0ajEjCqVbUU0VW8bSnpMI-25p1U&amp;s=1" title="Check out Moments." target="_blank" rel="nofollow" onmouseover="LinkshimAsyncLink.swap(this, &quot;http:\/\/momentsapp.com\/&quot;);" onclick="LinkshimAsyncLink.swap(this, &quot;http:\/\/l.facebook.com\/l.php?u=http\u00253A\u00252F\u00252Fmomentsapp.com\u00252F&amp;h=ATPgN-c1s4jHUQlPgiA6mc2rTCbxpaKc-Y04A0fLuiZgKLC9WkjVmS3biIAvXEyr__YSw_WuC6newwJ0ipPrngz6sDJB0ajEjCqVbUU0VW8bSnpMI-25p1U&amp;s=1&quot;);">मोमेंट्स</a></td><td class="_51m- hLeft plm"><a href="https://l.facebook.com/l.php?u=https%3A%2F%2Finstagram.com%2F&amp;h=ATN8uhMqW5XsKaL6EKOFuk2HG_RRLnwHcsSlKZgo8x7gWO4rJhBQzQ8N_92nCZeDulGF27ozp8S93anMpTYXc9OCDNhcrjfdlDdhlwrFS6A8jIaeHzEK0VE&amp;s=1" title="Check out Instagram" target="_blank" rel="nofollow" onmouseover="LinkshimAsyncLink.swap(this, &quot;https:\/\/instagram.com\/&quot;);" onclick="LinkshimAsyncLink.swap(this, &quot;https:\/\/l.facebook.com\/l.php?u=https\u00253A\u00252F\u00252Finstagram.com\u00252F&amp;h=ATN8uhMqW5XsKaL6EKOFuk2HG_RRLnwHcsSlKZgo8x7gWO4rJhBQzQ8N_92nCZeDulGF27ozp8S93anMpTYXc9OCDNhcrjfdlDdhlwrFS6A8jIaeHzEK0VE&amp;s=1&quot;);">इंस्‍टाग्राम</a></td><td class="_51m- hLeft plm"><a href="/facebook" accesskey="8" title="&#x906;&#x92e;&#x91a;&#x93e; &#x92c;&#x94d;&#x932;&#x949;&#x917; &#x935;&#x93e;&#x91a;&#x93e;, &#x938;&#x902;&#x938;&#x93e;&#x927;&#x928; &#x915;&#x947;&#x902;&#x926;&#x94d;&#x930;&#x93e;&#x938; &#x92d;&#x947;&#x91f; &#x926;&#x94d;&#x92f;&#x93e; &#x906;&#x923;&#x93f; &#x928;&#x94b;&#x915;&#x930;&#x940;&#x91a;&#x94d;&#x92f;&#x93e; &#x938;&#x902;&#x927;&#x940; &#x92e;&#x93f;&#x933;&#x935;&#x93e;.">च्याबद्दल</a></td><td class="_51m- hLeft plm"><a href="/campaign/landing.php?placement=pflo&amp;campaign_id=402047449186&amp;extra_1=auto" title="Facebook &#x935;&#x930; &#x91c;&#x93e;&#x939;&#x93f;&#x930;&#x93e;&#x924; &#x915;&#x930;&#x93e;.">जाहिरात तयार करा.</a></td><td class="_51m- hLeft plm"><a href="/pages/create/?ref_type=sitefooter" title="&#x92a;&#x943;&#x937;&#x94d;&#x920; &#x924;&#x92f;&#x93e;&#x930; &#x915;&#x930;&#x93e;">पृष्ठ तयार करा</a></td><td class="_51m- hLeft plm"><a href="https://developers.facebook.com/?ref=pf" title="&#x906;&#x92e;&#x91a;&#x94d;&#x92f;&#x93e; &#x92a;&#x94d;&#x200d;&#x932;&#x945;&#x91f;&#x92b;&#x949;&#x930;&#x94d;&#x92e;&#x935;&#x930; &#x935;&#x93f;&#x915;&#x938;&#x93f;&#x924; &#x915;&#x930;&#x93e;.">विकासक</a></td><td class="_51m- hLeft plm"><a href="/careers/?ref=pf" title="&#x906;&#x92e;&#x91a;&#x94d;&#x92f;&#x93e;  &#x905;&#x926;&#x94d;&#x92d;&#x941;&#x924; &#x915;&#x902;&#x92a;&#x928;&#x940;&#x924;, &#x906;&#x92a;&#x932;&#x947; &#x92a;&#x941;&#x922;&#x940;&#x932; &#x915;&#x930;&#x940;&#x905;&#x930; &#x915;&#x930;&#x93e;!">करीयर</a></td><td class="_51m- hLeft plm _51mw"><a data-nocookies="1" href="/privacy/explanation" title="Facebook &#x906;&#x923;&#x93f; &#x906;&#x92a;&#x932;&#x94d;&#x92f;&#x93e; &#x917;&#x94b;&#x92a;&#x928;&#x940;&#x92f;&#x924;&#x947;&#x92c;&#x926;&#x94d;&#x926;&#x932; &#x92e;&#x93e;&#x939;&#x93f;&#x924;&#x940; &#x92e;&#x93f;&#x933;&#x935;&#x93e;.">गोपनीयता</a></td></tr><tr class="_51mx"><td class="_51m- hLeft plm"><a href="/policies/cookies/" title="&#x915;&#x941;&#x915;&#x940;&#x91c; &#x906;&#x923;&#x93f; Facebook  &#x92c;&#x926;&#x94d;&#x926;&#x932; &#x91c;&#x93e;&#x923;&#x942;&#x928; &#x918;&#x94d;&#x92f;&#x93e;." data-nocookies="1">कुकीज</a></td><td class="_51m- hLeft plm"><a class="_41ug" data-nocookies="1" href="https://www.facebook.com/help/568137493302217" title="&#x91c;&#x93e;&#x939;&#x93f;&#x930;&#x93e;&#x924; &#x928;&#x93f;&#x935;&#x921;&#x940;&#x902;&#x935;&#x93f;&#x937;&#x92f;&#x940; &#x91c;&#x93e;&#x923;&#x942;&#x928; &#x918;&#x94d;&#x200d;&#x92f;&#x93e;">जाहिरात निवड<i class="img sp_Mlxwn39jCAE sx_19516e"></i></a></td><td class="_51m- hLeft plm"><a data-nocookies="1" href="/policies?ref=pf" accesskey="9" title="&#x906;&#x92e;&#x91a;&#x94d;&#x92f;&#x93e; &#x905;&#x91f;&#x940; &#x935; &#x927;&#x94b;&#x930;&#x923;&#x947; &#x92f;&#x93e;&#x902;&#x91a;&#x947; &#x92a;&#x941;&#x928;&#x930;&#x93e;&#x935;&#x932;&#x94b;&#x915;&#x928; &#x915;&#x930;&#x93e;.">अटी</a></td><td class="_51m- hLeft plm"><a href="/help/?ref=pf" accesskey="0" title="&#x906;&#x92e;&#x91a;&#x94d;&#x92f;&#x93e; &#x92e;&#x926;&#x924; &#x915;&#x947;&#x902;&#x926;&#x94d;&#x930;&#x93e;&#x932;&#x93e; &#x92d;&#x947;&#x91f; &#x926;&#x94d;&#x92f;&#x93e;.">मदत</a></td><td class="_51m- hLeft plm"><a class="accessible_elem" accesskey="6" href="/settings" title="&#x906;&#x92a;&#x932;&#x94d;&#x92f;&#x93e; Facebook  &#x938;&#x947;&#x91f;&#x93f;&#x902;&#x917;&#x94d;&#x91c; &#x92a;&#x939;&#x93e; &#x935; &#x938;&#x902;&#x92a;&#x93e;&#x926;&#x93f;&#x924; &#x915;&#x930;&#x93e;.">सेटिंग्ज</a></td><td class="_51m- hLeft plm"><a class="accessible_elem" accesskey="7" href="/allactivity?privacy_source=activity_log_top_menu" title="&#x906;&#x92a;&#x932;&#x93e; &#x915;&#x94d;&#x930;&#x93f;&#x92f;&#x93e;&#x915;&#x932;&#x93e;&#x92a; &#x932;&#x949;&#x917; &#x92a;&#x939;&#x93e;">क्रियाकलाप लॉग</a></td></tr></tbody></table></div><div class="mvl copyright"><div><span> Facebook © 2017</span></div></div></div></div></div></div><div></div>
<script>requireLazy(["Bootloader"], function(Bootloader) {Bootloader.setResourceMap({"7pDPb":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iN754\/yI\/l\/mr_IN\/fbdLMF3QdeW.js","permanent":1,"crossOrigin":1},"KO79V":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iDJY4\/y2\/l\/mr_IN\/3nxU7RxDaWt.js","permanent":1,"crossOrigin":1},"gzgdj":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iZn14\/yX\/l\/mr_IN\/GC0xR-FWwoE.js","permanent":1,"crossOrigin":1},"xIc5a":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yd\/r\/VvnMSIz-Kbf.js","permanent":1,"crossOrigin":1},"glg8M":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3i2ot4\/yX\/l\/mr_IN\/Iux4oe77em9.js","permanent":1,"crossOrigin":1},"tbDRX":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3ipJH4\/yi\/l\/mr_IN\/XjMCfmGORcw.js","permanent":1,"crossOrigin":1},"PyfSj":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3i8nb4\/yh\/l\/mr_IN\/-hRaUPZOCkC.js","permanent":1,"crossOrigin":1},"3q0pN":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3izDd4\/yh\/l\/mr_IN\/Tn6It5Tj6cj.js","permanent":1,"crossOrigin":1},"oE4Do":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yQ\/r\/JRn6lb4zeSH.js","permanent":1,"crossOrigin":1},"mgb8G":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yX\/r\/l1KABG_PvXW.js","crossOrigin":1},"xLI7Z":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3i9HE4\/y-\/l\/mr_IN\/HKfkAAAZWLi.js","permanent":1,"crossOrigin":1},"Klc20":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y3\/r\/87DNbm9ci3o.js","crossOrigin":1},"I\/Oj6":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iHKK4\/yW\/l\/mr_IN\/smxpQ_p58TU.js","permanent":1,"crossOrigin":1},"xiSec":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yL\/r\/a1Nq6aZova2.js","permanent":1,"crossOrigin":1},"VYTIU":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yd\/r\/ILqLysEtJbn.js","crossOrigin":1},"M0Hao":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yR\/r\/um2sdrZJYXX.js","crossOrigin":1},"2aVFz":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3i_k_4\/yM\/l\/mr_IN\/vA6eTLgL5W9.js","permanent":1,"crossOrigin":1},"VBj2e":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3izRE4\/ya\/l\/mr_IN\/uBFoIHO1Q-Z.js","permanent":1,"crossOrigin":1},"BnIxf":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yt\/r\/WBtF4eOGnLV.js","permanent":1,"crossOrigin":1},"oeUXN":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yz\/r\/tia2K7wPxLm.js","crossOrigin":1},"z1p7V":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iw-94\/yD\/l\/mr_IN\/hf40CIxJ_Db.js","permanent":1,"crossOrigin":1},"5PUV8":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3i1ZK4\/yS\/l\/mr_IN\/xqoPbENW_Ea.js","permanent":1,"crossOrigin":1},"DXyMM":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iVM04\/y-\/l\/mr_IN\/YbVwfRvghOU.js","permanent":1,"crossOrigin":1},"O+8J5":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y9\/r\/0M_D8O5LbB7.css","permanent":1,"crossOrigin":1},"rxn2o":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iKo94\/yu\/l\/mr_IN\/jrX01NvI8E3.js","permanent":1,"crossOrigin":1},"WQwNW":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iUWy4\/yh\/l\/mr_IN\/dlQ2OzfVKOq.js","permanent":1,"crossOrigin":1},"BoQ1G":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iJqH4\/yX\/l\/mr_IN\/QaO37L2XVi4.js","permanent":1,"crossOrigin":1},"gVLBA":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3i8gp4\/yO\/l\/mr_IN\/pMLl_YiXc-i.js","permanent":1,"crossOrigin":1},"QdGSO":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iB_z4\/yp\/l\/mr_IN\/d9mvuMlB-5f.js","permanent":1,"crossOrigin":1},"2qa5V":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3ijP34\/yK\/l\/mr_IN\/occrISAy8OC.js","permanent":1,"crossOrigin":1},"uXLLm":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yP\/r\/AWQcNqU3-YG.js","permanent":1,"crossOrigin":1},"8brkk":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3i5f-4\/yZ\/l\/mr_IN\/WlV1mQlV2hZ.js","permanent":1,"crossOrigin":1},"CnGE9":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yX\/r\/R2saIb6hdbu.js","permanent":1,"crossOrigin":1},"qVIf2":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yj\/r\/wx_wbJMP-6O.js","crossOrigin":1},"rgzm5":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/ye\/r\/yM68MmiDorc.js","permanent":1,"crossOrigin":1},"wb3qs":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y0\/r\/eOlBmRgsm8x.js","crossOrigin":1},"zEmvK":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iVLS4\/yS\/l\/mr_IN\/GXd4SyxZv49.js","permanent":1,"crossOrigin":1},"Xp5tm":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3ipJH4\/yV\/l\/mr_IN\/RixyttL2E_J.js","permanent":1,"crossOrigin":1},"jNgMf":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y9\/r\/IO4DIs8nJvq.js","permanent":1,"crossOrigin":1},"XxJQ4":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yE\/r\/pTMLxyFT7Hd.js","permanent":1,"crossOrigin":1},"54\/mu":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yR\/r\/-90KwH4neHw.js","permanent":1,"crossOrigin":1},"NcYb3":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iv5Y4\/yi\/l\/mr_IN\/i3p3xDyU6zz.js","permanent":1,"crossOrigin":1},"7o0h9":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yk\/r\/UosfsbRA9cM.js","permanent":1,"crossOrigin":1},"D7hFh":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y7\/r\/7MVvGg2soVw.js","permanent":1,"crossOrigin":1},"fwsN4":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y0\/r\/_JZoaqJA1lf.css","permanent":1,"crossOrigin":1},"aUqn9":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iAJe4\/yA\/l\/mr_IN\/zn6BWJcDD8p.js","permanent":1,"crossOrigin":1},"k\/dRv":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y2\/r\/76uEbwpzfbo.js","permanent":1,"crossOrigin":1},"J+tWg":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yt\/r\/Hq6dOMfpt1m.js","permanent":1,"crossOrigin":1},"wE\/xn":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y4\/r\/xkpiQ5LiVoI.js","permanent":1,"crossOrigin":1},"ahhl3":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3i98g4\/yx\/l\/mr_IN\/VxMWzqDZWxJ.js","permanent":1,"crossOrigin":1},"kF1+E":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/ya\/r\/ipIBu9zE2Ql.css","permanent":1,"crossOrigin":1},"lLT+Y":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3ijUn4\/ym\/l\/mr_IN\/PHl2SYvP2O_.js","permanent":1,"crossOrigin":1},"bn4q6":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yc\/r\/7sfhjY06emC.css","permanent":1,"crossOrigin":1},"MNa5l":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yx\/r\/g-8q9Q5HAct.js","permanent":1,"crossOrigin":1},"wiAMM":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yK\/r\/fNYKo98GkF-.js","permanent":1,"crossOrigin":1},"qLtVf":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yK\/r\/sJ7m0cs89Ar.js","permanent":1,"crossOrigin":1},"1QKzr":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yR\/r\/Vsug3SpELnW.js","permanent":1,"crossOrigin":1},"JVQrG":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yA\/r\/Yr7zPyhDSCp.css","permanent":1,"crossOrigin":1},"3py3C":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iPPx4\/yB\/l\/mr_IN\/aY8APYbdaBI.js","permanent":1,"crossOrigin":1},"S1OBF":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iaiF4\/yj\/l\/mr_IN\/-9Qj-DI8sNX.js","permanent":1,"crossOrigin":1},"yq8d4":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iLVE4\/yB\/l\/mr_IN\/owtvvcu29uD.js","permanent":1,"crossOrigin":1},"B8HgN":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3i4NU4\/y2\/l\/mr_IN\/TZauC440LtG.js","permanent":1,"crossOrigin":1},"622TF":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yq\/r\/yAvZmZDyl0s.css","permanent":1,"crossOrigin":1},"D+lWU":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3inMj4\/yw\/l\/mr_IN\/o9R5nRP8_2H.js","permanent":1,"crossOrigin":1},"F0FOt":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yZ\/r\/SEFZl-13gxP.js","permanent":1,"crossOrigin":1},"VyIGb":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3ivLi4\/yl\/l\/mr_IN\/-PMzUwDPF85.js","permanent":1,"crossOrigin":1},"BTuj2":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yu\/r\/0OyY5YXSrUN.js","permanent":1,"crossOrigin":1},"IiFdP":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3ifLt4\/yI\/l\/mr_IN\/dZxiQqvYIUK.js","permanent":1,"crossOrigin":1},"JHn9H":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yG\/r\/T9e3Uf_z7H-.css","permanent":1,"crossOrigin":1},"pPYY3":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yX\/r\/yUD32YzEf8o.css","permanent":1,"crossOrigin":1},"60YTU":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3ippC4\/yn\/l\/mr_IN\/_Gf5LPObPxA.js","permanent":1,"crossOrigin":1},"l4aBW":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yl\/r\/Nxsop1kE9cX.css","permanent":1,"crossOrigin":1},"9p0Oq":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3i_k74\/yX\/l\/mr_IN\/IouCGjgu5BZ.js","permanent":1,"crossOrigin":1},"IrfhN":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3i2yW4\/yU\/l\/mr_IN\/0c55Czxq2_6.js","permanent":1,"crossOrigin":1},"gaYz9":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/ym\/r\/ZqtvHHS-Iq-.css","permanent":1,"crossOrigin":1},"Vax3W":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iBc84\/yQ\/l\/mr_IN\/_LMqs9TzOI8.js","permanent":1,"crossOrigin":1},"FKaJK":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yC\/r\/Ic1ZJ58OM3_.css","permanent":1,"crossOrigin":1},"z4sTc":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yr\/r\/ceZi3Ow00T_.css","permanent":1,"crossOrigin":1},"RrQPb":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iRmR4\/yB\/l\/mr_IN\/xZNnvjL182T.js","permanent":1,"crossOrigin":1},"pI7AA":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yw\/r\/Lj3-3HF67_y.css","crossOrigin":1},"0Qz\/x":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y7\/r\/A0akup4vz1v.js","crossOrigin":1},"Hnz7V":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3ikLT4\/yZ\/l\/mr_IN\/VPPzLR4i8x6.js","crossOrigin":1},"2wfDx":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yi\/r\/ZGmg7MwELpO.js","permanent":1,"crossOrigin":1},"7ndNQ":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yT\/r\/-wFv4JjHeV7.js","permanent":1,"crossOrigin":1},"oQbcB":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iUE14\/yx\/l\/mr_IN\/X70FmpmPl6U.js","permanent":1,"crossOrigin":1},"4B2Qx":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y0\/r\/Klzsrk3OAVw.js","permanent":1,"crossOrigin":1},"73tQl":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y9\/r\/bHVduWQ2kiz.js","permanent":1,"crossOrigin":1},"I5cJ2":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yw\/r\/BcrcPl4FyRD.css","permanent":1,"crossOrigin":1},"HAcxX":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iNTL4\/yp\/l\/mr_IN\/D1Td-FNEIfy.js","permanent":1,"crossOrigin":1},"2\/maQ":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yc\/r\/pi6gaIyZu1E.js","crossOrigin":1},"F90WH":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yL\/r\/yWWiCwN9vjC.css","permanent":1,"crossOrigin":1},"B76cY":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3izZ-4\/ym\/l\/mr_IN\/J3DZf3he5wl.js","permanent":1,"crossOrigin":1},"7unvu":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y6\/r\/ZdWMWTwet3q.js","permanent":1,"crossOrigin":1},"\/mnVq":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3ioZX4\/yp\/l\/mr_IN\/tIpFrMdHC1X.js","permanent":1,"crossOrigin":1},"HWLe0":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iWrp4\/yv\/l\/mr_IN\/IdwUQgfkkYW.js","permanent":1,"crossOrigin":1},"itM80":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yi\/r\/CVQAyGDT5oA.css","permanent":1,"crossOrigin":1},"60TSu":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yf\/r\/WN4424Vy0Hq.js","permanent":1,"crossOrigin":1},"5hNXg":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/ye\/r\/YHxFodEpeWp.js","permanent":1,"crossOrigin":1},"X\/B82":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y7\/r\/a0EoqKy1hQ2.js","permanent":1,"crossOrigin":1},"zyFOp":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yr\/r\/H7pgFynyic_.js","crossOrigin":1},"6AU0l":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3i9By4\/yl\/l\/mr_IN\/4GepkCJUA1K.js","crossOrigin":1},"VDymv":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/ym\/r\/vfyTLT62WoX.css","permanent":1,"crossOrigin":1},"yFyUx":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yj\/r\/L4GI5c08pM4.js","permanent":1,"crossOrigin":1},"WEGtD":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iOJz4\/yZ\/l\/mr_IN\/Sls0fuKBDLY.js","permanent":1,"crossOrigin":1},"qnR1n":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iimk4\/yg\/l\/mr_IN\/0QMTlI7NH0s.js","permanent":1,"crossOrigin":1},"RZozx":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yG\/r\/2xmd_-xBhVj.js","permanent":1,"crossOrigin":1},"v1FBw":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yg\/r\/zuCQsug4SlJ.js","permanent":1,"crossOrigin":1},"qfzTq":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yN\/r\/hLtdyLf3Ixj.js","crossOrigin":1},"iMk7H":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yu\/r\/wlczAvWfcUi.js","permanent":1,"crossOrigin":1},"1qJfW":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3ixqn4\/yb\/l\/mr_IN\/pDkpZ-2VbCd.js","permanent":1,"crossOrigin":1},"asUmo":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3i7kC4\/yf\/l\/mr_IN\/_E57js3m8jY.js","permanent":1,"crossOrigin":1},"4\/h+Q":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y_\/r\/3QVkg44lWZc.css","permanent":1,"crossOrigin":1},"pmhcL":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3ipew4\/yt\/l\/mr_IN\/-794N6IR9E7.js","permanent":1,"crossOrigin":1},"E\/dNZ":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yS\/r\/Ic0YY_ezK2_.js","permanent":1,"crossOrigin":1},"5yQBc":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yA\/r\/ke72LqkNf5Z.js","permanent":1,"crossOrigin":1},"29r44":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3i9Ew4\/yV\/l\/mr_IN\/L0Nm9wTmjur.js","permanent":1,"crossOrigin":1},"LY13N":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yP\/r\/9TY1Ik6Vc-D.js","crossOrigin":1},"Dnlm1":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iI-y4\/yB\/l\/mr_IN\/UvP3l3rgBFj.js","permanent":1,"crossOrigin":1},"Qt9ub":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y2\/r\/ma6OAdUbf0e.js","permanent":1,"crossOrigin":1},"3PGYg":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yI\/r\/YLXZ7VXyysa.css","permanent":1,"crossOrigin":1},"8aeA9":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yr\/r\/oGy92c86mRb.js","permanent":1,"crossOrigin":1},"9EMwh":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iWVQ4\/yR\/l\/mr_IN\/B_zMIWxN95q.js","permanent":1,"crossOrigin":1},"U5YL3":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yz\/r\/IvwE1GPi6Zx.css","crossOrigin":1},"ybinV":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iKo94\/yl\/l\/mr_IN\/-YJzRaccuV1.js","crossOrigin":1},"+VWNr":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iTJf4\/yG\/l\/mr_IN\/BCSQDxx5tgL.js","crossOrigin":1},"29hGe":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3i9-F4\/y4\/l\/mr_IN\/zScKA7HiBtN.js","permanent":1,"crossOrigin":1},"T6by2":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yi\/r\/4Sy1hM7L6nZ.css","permanent":1,"crossOrigin":1},"a7Tia":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yj\/r\/ZwZpSmGR0uL.css","permanent":1,"crossOrigin":1},"pSiWa":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iBy44\/y0\/l\/mr_IN\/I2wzF5xXxhJ.js","permanent":1,"crossOrigin":1},"YyAHK":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yE\/r\/0MsI8q-u-hy.css","permanent":1,"crossOrigin":1},"krylL":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yn\/r\/t69dxVdKJbE.js","permanent":1,"crossOrigin":1},"hZXZf":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iYhK4\/yX\/l\/mr_IN\/njrnyOjkXOn.js","permanent":1,"crossOrigin":1},"UH7ZD":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3i68M4\/yF\/l\/mr_IN\/zKCI-SRXPw7.js","permanent":1,"crossOrigin":1},"Yu7nb":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3ihIW4\/yT\/l\/mr_IN\/atGKA-LSNX_.js","permanent":1,"crossOrigin":1},"zparn":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yM\/r\/h6-CQm1Bo2p.js","permanent":1,"crossOrigin":1},"AmMkr":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yZ\/r\/s5B5mO8QHLs.js","permanent":1,"crossOrigin":1},"FRpa\/":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yN\/r\/gx92ofE4W0e.css","permanent":1,"crossOrigin":1},"kn9pk":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3ikSO4\/yI\/l\/mr_IN\/IOoIO677QzQ.js","crossOrigin":1},"fM9ic":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3iFSg4\/yB\/l\/mr_IN\/28iQ83n_lo-.js","permanent":1,"crossOrigin":1},"DE+m6":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yS\/r\/fXdhfyF2RMl.js","permanent":1,"crossOrigin":1},"GmbvR":{"type":"css","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yd\/r\/7NfTZcyBMT2.css","permanent":1,"crossOrigin":1},"+\/EdC":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yv\/r\/1HXw2iYhIZF.js","permanent":1,"crossOrigin":1},"rSdpp":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yo\/r\/p2Dzbeuleoh.js","crossOrigin":1},"wg+SO":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3ipgf4\/ym\/l\/mr_IN\/ypVomYmCxfN.js","permanent":1,"crossOrigin":1},"i5RnR":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3il8j4\/yg\/l\/mr_IN\/QqKujn9lvGJ.js","permanent":1,"crossOrigin":1},"4L2ow":{"type":"js","src":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y9\/r\/L0iTpHEhxLH.js","permanent":1,"crossOrigin":1}});if (true) {Bootloader.enableBootload({"ExceptionDialog":{"resources":["7pDPb","KO79V","gzgdj","4LeXr","P8uBt","xIc5a","nfKia","glg8M","tbDRX","PyfSj"],"module":1},"React":{"resources":["xIc5a","KO79V","4LeXr"],"module":1},"AsyncDOM":{"resources":["4LeXr","KO79V","3q0pN"],"module":1},"ConfirmationDialog":{"resources":["4LeXr","KO79V","7pDPb","oE4Do"],"module":1},"Dialog":{"resources":["KO79V","7pDPb","4LeXr","mgb8G","nfKia","gzgdj","xLI7Z"],"module":1},"QuickSandSolver":{"resources":["KO79V","4LeXr","mgb8G","7pDPb","Klc20","I\/Oj6","xiSec"],"module":1},"ErrorSignal":{"resources":["KO79V","4LeXr","mgb8G","VYTIU","M0Hao","2aVFz"],"module":1},"ReactDOM":{"resources":["xIc5a","KO79V","4LeXr"],"module":1},"BanzaiODS":{"resources":["KO79V","4LeXr"],"module":1},"LogHistory":{"resources":["VBj2e"],"module":1},"SimpleXUIDialog":{"resources":["7pDPb","KO79V","gzgdj","4LeXr","P8uBt","glg8M","xIc5a","nfKia"],"module":1},"XUIButton.react":{"resources":["KO79V","7pDPb","xIc5a","4LeXr","nfKia"],"module":1},"XUIDialogButton.react":{"resources":["xIc5a","KO79V","4LeXr","7pDPb","nfKia","gzgdj"],"module":1},"Animation":{"resources":["KO79V","7pDPb","4LeXr"],"module":1},"Banzai":{"resources":["KO79V","4LeXr"],"module":1},"ResourceTimingBootloaderHelper":{"resources":["KO79V","BnIxf"],"module":1},"TimeSliceHelper":{"resources":["xIc5a","KO79V","4LeXr","BnIxf"],"module":1},"AsyncSignal":{"resources":["4LeXr","KO79V"],"module":1},"XLinkshimLogController":{"resources":["KO79V","7pDPb","oeUXN"],"module":1},"DialogX":{"resources":["7pDPb","KO79V","gzgdj","4LeXr","P8uBt"],"module":1},"XUIDialogBody.react":{"resources":["xIc5a","KO79V","4LeXr","nfKia","7pDPb","P8uBt","glg8M"],"module":1},"XUIDialogFooter.react":{"resources":["xIc5a","KO79V","4LeXr","nfKia","7pDPb","P8uBt","gzgdj","glg8M"],"module":1},"XUIDialogTitle.react":{"resources":["xIc5a","KO79V","4LeXr","nfKia","7pDPb","P8uBt","gzgdj"],"module":1},"XUIGrayText.react":{"resources":["xIc5a","KO79V","4LeXr","nfKia","7pDPb"],"module":1},"PageTransitions":{"resources":["4LeXr","KO79V","7pDPb","mgb8G","z1p7V","gzgdj","P8uBt","xIc5a"],"module":1},"AsyncDialog":{"resources":["KO79V","4LeXr","mgb8G","7pDPb","gzgdj","P8uBt","xIc5a","nfKia"],"module":1},"AsyncRequest":{"resources":["KO79V","4LeXr","mgb8G"],"module":1},"FormSubmit":{"resources":["KO79V","4LeXr","mgb8G","5PUV8"],"module":1},"Hovercard":{"resources":["4LeXr","KO79V","DXyMM","mgb8G","7pDPb","P8uBt","gzgdj","O+8J5","rxn2o"],"module":1},"MessengerGraphQLThreadFetcher":{"resources":["7pDPb","KO79V","4LeXr","mgb8G","WQwNW","BoQ1G","gVLBA","QdGSO","2qa5V","uXLLm","I\/Oj6","8brkk","CnGE9"],"module":1},"DelightsTextTriggerTypedLogger":{"resources":["KO79V","4LeXr","qVIf2"],"module":1},"NYE2017Animation":{"resources":["4LeXr","KO79V","rgzm5","I\/Oj6","wb3qs","P8uBt"],"module":1},"NYE2017Dispatcher":{"resources":["VBj2e"],"module":1},"NYE2017TriggerStrings":{"resources":["zEmvK"],"module":1},"EncryptedImg":{"resources":["KO79V","7pDPb","VBj2e","Xp5tm"],"module":1},"UFIAddCommentLiveTypingPublisher":{"resources":["7pDPb","KO79V","I\/Oj6","jNgMf","4LeXr","mgb8G"],"module":1},"XUIErrorDialogImpl":{"resources":["4LeXr","KO79V","DXyMM","7pDPb","P8uBt","gzgdj","XxJQ4"],"module":1},"UFIUploader":{"resources":["7pDPb","KO79V","4LeXr","mgb8G","VBj2e","54\/mu","P8uBt","xLI7Z","NcYb3","7o0h9","D7hFh","fwsN4","aUqn9","nfKia","gzgdj","k\/dRv","J+tWg","tbDRX","I\/Oj6","wE\/xn"],"module":1},"ScrollableArea":{"resources":["KO79V","7pDPb","4LeXr","P8uBt"],"module":1},"ChatContentSearchFlyout.react":{"resources":["KO79V","4LeXr","mgb8G","ahhl3","7pDPb","xIc5a","kF1+E","lLT+Y","bn4q6","BoQ1G","I\/Oj6","P8uBt","MNa5l","wiAMM","nfKia","qLtVf","VBj2e","fwsN4"],"module":1},"ContextualLayerAutoFlip":{"resources":["KO79V","7pDPb","gzgdj"],"module":1},"XUIContextualDialog.react":{"resources":["P8uBt","KO79V","DXyMM","xIc5a","4LeXr","7pDPb","gzgdj"],"module":1},"LayerTabIsolation":{"resources":["KO79V","4LeXr","7pDPb","gzgdj"],"module":1},"RelayRootContainer":{"resources":["xIc5a","KO79V","4LeXr","1QKzr","7o0h9","7pDPb","gzgdj","I\/Oj6"],"module":1},"StickersStore.react":{"resources":["KO79V","7pDPb","xIc5a","4LeXr","1QKzr","7o0h9","VBj2e","I\/Oj6","gzgdj","P8uBt","nfKia","JVQrG","3py3C","S1OBF","yq8d4","B8HgN","622TF","D+lWU"],"module":1},"StickersStorePackDetailRoute":{"resources":["7o0h9","1QKzr","xIc5a","KO79V","4LeXr","3py3C"],"module":1},"StickersStorePackListRoute":{"resources":["7o0h9","1QKzr","xIc5a","KO79V","4LeXr","3py3C"],"module":1},"StickersFlyout.react":{"resources":["7pDPb","xIc5a","KO79V","4LeXr","Xp5tm","B8HgN","F0FOt","VyIGb","I\/Oj6","1QKzr","7o0h9","gzgdj","BoQ1G","VBj2e","S1OBF","P8uBt","BTuj2","gVLBA","glg8M","nfKia","JVQrG","IiFdP","JHn9H","yq8d4","pPYY3","wiAMM","fwsN4"],"module":1},"EmoticonUtils":{"resources":["P8uBt","VBj2e","60YTU"],"module":1},"EmoticonsList":{"resources":["P8uBt","VBj2e"],"module":1},"SelectionPosition":{"resources":["4LeXr","KO79V","gzgdj","7pDPb","60YTU"],"module":1},"TextAreaControl":{"resources":["KO79V","5PUV8","4LeXr"],"module":1},"OptimisticVideoComment.react":{"resources":["KO79V","7pDPb","VBj2e","Xp5tm","xIc5a","4LeXr","nfKia","gzgdj","P8uBt","l4aBW","9p0Oq","k\/dRv","J+tWg","IrfhN","fwsN4","I\/Oj6","gaYz9"],"module":1},"Sticker.react":{"resources":["KO79V","7pDPb","xIc5a","4LeXr","BoQ1G","pPYY3","VBj2e","IiFdP"],"module":1},"UFIAttachedMediaPreview.react":{"resources":["xIc5a","KO79V","4LeXr","7pDPb","P8uBt","Xp5tm","gzgdj","VBj2e","nfKia","gaYz9","Vax3W"],"module":1},"UFICommentMarkdownPreview.react":{"resources":["xIc5a","KO79V","4LeXr","7pDPb","gzgdj","P8uBt","glg8M","nfKia","FKaJK","z4sTc","RrQPb","pI7AA","0Qz\/x","Hnz7V"],"module":1},"XUIAmbientNUX.react":{"resources":["xIc5a","KO79V","4LeXr","DXyMM","7pDPb","P8uBt","gzgdj","nfKia"],"module":1},"LiveSendTipButtonUtil":{"resources":["KO79V","4LeXr","2wfDx","I\/Oj6","7ndNQ"],"module":1},"PhotoSnowlift":{"resources":["KO79V","4LeXr","mgb8G","7pDPb","nfKia","gzgdj","xLI7Z","VBj2e","Xp5tm","P8uBt","2wfDx","I\/Oj6","oQbcB","xIc5a","4B2Qx","z1p7V","73tQl","I5cJ2","J+tWg"],"module":1},"VideoChannel":{"resources":["HAcxX"],"module":1},"AsyncResponse":{"resources":["KO79V"],"module":1},"Live":{"resources":["4LeXr","KO79V","3q0pN","VBj2e","2\/maQ"],"module":1},"PhotoInlineEditor":{"resources":["4LeXr","KO79V","7pDPb","oQbcB","5PUV8","P8uBt","DXyMM","VBj2e","F90WH","B76cY","7unvu"],"module":1},"PhotoTagApproval":{"resources":["4LeXr","KO79V","oQbcB","\/mnVq"],"module":1},"PhotoTagger":{"resources":["7pDPb","KO79V","4LeXr","mgb8G","HWLe0","DXyMM","P8uBt","gzgdj","O+8J5","rxn2o","xIc5a","9rG0r","itM80","60TSu","oQbcB","I\/Oj6","VBj2e","lLT+Y","nfKia","5hNXg"],"module":1},"PhotoTags":{"resources":["4LeXr","KO79V","oQbcB","\/mnVq"],"module":1},"PhotosButtonTooltips":{"resources":["KO79V","4LeXr","mgb8G","7pDPb","gzgdj","P8uBt","X\/B82"],"module":1},"SpotlightShareViewer":{"resources":["4LeXr","KO79V","7pDPb","mgb8G","73tQl","gzgdj","zyFOp"],"module":1},"TagTokenizer":{"resources":["4LeXr","KO79V","VBj2e","P8uBt","F90WH","B76cY","\/mnVq","7pDPb","DXyMM","5PUV8"],"module":1},"VideoRotate":{"resources":["KO79V","4LeXr","mgb8G","7pDPb","nfKia","gzgdj","xLI7Z","6AU0l"],"module":1},"css:fb-photos-snowlift-fullscreen-css":{"resources":["VDymv"]},"CompactTypeaheadRenderer":{"resources":["4LeXr","KO79V","P8uBt","VBj2e","gzgdj","bn4q6","7pDPb","yFyUx"],"module":1},"ContextualTypeaheadView":{"resources":["4LeXr","KO79V","P8uBt","VBj2e","F90WH","WEGtD","qnR1n","7pDPb","gzgdj"],"module":1},"InputSelection":{"resources":["4LeXr","KO79V","gzgdj"],"module":1},"HashtagParser":{"resources":["D7hFh","gzgdj","WEGtD"],"module":1},"MentionsInput":{"resources":["KO79V","4LeXr","gzgdj","7pDPb","RZozx","VBj2e","O+8J5","DXyMM"],"module":1},"Typeahead":{"resources":["KO79V","4LeXr","F90WH","WEGtD"],"module":1},"TypeaheadAreaCore":{"resources":["4LeXr","KO79V","gzgdj","5PUV8","7pDPb","P8uBt","DXyMM","qnR1n","RZozx"],"module":1},"TypeaheadBestName":{"resources":["VBj2e","RZozx"],"module":1},"TypeaheadHoistFriends":{"resources":["RZozx"],"module":1},"TypeaheadMetrics":{"resources":["KO79V","4LeXr","mgb8G","v1FBw","RZozx"],"module":1},"TypeaheadMetricsX":{"resources":["7pDPb","KO79V","4LeXr","mgb8G","v1FBw","qfzTq"],"module":1},"TypingDetector":{"resources":["KO79V","7pDPb","gVLBA","S1OBF"],"module":1},"UFIComments":{"resources":["7pDPb","I\/Oj6","4LeXr","KO79V","VBj2e","mgb8G","lLT+Y"],"module":1},"SpatialReactionsProductionStore":{"resources":["7pDPb","iMk7H","KO79V","4LeXr","xIc5a","F0FOt","1qJfW"],"module":1},"UFIReactionsMenuImpl.react":{"resources":["KO79V","7pDPb","xIc5a","4LeXr","itM80","nfKia","lLT+Y","asUmo","VBj2e","4\/h+Q","1qJfW","J+tWg","gzgdj","54\/mu","pmhcL","I\/Oj6","F0FOt","DXyMM","iMk7H","E\/dNZ","5yQBc","mgb8G"],"module":1},"UFIReactionsMenuWithAnimatedVectorIcons.react":{"resources":["xIc5a","KO79V","4LeXr","NcYb3","29r44","7pDPb","itM80","nfKia","lLT+Y","asUmo","VBj2e","4\/h+Q","1qJfW","J+tWg","gzgdj","54\/mu","pmhcL","I\/Oj6","F0FOt","DXyMM","iMk7H","E\/dNZ","5yQBc","mgb8G","LY13N"],"module":1},"UFIReactionsMenuWithStaticVectorIcons.react":{"resources":["xIc5a","KO79V","4LeXr","NcYb3","29r44","7pDPb","itM80","nfKia","lLT+Y","asUmo","VBj2e","4\/h+Q","1qJfW","J+tWg","gzgdj","54\/mu","pmhcL","I\/Oj6","F0FOt","DXyMM","iMk7H","E\/dNZ","5yQBc","mgb8G"],"module":1},"UFIReactionsNUX.react":{"resources":["KO79V","4LeXr","mgb8G","7pDPb","xIc5a","lLT+Y","DXyMM","P8uBt","gzgdj","nfKia","Dnlm1"],"module":1},"DOMScroll":{"resources":["4LeXr","KO79V","7pDPb"],"module":1},"LegacyContextualDialog":{"resources":["4LeXr","KO79V","7pDPb","Qt9ub","gzgdj","DXyMM","P8uBt","3PGYg","8aeA9"],"module":1},"UFICommentMarkdownFormattedLink.react":{"resources":["xIc5a","KO79V","4LeXr","VBj2e","lLT+Y","P8uBt","7pDPb","gzgdj","glg8M","nfKia","tbDRX","FKaJK","9EMwh"],"module":1},"UFICreatorInfo.react":{"resources":["xIc5a","KO79V","4LeXr","I\/Oj6","fwsN4","CnGE9","7pDPb","nfKia","IiFdP"],"module":1},"UFIReactionsTooltipImpl.react":{"resources":["7pDPb","KO79V","4LeXr","mgb8G","xIc5a","gzgdj","P8uBt","lLT+Y","U5YL3","ybinV"],"module":1},"UFICommentShareNUX.react":{"resources":["KO79V","4LeXr","mgb8G","7pDPb","gzgdj","xIc5a","lLT+Y","DXyMM","P8uBt","nfKia","+VWNr"],"module":1},"MultiPlacePageInfoCard.react":{"resources":["KO79V","4LeXr","mgb8G","xIc5a","Xp5tm","VBj2e","7pDPb","29hGe","P8uBt","wiAMM","gzgdj","I\/Oj6","nfKia","fwsN4","T6by2","v1FBw","a7Tia","pSiWa","YyAHK","krylL","DXyMM","hZXZf","glg8M","UH7ZD","Yu7nb"],"module":1},"PlaceListLiveCommentAttachment.react":{"resources":["pSiWa","zparn","KO79V","4LeXr","mgb8G","xIc5a","Xp5tm","VBj2e","7pDPb","29hGe","P8uBt","wiAMM","gzgdj","I\/Oj6","nfKia","fwsN4","T6by2","v1FBw","a7Tia","YyAHK","krylL","DXyMM","hZXZf","glg8M","UH7ZD","Yu7nb"],"module":1},"UFILiveCommentLinkPreviewMisinfoWarningFooter.react":{"resources":["KO79V","7pDPb","xIc5a","4LeXr","AmMkr","FRpa\/"],"module":1},"UFILiveCommentLinkPreview.react":{"resources":["xIc5a","KO79V","4LeXr","7pDPb","nfKia","D+lWU","VBj2e","P8uBt","itM80","kn9pk"],"module":1},"ContextualDialogArrow":{"resources":["4LeXr","KO79V","7pDPb","P8uBt","DXyMM"],"module":1},"PopoverMenu.react":{"resources":["xIc5a","KO79V","4LeXr","nfKia","7pDPb","gzgdj","P8uBt","glg8M"],"module":1},"ReactXUIMenu":{"resources":["KO79V","4LeXr","7pDPb","P8uBt","xIc5a","glg8M","gzgdj"],"module":1},"UFICommentRemovalControls.react":{"resources":["xIc5a","KO79V","4LeXr","7pDPb","glg8M","itM80","fM9ic"],"module":1},"UFILiveVideoAnnouncementCTAContainer.react":{"resources":["I\/Oj6","xIc5a","KO79V","4LeXr","7pDPb","DE+m6","lLT+Y","VBj2e","nfKia","F0FOt","DXyMM","mgb8G","GmbvR"],"module":1},"UFIScrollHighlight":{"resources":["4LeXr","KO79V","7pDPb","v1FBw","+\/EdC","rSdpp"],"module":1},"Toggler":{"resources":["KO79V","4LeXr","7pDPb","gzgdj","P8uBt"],"module":1},"Tooltip":{"resources":["KO79V","4LeXr","mgb8G","7pDPb","gzgdj","P8uBt"],"module":1},"DOM":{"resources":["4LeXr","KO79V"],"module":1},"Form":{"resources":["4LeXr","KO79V"],"module":1},"Input":{"resources":["KO79V"],"module":1},"trackReferrer":{"resources":[],"module":1}});}});
requireLazy(["ix"], function(ix) {ix.add({"images\/mercury\/clients\/messenger\/core\/LoadingSpinner.png":{"sprited":true,"spriteCssClass":"sx_cd54c9","spriteMapCssClass":"sp_TK0mQ66pSVs"},"86853":{"sprited":true,"spriteCssClass":"sx_cd54c9","spriteMapCssClass":"sp_TK0mQ66pSVs"},"images\/mercury\/clients\/messenger\/core\/LoadingSpinnerExtraLarge.png":{"sprited":true,"spriteCssClass":"sx_041def","spriteMapCssClass":"sp_TK0mQ66pSVs"},"86854":{"sprited":true,"spriteCssClass":"sx_041def","spriteMapCssClass":"sp_TK0mQ66pSVs"},"images\/mercury\/clients\/messenger\/core\/LoadingSpinnerGrey.png":{"sprited":true,"spriteCssClass":"sx_430ee5","spriteMapCssClass":"sp_TK0mQ66pSVs"},"86857":{"sprited":true,"spriteCssClass":"sx_430ee5","spriteMapCssClass":"sp_TK0mQ66pSVs"},"images\/messaging\/stickers\/store\/basket.png":{"sprited":true,"spriteCssClass":"sx_ff93dd","spriteMapCssClass":"sp_avtVGZ81hWA"},"87169":{"sprited":true,"spriteCssClass":"sx_ff93dd","spriteMapCssClass":"sp_avtVGZ81hWA"},"images\/messaging\/stickers\/store\/characters.png":{"sprited":true,"spriteCssClass":"sx_5c8a4d","spriteMapCssClass":"sp_avtVGZ81hWA"},"87170":{"sprited":true,"spriteCssClass":"sx_5c8a4d","spriteMapCssClass":"sp_avtVGZ81hWA"},"images\/messaging\/stickers\/store\/backarrow.png":{"sprited":true,"spriteCssClass":"sx_0933da","spriteMapCssClass":"sp_avtVGZ81hWA"},"87168":{"sprited":true,"spriteCssClass":"sx_0933da","spriteMapCssClass":"sp_avtVGZ81hWA"},"images\/messaging\/stickers\/icons\/emoji.png":{"sprited":true,"spriteCssClass":"sx_7ba6ac","spriteMapCssClass":"sp_DK-WgnuaQQB"},"87143":{"sprited":true,"spriteCssClass":"sx_7ba6ac","spriteMapCssClass":"sp_DK-WgnuaQQB"},"images\/messaging\/stickers\/icons\/recent.png":{"sprited":true,"spriteCssClass":"sx_80b618","spriteMapCssClass":"sp_DK-WgnuaQQB"},"87145":{"sprited":true,"spriteCssClass":"sx_80b618","spriteMapCssClass":"sp_DK-WgnuaQQB"},"images\/messaging\/stickers\/icons\/search.png":{"sprited":true,"spriteCssClass":"sx_652791","spriteMapCssClass":"sp_DK-WgnuaQQB"},"87147":{"sprited":true,"spriteCssClass":"sx_652791","spriteMapCssClass":"sp_DK-WgnuaQQB"},"images\/messaging\/stickers\/selector\/left.png":{"sprited":true,"spriteCssClass":"sx_485981","spriteMapCssClass":"sp_DK-WgnuaQQB"},"87153":{"sprited":true,"spriteCssClass":"sx_485981","spriteMapCssClass":"sp_DK-WgnuaQQB"},"images\/messaging\/stickers\/selector\/right.png":{"sprited":true,"spriteCssClass":"sx_0b3333","spriteMapCssClass":"sp_DK-WgnuaQQB"},"87156":{"sprited":true,"spriteCssClass":"sx_0b3333","spriteMapCssClass":"sp_DK-WgnuaQQB"},"images\/messaging\/stickers\/selector\/sticker_store.png":{"sprited":true,"spriteCssClass":"sx_0fd624","spriteMapCssClass":"sp_DK-WgnuaQQB"},"87160":{"sprited":true,"spriteCssClass":"sx_0fd624","spriteMapCssClass":"sp_DK-WgnuaQQB"},"images\/messaging\/stickers\/icons\/sad_face.png":{"sprited":true,"spriteCssClass":"sx_f27e23","spriteMapCssClass":"sp_DK-WgnuaQQB"},"87146":{"sprited":true,"spriteCssClass":"sx_f27e23","spriteMapCssClass":"sp_DK-WgnuaQQB"},"images\/mobile\/glyph\/arrow-right_white_s.png":{"sprited":true,"spriteCssClass":"sx_dc12ec","spriteMapCssClass":"sp_6zNiJImyNs1"},"88724":{"sprited":true,"spriteCssClass":"sx_dc12ec","spriteMapCssClass":"sp_6zNiJImyNs1"},"images\/assets_DO_NOT_HARDCODE\/fb_glyphs\/friend-id-card_12_fig-blue.png":{"sprited":true,"spriteCssClass":"sx_ccd9fc","spriteMapCssClass":"sp_n0mXYrvnubR"},"116571":{"sprited":true,"spriteCssClass":"sx_ccd9fc","spriteMapCssClass":"sp_n0mXYrvnubR"},"images\/assets_DO_NOT_HARDCODE\/fb_glyphs\/bulb_20_fig-white.png":{"sprited":true,"spriteCssClass":"sx_3c3dca","spriteMapCssClass":"sp_Rc0YJeq2Mmq"},"114492":{"sprited":true,"spriteCssClass":"sx_3c3dca","spriteMapCssClass":"sp_Rc0YJeq2Mmq"},"images\/assets_DO_NOT_HARDCODE\/fb_glyphs\/comment_20_fig-white.png":{"sprited":true,"spriteCssClass":"sx_1e635f","spriteMapCssClass":"sp_Rc0YJeq2Mmq"},"114673":{"sprited":true,"spriteCssClass":"sx_1e635f","spriteMapCssClass":"sp_Rc0YJeq2Mmq"},"images\/assets_DO_NOT_HARDCODE\/fb_glyphs\/eye_20_fig-white.png":{"sprited":true,"spriteCssClass":"sx_ec28c5","spriteMapCssClass":"sp_Rc0YJeq2Mmq"},"114860":{"sprited":true,"spriteCssClass":"sx_ec28c5","spriteMapCssClass":"sp_Rc0YJeq2Mmq"},"images\/assets_DO_NOT_HARDCODE\/fb_glyphs\/like_20_fig-white.png":{"sprited":true,"spriteCssClass":"sx_692757","spriteMapCssClass":"sp_Rc0YJeq2Mmq"},"115160":{"sprited":true,"spriteCssClass":"sx_692757","spriteMapCssClass":"sp_Rc0YJeq2Mmq"},"images\/assets_DO_NOT_HARDCODE\/fb_glyphs\/chevron-down_16_fig-light-20.png":{"sprited":true,"spriteCssClass":"sx_5e003c","spriteMapCssClass":"sp_xWGdfdP4lDL"},"125792":{"sprited":true,"spriteCssClass":"sx_5e003c","spriteMapCssClass":"sp_xWGdfdP4lDL"},"images\/tip_jar\/tip1.png":{"sprited":true,"spriteCssClass":"sx_e8a010","spriteMapCssClass":"sp_Rc0YJeq2Mmq"},"99652":{"sprited":true,"spriteCssClass":"sx_e8a010","spriteMapCssClass":"sp_Rc0YJeq2Mmq"},"images\/tip_jar\/tip2.png":{"sprited":true,"spriteCssClass":"sx_537fe3","spriteMapCssClass":"sp_Rc0YJeq2Mmq"},"99653":{"sprited":true,"spriteCssClass":"sx_537fe3","spriteMapCssClass":"sp_Rc0YJeq2Mmq"},"images\/tip_jar\/tip3.png":{"sprited":true,"spriteCssClass":"sx_140f2d","spriteMapCssClass":"sp_Rc0YJeq2Mmq"},"99654":{"sprited":true,"spriteCssClass":"sx_140f2d","spriteMapCssClass":"sp_Rc0YJeq2Mmq"},"images\/assets_DO_NOT_HARDCODE\/fb_glyphs\/pushpin_12_fig-blue.png":{"sprited":true,"spriteCssClass":"sx_695659","spriteMapCssClass":"sp_Rc0YJeq2Mmq"},"117058":{"sprited":true,"spriteCssClass":"sx_695659","spriteMapCssClass":"sp_Rc0YJeq2Mmq"},"images\/assets_DO_NOT_HARDCODE\/fb_glyphs\/plus_24_fig-blue.png":{"sprited":true,"spriteCssClass":"sx_e49622","spriteMapCssClass":"sp_4nDaFI5d8Px"},"117012":{"sprited":true,"spriteCssClass":"sx_e49622","spriteMapCssClass":"sp_4nDaFI5d8Px"},"images\/assets_DO_NOT_HARDCODE\/fb_glyphs\/briefcase-business_12_fig-light-50.png":{"sprited":true,"spriteCssClass":"sx_3610f5","spriteMapCssClass":"sp_4nDaFI5d8Px"},"122471":{"sprited":true,"spriteCssClass":"sx_3610f5","spriteMapCssClass":"sp_4nDaFI5d8Px"},"images\/assets_DO_NOT_HARDCODE\/fb_glyphs\/city_12_fig-light-50.png":{"sprited":true,"spriteCssClass":"sx_3e4673","spriteMapCssClass":"sp_4nDaFI5d8Px"},"122630":{"sprited":true,"spriteCssClass":"sx_3e4673","spriteMapCssClass":"sp_4nDaFI5d8Px"},"images\/assets_DO_NOT_HARDCODE\/fb_glyphs\/education_12_fig-light-50.png":{"sprited":true,"spriteCssClass":"sx_3f60e3","spriteMapCssClass":"sp_4nDaFI5d8Px"},"122834":{"sprited":true,"spriteCssClass":"sx_3f60e3","spriteMapCssClass":"sp_4nDaFI5d8Px"},"images\/assets_DO_NOT_HARDCODE\/fb_glyphs\/info-solid_12_fig-light-50.png":{"sprited":true,"spriteCssClass":"sx_18a3be","spriteMapCssClass":"sp_4nDaFI5d8Px"},"123136":{"sprited":true,"spriteCssClass":"sx_18a3be","spriteMapCssClass":"sp_4nDaFI5d8Px"},"images\/assets_DO_NOT_HARDCODE\/fb_glyphs\/network_12_fig-light-50.png":{"sprited":true,"spriteCssClass":"sx_e1f219","spriteMapCssClass":"sp_4nDaFI5d8Px"},"123290":{"sprited":true,"spriteCssClass":"sx_e1f219","spriteMapCssClass":"sp_4nDaFI5d8Px"},"images\/assets_DO_NOT_HARDCODE\/fb_glyphs\/like_16_fig-light-30.png":{"sprited":true,"spriteCssClass":"sx_2e8a75","spriteMapCssClass":"sp_RRZRm1Zr3oX"},"124770":{"sprited":true,"spriteCssClass":"sx_2e8a75","spriteMapCssClass":"sp_RRZRm1Zr3oX"},"images\/chat\/composer\/composerSearchTrending.png":{"sprited":false,"uri":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yL\/r\/MVLY03UaITD.png","width":16,"height":16},"28005":{"sprited":false,"uri":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yL\/r\/MVLY03UaITD.png","width":16,"height":16},"images\/loaders\/indicator_black.gif":{"sprited":false,"uri":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y7\/r\/pgEFhPxsWZX.gif","width":32,"height":32},"85423":{"sprited":false,"uri":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y7\/r\/pgEFhPxsWZX.gif","width":32,"height":32},"images\/loaders\/indicator_blue_large.gif":{"sprited":false,"uri":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y9\/r\/jKEcVPZFk-2.gif","width":32,"height":32},"85426":{"sprited":false,"uri":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y9\/r\/jKEcVPZFk-2.gif","width":32,"height":32},"images\/loaders\/indicator_blue_medium.gif":{"sprited":false,"uri":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yk\/r\/LOOn0JtHNzb.gif","width":16,"height":16},"85427":{"sprited":false,"uri":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yk\/r\/LOOn0JtHNzb.gif","width":16,"height":16},"images\/loaders\/indicator_blue_small.gif":{"sprited":false,"uri":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yb\/r\/GsNJNwuI-UM.gif","width":16,"height":11},"85428":{"sprited":false,"uri":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yb\/r\/GsNJNwuI-UM.gif","width":16,"height":11},"images\/loaders\/indicator_white_large.gif":{"sprited":false,"uri":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yG\/r\/b53Ajb4ihCP.gif","width":32,"height":32},"85429":{"sprited":false,"uri":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yG\/r\/b53Ajb4ihCP.gif","width":32,"height":32},"images\/loaders\/indicator_white_small.gif":{"sprited":false,"uri":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y-\/r\/AGUNXgX_Wx3.gif","width":16,"height":11},"85430":{"sprited":false,"uri":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/y-\/r\/AGUNXgX_Wx3.gif","width":16,"height":11},"images\/assets_DO_NOT_HARDCODE\/fb_glyphs\/checkmark_16_fig-light-30.png":{"sprited":false,"uri":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yT\/r\/Lk5iPocO97X.png","width":16,"height":16},"124180":{"sprited":false,"uri":"https:\/\/static.xx.fbcdn.net\/rsrc.php\/v3\/yT\/r\/Lk5iPocO97X.png","width":16,"height":16}});});</script>
<script>requireLazy(["InitialJSLoader"], function(InitialJSLoader) {InitialJSLoader.loadOnDOMContentReady(["KO79V","mgb8G","7pDPb","wg+SO","i5RnR","gzgdj","DXyMM","hZXZf","xIc5a","I\/Oj6","4L2ow"]);});</script>
<script>require("TimeSlice").guard(function() {require("ServerJSDefine").handleDefines([]);require("InitialJSLoader").handleServerJS({"markup":[["__markup_a588f507_0_0",{"__html":"\u003Cdiv class=\"_5633 _5634\">\u0906\u092a\u0923\u093e\u0902\u0938 \u0938\u0930\u094d\u0935 \u092e\u093e\u0939\u093f\u0924\u0940 \u092d\u0930\u0923\u0947 \u0906\u0935\u0936\u094d\u092f\u0915 \u0906\u0939\u0947.\u003C\/div>"},1],["__markup_9f5fac15_0_0",{"__html":"\u003Cdiv class=\"_5633 _5634\">\u0906\u092a\u0932\u0947 \u0928\u093e\u0935 \u0915\u093e\u092f \u0906\u0939\u0947 ?\u003C\/div>"},1],["__markup_9f5fac15_0_1",{"__html":"\u003Cdiv class=\"_5633 _5634\">\u0906\u092a\u0923 \u0932\u0949\u0917 \u0907\u0928 \u0915\u0930\u0924\u093e \u0924\u0947\u0935\u094d\u0939\u093e \u0906\u092a\u0932\u094d\u092f\u093e\u0932\u093e \u091c\u0930 \u0906\u092a\u0932\u093e \u092a\u093e\u0938\u0935\u0930\u094d\u0921 \u0930\u0940\u0938\u0947\u091f \u0915\u0930\u0923\u094d\u092f\u093e\u091a\u0940 \u0906\u0935\u0936\u094d\u092f\u0915\u0924\u093e \u0905\u0938\u0947\u0932 \u0924\u0930 \u0906\u092a\u0923 \u0939\u0947 \u0935\u093e\u092a\u0930\u093e\u0932.\u003C\/div>"},1],["__markup_9f5fac15_0_2",{"__html":"\u003Cdiv class=\"_5633 _5634\">\u0915\u093f\u092e\u093e\u0928 \u0938\u0939\u093e \u0905\u0915\u094d\u0937\u0930\u0947, \u0906\u0915\u0921\u0947 \u0935 \u0935\u093f\u0930\u093e\u092e\u091a\u093f\u0928\u094d\u0939\u0947 (\u091c\u0938\u0947 ! \u0906\u0923\u093f &amp;) \u092a\u094d\u0930\u0935\u093f\u0937\u094d\u091f \u0915\u0930\u093e.\u003C\/div>"},1],["__markup_a588f507_0_1",{"__html":"\u003Cdiv class=\"_5633 _5634\">\u0915\u0943\u092a\u092f\u093e \u0935\u0948\u0927 \u0908\u092e\u0947\u0932 \u092a\u094d\u0930\u0935\u093f\u0937\u094d\u0920 \u0915\u0930\u093e.\u003C\/div>"},1],["__markup_9f5fac15_0_3",{"__html":"\u003Cdiv class=\"_5633 _5634\">\u0915\u0943\u092a\u092f\u093e \u090f\u0915 \u0935\u0948\u0927 \u0908\u092e\u0947\u0932 \u092a\u0924\u094d\u0924\u093e \u0915\u093f\u0902\u0935\u093e \u092e\u094b\u092c\u093e\u0908\u0932 \u0928\u0902\u092c\u0930 \u092a\u094d\u0930\u0935\u093f\u0937\u094d\u091f \u0915\u0930\u093e.\u003C\/div>"},1],["__markup_a588f507_0_2",{"__html":"\u003Cdiv class=\"_5633 _5634\">\u0915\u0943\u092a\u092f\u093e \u0935\u0948\u0927 \u092e\u094b\u092c\u093e\u0908\u0932 \u0928\u0902\u092c\u0930 \u0915\u093f\u0902\u0935\u093e \u0908\u092e\u0947\u0932 \u092a\u0924\u094d\u200d\u0924\u093e \u092a\u094d\u0930\u0935\u093f\u0937\u094d\u200d\u091f \u0915\u0930\u093e.\u003C\/div>"},1],["__markup_a588f507_0_3",{"__html":"\u003Cdiv class=\"_5633 _5634\">\u0906\u092a\u0932\u093e \u0908\u092e\u0947\u0932 \u092a\u0924\u094d\u0924\u093e \u092a\u0941\u0928\u094d\u0939\u093e \u092a\u094d\u0930\u0935\u093f\u0937\u094d\u091f \u0915\u0930\u093e.\u003C\/div>"},1],["__markup_9f5fac15_0_4",{"__html":"\u003Cdiv class=\"_5633 _5634\">\u0915\u0943\u092a\u092f\u093e \u0905\u093e\u092a\u0932\u093e \u092e\u094b\u092c\u093e\u0908\u0932 \u0928\u0902\u092c\u0930 \u0915\u093f\u0902\u0935\u093e \u0908\u092e\u0947\u0932 \u092a\u0924\u094d\u200d\u0924\u093e \u092a\u0941\u0928\u094d\u200d\u0939\u093e-\u092a\u094d\u0930\u0935\u093f\u0937\u094d\u200d\u091f \u0915\u0930\u093e.\u003C\/div>"},1],["__markup_a588f507_0_4",{"__html":"\u003Cdiv class=\"_5633 _5634\">\u0906\u092a\u0932\u093e \u0908\u092e\u0947\u0932 \u092a\u0924\u094d\u0924\u093e \u091c\u0941\u0933\u0924 \u0928\u093e\u0939\u0940. \u0915\u0943\u092a\u092f\u093e \u092a\u0941\u0928\u094d\u0939\u093e \u092a\u094d\u0930\u092f\u0924\u094d\u0928 \u0915\u0930\u093e.\u003C\/div>"},1],["__markup_a588f507_0_5",{"__html":"\u003Cdiv class=\"_5633 _5634\">\u0906\u092a\u0932\u0947 \u0908\u092e\u0947\u0932 \u0915\u093f\u0902\u0935\u093e \u092e\u094b\u092c\u093e\u0908\u0932 \u0928\u0902\u092c\u0930 \u091c\u0941\u0933\u0924 \u0928\u093e\u0939\u0940\u0924. \u0915\u0943\u092a\u092f\u093e \u092a\u0941\u0928\u094d\u0939\u093e \u092a\u094d\u0930\u092f\u0924\u094d\u0928 \u0915\u0930\u093e.\u003C\/div>"},1],["__markup_9f5fac15_0_5",{"__html":"\u003Cdiv class=\"_5633 _5634\">\u0906\u092a\u0932\u093e \u0935\u093e\u0922\u0926\u093f\u0935\u0938 \u0928\u093f\u0935\u0921\u093e. \u0939\u0947 \u0915\u094b\u0923 \u092a\u093e\u0939\u0942 \u0936\u0915\u0924\u094b \u0924\u0947 \u0906\u092a\u0923 \u0928\u0902\u0924\u0930 \u092c\u0926\u0932\u0942 \u0936\u0915\u0924\u093e.\u003C\/div>"},1],["__markup_9f5fac15_0_6",{"__html":"\u003Cdiv class=\"_5633 _5634\">\u0915\u0943\u092a\u092f\u093e \u0932\u093f\u0902\u0917 \u0928\u093f\u0935\u0921\u093e. \u0924\u0941\u092e\u094d\u0939\u0940 \u0939\u093e \u092c\u0926\u0932 \u0928\u0902\u0924\u0930 \u092a\u093e\u0939\u0942 \u0936\u0915\u0924\u093e.\u003C\/div>"},1]],"elements":[["__elem_835c633a_0_0","reg",1],["__elem_9ae3fd6f_0_0","u_0_0",1],["__elem_3f8a34cc_0_0","u_0_1",3],["__elem_9ae3fd6f_0_1","u_0_2",1],["__elem_3f8a34cc_0_1","u_0_3",3],["__elem_9f5fac15_0_1","u_0_4",1],["__elem_9ae3fd6f_0_2","u_0_5",1],["__elem_3f8a34cc_0_2","u_0_6",2],["__elem_9f5fac15_0_0","u_0_7",1],["__elem_9ae3fd6f_0_3","u_0_8",1],["__elem_3f8a34cc_0_3","u_0_9",2],["__elem_9f5fac15_0_3","u_0_a",1],["__elem_3f8a34cc_0_4","u_0_b",1],["__elem_9f5fac15_0_2","password_field",1],["__elem_9ae3fd6f_0_4","u_0_c",1],["__elem_3f8a34cc_0_5","u_0_d",2],["__elem_ffa3c607_0_0","u_0_e",1],["__elem_2a23d31e_0_0","u_0_f",1],["__elem_5d172255_0_0","u_0_g",1],["__elem_ddac73b6_0_0","u_0_h",1],["__elem_072b8e64_0_0","u_0_i",1],["__elem_ddac73b6_0_1","u_0_j",1],["__elem_97e096cf_0_0","u_0_m",1],["__elem_2a23d31e_0_1","u_0_n",1],["__elem_85b7cbf7_0_0","reg",1],["__elem_da4ef9a3_0_0","u_0_o",1],["__elem_a588f507_0_1","captcha_buttons",1],["__elem_da4ef9a3_0_1","u_0_p",1],["__elem_a588f507_0_0","reg_pages_msg",1],["__elem_835c633a_0_1","login_form",1],["__elem_1edd4980_0_0","loginbutton",1],["__elem_f46f4946_0_0","u_0_r",1],["__elem_f46f4946_0_1","u_0_s",1],["__elem_85b7cbf7_0_1","login_form",1],["__elem_a6f65671_0_0","pagelet_bluebar",1],["__elem_a588f507_0_2","globalContainer",2]],"require":[["TrackingPixel","loadWithNoReferrer",[],["https:\/\/cx.atdmt.com\/?f=AYygc9nJO13AVcz0PPEvVDNameDiO715MMwJT7lXvi-kjAuUv6i8h-P56pgGUcxKp2atStz7YxCzV8NT24kaEzQz&c=1475276788&v=1&l=2"],[]],["WebPixelRatio","startDetecting",[],[1],[]],["FocusListener"],["FlipDirectionOnKeypress"],["RegistrationController","init",["__elem_835c633a_0_0","__elem_ddac73b6_0_0","__elem_ddac73b6_0_1","__elem_072b8e64_0_0","__elem_5d172255_0_0","__elem_a588f507_0_0","__elem_a588f507_0_1","__elem_da4ef9a3_0_0","__elem_da4ef9a3_0_1","__elem_9f5fac15_0_0","__elem_9f5fac15_0_1","__elem_9f5fac15_0_2","__elem_9f5fac15_0_3"],[{"__m":"__elem_835c633a_0_0"},false,"form_focus",{"__m":"__elem_ddac73b6_0_0"},{"__m":"__elem_ddac73b6_0_1"},{"__m":"__elem_072b8e64_0_0"},{"__m":"__elem_5d172255_0_0"},{"__m":"__elem_a588f507_0_0"},{"__m":"__elem_a588f507_0_1"},{"__m":"__elem_da4ef9a3_0_0"},{"__m":"__elem_da4ef9a3_0_1"},"show",{"__m":"__elem_9f5fac15_0_0"},false,{"__m":"__elem_9f5fac15_0_1"},{"__m":"__elem_9f5fac15_0_2"},"registration_www",true,true,false,{"__m":"__elem_9f5fac15_0_3"}],[]],["RegistrationInlineValidations","register",["__elem_9ae3fd6f_0_0","__elem_3f8a34cc_0_0"],[{"__m":"__elem_9ae3fd6f_0_0"},{"__m":"__elem_3f8a34cc_0_0"},"left","flyout_design",false],[]],["RegistrationGenderPronounWarning","registerNameInput",["__elem_3f8a34cc_0_0"],["firstname",{"__m":"__elem_3f8a34cc_0_0"}],[]],["StickyPlaceholderInput","registerInput",["__elem_3f8a34cc_0_0"],[{"__m":"__elem_3f8a34cc_0_0"}],[]],["RegistrationInlineValidations","register",["__elem_9ae3fd6f_0_1","__elem_3f8a34cc_0_1"],[{"__m":"__elem_9ae3fd6f_0_1"},{"__m":"__elem_3f8a34cc_0_1"},"below","flyout_design",false],[]],["RegistrationGenderPronounWarning","registerNameInput",["__elem_3f8a34cc_0_1"],["lastname",{"__m":"__elem_3f8a34cc_0_1"}],[]],["StickyPlaceholderInput","registerInput",["__elem_3f8a34cc_0_1"],[{"__m":"__elem_3f8a34cc_0_1"}],[]],["RegistrationInlineValidations","register",["__elem_9ae3fd6f_0_2","__elem_3f8a34cc_0_2"],[{"__m":"__elem_9ae3fd6f_0_2"},{"__m":"__elem_3f8a34cc_0_2"},"left","flyout_design",false],[]],["StickyPlaceholderInput","registerInput",["__elem_3f8a34cc_0_2"],[{"__m":"__elem_3f8a34cc_0_2"}],[]],["RegistrationInlineValidations","register",["__elem_9ae3fd6f_0_3","__elem_3f8a34cc_0_3"],[{"__m":"__elem_9ae3fd6f_0_3"},{"__m":"__elem_3f8a34cc_0_3"},"left","flyout_design",false],[]],["StickyPlaceholderInput","registerInput",["__elem_3f8a34cc_0_3"],[{"__m":"__elem_3f8a34cc_0_3"}],[]],["StickyPlaceholderInput","registerInput",["__elem_3f8a34cc_0_4"],[{"__m":"__elem_3f8a34cc_0_4"}],[]],["RegistrationInlineValidations","register",["__elem_9ae3fd6f_0_4","__elem_3f8a34cc_0_5"],[{"__m":"__elem_9ae3fd6f_0_4"},{"__m":"__elem_3f8a34cc_0_5"},"left","flyout_design",false],[]],["StickyPlaceholderInput","registerInput",["__elem_3f8a34cc_0_5"],[{"__m":"__elem_3f8a34cc_0_5"}],[]],["RegistrationInlineValidations","register",["__elem_ffa3c607_0_0","__elem_2a23d31e_0_0"],[{"__m":"__elem_ffa3c607_0_0"},{"__m":"__elem_2a23d31e_0_0"},"left","flyout_design",false],[]],["RegistrationInlineValidations","register",["__elem_97e096cf_0_0","__elem_2a23d31e_0_1"],[{"__m":"__elem_97e096cf_0_0"},{"__m":"__elem_2a23d31e_0_1"},"left","flyout_design",false],[]],["ScriptPath","set",[],["WebIndexReduxController","b2227d82",{"imp_id":"45a9b0ff"}],[]],["UITinyViewportAction","init",[],[],[]],["ResetScrollOnUnload","init",["__elem_a588f507_0_2"],[{"__m":"__elem_a588f507_0_2"}],[]],["AccessibilityWebVirtualCursorClickLogger","init",["__elem_a6f65671_0_0","__elem_a588f507_0_2"],[[{"__m":"__elem_a6f65671_0_0"},{"__m":"__elem_a588f507_0_2"}]],[]],["WebStorageMonster","schedule",[],[],[]],["AsyncRequestNectarLogging"],["IntlUtils"],["TimezoneAutoset","setInputValue",["__elem_f46f4946_0_0"],[{"__m":"__elem_f46f4946_0_0"},1489213892],[]],["ScreenDimensionsAutoSet","setInputValue",["__elem_f46f4946_0_1"],[{"__m":"__elem_f46f4946_0_1"}],[]],["LoginFormController","init",["__elem_835c633a_0_1","__elem_1edd4980_0_0"],[{"__m":"__elem_835c633a_0_1"},{"__m":"__elem_1edd4980_0_0"},null,true],[]]]},"iw");}, "ServerJS define", {"root":true})();

onloadRegister_DEPRECATED(function (){useragentcm();});
onloadRegister_DEPRECATED(function (){try { $("email").focus(); } catch (_ignore) { }});</script>
<!-- BigPipe construction and first response -->
<script>var bigPipe = new (require("BigPipe"))({"forceFinish":true,"__sf":"iw"});</script>
<script>bigPipe.beforePageletArrive("first_response")</script>
<script>require("TimeSlice").guard((function(){bigPipe.onPageletArrive({id:"first_response",phase:0,jsmods:{},is_last:true,resource_map:{"P/mr5":{type:"css",src:"data:text/css; charset=utf-8;base64,I2Jvb3Rsb2FkZXJfUF9tcjV7aGVpZ2h0OjQycHg7fS5ib290bG9hZGVyX1BfbXI1e2Rpc3BsYXk6YmxvY2shaW1wb3J0YW50O30=",crossOrigin:1}},allResources:["q3yEk","nfKia","KO79V","4LeXr","mgb8G","7pDPb","wg+SO","i5RnR","gzgdj","DXyMM","hZXZf","xIc5a","P8uBt","I/Oj6","4L2ow","9rG0r","P/mr5"],displayResources:["q3yEk","nfKia","4LeXr","P8uBt","9rG0r","P/mr5"]});}),"onPageletArrive first_response",{"root":true,"pagelet":"first_response"})();</script>
<script>bigPipe.setPageID("6396124964432882893");</script><script>bigPipe.beforePageletArrive("last_response")</script>
<script>require("TimeSlice").guard((function(){bigPipe.onPageletArrive({id:"last_response",phase:1,jsmods:{require:[["NavigationMetrics","setPage",[],[{page:"WebIndexReduxController",page_type:"normal",page_uri:"https://www.facebook.com/",serverLID:"6396124964432882893"}],[]],["DimensionTracking"],["HighContrastMode","init",[],[{isHCM:false,spacerImage:"https://static.xx.fbcdn.net/rsrc.php/v3/y4/r/-PAXP-deijE.gif"}],[]],["ClickRefLogger"],["DetectBrokenProxyCache","run",[],[0,"c_user"],[]],["TimeSlice","setLogging",[],[false,0.01],[]],["NavigationClickPointHandler"],["UserActionHistory"],["ScriptPathLogger","startLogging",[],[],[]],["TimeSpentBitArrayLogger","init",[],[],[]],["CookieCore","setWithoutChecksIfFirstPartyContext",[],["_js_datr","xJnDWD4XakvefQcoLP-pG1Ew",63072000000,"/",false],[]],["CookieCore","setWithoutChecksIfFirstPartyContext",[],["_js_reg_fb_ref","https://www.facebook.com/",0,"/",true],[]],["CookieCore","setWithoutChecksIfFirstPartyContext",[],["_js_reg_fb_gate","https://www.facebook.com/",0,"/",true],[]]],define:[["UACMConfig",[],{ffver:63083,ffid1:"AcHzJDiCWpuvZBdqioQXS-qGqqEppRYieScotni3OMeg9srmd_bx7ZnUx8g_JVyf2q0",ffid2:"AcGqupzwMHFGQG4rhFZXzg195vB2ZuccSAcmsXyPAMfRo9n1Sce8WXGuEHrrkIvri9k",ffid3:"AcFYaq9HGuhdCMjZ-mhsBinn_dt-zdfr6ZXMPUMSk8dUhlsk30LXJRD5FrD96ri7RHRJwV8H-FzqVkUeMKBYH-5j",ffid4:"AcG6ftXnaQ71pC7LrxC84ec_FI8znpYCAJ542ps9QLKKu1m6tUfvUOFx2Vj7IiJG6DA"},308],["CaptchaClientConfig",[],{recaptchaPublicKey:"6LfDxsYSAAAAAGGLBGaRurawNnbvAGQw5UwRWYXL"},83],["LocaleInitialData",[],{locale:"mr_IN",language:"मराठी"},273],["RegistrationClientConfig",["__markup_a588f507_0_0","__markup_9f5fac15_0_0","__markup_9f5fac15_0_1","__markup_9f5fac15_0_2","__markup_a588f507_0_1","__markup_9f5fac15_0_3","__markup_a588f507_0_2","__markup_a588f507_0_3","__markup_9f5fac15_0_4","__markup_a588f507_0_4","__markup_a588f507_0_5","__markup_9f5fac15_0_5","__markup_9f5fac15_0_6"],{fields:{NAME:"name",FIRSTNAME:"firstname",LASTNAME:"lastname",EMAIL:"reg_email__",EMAIL_CONFIRMATION:"reg_email_confirmation__",SECOND_CONTACTPOINT:"reg_second_contactpoint__",GENDER:"sex",PASSWORD:"reg_passwd__",BIRTHDAY_DAY:"birthday_day",BIRTHDAY_MONTH:"birthday_month",BIRTHDAY_YEAR:"birthday_year",BIRTHDAY_WRAPPER:"birthday_wrapper",GENDER_WRAPPER:"gender_wrapper"},tooltips:{FIRSTNAME:"firstname_tooltip",LASTNAME:"lastname_tooltip",EMAIL:"email_tooltip",EMAIL_CONFIRMATION:"email_confirmation_tooltip",EMAIL_ONLY_CONFIRMATION:"email_only_confirmation_tooltip",SECOND_CONTACTPOINT:"second_contactpoint_tooltip",PASSWORD:"password_tooltip"},validators:{types:{TEXT:"text",SELECTORS:"selectors",RADIO:"radio"}},messages:{MISSING_FIELDS:{__m:"__markup_a588f507_0_0"},INCORRECT_NAME:{__m:"__markup_9f5fac15_0_0"},INCORRECT_CONTACTPOINT:{__m:"__markup_9f5fac15_0_1"},PASSWORD_BLANK:{__m:"__markup_9f5fac15_0_2"},INVALID_EMAIL:{__m:"__markup_a588f507_0_1"},INVALID_CONTACTPOINT:{__m:"__markup_9f5fac15_0_3"},INVALID_NUMBER_OR_EMAIL:{__m:"__markup_a588f507_0_2"},INCORRECT_EMAIL_CONF:{__m:"__markup_a588f507_0_3"},INCORRECT_NUMBER_OR_EMAIL_CONF:{__m:"__markup_9f5fac15_0_4"},EMAIL_RETYPE_DIFFERENT:{__m:"__markup_a588f507_0_4"},CONTACTPOINT_RETYPE_DIFFERENT:{__m:"__markup_a588f507_0_5"},INCOMPLETE_BIRTHDAY:{__m:"__markup_9f5fac15_0_5"},NO_GENDER:{__m:"__markup_9f5fac15_0_6"}},logging:{enabled:false,categories:{INLINE:"inline",SERVER:"server"},types:{IS_EMPTY:"is_empty",CONTACTPOINT_INVALID:"contactpoint_invalid",CONTACTPOINT_TAKEN:"contactpoint_taken",CONTACTPOINT_MATCH:"contactpoint_match",PASSWORD_WEAK:"password_weak",PASSWORD_SHORT:"password_short",TERMS_AGREEMENT:"terms_agreement",TOO_YOUNG:"too_young",ACCOUNT_DISABLED:"account_disabled",BAD_CAPTCHA:"bad_captcha",NAME_REJECTED:"name_rejected",SI_BLOCK:"si_block",BIRTHDAY_INVALID:"birthday_invalid"}},www_phone:true},87],["BanzaiVitalWWW",[],{useVital:true},1781],["TimeSpentConfig",[],{"0_delay":0,"0_timeout":8,delay:200000,timeout:64},142],["ImmediateActiveSecondsConfig",[],{sampling_rate:0},423]]},is_last:true,allResources:["q3yEk","nfKia","KO79V","4LeXr","mgb8G","7pDPb","wg+SO","i5RnR","gzgdj","DXyMM","hZXZf","xIc5a","P8uBt","I/Oj6","4L2ow","9rG0r","P/mr5"],displayResources:["q3yEk","nfKia","4LeXr","P8uBt","9rG0r","P/mr5"],the_end:true});}),"onPageletArrive last_response",{"root":true,"pagelet":"last_response"})();</script></body></html>
>>> 
============= RESTART: C:/Users/CEC-07/Desktop/pooja/file/url.py =============
<html><head><META HTTP-EQUIV="refresh" CONTENT="0;URL=/cgi-sys/defaultwebpage.cgi"></head><body></body></html>
>>> 
============= RESTART: C:/Users/CEC-07/Desktop/pooja/file/url.py =============






<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">



<link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-19e26a1cefb5f1e92203a9468134dbf46b5a5308aeeeee09c96b32fec8c8b044.css" media="all" rel="stylesheet" />
<link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-29c1cf342cce83bc5ed40adbf7f2757224d81dc757647eb0b0f3871bf773f40c.css" media="all" rel="stylesheet" />


<link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/site-2798f974141c19d38ae985c943b406198a2c1be7de3c6c882e955c0a544aa12a.css" media="all" rel="stylesheet" />


<meta name="viewport" content="width=device-width">

<title>The world&#39;s leading software development platform · GitHub</title>
<link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
<link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
<meta property="fb:app_id" content="1401488693436528">

<meta property="og:url" content="https://github.com">
<meta property="og:site_name" content="GitHub">
<meta property="og:title" content="Build software better, together">
<meta property="og:description" content="GitHub is where people build software. More than 20 million people use GitHub to discover, fork, and contribute to over 54 million projects.">
<meta property="og:image" content="https://assets-cdn.github.com/images/modules/open_graph/github-logo.png">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="1200">
<meta property="og:image" content="https://assets-cdn.github.com/images/modules/open_graph/github-mark.png">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="620">
<meta property="og:image" content="https://assets-cdn.github.com/images/modules/open_graph/github-octocat.png">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="620">


<link rel="assets" href="https://assets-cdn.github.com/">

<meta name="pjax-timeout" content="1000">

<meta name="request-id" content="C08C:4821:3FB3B7E:6427B8E:58C39A34" data-pjax-transient>


<meta name="selected-link" value="/" data-pjax-transient>

<meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
<meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="https://collector.githubapp.com/github-external/browser_event" name="octolytics-event-url" /><meta content="C08C:4821:3FB3B7E:6427B8E:58C39A34" name="octolytics-dimension-request_id" />





<meta class="js-ga-set" name="dimension1" content="Logged Out">




<meta name="hostname" content="github.com">
<meta name="user-login" content="">

<meta name="expected-hostname" content="github.com">
<meta name="js-proxy-site-detection-payload" content="MWU0YTNiZDQyNTY2Zjg3N2E2OThmMzI2ZWJiMTQ3YWFhNGE1ZGJiOWI0ZGExMGViZTFiZmIwNmYyMTQ2MWMxNHx7InJlbW90ZV9hZGRyZXNzIjoiMTAzLjU3LjcwLjg2IiwicmVxdWVzdF9pZCI6IkMwOEM6NDgyMTozRkIzQjdFOjY0MjdCOEU6NThDMzlBMzQiLCJ0aW1lc3RhbXAiOjE0ODkyMTQwMDUsImhvc3QiOiJnaXRodWIuY29tIn0=">


<meta name="html-safe-nonce" content="a11e0b2aa90516938157a1977b09a32c1af26241">

<meta http-equiv="x-pjax-version" content="83c1dcf1d80ba3c0dd0a2fb8c4e6d3e5">


<meta name="viewport" content="width=device-width">
<link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/site-2798f974141c19d38ae985c943b406198a2c1be7de3c6c882e955c0a544aa12a.css" media="all" rel="stylesheet" />


<link rel="canonical" href="https://github.com/" data-pjax-transient>


<meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

<meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

<link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
<link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">



</head>

<body class="logged-out env-production page-responsive min-width-0 alt-body-font site-header-dark">


<div class="position-relative js-header-wrapper ">
<a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
<div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>







<header class="site-header js-details-container Details" role="banner">
<div class="container-responsive">
<a class="header-logo-invertocat" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
<svg aria-hidden="true" class="octicon octicon-mark-github" height="32" version="1.1" viewBox="0 0 16 16" width="32"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>

<button class="btn-link float-right site-header-toggle js-details-target" type="button" aria-label="Toggle navigation">
<svg aria-hidden="true" class="octicon octicon-three-bars" height="24" version="1.1" viewBox="0 0 12 16" width="18"><path fill-rule="evenodd" d="M11.41 9H.59C0 9 0 8.59 0 8c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zm0-4H.59C0 5 0 4.59 0 4c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM.59 11H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1H.59C0 13 0 12.59 0 12c0-.59 0-1 .59-1z"/></svg>
</button>

<div class="site-header-menu">
<nav class="site-header-nav">
<a href="/features" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:features" data-selected-links="/features /features">
Features
</a>        <a href="/explore" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship /showcases /explore">
Explore
</a>        <a href="/pricing" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:pricing" data-selected-links="/pricing /pricing">
Pricing
</a>      </nav>

<div class="site-header-actions">
<div class="header-search   js-site-search" role="search">
<!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/search" class="js-site-search-form" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
<label class="form-control header-search-wrapper js-chromeless-input-container">
<div class="header-search-scope"></div>
<input type="text"
class="form-control header-search-input js-site-search-focus "
data-hotkey="s"
name="q"
placeholder="Search GitHub"
aria-label="Search GitHub"
data-unscoped-placeholder="Search GitHub"
data-scoped-placeholder="Search"
autocapitalize="off">
</label>
</form></div>


<a class="text-bold site-header-link" href="/login" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign in</a>
<span class="text-gray">or</span>
<a class="text-bold site-header-link" href="/join?source=header-home" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">Sign up</a>
</div>
</div>
</div>
</header>



</div>

<div id="start-of-content" class="accessibility-aid"></div>

<div id="js-flash-container">
</div>



<div role="main">

<div class="sn-jumbotron sn-jumbotron-no-overlay jumbotron-home jumbotron-dark">
<div class="container-responsive position-relative">
<div class="d-md-flex flex-items-center gut-lg">
<div class="col-md-7 ">
<h1 class="alt-h0 lh-condensed-ultra mb-3 text-white">Built for developers</h1>
<p class="f3-light mb-4">
GitHub is a development platform inspired by the way you work. Host code, manage projects, and build software alongside millions of other developers.
</p>
</div>
<div class="col-md-5">
<div class="d-none-sm-dn">
<!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/join" autocomplete="off" class="home-hero-signup js-signup-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="fHCFC2jcuSfUL6OaTiVtj9fboAj4SBBGSklpXO+n00lHniA/3OwcbPuIzIdC3nY7JidlnjS+BlX4sFFFKhQrug==" /></div>              <dl class="form">
<dd>
<label class="form-label text-shadow-light sr-only" for="user[login]">Pick a username</label>
<input type="text" name="user[login]" id="user[login]" class="form-control form-control-lg input-block" placeholder="Pick a username" data-autocheck-url="/signup_check/username" data-autocheck-authenticity-token="xdeYyOTorde0SYgd0j4bHepqbGvnt8L/nHE/drkus6mPvNbsLvo3A2NX0bjpKEmNqQhuNhrKU/k7o2hLFI7S9A==" autofocus>
</dd>
</dl>
<dl class="form">
<dd>
<label class="form-label text-shadow-light sr-only" for="user[email]">Enter your email address</label>
<input type="text" name="user[email]" id="user[email]" class="form-control form-control-lg input-block js-email-notice-trigger" placeholder="Your email address" data-autocheck-url="/signup_check/email" data-autocheck-authenticity-token="pgjlplxuiQ6OqVtiaiwJPigCXMxpFkUS0qtykfZkAZmaANueCJMNChNSzhQKwax0cTcaVieBS7T+CRJSyZrkUw==">
</dd>
</dl>
<dl class="form">
<dd>
<label class="form-label text-shadow-light sr-only" for="user[password]">Create a password</label>
<input type="password" name="user[password]" id="user[password]" class="form-control form-control-lg input-block" placeholder="Create a password" data-autocheck-url="/signup_check/password" data-autocheck-authenticity-token="J8dAvi6SqPam2evcD2ArfLZu3XVai04eH/F2ryjrxKCw4zqWNqDiiN/7AFciLTvGWjX315Kft9iNfREm7GFRKQ==">
</dd>
<p class="form-control-note text-gray">Use at least one letter, one numeral, and seven characters.</p>
</dl>
<input type="hidden" name="source" class="js-signup-source" value="form-home">
<button class="btn btn-primary btn-large f4 btn-block" type="submit">Sign up for GitHub</button>
<p class="form-control-note text-gray text-center">
By clicking "Sign up for GitHub", you agree to our
<a class="text-white" href="https://help.github.com/terms" target="_blank">terms of service</a> and
<a class="text-white" href="https://help.github.com/privacy" target="_blank">privacy policy</a>. <span class="js-email-notice">We’ll occasionally send you account related emails.</span>
</p>
</form>          </div>
<div class="d-sm-none">
<a href="/join?source=button-home" class="btn btn-primary btn-large border-0" rel="nofollow">Sign up for GitHub</a>
</div>
</div>
</div>
</div>
</div>

<div class="featurette">
<div class="container-responsive">
<svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewbox="0 0 47.78 47.47" class="d-block mx-auto mb-2" width="56"><defs><style>.cls-1{fill:currentColor}</style></defs><title>features-icon-code-review</title>
<path class="cls-1" d="M262.84 234.93H221a3 3 0 0 0-3 3V272a3 3 0 0 0 2.93 3l4 .1a5.65 5.65 0 0 0 4.57 2.34h7.24l4.69 4.69a1 1 0 0 0 1.71-.71V275h19.74a3 3 0 0 0 3-3v-34.11a3 3 0 0 0-3.04-2.96zm-41.87 2h41.87a1 1 0 0 1 1 1v5H220v-5a1 1 0 0 1 1-1zM241.11 279l-3.27-3.27a1 1 0 0 0-.71-.29h-7.65a3.66 3.66 0 0 1-3.66-3.66v-5.48a3.66 3.66 0 0 1 3.66-3.66h8a3.66 3.66 0 0 1 3.66 3.66zm-17.34-6H221a1 1 0 0 1-1-1v-27.14h43.8V272a1 1 0 0 1-1 1h-19.69v-6.7a5.66 5.66 0 0 0-5.66-5.66h-8a5.66 5.66 0 0 0-5.66 5.66v5.46A5.52 5.52 0 0 0 224 273z" transform="translate(-218.02 -234.93)"></path><path class="cls-1" d="M225.81 251.07h5.71a1 1 0 0 0 0-2h-5.71a1 1 0 0 0 0 2zm11.19 3.02h-11.2a1 1 0 0 0 0 2H237a1 1 0 0 0 0-2zm7.4 0h-3.31a1 1 0 0 0 0 2h3.31a1 1 0 1 0 0-2zm-8.92-3.02h16.18a1 1 0 0 0 0-2h-16.18a1 1 0 0 0 0 2zm20.23 0h2.51a1 1 0 0 0 0-2h-2.51a1 1 0 0 0 0 2zm-1.09 9.61h-3.79a1 1 0 0 0 0 2h3.79a1 1 0 0 0 0-2z" transform="translate(-218.02 -234.93)"></path><path class="cls-1" d="M255.38 255.74h-5.31a4.11 4.11 0 0 0-4.1 4.1v3.69c0 .05 0 0 0 0v6.31a1 1 0 0 0 1.71.71l3-3h4.68a4.11 4.11 0 0 0 4.1-4.1v-3.64a4.11 4.11 0 0 0-4.08-4.07zm2.1 7.74a2.1 2.1 0 0 1-2.1 2.1h-5.1a1 1 0 0 0-.71.29l-1.57 1.61v-7.64a2.1 2.1 0 0 1 2.1-2.1h5.31a2.1 2.1 0 0 1 2.1 2.1zm-22.1 3.3l-3 3.11-1-1.18a1 1 0 0 0-1.5 1.32l1.75 2a1 1 0 0 0 .72.34 1 1 0 0 0 .71-.3l3.8-3.88a1 1 0 0 0-1.43-1.4z" transform="translate(-218.02 -234.93)"></path></svg>
<h6 class="alt-h4 text-normal text-gray text-center">
GitHub for teams
</h6>
<h2 class="alt-h1 lh-condensed mt-3 mb-2 text-center">
A better way to work together
</h2>
<p class="f3 text-center col-md-8 mx-auto">
GitHub brings teams together to work through problems, move ideas forward, and learn from each other along the way.
</p>
<p class="text-center mb-5 col-md-8 mx-auto">
<a href="/features">See how teams work together on GitHub</a>
</p>
<div class="text-center">
<a href="/join?plan=business&amp;setup_organization=true&amp;source=business-page" class="btn btn-large btn-blue">Sign up your team</a>
</div>

<div class="d-md-flex flex-items-center flex-row-reverse my-5">
<div class="col-sm-8 col-md-6 mx-auto text-center p-5">
<img src="https://assets-cdn.github.com/images/modules/sitenextnext/home-illo-conversation.svg" alt="" width="360" class="d-block width-fit mx-auto">
</div>
<div class="col-sm-8 col-md-6 mx-auto text-center text-md-left pr-md-5">
<h3 class="alt-h3 mb-1">Write better code</h3>
<p class="">
Collaboration makes perfect. The conversations and code reviews that happen in Pull Requests help your team share the weight of your work and improve the software you build.
</p>
</div>
</div>

<div class="d-md-flex flex-items-center my-5">
<div class="col-sm-8 col-md-6 mx-auto text-center p-5">
<img src="https://assets-cdn.github.com/images/modules/sitenextnext/home-illo-chaos.svg" alt="" class="d-block width-fit mx-auto">
</div>
<div class="col-sm-8 col-md-6 mx-auto text-center text-md-left pl-md-5">
<h3 class="alt-h3 mb-1">Manage your chaos</h3>
<p class="">
Take a deep breath. On GitHub project management happens in Issues and Projects, right alongside your code. All you have to do is mention a teammate to get them involved.
</p>
</div>
</div>
</div>
</div>

<div class="featurette">
<div class="container-responsive">
<svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewbox="0 0 99.29 63.65" class="d-block mx-auto mb-2" width="92"><defs><style>.cls-1{fill:#231f20;}</style></defs><title>features-icon-administration</title>
<path class="cls-1" d="M217.28,342.72h-.9v-3.85a5.35,5.35,0,0,0-10.7,0v3.85h-.9a2.44,2.44,0,0,0-2.44,2.44v9.13a2.44,2.44,0,0,0,2.44,2.44h12.5a2.44,2.44,0,0,0,2.44-2.44v-9.13A2.44,2.44,0,0,0,217.28,342.72Zm-9.6-3.85a3.35,3.35,0,0,1,6.7,0v3.85h-6.7Zm10,15.42a.44.44,0,0,1-.44.44h-12.5a.44.44,0,0,1-.44-.44v-9.13a.44.44,0,0,1,.44-.44h12.5a.44.44,0,0,1,.44.44Z" transform="translate(-120.43 -312)"></path><path class="cls-1" d="M212.21,347.44a1.91,1.91,0,0,0-1.64-.36,1.9,1.9,0,0,0-.69,3.37v1.15a1.14,1.14,0,1,0,2.29,0v-1.15a1.9,1.9,0,0,0,0-3Z" transform="translate(-120.43 -312)"></path><path class="cls-1" d="M171.12,325.13a.52.52,0,0,0,.38.18h0a.54.54,0,0,0,.38-.18l3.72-3.7a.43.43,0,0,0,.06-.57c-.16-.19-.55-.58-.55-.58a.53.53,0,0,0-.37-.18h0a.52.52,0,0,0-.37.17l-2.86,2.84-1-1a.49.49,0,0,0-.73,0l-.54.52a.48.48,0,0,0,0,.64ZM169.47,323h0Z" transform="translate(-120.43 -312)"></path><path class="cls-1" d="M206.81,365.43H196.23V323.5a2.15,2.15,0,0,0-2.14-2.14H182.8a10.35,10.35,0,0,0-20.63.23l-.08,0H150.5a2.08,2.08,0,0,0-2.08,2.08v42.47a9.19,9.19,0,0,0,9.79,9.51l.2,0h40.17a9.23,9.23,0,0,0,9.21-9.21A1,1,0,0,0,206.81,365.43ZM172.5,314a8.36,8.36,0,1,1-8.36,8.36A8.37,8.37,0,0,1,172.5,314Zm-10.08,57.84a7.14,7.14,0,0,1-5.69,1.76,7.38,7.38,0,0,1-6.31-7.47V323.65a.08.08,0,0,1,.08-.08h11.59l.12,0a10.35,10.35,0,0,0,20.59-.19h11.28a.15.15,0,0,1,.14.14v41.93H165.85a1,1,0,0,0-1,1A7.22,7.22,0,0,1,162.42,371.84Zm36.17,1.81H163.37l.38-.32a9.23,9.23,0,0,0,3.05-5.9h38.94A7.23,7.23,0,0,1,198.59,373.65Z" transform="translate(-120.43 -312)"></path><path class="cls-1" d="M168.21,340h8.24a1,1,0,1,0,0-2h-8.24a1,1,0,0,0,0,2Z" transform="translate(-120.43 -312)"></path><path class="cls-1" d="M159.56,346.34h25.53a1,1,0,0,0,0-2H159.56a1,1,0,0,0,0,2Z" transform="translate(-120.43 -312)"></path><path class="cls-1" d="M159.56,352.72h25.53a1,1,0,0,0,0-2H159.56a1,1,0,0,0,0,2Z" transform="translate(-120.43 -312)"></path><path class="cls-1" d="M186.09,358.11a1,1,0,0,0-1-1H159.56a1,1,0,0,0,0,2h25.53A1,1,0,0,0,186.09,358.11Z" transform="translate(-120.43 -312)"></path><path class="cls-1" d="M143.12,344.78l-2.52-.84-.34-.84,1.15-2.41a1,1,0,0,0-.19-1.14l-1.71-1.72a1,1,0,0,0-1.15-.19L136,338.81l-.84-.35-.89-2.52a1,1,0,0,0-.94-.67h-2.44a1,1,0,0,0-1,.69l-.82,2.51-.85.34-2.41-1.15a1,1,0,0,0-1.14.19L123,339.56a1,1,0,0,0-.19,1.15l1.17,2.36-.35.84-2.52.89a1,1,0,0,0-.67.94v2.43a1,1,0,0,0,.68,1l2.52.84.34.84-1.15,2.41a1,1,0,0,0,.19,1.14l1.71,1.72a1,1,0,0,0,1.15.19l2.36-1.17.84.35L130,358a1,1,0,0,0,.94.67h2.44a1,1,0,0,0,1-.69l.82-2.51.85-.35,2.41,1.16a1,1,0,0,0,1.14-.19l1.72-1.71a1,1,0,0,0,.19-1.16l-1.19-2.35.36-.84,2.53-.89a1,1,0,0,0,.67-.94v-2.43A1,1,0,0,0,143.12,344.78Zm-1.32,2.67-2.27.8a1,1,0,0,0-.58.54l-.72,1.67a1,1,0,0,0,0,.85l1.07,2.12-.71.7-2.17-1a1,1,0,0,0-.81,0l-1.7.69a1,1,0,0,0-.58.62l-.74,2.26h-1l-.8-2.27a1,1,0,0,0-.56-.59l-1.67-.7a1,1,0,0,0-.83,0l-2.12,1.05-.71-.71,1-2.17a1,1,0,0,0,0-.81l-.69-1.67a1,1,0,0,0-.61-.57l-2.27-.76v-1l2.27-.8a1,1,0,0,0,.59-.56l.7-1.67a1,1,0,0,0,0-.83l-1.05-2.13.71-.71,2.17,1a1,1,0,0,0,.81,0l1.7-.68a1,1,0,0,0,.58-.62l.74-2.26h1l.8,2.27a1,1,0,0,0,.56.59l1.67.7a1,1,0,0,0,.83,0l2.13-1.05.71.71-1,2.17a1,1,0,0,0,0,.81l.69,1.67a1,1,0,0,0,.61.57l2.27.76Z" transform="translate(-120.43 -312)"></path><path class="cls-1" d="M132.19,342.57a4.38,4.38,0,1,0,4.38,4.38A4.39,4.39,0,0,0,132.19,342.57Zm0,6.76a2.38,2.38,0,1,1,2.38-2.38A2.38,2.38,0,0,1,132.19,349.34Z" transform="translate(-120.43 -312)"></path></svg>
<h6 class="alt-h4 text-normal text-gray text-center">
Security and administration
</h6>
<h2 class="alt-h1 mt-3 mb-2 text-center">
Boxes? Check.
</h2>
<p class="f3 text-center mb-3 col-md-8 mx-auto">
We worried about your administrative and security needs so you don’t have to. From flexible hosting to authentication options, GitHub can help you meet your team’s requirements.
</p>
<p class="text-center mb-5">
<a href="/business">See how Businesses work on GitHub</a>
</p>

<div class="d-md-flex flex-items-center flex-row-reverse my-5">
<div class="col-sm-8 col-md-6 mx-auto px-5 pr-md-0 text-center">
<img src="https://assets-cdn.github.com/images/modules/sitenextnext/home-illo-business.svg" alt="" class="d-block width-fit mx-auto mb-4">
</div>
<div class="col-sm-8 col-md-6 mx-auto text-center text-md-left">
<h3 class="alt-h3 mb-1">Code security</h3>
<p class="mb-3 mb-md-5">
Prevent problems before they happen. Protected branches, signed commits, and required status checks protect your work and help you maintain a high standard for your code.
</p>

<h3 class="alt-h3 mb-1">Access controlled</h3>
<p class="mb-3 mb-md-5">
Encourage teams to work together while limiting access to those who need it with granular permissions and authentication through SAML/SSO and LDAP.
</p>

<h3 class="alt-h3 mb-1">Hosted where you need it</h3>
<p class="mb-3 mb-md-4">
Securely and reliably host your work on GitHub.com. Or, deploy GitHub Enterprise on your own servers or in a private cloud using Amazon Web Services, Azure or Google Cloud Platform.
</p>
</div>
</div>

<div class="text-center text-gray">
<a href="/join?plan=business&amp;setup_organization=true&amp;source=home-security" class="btn btn-large btn-outline">Sign up your team</a>
<p class="f5 mt-3 mb-0">
Want to host GitHub on your servers?<br> <a href="https://enterprise.github.com/sn-trial">Try GitHub Enterprise for free</a>
</p>
</div>
</div>
</div>

<div class="featurette position-relative">
<div class="container-responsive text-center py-md-6">
<div class="col-md-8 py-md-6 mx-auto">
<svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewbox="0 0 47.76 43.85" class="d-block mx-auto mb-2" width="56"><defs><style>.cls-1{fill:currentColor}</style></defs><title>features-icon-integrations</title>
<path class="cls-1" d="M246.2 214.8a23.91 23.91 0 0 0-23.88 23.88v15.44c0 4.31 19.91 4.53 23.9 4.53s23.86-.22 23.86-4.53v-15.44a23.91 23.91 0 0 0-23.88-23.88zM224.32 254v-15.32a21.88 21.88 0 1 1 43.76 0V254c-1 1.11-9.23 2.66-21.86 2.66s-20.87-1.57-21.9-2.66z" transform="translate(-222.32 -214.8)"></path><path class="cls-1" d="M251.2 247.13c-.43-1.16-1.15-1.41-1.69-1.41h-6.81a1.76 1.76 0 0 0-1.73 1.53c-.11.46-.74 3-.74 3a1 1 0 0 0 0 .25 1.75 1.75 0 0 0 1.75 1.75h8.31a1.75 1.75 0 0 0 1.75-1.75 1 1 0 0 0 0-.23c-.25-.84-.71-2.78-.84-3.14zm-8.91 3.1c.19-.75.54-2.12.63-2.5h6.37v.09c.07.19.34 1.3.6 2.41zm14.91-21.01h-22a5 5 0 0 0-5 5V237a5 5 0 0 0 5 5h22a5 5 0 0 0 5-5v-2.74a5 5 0 0 0-5-5.04zm-22 2h22a3 3 0 0 1 3 3v.37H253l-1-1a1 1 0 0 0-1.41 0l-1.3 1.3-.6.6-.6-.6-1.3-1.3a1 1 0 0 0-1.41 0l-1.9 1.91-1.9-1.91a1 1 0 0 0-1.41 0l-1 1h-7v-.37a3 3 0 0 1 3.04-3zm22 8.74h-22a3 3 0 0 1-3-3v-.37h7.39a1 1 0 0 0 .71-.29l.6-.6 1.9 1.9a1 1 0 0 0 1.41 0l1.89-1.9 1.91 1.9a1 1 0 0 0 .71.29 1 1 0 0 0 .71-.29l1.3-1.3.6-.6.6.6a1 1 0 0 0 .71.29h7.58v.41a3 3 0 0 1-3.02 3z" transform="translate(-222.32 -214.8)"></path></svg>
<h6 class="alt-h4 text-normal text-gray">
Integrations
</h6>
<h2 class="alt-h1 lh-condensed mt-3 mb-2">
Perfect the way you&nbsp;work
</h2>
<p class="f3 mb-3 px-md-3">
Customize your process with hundreds of integrations and an intuitive API. Integrate the tools you already use or discover new favorites to create a happier, more efficient way of working.
</p>
<p class="mb-4">
<a href="/features#integrations" class="btn btn-large btn-outline">Learn more about integrations</a>
</p>

<div class="integrations-collage integrations-collage-split d-flex flex-justify-center flex-wrap d-md-block">
<div class="integrations-collage-item m-2"><img src="https://assets-cdn.github.com/images/modules/sitenextnext/integrators/slackhq.png" alt="" class="d-block integrations-collage-img width-fit mx-auto"></div>
<div class="integrations-collage-item m-2"><img src="https://assets-cdn.github.com/images/modules/sitenextnext/integrators/zenhubio.png" alt="" class="d-block integrations-collage-img width-fit mx-auto"></div>
<div class="integrations-collage-item m-2"><img src="https://assets-cdn.github.com/images/modules/sitenextnext/integrators/travis-ci.png" alt="" class="d-block integrations-collage-img width-fit mx-auto"></div>
<div class="integrations-collage-item m-2"><img src="https://assets-cdn.github.com/images/modules/sitenextnext/integrators/atom.png" alt="" class="d-block integrations-collage-img width-fit mx-auto"></div>
<div class="integrations-collage-item m-2"><img src="https://assets-cdn.github.com/images/modules/sitenextnext/integrators/circleci.png" alt="" class="d-block integrations-collage-img width-fit mx-auto"></div>
<div class="integrations-collage-item m-2"><img src="https://assets-cdn.github.com/images/modules/sitenextnext/integrators/codeship.png" alt="" class="d-block integrations-collage-img width-fit mx-auto"></div>
<div class="integrations-collage-item m-2"><img src="https://assets-cdn.github.com/images/modules/sitenextnext/integrators/codeclimate.png" alt="" class="d-block integrations-collage-img width-fit mx-auto"></div>
<div class="integrations-collage-item m-2"><img src="https://assets-cdn.github.com/images/modules/sitenextnext/integrators/gitterhq.png" alt="" class="d-block integrations-collage-img width-fit mx-auto"></div>
<div class="integrations-collage-item m-2"><img src="https://assets-cdn.github.com/images/modules/sitenextnext/integrators/waffleio.png" alt="" class="d-block integrations-collage-img width-fit mx-auto"></div>
<div class="integrations-collage-item m-2"><img src="https://assets-cdn.github.com/images/modules/sitenextnext/integrators/heroku.png" alt="" class="d-block integrations-collage-img width-fit mx-auto"></div>
</div>

<svg aria-hidden="true" class="octicon octicon-mark-github mt-3 mt-md-6" height="64" version="1.1" viewBox="0 0 16 16" width="64"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
<p class="my-2 alt-text-small col-sm-8 col-md-6 mx-auto">
Sometimes, there’s more than one tool for the job. Why not try something new?
</p>
<p>
<a href="/integrations">Explore integrations</a>
</p>
</div>
</div>

</div>

<div class="featurette overflow-hidden">
<div class="container-responsive position-relative">
<svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewbox="0 0 84.54 70.52" class="d-block mx-auto mb-2" width="72"><defs><style>.cls-1{fill:#231f20;}</style></defs><title>features-icon-community</title>
<path class="cls-1" d="M238.94,282.68a1,1,0,0,1-1-1.3,5.67,5.67,0,0,0,.26-1.71A5.78,5.78,0,0,0,233,274a1,1,0,0,1-.91-1v-5a7.46,7.46,0,0,0-4.66-6.92,1,1,0,1,1,.76-1.85,9.46,9.46,0,0,1,5.9,8.77v4.16a7.81,7.81,0,0,1,6.14,7.57,7.69,7.69,0,0,1-.36,2.31A1,1,0,0,1,238.94,282.68Z" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M234,241.8" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M226.13,269.19a8.81,8.81,0,0,1-8.13-4.67h-6.6a3.18,3.18,0,0,1-3.18-3.18v-8a3.18,3.18,0,0,1,3.18-3.18h14.08a3.18,3.18,0,0,1,3.18,3.18v8a3.18,3.18,0,0,1-3.18,3.18h-.94c.5,2.46,1.93,2.56,2.44,2.6a1.05,1.05,0,0,1,1,1,1,1,0,0,1-.95,1C226.7,269.17,226.42,269.19,226.13,269.19Zm-14.73-17a1.18,1.18,0,0,0-1.18,1.18v8a1.18,1.18,0,0,0,1.18,1.18h7.24a1,1,0,0,1,.92.61,6.21,6.21,0,0,0,3.6,3.53,8.09,8.09,0,0,1-.76-3.07,1,1,0,0,1,1-1.07h2.08a1.18,1.18,0,0,0,1.18-1.18v-8a1.18,1.18,0,0,0-1.18-1.18Z" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M275,240.19q-.44,0-.85,0a1,1,0,0,1-.94-1,1.05,1.05,0,0,1,1-1c.5,0,1.91-.13,2.4-2.54h-.92a3.15,3.15,0,0,1-3.15-3.15V224.5a3.15,3.15,0,0,1,3.15-3.15h13.91a3.15,3.15,0,0,1,3.15,3.15v7.92a3.15,3.15,0,0,1-3.15,3.15h-6.51A8.72,8.72,0,0,1,275,240.19Zm.65-16.84a1.15,1.15,0,0,0-1.15,1.15v7.92a1.15,1.15,0,0,0,1.15,1.15h2.06a1,1,0,0,1,1,1.07,8,8,0,0,1-.74,3,6.12,6.12,0,0,0,3.52-3.47,1,1,0,0,1,.92-.61h7.15a1.15,1.15,0,0,0,1.15-1.15V224.5a1.15,1.15,0,0,0-1.15-1.15Z" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M273.35,225a1,1,0,0,1-.67-.26,33.25,33.25,0,0,0-34-6.43,1,1,0,0,1-.71-1.87,35.25,35.25,0,0,1,36,6.81,1,1,0,0,1-.67,1.74Z" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M238.94,282.68a1,1,0,0,1-.33-.06,35.31,35.31,0,0,1-18.78-15.71,1,1,0,1,1,1.74-1,33.31,33.31,0,0,0,17.71,14.82,1,1,0,0,1-.33,1.94Z" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M216.19,251.66a1,1,0,0,1-1-1q0-.65,0-1.3a34.91,34.91,0,0,1,3.35-15,1,1,0,0,1,1.81.85,32.92,32.92,0,0,0-3.16,14.14q0,.61,0,1.22a1,1,0,0,1-1,1Z" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M268.84,279.27a1,1,0,0,1-.54-1.84,33.06,33.06,0,0,0,14.51-20.57,1,1,0,1,1,1.95.45,35.05,35.05,0,0,1-15.38,21.81A1,1,0,0,1,268.84,279.27Z" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M284.63,249a1,1,0,0,1-1-1,33.07,33.07,0,0,0-2.55-11.5,1,1,0,1,1,1.84-.77,35.06,35.06,0,0,1,2.7,12.2,1,1,0,0,1-1,1Z" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M283.79,258.08l-.22,0a1,1,0,0,1-.75-1.2,33.45,33.45,0,0,0,.85-7.45c0-.46,0-.91,0-1.36a1,1,0,1,1,2-.08c0,.48,0,1,0,1.44a35.44,35.44,0,0,1-.9,7.9A1,1,0,0,1,283.79,258.08Z" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M233.55,220.6a1,1,0,0,1-.49-1.87,35.2,35.2,0,0,1,4.93-2.31,1,1,0,0,1,.71,1.87,33.18,33.18,0,0,0-4.65,2.18A1,1,0,0,1,233.55,220.6Z" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M250.41,284.68a35.17,35.17,0,0,1-11.83-2,1,1,0,0,1,.67-1.88,33.33,33.33,0,0,0,29.06-3.31,1,1,0,0,1,1.08,1.68A35.13,35.13,0,0,1,250.41,284.68Z" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M224.49,240.92h0a1,1,0,0,1-.9-.65l-1.9-5h-3.91a3.15,3.15,0,0,1-3.15-3.15V221a3.15,3.15,0,0,1,3.15-3.15h13.91A3.15,3.15,0,0,1,234.8,221v11.1a3.15,3.15,0,0,1-3.15,3.15h-4l-2.29,5.09A1,1,0,0,1,224.49,240.92Zm-6.75-21.07a1.15,1.15,0,0,0-1.15,1.15v11.1a1.15,1.15,0,0,0,1.15,1.15h4.61a1,1,0,0,1,.94.65l1.29,3.41,1.56-3.47a1,1,0,0,1,.91-.59h4.61a1.15,1.15,0,0,0,1.15-1.15V221a1.15,1.15,0,0,0-1.15-1.15Z" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M224.71,231.49a1.94,1.94,0,0,1-1.19-.42c-1.28-1-3.43-3-3.43-5.28a2.81,2.81,0,0,1,4.61-2.16,2.81,2.81,0,0,1,4.61,2.16c0,2.3-2.18,4.32-3.48,5.32A1.81,1.81,0,0,1,224.71,231.49ZM222.9,225a.82.82,0,0,0-.81.81c0,1,1,2.38,2.61,3.67,1.64-1.28,2.61-2.65,2.61-3.67a.81.81,0,0,0-1.57-.29,1.11,1.11,0,0,1-1,.74h0a1.11,1.11,0,0,1-1-.74A.82.82,0,0,0,222.9,225Z" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M227.26,253.07a1,1,0,0,1-.4-1.92,10.17,10.17,0,0,0,3.89-15.73,1,1,0,1,1,1.56-1.26A12.17,12.17,0,0,1,227.66,253,1,1,0,0,1,227.26,253.07Z" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M234,227h-.15a1,1,0,0,1-1-1l-.15-6.71a1,1,0,0,1,.62-.95l4.62-1.9a1,1,0,0,1,1.18.33,6.33,6.33,0,0,1,1.28,3.8A6.41,6.41,0,0,1,234,227Zm.71-7,.11,5a4.41,4.41,0,0,0,3.58-4.32,4.27,4.27,0,0,0-.48-2Z" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M281.73,227.37h-3.64a1,1,0,0,1,0-2h3.64a1,1,0,0,1,0,2Z" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M285.28,231.37h-7.19a1,1,0,0,1,0-2h7.19a1,1,0,0,1,0,2Z" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M217.14,256.43H213.5a1,1,0,0,1,0-2h3.64a1,1,0,0,1,0,2Z" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M220.69,260.43H213.5a1,1,0,0,1,0-2h7.19a1,1,0,1,1,0,2Z" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M284.63,249h-9.72a9.88,9.88,0,0,1-5.51-1.67h-7a5.07,5.07,0,1,1,0-10.15h2.66a10.06,10.06,0,0,1,7.92-8,1,1,0,0,1,.38,2,8,8,0,0,0-6.44,7.11,1,1,0,0,1-1,.91h-3.53a3.07,3.07,0,1,0,0,6.15h7.29a1,1,0,0,1,.58.19,7.91,7.91,0,0,0,4.61,1.49h9.72a1,1,0,0,1,0,2Z" transform="translate(-208.22 -214.16)"></path><path class="cls-1" d="M268.84,279.27a1,1,0,0,1-.74-.32,9.35,9.35,0,0,1-2.49-6.33v-1.36h-.8a9.63,9.63,0,0,1,0-19.26h11.65a9.59,9.59,0,0,1,8.17,4.56,1,1,0,1,1-1.7,1.06,7.6,7.6,0,0,0-6.47-3.62H264.82a7.63,7.63,0,0,0,0,15.26h1.8a1,1,0,0,1,1,1v2.36a7.36,7.36,0,0,0,2,5,1,1,0,0,1-.74,1.68Z" transform="translate(-208.22 -214.16)"></path></svg>
<h6 class="alt-h4 text-normal text-gray text-center">
Community
</h6>
<h2 class="alt-h1 mt-3 mb-2 lh-condensed text-center">
Welcome home, developers
</h2>
<p class="f3 text-center col-md-8 mx-auto pb-md-6">
GitHub is home to the world’s largest community of developers and their projects. Whether you’re making your first commit or sending a Rover to Mars, there’s room for you here, too.
</p>

<div class="d-flex flex-wrap gut-md mt-6 py-6">
<a href="/personal" class="p-4 flex-md-item-equal mx-auto mx-md-3 mb-4 no-underline bg-white border rounded-2 home-community-developers">
<p class="mt-1 mb-1 text-gray-dark">
<span class="alt-h2 text-bold d-block lh-condensed-ultra">19M</span>
<span class="f3">Developers worldwide</span>
</p>
<p class="f5 text-gray-dark">
Developers use GitHub for personal projects, from experimenting with new programming languages to hosting their life’s work.
</p>
<p class="text-blue f5 text-bold mb-0">See how developers use GitHub</p>
</a>

<a href="/open-source" class="p-4 flex-md-item-equal mx-auto mx-md-3 mb-4 no-underline bg-white border rounded-2 home-community-repositories">
<p class="mt-1 mb-1 text-gray-dark">
<span class="alt-h2 text-bold d-block lh-condensed-ultra">52M</span>
<span class="f3">Repositories worldwide</span>
</p>
<p class="f5 text-gray-dark">
GitHub’s users create and maintain influential technologies alongside the world's largest open source community.
</p>
<p class="text-orange-light f5 text-bold mb-0">Learn about open source</p>
</a>

<a href="/business" class="p-4 flex-md-item-equal mx-auto mx-md-3 mb-4 no-underline bg-white border rounded-2 home-community-teams">
<p class="mt-1 mb-1 text-gray-dark">
<span class="alt-h2 text-bold d-block lh-condensed-ultra">100K</span>
<span class="f3">Teams worldwide</span>
</p>
<p class="f5 text-gray-dark">
Businesses of all sizes use GitHub to support their development process and to securely build software.
</p>
<p class="text-purple f5 text-bold">See how businesses use GitHub</p>
</a>

<div class="mt-5 col-10 col-md-12 flex-shrink-0 mx-auto home-community-svg">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1055.96 472.75">
<defs>
<style>
.cls-1{isolation:isolate;}
.cls-2{opacity:0.1;}
.cls-3,.cls-4,.community-svg-orange,.community-svg-purple,.community-svg-blue{fill:none;stroke-linecap:round;stroke-miterlimit:10;stroke-width:4.45px;}
.cls-3{stroke:#929497;}
.cls-4{stroke:#6e7074;}
.community-svg-orange{stroke:#f66a0a;}
.community-svg-orange,.community-svg-purple,.community-svg-blue{mix-blend-mode:multiply;}
.community-svg-purple{stroke:#6f42c1;}
.community-svg-blue{stroke:#006eeb;}
</style>
</defs>

<title>home-illo-community</title>
<g class="cls-1">
<g id="Layer_1" data-name="Layer 1">
<g class="cls-2">
<line class="cls-3" x1="382.18" y1="2.22" x2="417.53" y2="2.22"></line>
<line class="cls-3" x1="249.64" y1="11.06" x2="284.99" y2="11.06"></line>
<line class="cls-3" x1="399.86" y1="11.06" x2="435.2" y2="11.06"></line>
<line class="cls-3" x1="293.82" y1="11.06" x2="311.49" y2="11.06"></line><line class="cls-3" x1="346.84" y1="11.06" x2="391.02" y2="11.06"></line><line class="cls-3" x1="223.13" y1="19.89" x2="461.71" y2="19.89"></line><line class="cls-3" x1="620.76" y1="19.89" x2="629.6" y2="19.89"></line><line class="cls-3" x1="664.94" y1="19.89" x2="673.78" y2="19.89"></line><line class="cls-3" x1="779.81" y1="19.89" x2="779.81" y2="19.89"></line><line class="cls-3" x1="302.66" y1="28.73" x2="444.04" y2="28.73"></line><line class="cls-3" x1="214.29" y1="28.73" x2="284.99" y2="28.73"></line><line class="cls-3" x1="223.13" y1="37.57" x2="267.31" y2="37.57"></line><line class="cls-3" x1="187.79" y1="37.57" x2="205.46" y2="37.57"></line><line class="cls-3" x1="240.8" y1="46.4" x2="258.48" y2="46.4"></line><line class="cls-3" x1="125.93" y1="81.75" x2="187.79" y2="81.75"></line><line class="cls-3" x1="152.44" y1="90.56" x2="223.13" y2="90.56"></line><line class="cls-3" x1="178.95" y1="99.4" x2="249.64" y2="99.4"></line><line class="cls-3" x1="205.46" y1="81.75" x2="214.29" y2="81.75"></line><line class="cls-3" x1="267.31" y1="125.93" x2="276.15" y2="125.93"></line><line class="cls-3" x1="293.82" y1="125.93" x2="302.66" y2="125.93"></line><line class="cls-3" x1="28.73" y1="81.75" x2="37.57" y2="81.75"></line><line class="cls-3" x1="19.9" y1="90.59" x2="81.75" y2="90.59"></line><line class="cls-3" x1="2.22" y1="99.42" x2="152.44" y2="99.42"></line><line class="cls-3" x1="2.22" y1="108.26" x2="249.64" y2="108.26"></line><line class="cls-3" x1="2.22" y1="117.09" x2="249.64" y2="117.09"></line><line class="cls-3" x1="11.06" y1="125.93" x2="223.13" y2="125.93"></line><line class="cls-3" x1="11.06" y1="134.73" x2="214.29" y2="134.73"></line><line class="cls-3" x1="231.97" y1="81.75" x2="284.99" y2="81.75"></line><line class="cls-3" x1="240.79" y1="90.57" x2="293.81" y2="90.57"></line><line class="cls-3" x1="284.99" y1="99.42" x2="302.66" y2="99.42"></line><line class="cls-3" x1="284.99" y1="108.26" x2="311.49" y2="108.26"></line><line class="cls-3" x1="267.31" y1="117.09" x2="302.66" y2="117.09"></line><line class="cls-3" x1="231.97" y1="64.08" x2="258.48" y2="64.08"></line><line class="cls-3" x1="125.93" y1="72.91" x2="152.44" y2="72.91"></line><line class="cls-3" x1="108.26" y1="90.59" x2="134.77" y2="90.59"></line><line class="cls-3" x1="178.95" y1="72.91" x2="258.48" y2="72.91"></line><line class="cls-3" x1="223.13" y1="55.23" x2="231.97" y2="55.23"></line><line class="cls-3" x1="143.61" y1="46.4" x2="170.11" y2="46.4"></line><line class="cls-3" x1="134.77" y1="55.23" x2="205.46" y2="55.23"></line><line class="cls-3" x1="196.62" y1="28.73" x2="196.62" y2="28.73"></line><line class="cls-3" x1="170.11" y1="37.57" x2="170.11" y2="37.57"></line><line class="cls-3" x1="214.29" y1="46.4" x2="214.29" y2="46.4"></line><line class="cls-3" x1="161.28" y1="64.05" x2="161.28" y2="64.05"></line><line class="cls-3" x1="267.3" y1="99.4" x2="267.3" y2="99.4"></line><line class="cls-3" x1="249.64" y1="125.93" x2="249.64" y2="125.93"></line><line class="cls-3" x1="187.79" y1="46.39" x2="187.79" y2="46.39"></line><line class="cls-3" x1="134.77" y1="64.08" x2="134.77" y2="64.08"></line><line class="cls-3" x1="284.99" y1="37.56" x2="435.2" y2="37.56"></line><line class="cls-3" x1="284.99" y1="46.39" x2="435.2" y2="46.39"></line><line class="cls-3" x1="550.07" y1="28.73" x2="576.58" y2="28.73"></line><line class="cls-3" x1="656.11" y1="28.73" x2="691.45" y2="28.73"></line><line class="cls-3" x1="770.98" y1="28.73" x2="788.65" y2="28.73"></line><line class="cls-3" x1="629.6" y1="28.73" x2="638.44" y2="28.73"></line><line class="cls-3" x1="532.4" y1="37.56" x2="558.91" y2="37.56"></line><line class="cls-3" x1="779.81" y1="37.56" x2="806.32" y2="37.56"></line><line class="cls-3" x1="541.24" y1="46.39" x2="550.07" y2="46.39"></line><line class="cls-3" x1="797.49" y1="46.39" x2="806.33" y2="46.39"></line><line class="cls-3" x1="567.75" y1="46.39" x2="567.75" y2="46.39"></line><line class="cls-3" x1="293.82" y1="55.23" x2="435.2" y2="55.23"></line><line class="cls-3" x1="329.17" y1="64.06" x2="435.2" y2="64.06"></line><line class="cls-3" x1="338" y1="72.9" x2="426.37" y2="72.9"></line><line class="cls-3" x1="338" y1="81.73" x2="426.37" y2="81.73"></line><line class="cls-3" x1="338" y1="90.56" x2="426.36" y2="90.56"></line><line class="cls-3" x1="770.98" y1="55.23" x2="832.83" y2="55.23"></line><line class="cls-3" x1="673.78" y1="55.23" x2="700.29" y2="55.23"></line><line class="cls-3" x1="753.31" y1="64.06" x2="832.83" y2="64.06"></line><line class="cls-3" x1="664.94" y1="64.06" x2="673.78" y2="64.06"></line><line class="cls-3" x1="700.29" y1="72.9" x2="877.01" y2="72.9"></line><line class="cls-3" x1="656.11" y1="72.9" x2="664.94" y2="72.9"></line><line class="cls-3" x1="903.52" y1="55.23" x2="921.19" y2="55.23"></line><line class="cls-3" x1="903.52" y1="64.06" x2="938.87" y2="64.06"></line><line class="cls-3" x1="912.36" y1="72.9" x2="921.19" y2="72.9"></line><line class="cls-3" x1="691.45" y1="81.73" x2="947.7" y2="81.73"></line><line class="cls-3" x1="576.58" y1="81.73" x2="585.42" y2="81.73"></line><line class="cls-3" x1="647.27" y1="81.73" x2="664.94" y2="81.73"></line><line class="cls-3" x1="1027.23" y1="81.73" x2="1036.07" y2="81.73"></line><line class="cls-3" x1="1044.9" y1="117.09" x2="1044.9" y2="117.09"></line><line class="cls-3" x1="673.78" y1="90.56" x2="1018.39" y2="90.56"></line><line class="cls-3" x1="541.24" y1="99.4" x2="1036.07" y2="99.4"></line><line class="cls-3" x1="532.4" y1="108.23" x2="1053.74" y2="108.23"></line><line class="cls-3" x1="523.56" y1="117.07" x2="1027.23" y2="117.07"></line><line class="cls-3" x1="558.91" y1="125.9" x2="1027.23" y2="125.9"></line><line class="cls-3" x1="514.73" y1="125.9" x2="541.24" y2="125.9"></line><line class="cls-3" x1="514.73" y1="134.73" x2="550.07" y2="134.73"></line><line class="cls-3" x1="488.22" y1="134.73" x2="497.06" y2="134.73"></line><line class="cls-3" x1="514.73" y1="143.57" x2="541.24" y2="143.57"></line><line class="cls-3" x1="479.38" y1="143.57" x2="488.22" y2="143.57"></line><line class="cls-3" x1="541.24" y1="152.4" x2="541.24" y2="152.4"></line><line class="cls-3" x1="523.56" y1="152.4" x2="523.56" y2="152.4"></line><line class="cls-3" x1="470.55" y1="152.44" x2="488.22" y2="152.44"></line><line class="cls-3" x1="974.22" y1="134.73" x2="1000.72" y2="134.73"></line><line class="cls-3" x1="567.74" y1="134.73" x2="956.53" y2="134.73"></line><line class="cls-3" x1="550.07" y1="90.56" x2="585.42" y2="90.56"></line><line class="cls-3" x1="638.43" y1="90.56" x2="638.43" y2="90.56"></line><line class="cls-3" x1="338" y1="99.4" x2="408.69" y2="99.4"></line><line class="cls-3" x1="338" y1="108.23" x2="391.02" y2="108.23"></line><line class="cls-3" x1="426.37" y1="108.23" x2="444.04" y2="108.23"></line><line class="cls-3" x1="347.06" y1="117.07" x2="373.35" y2="117.07"></line><line class="cls-3" x1="426.37" y1="117.07" x2="435.2" y2="117.07"></line><line class="cls-3" x1="346.84" y1="125.9" x2="373.35" y2="125.9"></line><line class="cls-3" x1="470.55" y1="125.9" x2="470.55" y2="125.9"></line><line class="cls-3" x1="355.68" y1="134.73" x2="364.51" y2="134.73"></line><line class="cls-3" x1="267.31" y1="134.73" x2="284.98" y2="134.73"></line><line class="cls-3" x1="90.59" y1="143.6" x2="223.13" y2="143.6"></line><line class="cls-3" x1="19.9" y1="143.6" x2="46.41" y2="143.6"></line><line class="cls-3" x1="267.31" y1="143.6" x2="302.66" y2="143.6"></line><line class="cls-3" x1="99.42" y1="152.47" x2="231.97" y2="152.47"></line><line class="cls-3" x1="19.9" y1="152.47" x2="37.57" y2="152.47"></line><line class="cls-3" x1="276.62" y1="152.47" x2="311.49" y2="152.47"></line><line class="cls-3" x1="99.42" y1="161.34" x2="249.64" y2="161.34"></line><line class="cls-3" x1="267.31" y1="161.34" x2="320.33" y2="161.34"></line><line class="cls-3" x1="2.22" y1="161.34" x2="19.9" y2="161.34"></line><line class="cls-3" x1="2.22" y1="170.11" x2="2.22" y2="170.11"></line><line class="cls-3" x1="117.1" y1="170.21" x2="249.64" y2="170.21"></line><line class="cls-3" x1="117.1" y1="178.95" x2="294.05" y2="178.95"></line><line class="cls-3" x1="267.31" y1="170.21" x2="329.16" y2="170.21"></line><line class="cls-3" x1="329.16" y1="178.95" x2="329.16" y2="178.95"></line><line class="cls-3" x1="134.77" y1="187.69" x2="302.66" y2="187.69"></line><line class="cls-3" x1="134.77" y1="196.62" x2="311.49" y2="196.62"></line><line class="cls-3" x1="134.77" y1="205.45" x2="284.98" y2="205.45"></line><line class="cls-3" x1="134.77" y1="214.28" x2="276.15" y2="214.28"></line><line class="cls-3" x1="134.77" y1="223.12" x2="267.31" y2="223.12"></line><line class="cls-3" x1="143.61" y1="231.95" x2="267.31" y2="231.95"></line><line class="cls-3" x1="152.44" y1="240.78" x2="258.48" y2="240.78"></line><line class="cls-3" x1="161.28" y1="249.61" x2="258.48" y2="249.61"></line><line class="cls-3" x1="161.28" y1="258.44" x2="205.57" y2="258.44"></line><line class="cls-3" x1="258.48" y1="258.44" x2="258.48" y2="258.44"></line><line class="cls-3" x1="170.11" y1="267.28" x2="205.46" y2="267.28"></line><line class="cls-3" x1="187.79" y1="276.11" x2="205.57" y2="276.11"></line><line class="cls-3" x1="231.91" y1="276.11" x2="240.81" y2="276.11"></line><line class="cls-3" x1="258.48" y1="276.11" x2="284.98" y2="276.11"></line><line class="cls-3" x1="187.79" y1="284.98" x2="231.97" y2="284.98"></line><line class="cls-3" x1="205.53" y1="293.82" x2="249.64" y2="293.82"></line><line class="cls-3" x1="231.82" y1="302.66" x2="249.61" y2="302.66"></line><line class="cls-3" x1="284.98" y1="302.66" x2="284.98" y2="302.66"></line><line class="cls-3" x1="240.81" y1="311.49" x2="311.49" y2="311.49"></line><line class="cls-3" x1="258.48" y1="320.33" x2="320.33" y2="320.33"></line><line class="cls-3" x1="267.31" y1="329.08" x2="346.84" y2="329.08"></line><line class="cls-3" x1="258.48" y1="337.92" x2="346.84" y2="337.92"></line><line class="cls-3" x1="258.48" y1="346.76" x2="364.51" y2="346.76"></line><line class="cls-3" x1="258.48" y1="355.6" x2="391.02" y2="355.6"></line><line class="cls-3" x1="267.31" y1="364.44" x2="391.02" y2="364.44"></line><line class="cls-3" x1="267.31" y1="373.28" x2="381.95" y2="373.28"></line><line class="cls-3" x1="276.15" y1="382.12" x2="381.95" y2="382.12"></line><line class="cls-3" x1="284.98" y1="390.96" x2="381.95" y2="390.96"></line><line class="cls-3" x1="293.82" y1="399.8" x2="373.35" y2="399.8"></line><line class="cls-3" x1="293.82" y1="408.64" x2="373.35" y2="408.64"></line><line class="cls-3" x1="293.82" y1="417.48" x2="355.68" y2="417.48"></line><line class="cls-3" x1="284.98" y1="426.32" x2="346.84" y2="426.32"></line><line class="cls-3" x1="284.98" y1="435.16" x2="346.84" y2="435.16"></line><line class="cls-3" x1="284.98" y1="444" x2="338" y2="444"></line><line class="cls-3" x1="284.98" y1="452.84" x2="329.16" y2="452.84"></line><line class="cls-3" x1="284.98" y1="461.68" x2="320.33" y2="461.68"></line><line class="cls-3" x1="276.15" y1="470.52" x2="311.49" y2="470.52"></line><line class="cls-3" x1="267.31" y1="284.98" x2="302.66" y2="284.98"></line><line class="cls-3" x1="338" y1="187.69" x2="320.33" y2="187.69"></line><line class="cls-3" x1="567.75" y1="143.57" x2="912.36" y2="143.57"></line><line class="cls-3" x1="558.91" y1="152.4" x2="903.52" y2="152.4"></line><line class="cls-3" x1="523.43" y1="161.24" x2="912.36" y2="161.24"></line><line class="cls-3" x1="461.71" y1="161.24" x2="497.06" y2="161.24"></line><line class="cls-3" x1="479.38" y1="170.21" x2="488.22" y2="170.21"></line><line class="cls-3" x1="965.37" y1="143.57" x2="974.21" y2="143.57"></line><line class="cls-3" x1="965.38" y1="152.44" x2="974.21" y2="152.44"></line><line class="cls-3" x1="956.54" y1="161.24" x2="974.21" y2="161.24"></line><line class="cls-3" x1="965.37" y1="170.21" x2="965.37" y2="170.21"></line><line class="cls-3" x1="505.89" y1="170.07" x2="921.19" y2="170.07"></line><line class="cls-3" x1="497.06" y1="178.9" x2="921.19" y2="178.9"></line><line class="cls-3" x1="479.38" y1="187.74" x2="921.19" y2="187.74"></line><line class="cls-3" x1="497.06" y1="196.57" x2="921.19" y2="196.57"></line><line class="cls-3" x1="620.76" y1="205.41" x2="894.69" y2="205.41"></line><line class="cls-3" x1="470.55" y1="205.41" x2="532.4" y2="205.41"></line><line class="cls-3" x1="550.07" y1="205.41" x2="576.58" y2="205.41"></line><line class="cls-3" x1="558.91" y1="214.24" x2="877.01" y2="214.24"></line><line class="cls-3" x1="558.91" y1="223.07" x2="850.5" y2="223.07"></line><line class="cls-3" x1="470.54" y1="214.24" x2="497.06" y2="214.24"></line><line class="cls-3" x1="523.56" y1="214.24" x2="523.56" y2="214.24"></line><line class="cls-3" x1="541.24" y1="214.24" x2="541.24" y2="214.24"></line><line class="cls-3" x1="470.54" y1="223.07" x2="488.22" y2="223.07"></line><line class="cls-3" x1="532.4" y1="223.07" x2="541.24" y2="223.07"></line><line class="cls-3" x1="912.36" y1="205.41" x2="921.19" y2="205.41"></line><line class="cls-3" x1="912.36" y1="214.24" x2="912.36" y2="214.24"></line><line class="cls-3" x1="903.52" y1="223.07" x2="912.36" y2="223.07"></line><line class="cls-3" x1="868.18" y1="223.07" x2="877.01" y2="223.07"></line><line class="cls-3" x1="594.25" y1="231.91" x2="850.5" y2="231.91"></line><line class="cls-3" x1="479.38" y1="231.91" x2="523.56" y2="231.91"></line><line class="cls-3" x1="470.54" y1="240.8" x2="532.4" y2="240.8"></line><line class="cls-3" x1="558.91" y1="240.8" x2="567.74" y2="240.8"></line><line class="cls-3" x1="877.01" y1="231.91" x2="912.36" y2="231.91"></line><line class="cls-3" x1="885.85" y1="240.74" x2="885.85" y2="240.74"></line><line class="cls-3" x1="885.85" y1="249.58" x2="885.85" y2="249.58"></line><line class="cls-3" x1="877.01" y1="258.41" x2="877.01" y2="258.41"></line><line class="cls-3" x1="603.09" y1="240.74" x2="850.5" y2="240.74"></line><line class="cls-3" x1="470.54" y1="249.58" x2="850.5" y2="249.58"></line><line class="cls-3" x1="461.71" y1="258.41" x2="638.43" y2="258.41"></line><line class="cls-3" x1="656.11" y1="258.41" x2="850.5" y2="258.41"></line><line class="cls-3" x1="611.93" y1="267.24" x2="647.27" y2="267.24"></line><line class="cls-3" x1="452.87" y1="267.24" x2="594.26" y2="267.24"></line><line class="cls-3" x1="700.29" y1="267.24" x2="850.5" y2="267.24"></line><line class="cls-3" x1="700.29" y1="276.08" x2="824" y2="276.08"></line><line class="cls-3" x1="717.96" y1="284.91" x2="744.47" y2="284.91"></line><line class="cls-3" x1="779.81" y1="284.91" x2="806.32" y2="284.91"></line><line class="cls-3" x1="850.5" y1="284.91" x2="859.34" y2="284.91"></line><line class="cls-3" x1="824" y1="284.91" x2="824" y2="284.91"></line><line class="cls-3" x1="850.51" y1="293.75" x2="859.34" y2="293.75"></line><line class="cls-3" x1="788.66" y1="293.75" x2="815.15" y2="293.75"></line><line class="cls-3" x1="717.96" y1="293.75" x2="735.64" y2="293.75"></line><line class="cls-3" x1="850.51" y1="302.58" x2="868.18" y2="302.58"></line><line class="cls-3" x1="788.64" y1="302.58" x2="815.15" y2="302.58"></line><line class="cls-3" x1="717.89" y1="302.58" x2="735.63" y2="302.58"></line><line class="cls-3" x1="726.8" y1="311.41" x2="726.8" y2="311.41"></line><line class="cls-3" x1="788.66" y1="311.41" x2="788.66" y2="311.41"></line><line class="cls-3" x1="806.32" y1="311.41" x2="806.32" y2="311.41"></line><line class="cls-3" x1="868.18" y1="311.41" x2="859.34" y2="311.41"></line><line class="cls-3" x1="788.64" y1="320.25" x2="797.49" y2="320.25"></line><line class="cls-3" x1="735.64" y1="320.25" x2="735.64" y2="320.25"></line><line class="cls-3" x1="859.34" y1="320.25" x2="868.19" y2="320.25"></line><line class="cls-3" x1="841.68" y1="320.25" x2="841.68" y2="320.25"></line><line class="cls-3" x1="779.81" y1="329.08" x2="806.32" y2="329.08"></line><line class="cls-3" x1="832.83" y1="329.08" x2="841.67" y2="329.08"></line><line class="cls-3" x1="823.99" y1="337.92" x2="877.01" y2="337.92"></line><line class="cls-3" x1="788.64" y1="337.92" x2="806.34" y2="337.92"></line><line class="cls-3" x1="823.99" y1="346.75" x2="912.36" y2="346.75"></line><line class="cls-3" x1="894.68" y1="355.59" x2="947.7" y2="355.59"></line><line class="cls-3" x1="850.51" y1="355.59" x2="868.17" y2="355.59"></line><line class="cls-3" x1="806.32" y1="355.59" x2="815.16" y2="355.59"></line><line class="cls-3" x1="956.53" y1="364.42" x2="965.37" y2="364.42"></line><line class="cls-3" x1="885.85" y1="364.42" x2="930.03" y2="364.42"></line><line class="cls-3" x1="815.15" y1="364.42" x2="868.19" y2="364.42"></line><line class="cls-3" x1="850.5" y1="373.25" x2="859.34" y2="373.25"></line><line class="cls-3" x1="885.85" y1="373.25" x2="885.85" y2="373.25"></line><line class="cls-3" x1="938.87" y1="373.25" x2="938.87" y2="373.25"></line><line class="cls-3" x1="868.17" y1="382.09" x2="894.68" y2="382.09"></line><line class="cls-3" x1="921.19" y1="382.09" x2="921.19" y2="382.09"></line><line class="cls-3" x1="850.5" y1="390.92" x2="930.03" y2="390.92"></line><line class="cls-3" x1="850.5" y1="399.76" x2="930.03" y2="399.76"></line><line class="cls-3" x1="832.83" y1="408.59" x2="938.87" y2="408.59"></line><line class="cls-3" x1="983.05" y1="399.76" x2="991.89" y2="399.76"></line><line class="cls-3" x1="983.05" y1="408.59" x2="991.89" y2="408.59"></line><line class="cls-3" x1="832.83" y1="417.42" x2="947.7" y2="417.42"></line><line class="cls-3" x1="832.83" y1="426.26" x2="947.7" y2="426.26"></line><line class="cls-3" x1="841.68" y1="435.09" x2="947.7" y2="435.09"></line><line class="cls-3" x1="894.68" y1="443.93" x2="938.87" y2="443.93"></line><line class="cls-3" x1="841.68" y1="443.93" x2="859.33" y2="443.93"></line><line class="cls-3" x1="1009.56" y1="443.93" x2="1009.56" y2="443.93"></line><line class="cls-3" x1="912.36" y1="452.76" x2="938.87" y2="452.76"></line><line class="cls-3" x1="930.03" y1="461.59" x2="921.19" y2="461.59"></line><line class="cls-3" x1="1009.56" y1="452.76" x2="1018.39" y2="452.76"></line><line class="cls-3" x1="1027.23" y1="461.59" x2="1009.56" y2="461.59"></line><line class="cls-3" x1="1009.56" y1="470.43" x2="1018.39" y2="470.43"></line><line class="cls-3" x1="930.03" y1="470.43" x2="930.03" y2="470.43"></line><line class="cls-3" x1="797.49" y1="346.75" x2="806.34" y2="346.75"></line><line class="cls-3" x1="444.04" y1="276.08" x2="664.94" y2="276.08"></line><line class="cls-3" x1="620.77" y1="284.91" x2="656.11" y2="284.91"></line><line class="cls-3" x1="452.87" y1="284.91" x2="603.08" y2="284.91"></line><line class="cls-3" x1="629.6" y1="293.75" x2="647.27" y2="293.75"></line><line class="cls-3" x1="452.87" y1="293.75" x2="611.92" y2="293.75"></line><line class="cls-3" x1="629.6" y1="302.58" x2="452.87" y2="302.58"></line><line class="cls-3" x1="461.71" y1="311.41" x2="647.27" y2="311.41"></line><line class="cls-3" x1="461.71" y1="320.25" x2="647.27" y2="320.25"></line><line class="cls-3" x1="523.56" y1="329.08" x2="629.6" y2="329.08"></line><line class="cls-3" x1="470.54" y1="329.08" x2="479.38" y2="329.08"></line><line class="cls-3" x1="523.56" y1="337.92" x2="620.76" y2="337.92"></line><line class="cls-3" x1="611.92" y1="346.75" x2="523.56" y2="346.75"></line><line class="cls-3" x1="611.92" y1="355.59" x2="532.4" y2="355.59"></line><line class="cls-3" x1="611.92" y1="364.42" x2="541.24" y2="364.42"></line><line class="cls-3" x1="611.92" y1="373.25" x2="541.24" y2="373.25"></line><line class="cls-3" x1="611.92" y1="382.09" x2="532.4" y2="382.09"></line><line class="cls-3" x1="611.92" y1="390.92" x2="532.4" y2="390.92"></line><line class="cls-3" x1="603.09" y1="399.76" x2="541.24" y2="399.76"></line><line class="cls-3" x1="603.09" y1="408.59" x2="541.24" y2="408.59"></line><line class="cls-3" x1="603.09" y1="417.42" x2="541.24" y2="417.42"></line><line class="cls-3" x1="647.27" y1="382.09" x2="638.43" y2="382.09"></line><line class="cls-3" x1="629.6" y1="390.92" x2="638.43" y2="390.92"></line><line class="cls-3" x1="629.6" y1="399.76" x2="638.43" y2="399.76"></line><line class="cls-3" x1="629.6" y1="408.59" x2="638.43" y2="408.59"></line><line class="cls-3" x1="629.6" y1="417.42" x2="629.6" y2="417.42"></line><line class="cls-3" x1="585.42" y1="426.26" x2="550.07" y2="426.26"></line><line class="cls-3" x1="585.42" y1="435.09" x2="550.07" y2="435.09"></line><line class="cls-3" x1="576.58" y1="443.93" x2="550.07" y2="443.93"></line><line class="cls-4" x1="267.31" y1="19.89" x2="284.99" y2="19.89"></line><line class="cls-4" x1="322.82" y1="19.9" x2="364.51" y2="19.9"></line><line class="cls-4" x1="355.68" y1="28.73" x2="397.37" y2="28.73"></line><line class="cls-4" x1="417.53" y1="19.89" x2="417.53" y2="19.89"></line><line class="cls-4" x1="249.64" y1="28.73" x2="276.15" y2="28.73"></line><line class="cls-4" x1="426.37" y1="28.73" x2="444.04" y2="28.73"></line><line class="cls-4" x1="311.49" y1="37.57" x2="338" y2="37.57"></line><line class="cls-4" x1="373.35" y1="37.56" x2="426.36" y2="37.56"></line><line class="cls-4" x1="249.64" y1="37.57" x2="223.13" y2="37.57"></line><line class="cls-4" x1="170.11" y1="55.23" x2="187.79" y2="55.23"></line><line class="cls-4" x1="399.85" y1="46.39" x2="435.2" y2="46.39"></line><line class="cls-4" x1="329.16" y1="46.4" x2="355.68" y2="46.4"></line><line class="cls-4" x1="293.82" y1="55.23" x2="320.33" y2="55.23"></line><line class="cls-4" x1="373.35" y1="55.23" x2="408.69" y2="55.23"></line><line class="cls-4" x1="435.2" y1="64.06" x2="399.86" y2="64.06"></line><line class="cls-4" x1="347.06" y1="64.06" x2="355.68" y2="64.08"></line><line class="cls-4" x1="214.3" y1="72.91" x2="240.81" y2="72.91"></line><line class="cls-4" x1="143.61" y1="81.73" x2="178.95" y2="81.73"></line><line class="cls-4" x1="382.18" y1="72.91" x2="408.69" y2="72.91"></line><line class="cls-4" x1="338" y1="81.73" x2="364.51" y2="81.73"></line><line class="cls-4" x1="399.86" y1="81.75" x2="417.53" y2="81.75"></line><line class="cls-4" x1="355.68" y1="90.56" x2="391.02" y2="90.56"></line><line class="cls-4" x1="382.18" y1="99.4" x2="399.86" y2="99.4"></line><line class="cls-4" x1="19.9" y1="99.4" x2="55.24" y2="99.4"></line><line class="cls-4" x1="108.26" y1="99.4" x2="117.1" y2="99.4"></line><line class="cls-4" x1="11.06" y1="108.23" x2="72.92" y2="108.23"></line><line class="cls-4" x1="134.77" y1="108.23" x2="170.11" y2="108.23"></line><line class="cls-4" x1="231.91" y1="108.23" x2="249.64" y2="108.23"></line><line class="cls-4" x1="338" y1="108.23" x2="364.51" y2="108.23"></line><line class="cls-4" x1="46.41" y1="117.09" x2="99.42" y2="117.09"></line><line class="cls-4" x1="152.44" y1="117.07" x2="170.11" y2="117.07"></line><line class="cls-4" x1="11.06" y1="125.93" x2="64.08" y2="125.93"></line><line class="cls-4" x1="125.93" y1="125.9" x2="161.28" y2="125.9"></line><line class="cls-4" x1="46.41" y1="134.77" x2="72.92" y2="134.77"></line><line class="cls-4" x1="117.1" y1="134.73" x2="134.77" y2="134.73"></line><line class="cls-4" x1="214.29" y1="134.73" x2="170.11" y2="134.73"></line><line class="cls-4" x1="125.93" y1="143.6" x2="178.95" y2="143.6"></line><line class="cls-4" x1="99.42" y1="152.47" x2="134.77" y2="152.47"></line><line class="cls-4" x1="196.62" y1="152.47" x2="214.3" y2="152.47"></line><line class="cls-4" x1="117.1" y1="161.28" x2="161.28" y2="161.28"></line><line class="cls-4" x1="205.46" y1="161.28" x2="231.97" y2="161.28"></line><line class="cls-4" x1="134.77" y1="170.21" x2="178.95" y2="170.21"></line><line class="cls-4" x1="214.3" y1="170.11" x2="223.13" y2="170.11"></line><line class="cls-4" x1="117.1" y1="178.95" x2="143.61" y2="178.95"></line><line class="cls-4" x1="196.62" y1="178.95" x2="240.71" y2="178.95"></line><line class="cls-4" x1="294.05" y1="161.34" x2="311.49" y2="161.34"></line><line class="cls-4" x1="276.62" y1="178.95" x2="294.05" y2="178.95"></line><line class="cls-4" x1="143.61" y1="187.78" x2="170.11" y2="187.78"></line><line class="cls-4" x1="214.29" y1="187.69" x2="231.82" y2="187.69"></line><line class="cls-4" x1="258.48" y1="187.69" x2="285.33" y2="187.69"></line><line class="cls-4" x1="134.77" y1="196.62" x2="161.28" y2="196.62"></line><line class="cls-4" x1="187.79" y1="196.62" x2="223.06" y2="196.62"></line><line class="cls-4" x1="249.64" y1="196.62" x2="267.31" y2="196.62"></line><line class="cls-4" x1="311.49" y1="196.62" x2="285.33" y2="196.62"></line><line class="cls-4" x1="152.44" y1="205.45" x2="187.79" y2="205.45"></line><line class="cls-4" x1="214.3" y1="205.45" x2="240.71" y2="205.45"></line><line class="cls-4" x1="134.77" y1="214.28" x2="161.28" y2="214.28"></line><line class="cls-4" x1="205.46" y1="214.29" x2="231.97" y2="214.29"></line><line class="cls-4" x1="276.15" y1="214.28" x2="267.3" y2="214.28"></line><line class="cls-4" x1="146.1" y1="223.12" x2="170.12" y2="223.12"></line><line class="cls-4" x1="196.68" y1="223.13" x2="258.48" y2="223.13"></line><line class="cls-4" x1="143.61" y1="231.95" x2="178.95" y2="231.95"></line><line class="cls-4" x1="214.3" y1="231.95" x2="249.64" y2="231.95"></line><line class="cls-4" x1="170.11" y1="240.78" x2="187.79" y2="240.78"></line><line class="cls-4" x1="214.29" y1="249.61" x2="240.71" y2="249.61"></line><line class="cls-4" x1="187.79" y1="267.31" x2="205.46" y2="267.31"></line><line class="cls-4" x1="214.3" y1="284.91" x2="231.97" y2="284.91"></line><line class="cls-4" x1="276.15" y1="284.98" x2="267.31" y2="284.98"></line><line class="cls-4" x1="276.62" y1="311.41" x2="240.81" y2="311.41"></line><line class="cls-4" x1="294.05" y1="329.08" x2="329.16" y2="329.08"></line><line class="cls-4" x1="276.15" y1="337.92" x2="311.49" y2="337.92"></line><line class="cls-4" x1="302.66" y1="346.84" x2="346.84" y2="346.84"></line><line class="cls-4" x1="373.35" y1="355.67" x2="338" y2="355.67"></line><line class="cls-4" x1="284.98" y1="355.67" x2="258.48" y2="355.67"></line><line class="cls-4" x1="276.62" y1="364.44" x2="311.49" y2="364.44"></line><line class="cls-4" x1="391.02" y1="364.44" x2="364.51" y2="364.44"></line><line class="cls-4" x1="293.82" y1="373.28" x2="338" y2="373.28"></line><line class="cls-4" x1="276.15" y1="382.12" x2="311.61" y2="382.12"></line><line class="cls-4" x1="355.67" y1="382.18" x2="373.35" y2="382.18"></line><line class="cls-4" x1="329.05" y1="391.02" x2="381.95" y2="391.02"></line><line class="cls-4" x1="311.49" y1="399.85" x2="346.84" y2="399.85"></line><line class="cls-4" x1="302.66" y1="408.64" x2="329.16" y2="408.64"></line><line class="cls-4" x1="355.68" y1="417.48" x2="320.33" y2="417.48"></line><line class="cls-4" x1="284.98" y1="426.32" x2="311.49" y2="426.32"></line><line class="cls-4" x1="311.49" y1="444" x2="338" y2="444"></line><line class="cls-4" x1="806.34" y1="55.24" x2="832.83" y2="55.24"></line><line class="cls-4" x1="753.31" y1="64.06" x2="770.98" y2="64.06"></line><line class="cls-4" x1="726.76" y1="72.91" x2="762.14" y2="72.91"></line><line class="cls-4" x1="823.99" y1="72.91" x2="850.51" y2="72.91"></line><line class="cls-4" x1="709.13" y1="81.75" x2="744.47" y2="81.75"></line><line class="cls-4" x1="788.64" y1="81.73" x2="806.32" y2="81.73"></line><line class="cls-4" x1="877.01" y1="81.73" x2="921.19" y2="81.73"></line><line class="cls-4" x1="691.45" y1="90.59" x2="753.31" y2="90.59"></line><line class="cls-4" x1="815.15" y1="90.56" x2="850.5" y2="90.56"></line><line class="cls-4" x1="947.7" y1="90.59" x2="983.05" y2="90.59"></line><line class="cls-4" x1="1000.72" y1="99.4" x2="965.38" y2="99.4"></line><line class="cls-4" x1="541.24" y1="99.4" x2="620.76" y2="99.4"></line><line class="cls-4" x1="788.66" y1="99.4" x2="877.01" y2="99.4"></line><line class="cls-4" x1="567.74" y1="108.23" x2="629.6" y2="108.23"></line><line class="cls-4" x1="691.45" y1="108.26" x2="709.13" y2="108.26"></line><line class="cls-4" x1="806.34" y1="108.26" x2="815.16" y2="108.26"></line><line class="cls-4" x1="903.52" y1="108.23" x2="921.19" y2="108.23"></line><line class="cls-4" x1="859.35" y1="117.09" x2="912.36" y2="117.09"></line><line class="cls-4" x1="753.31" y1="117.09" x2="788.64" y2="117.09"></line><line class="cls-4" x1="611.92" y1="117.09" x2="700.29" y2="117.09"></line><line class="cls-4" x1="523.56" y1="117.07" x2="550.07" y2="117.07"></line><line class="cls-4" x1="1027.23" y1="117.07" x2="965.38" y2="117.07"></line><line class="cls-4" x1="585.42" y1="125.93" x2="629.6" y2="125.93"></line><line class="cls-4" x1="726.8" y1="125.9" x2="815.16" y2="125.9"></line><line class="cls-4" x1="885.85" y1="125.9" x2="921.19" y2="125.9"></line><line class="cls-4" x1="983.05" y1="125.9" x2="1000.72" y2="125.9"></line><line class="cls-4" x1="567.74" y1="134.73" x2="656.11" y2="134.73"></line><line class="cls-4" x1="717.89" y1="134.77" x2="726.76" y2="134.77"></line><line class="cls-4" x1="744.45" y1="134.77" x2="744.45" y2="134.77"></line><line class="cls-4" x1="673.78" y1="231.97" x2="673.78" y2="231.97"></line><line class="cls-4" x1="550.07" y1="276.15" x2="550.07" y2="276.15"></line><line class="cls-4" x1="505.89" y1="284.98" x2="505.89" y2="284.98"></line><line class="cls-4" x1="647.27" y1="240.8" x2="647.27" y2="240.8"></line><line class="cls-4" x1="735.64" y1="214.29" x2="735.64" y2="214.29"></line><line class="cls-4" x1="700.29" y1="170.07" x2="700.29" y2="170.07"></line><line class="cls-4" x1="859.34" y1="205.46" x2="859.34" y2="205.46"></line><line class="cls-4" x1="806.32" y1="258.47" x2="806.32" y2="258.47"></line><line class="cls-4" x1="735.64" y1="249.64" x2="735.64" y2="249.64"></line><line class="cls-4" x1="770.98" y1="90.56" x2="770.98" y2="90.56"></line><line class="cls-4" x1="717.89" y1="108.26" x2="717.89" y2="108.26"></line><line class="cls-4" x1="815.16" y1="72.91" x2="815.16" y2="72.91"></line><line class="cls-4" x1="143.61" y1="152.44" x2="143.61" y2="152.44"></line><line class="cls-4" x1="223.06" y1="108.23" x2="223.06" y2="108.23"></line><line class="cls-4" x1="187.79" y1="81.75" x2="187.79" y2="81.75"></line><line class="cls-4" x1="240.71" y1="187.78" x2="240.71" y2="187.78"></line><line class="cls-4" x1="205.42" y1="249.64" x2="205.42" y2="249.64"></line><line class="cls-4" x1="187.79" y1="231.97" x2="187.79" y2="231.97"></line><line class="cls-4" x1="205.57" y1="284.98" x2="205.57" y2="284.98"></line><line class="cls-4" x1="285.33" y1="311.41" x2="285.33" y2="311.41"></line><line class="cls-4" x1="293.81" y1="311.49" x2="293.81" y2="311.49"></line><line class="cls-4" x1="178.95" y1="117.07" x2="178.95" y2="117.07"></line><line class="cls-4" x1="37.57" y1="117.09" x2="37.57" y2="117.09"></line><line class="cls-4" x1="258.48" y1="37.56" x2="258.48" y2="37.56"></line><line class="cls-4" x1="373.35" y1="72.91" x2="373.35" y2="72.91"></line><line class="cls-4" x1="417.53" y1="55.24" x2="417.53" y2="55.24"></line><line class="cls-4" x1="373.35" y1="108.26" x2="373.35" y2="108.26"></line><line class="cls-4" x1="797.48" y1="117.09" x2="797.48" y2="117.09"></line><line class="cls-4" x1="638.43" y1="125.93" x2="638.43" y2="125.93"></line><line class="cls-4" x1="797.49" y1="134.73" x2="850.51" y2="134.73"></line><line class="cls-4" x1="912.36" y1="143.57" x2="885.85" y2="143.57"></line><line class="cls-4" x1="815.15" y1="143.57" x2="762.14" y2="143.57"></line><line class="cls-4" x1="682.61" y1="143.57" x2="717.89" y2="143.57"></line><line class="cls-4" x1="567.75" y1="143.57" x2="594.25" y2="143.57"></line><line class="cls-4" x1="585.42" y1="152.4" x2="647.27" y2="152.4"></line><line class="cls-4" x1="709.13" y1="152.4" x2="744.45" y2="152.4"></line><line class="cls-4" x1="797.49" y1="152.44" x2="850.5" y2="152.44"></line><line class="cls-4" x1="523.43" y1="161.24" x2="567.74" y2="161.24"></line><line class="cls-4" x1="638.43" y1="161.24" x2="673.78" y2="161.24"></line><line class="cls-4" x1="735.63" y1="161.28" x2="779.81" y2="161.28"></line><line class="cls-4" x1="788.64" y1="161.24" x2="815.16" y2="161.24"></line><line class="cls-4" x1="585.42" y1="170.07" x2="656.11" y2="170.07"></line><line class="cls-4" x1="709.13" y1="170.07" x2="770.98" y2="170.07"></line><line class="cls-4" x1="832.84" y1="170.07" x2="894.68" y2="170.07"></line><line class="cls-4" x1="497.06" y1="178.9" x2="558.91" y2="178.9"></line><line class="cls-4" x1="673.78" y1="178.95" x2="726.8" y2="178.95"></line><line class="cls-4" x1="779.81" y1="178.9" x2="850.5" y2="178.9"></line><line class="cls-4" x1="576.58" y1="187.78" x2="611.92" y2="187.78"></line><line class="cls-4" x1="656.11" y1="187.74" x2="753.31" y2="187.74"></line><line class="cls-4" x1="762.14" y1="187.74" x2="770.98" y2="187.74"></line><line class="cls-4" x1="868.19" y1="187.74" x2="921.19" y2="187.74"></line><line class="cls-4" x1="885.85" y1="196.57" x2="841.67" y2="196.57"></line><line class="cls-4" x1="797.49" y1="196.62" x2="735.63" y2="196.62"></line><line class="cls-4" x1="558.91" y1="196.57" x2="594.25" y2="196.57"></line><line class="cls-4" x1="497.06" y1="205.41" x2="470.55" y2="205.41"></line><line class="cls-4" x1="558.91" y1="214.24" x2="611.92" y2="214.24"></line><line class="cls-4" x1="673.78" y1="214.24" x2="682.61" y2="214.24"></line><line class="cls-4" x1="700.25" y1="214.29" x2="726.8" y2="214.29"></line><line class="cls-4" x1="824" y1="214.29" x2="877.01" y2="214.29"></line><line class="cls-4" x1="850.5" y1="205.41" x2="815.16" y2="205.41"></line><line class="cls-4" x1="770.98" y1="205.41" x2="744.45" y2="205.41"></line><line class="cls-4" x1="673.78" y1="205.41" x2="647.27" y2="205.41"></line><line class="cls-4" x1="594.25" y1="223.07" x2="638.43" y2="223.07"></line><line class="cls-4" x1="691.45" y1="223.13" x2="753.31" y2="223.13"></line><line class="cls-4" x1="806.32" y1="223.13" x2="824" y2="223.13"></line><line class="cls-4" x1="620.76" y1="231.91" x2="664.94" y2="231.91"></line><line class="cls-4" x1="744.47" y1="231.91" x2="779.82" y2="231.91"></line><line class="cls-4" x1="850.5" y1="231.91" x2="832.83" y2="231.91"></line><line class="cls-4" x1="603.09" y1="240.74" x2="638.44" y2="240.74"></line><line class="cls-4" x1="700.29" y1="240.74" x2="717.96" y2="240.74"></line><line class="cls-4" x1="762.14" y1="240.74" x2="815.16" y2="240.74"></line><line class="cls-4" x1="514.73" y1="249.64" x2="567.74" y2="249.64"></line><line class="cls-4" x1="629.6" y1="249.64" x2="682.61" y2="249.64"></line><line class="cls-4" x1="744.47" y1="249.64" x2="779.81" y2="249.64"></line><line class="cls-4" x1="717.89" y1="258.41" x2="762.14" y2="258.41"></line><line class="cls-4" x1="850.5" y1="258.41" x2="815.15" y2="258.41"></line><line class="cls-4" x1="824" y1="267.24" x2="777.33" y2="267.24"></line><line class="cls-4" x1="700.29" y1="267.24" x2="735.64" y2="267.24"></line><line class="cls-4" x1="479.38" y1="276.15" x2="541.24" y2="276.15"></line><line class="cls-4" x1="514.73" y1="284.98" x2="558.91" y2="284.98"></line><line class="cls-4" x1="452.87" y1="284.98" x2="479.38" y2="284.98"></line><line class="cls-4" x1="558.91" y1="302.58" x2="629.6" y2="302.58"></line><line class="cls-4" x1="585.42" y1="311.49" x2="532.4" y2="311.49"></line><line class="cls-4" x1="461.71" y1="311.41" x2="488.22" y2="311.41"></line><line class="cls-4" x1="479.38" y1="320.33" x2="514.73" y2="320.33"></line><line class="cls-4" x1="567.74" y1="320.25" x2="620.76" y2="320.25"></line><line class="cls-4" x1="550.07" y1="329.08" x2="594.25" y2="329.08"></line><line class="cls-4" x1="576.58" y1="338" x2="611.92" y2="338"></line><line class="cls-4" x1="523.56" y1="346.75" x2="550.07" y2="346.75"></line><line class="cls-4" x1="567.75" y1="355.67" x2="594.25" y2="355.67"></line><line class="cls-4" x1="585.42" y1="364.51" x2="611.92" y2="364.51"></line><line class="cls-4" x1="558.91" y1="373.25" x2="541.24" y2="373.25"></line><line class="cls-4" x1="576.58" y1="390.92" x2="611.92" y2="390.92"></line><line class="cls-4" x1="558.91" y1="408.69" x2="594.26" y2="408.69"></line></g><line class="community-svg-orange" x1="90.59" y1="143.6" x2="99.42" y2="143.6"></line><line class="community-svg-orange" x1="134.77" y1="205.45" x2="152.44" y2="205.45"></line><line class="community-svg-orange" x1="342.42" y1="364.44" x2="360.09" y2="364.44"></line><line class="community-svg-orange" x1="205.42" y1="231.97" x2="223.06" y2="231.97"></line><line class="community-svg-orange" x1="134.81" y1="196.62" x2="143.57" y2="196.62"></line><line class="community-svg-orange" x1="523.59" y1="161.34" x2="541.24" y2="161.34"></line><line class="community-svg-orange" x1="258.48" y1="214.29" x2="267.24" y2="214.29"></line><line class="community-svg-orange" x1="470.59" y1="152.47" x2="479.35" y2="152.47"></line><line class="community-svg-purple" x1="134.81" y1="214.29" x2="143.57" y2="214.29"></line><line class="community-svg-blue" x1="143.64" y1="214.29" x2="152.4" y2="214.29"></line><line class="community-svg-blue" x1="461.71" y1="161.34" x2="488.22" y2="161.34"></line><line class="community-svg-blue" x1="162.49" y1="205.45" x2="162.49" y2="205.45"></line><line class="community-svg-purple" x1="231.82" y1="231.95" x2="231.82" y2="231.95"></line><line class="community-svg-purple" x1="360.2" y1="364.44" x2="360.2" y2="364.44"></line><line class="community-svg-purple" x1="258.71" y1="205.45" x2="284.91" y2="205.45"></line><line class="community-svg-purple" x1="267.34" y1="214.29" x2="276.11" y2="214.29"></line><line class="community-svg-purple" x1="488.26" y1="161.34" x2="497.02" y2="161.34"></line><line class="community-svg-purple" x1="479.42" y1="152.47" x2="488.18" y2="152.47"></line><line class="community-svg-purple" x1="342.46" y1="355.67" x2="351.22" y2="355.67"></line><line class="community-svg-orange" x1="223.21" y1="240.78" x2="231.97" y2="240.78"></line><line class="community-svg-orange" x1="479.42" y1="143.6" x2="488.18" y2="143.6"></line><line class="community-svg-blue" x1="223.06" y1="240.78" x2="223.06" y2="240.78"></line><line class="community-svg-orange" x1="912.36" y1="231.91" x2="903.52" y2="231.91"></line><line class="community-svg-orange" x1="877.01" y1="231.91" x2="894.68" y2="231.91"></line><line class="community-svg-orange" x1="850.5" y1="249.58" x2="841.67" y2="249.58"></line><line class="community-svg-orange" x1="850.5" y1="258.41" x2="832.83" y2="258.41"></line><line class="community-svg-orange" x1="850.5" y1="240.74" x2="823.99" y2="240.74"></line><line class="community-svg-orange" x1="832.83" y1="408.59" x2="841.68" y2="408.59"></line><line class="community-svg-orange" x1="841.68" y1="435.09" x2="857.86" y2="435.09"></line><line class="community-svg-orange" x1="947.7" y1="417.42" x2="930.03" y2="417.42"></line><line class="community-svg-orange" x1="576.58" y1="443.93" x2="558.91" y2="443.93"></line><line class="community-svg-orange" x1="550.07" y1="134.73" x2="532.42" y2="134.73"></line><line class="community-svg-orange" x1="505.89" y1="170.07" x2="532.42" y2="170.07"></line><line class="community-svg-orange" x1="470.55" y1="205.41" x2="479.42" y2="205.41"></line><line class="community-svg-orange" x1="550.07" y1="187.78" x2="523.59" y2="187.78"></line><line class="community-svg-blue" x1="479.38" y1="187.74" x2="510.31" y2="187.74"></line><line class="community-svg-blue" x1="550.07" y1="170.21" x2="532.42" y2="170.21"></line><line class="community-svg-blue" x1="514.73" y1="143.57" x2="523.56" y2="143.57"></line><line class="community-svg-blue" x1="550.07" y1="443.93" x2="558.91" y2="443.93"></line><line class="community-svg-blue" x1="585.42" y1="435.09" x2="567.74" y2="435.09"></line><line class="community-svg-blue" x1="196.68" y1="223.13" x2="223.21" y2="223.13"></line><line class="community-svg-blue" x1="267.31" y1="196.62" x2="249.64" y2="196.62"></line><line class="community-svg-blue" x1="240.71" y1="205.45" x2="249.64" y2="205.45"></line><line class="community-svg-blue" x1="267.31" y1="223.12" x2="249.61" y2="223.12"></line><line class="community-svg-blue" x1="196.68" y1="240.78" x2="214.3" y2="240.78"></line><line class="community-svg-blue" x1="125.93" y1="143.6" x2="99.42" y2="143.6"></line><line class="community-svg-blue" x1="894.68" y1="231.91" x2="903.52" y2="231.91"></line><line class="community-svg-blue" x1="868.18" y1="223.07" x2="877.01" y2="223.07"></line><line class="community-svg-blue" x1="912.36" y1="223.07" x2="903.52" y2="223.07"></line><line class="community-svg-blue" x1="841.67" y1="249.58" x2="806.32" y2="249.58"></line><line class="community-svg-blue" x1="793.07" y1="284.98" x2="806.32" y2="284.98"></line><line class="community-svg-blue" x1="841.68" y1="408.59" x2="863.76" y2="408.59"></line><line class="community-svg-blue" x1="857.86" y1="435.09" x2="872.59" y2="435.09"></line><line class="community-svg-blue" x1="832.83" y1="426.26" x2="849.77" y2="426.26"></line><line class="community-svg-blue" x1="930.03" y1="417.42" x2="912.36" y2="417.42"></line><line class="community-svg-purple" x1="187.79" y1="231.97" x2="205.42" y2="231.97"></line><line class="community-svg-purple" x1="99.42" y1="152.47" x2="112.68" y2="152.47"></line><line class="community-svg-purple" x1="152.44" y1="187.69" x2="134.77" y2="187.69"></line><line class="community-svg-purple" x1="214.29" y1="249.61" x2="240.71" y2="249.61"></line><line class="community-svg-purple" x1="240.81" y1="214.24" x2="258.48" y2="214.24"></line><line class="community-svg-purple" x1="541.24" y1="161.34" x2="567.74" y2="161.34"></line><line class="community-svg-purple" x1="523.56" y1="143.57" x2="541.24" y2="143.57"></line><line class="community-svg-purple" x1="488.22" y1="134.73" x2="497.06" y2="134.73"></line><line class="community-svg-purple" x1="479.38" y1="170.21" x2="488.22" y2="170.21"></line><line class="community-svg-purple" x1="510.31" y1="187.74" x2="523.59" y2="187.74"></line><line class="community-svg-purple" x1="497.06" y1="178.9" x2="523.59" y2="178.9"></line><line class="community-svg-purple" x1="479.42" y1="205.41" x2="497.06" y2="205.41"></line><line class="community-svg-purple" x1="558.91" y1="435.16" x2="567.74" y2="435.16"></line><line class="community-svg-purple" x1="832.83" y1="258.41" x2="815.15" y2="258.41"></line><line class="community-svg-purple" x1="859.35" y1="214.24" x2="877.01" y2="214.24"></line><line class="community-svg-purple" x1="849.77" y1="417.42" x2="872.59" y2="417.42"></line><line class="community-svg-purple" x1="925.61" y1="426.32" x2="947.7" y2="426.32"></line><line class="community-svg-blue" x1="351.26" y1="408.55" x2="333.58" y2="408.55"></line><line class="community-svg-purple" x1="324.75" y1="408.62" x2="333.58" y2="408.62"></line><line class="community-svg-orange" x1="655.42" y1="116.97" x2="673.06" y2="116.97"></line><line class="community-svg-purple" x1="637.79" y1="116.97" x2="655.42" y2="116.97"></line><line class="community-svg-orange" x1="647.59" y1="125.6" x2="656.42" y2="125.6"></line><line class="community-svg-blue" x1="682.93" y1="125.6" x2="656.42" y2="125.6"></line><line class="community-svg-purple" x1="634.61" y1="134.32" x2="656.7" y2="134.32"></line><line class="community-svg-orange" x1="382.5" y1="373.58" x2="373.67" y2="373.58"></line><line class="community-svg-blue" x1="373.67" y1="373.58" x2="338.32" y2="373.58"></line><line class="community-svg-orange" x1="894.48" y1="178.29" x2="903.24" y2="178.29"></line><line class="community-svg-purple" x1="894.71" y1="169.45" x2="920.91" y2="169.45"></line><line class="community-svg-purple" x1="903.34" y1="178.29" x2="912.11" y2="178.29"></line><line class="community-svg-blue" x1="903.31" y1="160.62" x2="885.64" y2="160.62"></line><line class="community-svg-orange" x1="466.81" y1="320.62" x2="475.57" y2="320.62"></line></g></g></svg>

</div>
</div>

<div class="text-center">
<ul class="d-flex flex-justify-center flex-items-center flex-wrap list-style-none my-2 my-md-3 grayscale">
<li class="mb-3"><img src="https://assets-cdn.github.com/images/modules/site/logos/airbnb-logo.png" alt="Airbnb" class="logo-img px-2 px-sm-4 px-md-5 px-lg-0"></li>
<li class="mb-3"><img src="https://assets-cdn.github.com/images/modules/site/logos/sap-logo.png" alt="SAP" class="logo-img px-2 px-sm-4 px-md-5 px-lg-0"></li>
<li class="mb-3"><img src="https://assets-cdn.github.com/images/modules/site/logos/ibm-logo.png" alt="IBM" class="logo-img px-2 px-sm-4 px-md-5 px-lg-0"></li>
<li class="mb-3"><img src="https://assets-cdn.github.com/images/modules/site/google_logo.png" alt="Google" class="logo-img px-2 px-sm-4 px-md-5 px-lg-0"></li>
<li class="mb-3"><img src="https://assets-cdn.github.com/images/modules/site/logos/paypal-logo.png" alt="PayPal" class="logo-img px-2 px-sm-4 px-md-5 px-lg-0"></li>
<li class="mb-3"><img src="https://assets-cdn.github.com/images/modules/site/logos/bloomberg-logo.png" alt="Bloomberg" class="logo-img px-2 px-sm-4 px-md-5 px-lg-0"></li>
<li class="mb-3"><img src="https://assets-cdn.github.com/images/modules/site/logos/spotify-logo.png" alt="Spotify" class="logo-img px-2 px-sm-4 px-md-5 px-lg-0"></li>
<li class="mb-3"><img src="https://assets-cdn.github.com/images/modules/site/swift_logo.png" alt="Swift" class="logo-img px-2 px-sm-4 px-md-5 px-lg-0"></li>
<li class="mb-3"><img src="https://assets-cdn.github.com/images/modules/site/facebook_logo.png" alt="Rails" class="logo-img px-2 px-sm-4 px-md-5 px-lg-0"></li>
<li class="mb-3"><img src="https://assets-cdn.github.com/images/modules/site/node_logo.png" alt="Node" class="logo-img px-2 px-sm-4 px-md-5 px-lg-0"></li>
<li class="mb-3"><img src="https://assets-cdn.github.com/images/modules/site/nasa_logo.png" alt="Nasa" class="logo-img px-2 px-sm-4 px-md-5 px-lg-0"></li>
<li class="mb-3"><img src="https://assets-cdn.github.com/images/modules/site/logos/walmart-logo.png" alt="Walmart" class="logo-img px-2 px-sm-4 px-md-5 px-lg-0"></li>
</ul>
</div>

</div>
</div>

<div class="featurette bg-gray-light">
<div class="container-responsive text-center">
<h2 class="alt-h2 mt-0 mb-1">
Get started for free
</h2>
<p class="f3 mb-3 col-md-8 mx-auto">
Join the millions of developers already using GitHub to share their code, work together, and build amazing things.
</p>
<p class="f3">
<a href="/join" class="btn btn-large btn-primary">Sign up for GitHub</a>
</p>
</div>
</div>


<div class="modal-backdrop js-touch-events"></div>

</div>

<div class="container-responsive mt-6" role="contentinfo">
<div class="site-footer-marketing d-flex flex-wrap py-5 mb-5">
<div class="site-footer-marketing-col mb-3">
<svg aria-hidden="true" class="octicon octicon-logo-github" height="24" version="1.1" viewBox="0 0 45 16" width="67"><path fill-rule="evenodd" d="M18.53 12.03h-.02c.009 0 .015.01.024.011h.006l-.01-.01zm.004.011c-.093.001-.327.05-.574.05-.78 0-1.05-.36-1.05-.83V8.13h1.59c.09 0 .16-.08.16-.19v-1.7c0-.09-.08-.17-.16-.17h-1.59V3.96c0-.08-.05-.13-.14-.13h-2.16c-.09 0-.14.05-.14.13v2.17s-1.09.27-1.16.28c-.08.02-.13.09-.13.17v1.36c0 .11.08.19.17.19h1.11v3.28c0 2.44 1.7 2.69 2.86 2.69.53 0 1.17-.17 1.27-.22.06-.02.09-.09.09-.16v-1.5a.177.177 0 0 0-.146-.18zm23.696-2.2c0-1.81-.73-2.05-1.5-1.97-.6.04-1.08.34-1.08.34v3.52s.49.34 1.22.36c1.03.03 1.36-.34 1.36-2.25zm2.43-.16c0 3.43-1.11 4.41-3.05 4.41-1.64 0-2.52-.83-2.52-.83s-.04.46-.09.52c-.03.06-.08.08-.14.08h-1.48c-.1 0-.19-.08-.19-.17l.02-11.11c0-.09.08-.17.17-.17h2.13c.09 0 .17.08.17.17v3.77s.82-.53 2.02-.53l-.01-.02c1.2 0 2.97.45 2.97 3.88zm-8.72-3.61H33.84c-.11 0-.17.08-.17.19v5.44s-.55.39-1.3.39-.97-.34-.97-1.09V6.25c0-.09-.08-.17-.17-.17h-2.14c-.09 0-.17.08-.17.17v5.11c0 2.2 1.23 2.75 2.92 2.75 1.39 0 2.52-.77 2.52-.77s.05.39.08.45c.02.05.09.09.16.09h1.34c.11 0 .17-.08.17-.17l.02-7.47c0-.09-.08-.17-.19-.17zm-23.7-.01h-2.13c-.09 0-.17.09-.17.2v7.34c0 .2.13.27.3.27h1.92c.2 0 .25-.09.25-.27V6.23c0-.09-.08-.17-.17-.17zm-1.05-3.38c-.77 0-1.38.61-1.38 1.38 0 .77.61 1.38 1.38 1.38.75 0 1.36-.61 1.36-1.38 0-.77-.61-1.38-1.36-1.38zm16.49-.25h-2.11c-.09 0-.17.08-.17.17v4.09h-3.31V2.6c0-.09-.08-.17-.17-.17h-2.13c-.09 0-.17.08-.17.17v11.11c0 .09.09.17.17.17h2.13c.09 0 .17-.08.17-.17V8.96h3.31l-.02 4.75c0 .09.08.17.17.17h2.13c.09 0 .17-.08.17-.17V2.6c0-.09-.08-.17-.17-.17zM8.81 7.35v5.74c0 .04-.01.11-.06.13 0 0-1.25.89-3.31.89-2.49 0-5.44-.78-5.44-5.92S2.58 1.99 5.1 2c2.18 0 3.06.49 3.2.58.04.05.06.09.06.14L7.94 4.5c0 .09-.09.2-.2.17-.36-.11-.9-.33-2.17-.33-1.47 0-3.05.42-3.05 3.73s1.5 3.7 2.58 3.7c.92 0 1.25-.11 1.25-.11v-2.3H4.88c-.11 0-.19-.08-.19-.17V7.35c0-.09.08-.17.19-.17h3.74c.11 0 .19.08.19.17z"/></svg>
<p class="text-gray alt-text-small">
&copy; 2017
</p>
</div>
<div class="site-footer-marketing-col mb-3 pr-3">
<h4 class="mb-2">Features</h4>
<ul class="list-unstyled text-gray">
<li class="lh-condensed mb-2"><a href="/features#code-review" class="muted-link alt-text-small">Code review</a></li>
<li class="lh-condensed mb-2"><a href="/features#project-management" class="muted-link alt-text-small">Project management</a></li>
<li class="lh-condensed mb-2"><a href="/features#integrations" class="muted-link alt-text-small">Integrations</a></li>
<li class="lh-condensed mb-2"><a href="/features#community-management" class="muted-link alt-text-small">Community</a></li>
<li class="lh-condensed mb-2"><a href="/features#documentation" class="muted-link alt-text-small">Documentation</a></li>
<li class="lh-condensed mb-2"><a href="/features#code-hosting" class="muted-link alt-text-small">Code hosting</a></li>
</ul>
</div>
<div class="site-footer-marketing-col mb-3 pr-3">
<h4 class="mb-2">Platform</h4>
<ul class="list-unstyled">
<li class="lh-condensed mb-2"><a href="https://atom.io" class="muted-link alt-text-small">Atom</a></li>
<li class="lh-condensed mb-2"><a href="http://electron.atom.io/" class="muted-link alt-text-small">Electron</a></li>
<li class="lh-condensed mb-2"><a href="https://desktop.github.com/" class="muted-link alt-text-small">GitHub Desktop</a></li>
<li class="lh-condensed mb-2"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api" class="muted-link alt-text-small">Developers</a></li>
</ul>
</div>
<div class="site-footer-marketing-col mb-3 pr-3">
<h4 class="mb-2">Community</h4>
<ul class="list-unstyled">
<li class="lh-condensed mb-2"><a href="/personal" class="muted-link alt-text-small">Personal</a></li>
<li class="lh-condensed mb-2"><a href="/open-source" class="muted-link alt-text-small">Open source</a></li>
<li class="lh-condensed mb-2"><a href="/business" class="muted-link alt-text-small">For Business</a></li>
<li class="lh-condensed mb-2"><a href="https://education.github.com/" class="muted-link alt-text-small">For Education</a></li>
<li class="lh-condensed mb-2"><a href="https://community.github.com/" class="muted-link alt-text-small">Sponsorships</a></li>
</ul>
</div>
<div class="site-footer-marketing-col mb-3 pr-3">
<h4 class="mb-2">Company</h4>
<ul class="list-unstyled">
<li class="lh-condensed mb-2"><a href="https://github.com/about" class="muted-link alt-text-small" data-ga-click="Footer, go to about, text:about">About</a></li>
<li class="lh-condensed mb-2"><a href="https://github.com/blog" class="muted-link alt-text-small" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
<li class="lh-condensed mb-2"><a href="/business/customers" class="muted-link alt-text-small">Customers</a></li>
<li class="lh-condensed mb-2"><a href="/about/careers" class="muted-link alt-text-small">Careers</a></li>
<li class="lh-condensed mb-2"><a href="/about/press" class="muted-link alt-text-small">Press</a></li>
<li class="lh-condensed mb-2"><a href="https://shop.github.com" class="muted-link alt-text-small">Shop</a></li>
</ul>
</div>
<div class="site-footer-marketing-col mb-3 pr-3">
<h4 class="mb-2">Resources</h4>
<ul class="list-unstyled">
<li class="lh-condensed mb-2"><a href="https://github.com/contact" class="muted-link alt-text-small" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
<li class="lh-condensed mb-2"><a href="https://help.github.com" class="muted-link alt-text-small" data-ga-click="Footer, go to help, text:help">Help</a></li>
<li class="lh-condensed mb-2"><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status" class="muted-link alt-text-small">Status</a></li>
<li class="lh-condensed mb-2"><a href="https://github.com/site/terms" class="muted-link alt-text-small" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
<li class="lh-condensed mb-2"><a href="https://github.com/site/privacy" class="muted-link alt-text-small" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
<li class="lh-condensed mb-2"><a href="https://github.com/security" class="muted-link alt-text-small" data-ga-click="Footer, go to security, text:security">Security</a></li>
<li class="lh-condensed mb-2"><a href="https://services.github.com/" class="muted-link alt-text-small">Training</a></li>
</ul>
</div>
</div>
</div>






<div id="ajax-error-message" class="ajax-error-message flash flash-error">
<svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
<button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
<svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
</button>
You can't perform that action at this time.
</div>


<script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/compat-8e19569aacd39e737a14c8515582825f3c90d1794c0e5539f9b525b8eb8b5a8e.js"></script>
<script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-d192e80fd36e12d318d28c466a8998ebca9d20a15a38122f99edfe44612a034b.js"></script>
<script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-636e7017c8fb903d4c697aeea0d7c32a07e26501813f52f241f840c727ee9c7e.js"></script>




<div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
<svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
<span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
<span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
</div>
<div class="facebox" id="facebox" style="display:none;">
<div class="facebox-popup">
<div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
</div>
<button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
<svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
</button>
</div>
</div>


</body>
</html>

>>> 
