Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
"A" < 'a'
True
>>> user = 4.253
>>> user = input()
input = 4.253
>>> user = input
>>> user = input()
4.253
>>> user
'4.253'
>>> float(user)
4.253
>>> int(float(user))
4
>>> int(user)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    int(user)
ValueError: invalid literal for int() with base 10: '4.253'
>>> 'abc' < 'abd
SyntaxError: EOL while scanning string literal
>>> 'abc' < 'abd'
True
>>> 1 +3 <7
True
>>> ph = int('please enter the ph level')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    ph = int('please enter the ph level')
ValueError: invalid literal for int() with base 10: 'please enter the ph level'
>>> ph = input('please enter the ph level')
please enter the ph level
>>> import math
>>> math.pi
3.141592653589793
>>> math.sin(1)
0.8414709848078965
>>> math.sqrt(9)
3.0
>>> numbers = [1,4,5,7,8,9,0]
>>> numbers[0]
1
>>> numbers[5]
9
>>> []
[]
>>> numbers[1:4]
[4, 5, 7]
>>> numbers[-1]
0
>>> numbers[-2]
9
>>> diff = [1,2,'R',4.345,[1,2]]
>>> iodine = [35535, 3636, 'I',"halogen"]
>>> name = 'Yomna'
>>> name[1] = 'B'
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    name[1] = 'B'
TypeError: 'str' object does not support item assignment
>>> name = ['Alex', ' Sam']
>>> name[1] = 'Yomna'
>>> name
['Alex', 'Yomna']
>>> numbers = [1,2,3,4,10.97,7]
>>> len(numbers)
6
>>> max(numbers)
10.97
>>> min(numbers)
1
>>> sum(numbers)
27.97
>>> sorted(numbers)
[1, 2, 3, 4, 7, 10.97]
>>> numbers
[1, 2, 3, 4, 10.97, 7]
>>> numbers + 2
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    numbers + 2
TypeError: can only concatenate list (not "int") to list
>>> numbers.append(2)
>>> numbers
[1, 2, 3, 4, 10.97, 7, 2]
>>> numbers.remove(2)
>>> numbers
[1, 3, 4, 10.97, 7, 2]
>>> 
