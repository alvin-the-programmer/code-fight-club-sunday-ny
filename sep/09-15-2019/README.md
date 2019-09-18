# 09-15-2019: Binary Trees

## Topics Covered:
- Binary Trees
  + Depth First
  + Breadth First
- Python
  + List Comprehension
  + Tuple
  + Deque
  + List deconstruction
- Leet Code Problems
  + [leetcode #257](https://leetcode.com/problems/binary-tree-paths/)
    - [lc257 notes](lc_257.md)
  + [leetcode #515](https://leetcode.com/problems/find-largest-value-in-each-tree-row/)
    - [lc515 notes](lc_515.md)

## Binary trees notes

Binary Trees have at most two children

```
     a
   /   \
  b     c
 / \   /
d   e f
   /
  g
```

A leaf is a node with no children, so d, f, and g would be the leaves  

Both a single node and even no nodes at all counts as a tree.

There are two main methods of traversing a tree:
 - depth first, which is implemented using a stack
 - breadth first, which is implemented using a queue  

For both of these methods we consider a node to be visited when it leaves the 
stack/queue

# Python notes

## List comprehension

In JavaScript we have the map function `Array.prototype.map` which allows us to
iterate through each element in an array and perform some logic on the element 
before putting it into a new array.  

In python we can do something called a list comprehension instead.  

Given an array we can iterate through it using a for loop  

```python
my_list = [5, 6, 7, 8, 9, 10]

for ele in my_list: print(ele)

# output:
# 5
# 6
# 7
# 8
# 9
# 10 
```

To put all the elements back into a list we can put the for loop inside
square brackets, and have the variable name of the element to the left of the 
for loop. That puts each element into a new list.

```python
my_list = [5, 6, 7, 8, 9, 10]
list_comprehension = [ ele for ele in my_list ]

print(list_comprehension)
# output: [5, 6, 7, 8, 9, 10]
```

That's not very useful as it is but we can do some logic on the element before 
we put it into the array. For example we could square the number.

```python
my_list = [5, 6, 7, 8, 9, 10]
list_comprehension = [ ele ** 2 for ele in my_list ]

print(list_comprehension)
# output: [25, 36, 49, 64, 81, 100]
```

Or we could strigify it then append a arrow after it

```python
my_list = [5, 6, 7, 8, 9, 10]
list_comprehension = [ str(ele) + '->' for ele in my_list ]

print(list_comprehension)
#output: ['5->', '6->', '7->', '8->', '9->', '10->']
```

This allows us to do what `Array.protoype.map` does in 
JavaScript, but in python style!

## Tuple

Tuples are just like lists, with two exceptions:  
1. Tuples are defined using parentheses instead of square brackets
2. Tuples can not be modified. In other words, they are immutable

```python
t = (1, 2, 3)
print(t[0]) # output: 1

t[0] = 4 # error is thrown
```

## Deque

A deque is like a two sided queue, you are able to append and pop from both 
sides. (Just like a javascript array!)  

To get access to deque we need to import it from collections.  

Collections is a built in module, so no need to download anything extra

```python
from collections import deque
```

We can instantiate a new deque with default values by passing it a iterable as
its argument.  

Deques, along with append and pop also have additional methods appendleft and 
popleft.

```python
from collections import deque

d = deque([1, 2, 3]) # deque([1, 2, 3])
d.append(5) # deque([1, 2, 3, 5])
d.popleft() # deque([2, 3, 5])
d.appendleft(0) # deque([0, 2, 3, 5])
```

## List deconstruction

Like in other languages, Python also has list deconstruction

```python
my_list = ['first', 'second', 'third']
a, b, c = my_list

print(a) # output: 'first'
print(b) # output: 'second'
print(c) # output: 'third'
```