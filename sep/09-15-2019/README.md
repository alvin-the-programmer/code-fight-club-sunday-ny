# 09-15-2019: Binary Trees

## Topics Covered:
- Binary Trees
  + Depth First
  + Breadth First
- List Comprehension
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

A leaf is a node with no children, so d, f, and g would be leaves  

Both a single node and even no nodes at all counts as a tree.

There are two main methods of traversing a tree:
 - depth first, which is implemented using a stack
 - breadth first, which is implemented using a queue  

For both of these methods we consider a node to be visited when it leaves the 
stack/queue

## List comprehension in python

Instead of the map function for arrays in a language like JavaScript we can do 
something called a list comprehension instead.  

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

To put all the elements back into an array we can put the for loop inside
square brackets, and have the variable name of the element to
 the left of the for loop. That puts each element into a new list.

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
