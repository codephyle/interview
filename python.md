### Python Essentials

_Python is an experiment in how much freedom programmers need_ - Guido

This document captures some of the core python language contructs that will help problem solving and writing concise code. We will cover looping, iterators, generators, comprehension, and some general patterns for programming simple problems. We will also ponder some of the most useful standard library classes and functions.

![https://xkcd.com/353/](https://imgs.xkcd.com/comics/python.png)
Things like modules, packages, async, threading, etc., are not covered.

Reader is advised to treat this post as a crash course on basic Python. The reader is assumed to have a little prior programming knowledge.

### Basics

Types: ``` bool, int, float, string```
Sequences: ``` list, tuple, set, dict ```
Collections: ``` deque, heapq, defaultdict, namedcollection ```

<h3>Iterables</h3>

Iteration is a novel feature of Python's containers (list, tuples, dicts etc.,) and generators. Let us see some of the most used operations on iterables.

```python

# Looping (a.k.a Iteration)
>>> s = [1, 2, 3, 4, 5]
>>> for v in s:
...     print(v, end=" ")
1 2 3 4 5

# Variable unpacking
>>> s = (1, 2, 3)
>>> x, y, z = s
>>> y
2
>>> x, *extra = s
>>> extra
[2, 3]

# Membership
>>> s = [1, 2, 3, 4, 5]
>>> 5 in s
True
>>> 4 not in s
False

```
<br/>
A variety of python built-in functions accept iterables as input. <br/>
Notable ones are <pre>min, max, sum, any, all, sorted, reversed</pre>.
<br/> <br/>

```python
>>> s = [1, 2, 2, 3, -4, 50, 6, 7, 8, 9, 9, 0]
>>> tuple(s)
(1, 2, 2, 3, -4, 50, 6, 7, 8, 9, 9, 0)
>>> set(s)
{0, 1, 2, 3, 6, 7, 8, 9, 50, -4}
>>> min(s), max(s), any(s), all(s), sum(s)
(-4, 50, True, False, 93)
>>> sorted(s) # rer
[-4, 0, 1, 2, 2, 3, 6, 7, 8, 9, 9, 50]
# s is NOT modified by any of the above operations
>>> s
[1, 2, 2, 3, -4, 50, 6, 7, 8, 9, 9, 0]
```

<h3>Sequences</h3>
A sequence is an iterable container that has a size and allows items to accessed by integer index starting at 0. For ex., ```string, list, tuple</span> are sequences. <br/>

Operations on sequence (s)

```python
>>> # Concatenation
>>> s = (1, 2, 3)
>>> r = (4, 5, 6)
>>> s + r
(1, 2, 3, 4, 5, 6)

>>> # Making copies
>>> s = [1, 2, 3]
>>> s * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]

```

<br/> Indexing and Slicing <br/>

```
s[i]   => Element at index 'i'. First index is '0'
s[i:j] => elements from index 'i' upto 'j'.
        (not including j). total of 'j-i' elements.

s[i:j:stride] => elements s[i], s[i+stride], s[i+2*stride]
                        ... until index j is reached.

s[:i] => first 'i' elements
s[j:] => elements from j onwards. last "len(s) - j" elements.

s[::2]  => elements at even indices
s[::-1] => reversed copy of s
```

<br/>

```python
>>> s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> s[:4]
[1, 2, 3, 4]
>>> s[1:4]
[2, 3, 4]
>>> s[1:]
[2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> s[::2]
[1, 3, 5, 7, 9]
>>> s[::-1]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

<h3>Looping</h3>

Range loop
```python
for i in range(len(s)):
...
```      
Enumeration

```python
for i, v in enumerate(s):
...
```
Loop till `s` is NOT empty

```python
while s:
        ...
```
Looping in dict d
```python
for k, v in d.items():
...
for k in d.keys():
...
for v in d.values():
...
```

```python
>>> s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for i in range(len(s)):
...     print((i, s[i]), end=" ")
(0, 1) (1, 2) (2, 3) (3, 4) (4, 5) (5, 6) (6, 7) (7, 8) (8, 9) (9, 10)
>>>
>>> for i, v in enumerate(s): print((i,v), end=" ")
...
(0, 1) (1, 2) (2, 3) (3, 4) (4, 5) (5, 6) (6, 7) (7, 8) (8, 9) (9, 10)
>>>
```

<h3> Comprehension </h3>

Use comprehension to transform a collection of data into another data structure. <br/>
For example, taking all the items in a list, applying an operation, and creating a new list:

```python
nums = [1, 2, 3, 4, 5]
squared = [ n * n for n in nums ]
```

It is also possible to apply a filter for transformation

```python
nums = [1, 2, 3, 4, 5]
squared = [ n * n for n in nums if n % 2 == 0]
```

Creating a bucket
```python
bucket = [[] for _ in range(len(nums)+1)]
```
General syntax for list comprehension. sets and dict comprehension has similar syntax

```python
[expression for item1 in iterable1 if condition1
            for item2 in iterable2 if condition2
                ...
            for itemN in iterableN if conditionN ]
```

```python
>>> stocks = [
...   {'name': 'PYPL', 'shares': 100, 'price': 91.1 },
...   {'name': 'MSFT', 'shares': 50, 'price': 123.67 },
...   {'name': 'AAPL', 'shares': 75, 'price': 340.51 },
...   {'name': 'AMZN', 'shares': 60, 'price': 1667.89 },
...   {'name': 'XOM', 'shares': 200, 'price': 95.25 }
... ]
>>>
# Collect all stock names
>>> names = [s['name'] for s in stocks]
['PYPL', 'MSFT', 'AAPL', 'AMZN', 'XOM']
# Entries with atleast 100 shares
>>> atleast100 = [s['name'] for s in stocks if s['shares'] >= 100 ]
['PYPL', 'XOM']
# Total shares*price
>>> total = sum([s['shares']*s['price'] for s in stocks])
159955.15000000002
# Collect (name, shares) tuples
>>> ns = [ (s['name'], s['shares']) for s in stocks ]
[('PYPL', 100), ('MSFT', 50), ('AAPL', 75), ('AMZN', 60), ('XOM', 200)]

# Set comprehension
>>> names = { s['name'] for s in portfolio }
{'PYPL', 'AMZN', 'AAPL', 'MSFT', 'XOM'}

# Dict comprehension
>>> ns = { s['name']:s['price'] for s in stocks }
{'PYPL': 91.1,'MSFT': 123.67,'AAPL': 340.51,'AMZN': 1667.89,'XOM': 95.25}
```


<h3> Generators </h3>
Same as a list comprehension, but produces the result iteratively. The syntax is the same as for list comprehensions except that parentheses are used instead of square brackets.

```python
>>> nums = [1,2,3,4,5]
>>> nums
[1, 2, 3, 4, 5]
>>> squares = ( n * n for n in nums)
>>> squares
<generator object <genexpr> at 0x100558580>
>>> s = sum( n * n for n in nums )
```

A generator object that produces the values on demand via iteration, lazily. ```yield``` is the magic keyword.

```python
>>> def countdown(n):
...      print('Counting down from', n)
...      while n > 0:
...           yield n
...           n -= 1
...
>>> for x in countdown(5):
...     print('yielding ', x)
...
Counting down from 5
yielding  5
yielding  4
yielding  3
yielding  2
yielding  1
>>> c = countdown(100)
>>> c
<generator object countdown at 0x1004e2740>
>>>
>>> next(c)
Counting down from 100
100
>>> next(c)
99
>>> next(c)
98
```

<h3> Strings </h3>

Strings are first-class objects in Python. They are immutable sequences of characters. Any operation on a string produces a new immutable string.

        s = "pythonic"
        for c in s:
            print(c)

Some of the most useful string methods: ``` find, lower, upper, split, strip, endswith, startswith```

<h3> Miscellaneous </h3>

**Functions and Lambda Expressions**

Functions are the building blocks for Python programs, defined with ```def``` keyword.

        # Euclid's GCD algorithm
        def gcd(m,n):
            r = m % n
            if r == 0:
                return n
            return gcd(n, r)


An anonymous function can be defined using a lambda expression:

        lambda args: expression

'args'</span> is a comma-separated list of arguments, and expression is an expression involving those arguments. Here’s an example:

        a = lambda x, y: x + y

equivalent to

        def add_lambda(x, y): return x + y

but, consise without a name. Useful in many in many instances, where we have to pass functions.

For ramdom number.

```python
import random
random.choice(values)
```

```python
a = a[k:] + a[:k] # rotates a by 'k'
```

<h4> Files </h4>

```python
import os
files = os.listdir("/tmp")
with open(filename) as f:
    lines = (l.strip() for line in f)
    for line in lines:
        line.split(':')
```

2' Complement => (1's complement + 1)

```python
# Clear the rightmost set bit. Used in counting bits.
n = n & (n-1) 

# Extracts rightmost set bit only
x = n & ~ (n-1)

x = x >> 1 # divide by 2 
x = x << 1 # multiply by 2

1 << i # creating masks -> will give 1 followed by 'i zeros'

```
<h4> RegEx </h4>

```python
import re

pattern = r'(\d+)-(\d+)-(\d+)'
string = '123-456-7890'

re.match(pattern, string) # match only with the start of the string
re.search(pattern, string) # first occurence
re.findall(pattern. string) # all occurences

text = "Contact us at support@example.com or sales@example.com. Call 123-456-7890 or 987-654-3210."

# Match: Check if the text starts with an email address
pattern_match = r'\w+@\w+\.\w+'
match_result = re.match(pattern_match, text)
print("Match result:", match_result)  # None, because text does not start with an email

# Search: Find the first email address in the text
pattern_search = r'\w+@\w+\.\w+'
search_result = re.search(pattern_search, text)
print("Search result:", search_result.group())  # 'support@example.com'

# Findall: Find all phone numbers in the text
pattern_findall = r'\d{3}-\d{3}-\d{4}'
findall_result = re.findall(pattern_findall, text)
print("Findall result:", findall_result)  # ['123-456-7890', '987-654-3210']

# Compile the patterns for reuse
email_pattern = re.compile(r'\w+@\w+\.\w+')
phone_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')

# Find all emails
emails = email_pattern.findall(text)
print("Emails found:", emails)

# Find all phone numbers
phones = phone_pattern.findall(text)
print("Phone numbers found:", phones)

# Replace phone numbers with a placeholder
new_text = phone_pattern.sub('PHONE_NUMBER', text)
print("Text with phone numbers replaced:", new_text)

# Split text on email addresses
split_text = email_pattern.split(text)
print("Text split on emails:", split_text)

# Iterate over all email matches
for match in email_pattern.finditer(text):
    print(f"Email found at {match.start()}-{match.end()}: {match.group()}")

```

<h4> Decorators</h4>
<h4> Classes</h4>
<h4> Collections </h4>
<h5> Deque</h5>
<h5> Heap</h5>
<h5> Counter</h5>
<h5> Defaultdict </h5>
<h4> Python Object Model </h4>