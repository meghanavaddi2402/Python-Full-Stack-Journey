'''
=> Regular expression :-
- RegEx is an sequence of char that can be searching pattern
- To usde regular expressions we have to import re module
- SYNTAX :- import re
- Functions :-
1.findall() :- It will find all the cahr that are in string 
- EXAMPLE :-
import re
a = 'python is a language is also a dynamically typed language'
print(re.findall('[a]',a))

- output:- ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']    

2.search() :- It will find the char, but it will give the first sequence that found in string
- EXAMPLE :-
import re
a = 'python is a language is also a dynamically typed language'
print(re.split(' ',a))

- output:- ['python', 'is', 'a', 'language', 'is', 'also', 'a', 'dynamically', 'typed', 'language']

3.split() :-
- EXAMPLE :-
import re
a = 'python is a language is also a dynamically typed language'
print(re.search('[a]',a))

- output:- <re.Match object; span=(10, 11), match='a'>

4.sub() :-
- EXAMPLE :-
import re
a = 'python is a language is also a dynamically typed language'
print(re.sub(' ','&',a))

- output:- python&is&a&language&is&also&a&dynamically&typed&language

5.fullmatch() :-
- EXAMPLE :-

- output:-


=> Metachar :-
[]
---------
- EXAMPLE :-
import re
a = 'I have 100 Rupees'
print(re.findall('[abc]',a))
print(re.findall('[0-9]',a))
print(re.findall('[a-z]',a))
print(re.findall('[A-Z]',a))

print(re.search('[abc]',a))
print(re.search('[0-9]',a))
print(re.search('[a-z]',a))
print(re.search('[A-Z]',a))

- output:-
['a']
['1', '0', '0']
['h', 'a', 'v', 'e', 'u', 'p', 'e', 'e', 's']
['I', 'R']
<re.Match object; span=(3, 4), match='a'>
<re.Match object; span=(7, 8), match='1'>
<re.Match object; span=(2, 3), match='h'>
<re.Match object; span=(0, 1), match='I'>

^
--------------
- EXAMPLE :-
import re
a = 'I have 100 Rupees'
print(re.findall('^I have',a))

print(re.search('^I have',a))

- output:-
['I have']
<re.Match object; span=(0, 6), match='I have'>

$
--------------
- EXAMPLE :-
import re
a = 'I am going to school'
print(re.findall('school$',a))

print(re.search('school$',a))
- output:-
['school']
<re.Match object; span=(14, 20), match='school'>

.
---------------
- EXAMPLE :-
import re
a = 'I am going to school'
print(re.findall('s.....',a))
print(re.search('s.....',a))

- output:-
['school']
<re.Match object; span=(14, 20), match='school'>

*
----------------
- EXAMPLE :-
import re
a = 'python will be completed by this week'
print(re.findall('p.*',a))
print(re.findall('p.*ython',a))
print(re.findall('p.*n',a))

print(re.search('p.*',a))
print(re.search('p.*ython',a))
print(re.search('p.*n',a))

- output:-
['python will be completed by this week']
['python']
['python']
<re.Match object; span=(0, 37), match='python will be completed by this week'>
<re.Match object; span=(0, 6), match='python'>
<re.Match object; span=(0, 6), match='python'>

+
------------
- EXAMPLE :-
import re
a = 'python is a language'
print(re.findall('p.+n',a))
print(re.search('p.+n',a))

- output:-

['python is a lan']
<re.Match object; span=(0, 15), match='python is a lan'>

{}
-----------
- EXAMPLE :-
impo
rt re
a = 'python is a language'
print(re.findall('p.{10}',a))
print(re.search('p.{10}',a))
- output:-
['python is a']
<re.Match object; span=(0, 11), match='python is a'>


'''

import re
a = 'python is a language'
print(re.findall('p.{10}',a))
print(re.search('p.{10}',a))

