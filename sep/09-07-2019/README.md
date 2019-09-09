# 09-07-2019: Classes and Linked Lists

## Topics Covered:
+ Python3
  + self in instance methods
  + global methods
+ Linked Lists
  + nodes
  + [leetcode #60](https://leetcode.com/problems/add-two-numbers/)

### Notes about classes in Python3

To run some code on creation of a new class in Ruby we have the initialize method

```ruby
class Dog
  def initialize(name)
    self.name = name
  end
end
```

In JavaScript we have constructor

```javascript
class Dog {
  constructor(name) {
    this.name = name;
  }
}
```

In Python we use dunder init (dunder means **D**ouble **U**nderscores)

```python
class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
```

 **In order to have access to self in python classes we must pass self as the first argument**
 We could name self something else. self is not a reservered keyword in Python although it is convention to use self
***

If our Dog class had a bark method we could access it by writing `d.bark('Alvin')`

```python
def bark(self, person):
  print(self.name + ' barks at ' + person)

d = Dog('Fido', 3)
d.bark('alvin') # => Fido barks at alvin
```

which syntantic sugar for

```python
Dog.bark(d, 'alvin') # also outputs => Fido barks at alvin
```

You can see we pass a class instance as the first argument, which is why we take self as the first argument

***
Python has global methods like len() that works on all sorts of data structures

```python
my_str = 'potato'
my_list = [1,2,3,4,6]
my_dictionary = {
  'name': 'a/A',
  'color': 'red'
}

len(my_str) # => 6
len(my_list) # => 5
len(my_dictionary) # => 2
```

If we want to do something like len(dog) we can write a dunder len method that allows len() to work on our classes

```python
def __len__(self):
  return 7
```

Outside the class if we made a instance of a dog and called len on it we would get 7 as the result

```python
d = Dog('fido', 3)
print(len(d)) # 7
```

Under the hood Python's len() method does something like

```python
def len(ob):
  return ob.__len__
```

***

## Linked Lists

We are given the problem description below for the leetcode problem

```
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
```

**In order to solve this problem we need to understand what a linked list is**  
A linked list is a collection of nodes where a node contains just a value and a pointer to the next node. The last node in a linked list points to ```None``` or the language's equivalent (i.e. nil, null)

leetcode provides us the definition for a node below

```python
# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```

Given a simple list node where we want a pointing to b which points to c we can write

```python
a = ListNode('a')
b = ListNode('b')
c = ListNode('c')

a.next = b
b.next = c
# a -> b -> c -> None
```

Manually linking up nodes like this is time consuming and prone to errors
So instead when we writing a LinkedList class we should also write a method to do that for us

```python
class LinkedList:
  # A linked list only needs access to the head of the list to have access to everything in the linkedlist
  def __init__(self):
    self.head = None

  # A method to add a value to the linked list written recursively
  def add(self, val, current=None):
    # If the head of the list is empty then we set the head to be the value added
    if self.head is None:
      self.head = ListNode(val)
      return

    # Sets the default value of current to be the head of the linked list
    if current is None: current = self.head

    if current.next is None:
      # If we reach the tail of the list so we add a new node containing the value to the linked list
      current.next = ListNode(val)
    else:
      # Else we recursively call add with the next node in the list
      self.add(val, current.next)
```

Back to the leetcode problem we are given the boilerplate code

```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
```

**Lets try to find a recursive solution to the problem**  
If we ignore the edge cases we have an almost trivially simple problem.  
Assume we are given the following linked lists

```
list1 = 6 -> 2 -> None
list2 = 1 -> 3 -> None

result = 7 -> 5 -> None
```

We create a new ListNode with the value being the sum of the two nodes values at the head, then we move onto the next node's value for both lists

```
list1 = 6 -> 2
list2 = 1 -> 3

current values = 6 + 1 = 7
result = 7
***
current values = 2 + 3 = 5
result = 7 -> 5
***
current values = None, None
result = 7 -> 5 -> None
```

If we translate that logic into code

```python
  def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry = 0) -> ListNode:
    # If both lists point to None then we should return None since there are no more numbers to add and linked lists should have the tail pointing to None
    if l1 is None and l2 is None:
      return None
    # add the two numbers together and make a new node with that value
    result_node = ListNode(l1.val + l2.val)
    # recursive call with the next value of both linked lists
    result_node.next = self.addTwoNumbers(l1.next, l2.next)
    return result_node
```

## Side note about the keyword `is`

In python we have english word keywords for operators

```python
not # !
or  # ||
and # &&
```
However the keyword `is` is not the same as the equivalency operator `==`  
Python's `==` is most similar to Ruby's `==`

```ruby
# in ruby
a = [3, 4]
b = [3, 4]
a == b # true

c = [4, 3]
a = c # false
```

We get the same results in python

```python
# in python
a = [3, 4]
b = [3, 4]
a == b # true

c = [4, 3]
a = c # false
```

However if we use `is` then a `is` b returns false

```python
# in python
a = [3, 4]
b = [3, 4]
a is b # false
```

While the two arrays contains the same values in the same order they are not the same array, so if we were to modify one of them then the other array would not be modified

```python
a[0] = '!'
b[1] = '!'

a # ['!', 4]
b # [3, '!']
```

In order for `a is b` to be true then we would need to assign a to b

```python
a = [3, 4]
b = a

a is b # true
```

## Back to the problem, we should start accounting for some edge cases

The edge cases we should account for is
+ linked lists of different lengths

```
list1 = 6 -> 2 -> None
list2 = 1 -> None

result = 7 -> 2 -> None
26 + 2 = 27
```

+ when the values sum is greater or equal 10 then we need to carry

```
list1 = 6 -> 2 -> None
list2 = 5 -> 1 -> None

result = 1 -> 4 -> None
26 + 15 = 41
```

+ when the last two values in the linked list sums to a value greater or equal 10 then we need to add an additional node for that carry

```
list1 = 6 -> 2 -> None
list2 = 1 -> 9 -> None

result = 7 -> 1 -> 1 -> None
26 + 91 = 117
```

## quick aside for ternaries in python

In other languages we write a ternary like so  
`variable =` (conditional) `?` (assignment if conditional is true) `:` (assignment if conditional is false)


In python we instead write it like  
`variable =` (assignment if conditional is true) `if` (conditional) `else` (assignment if conditional is false)
***
Lets tackle these edges cases in order  
First to deal with lists of different lengths, when a node is currently at None then we can instead say the value for that node is 0

```python
  # Set the value to 0 if there is no number to add
  val1 = 0 if l1 is None else l1.val
  val2 = 0 if l2 is None else l2.val
  # Don't proceed to next if there is no next
  next1 = l1.next if l1 is not None else None
  next2 = l2.next if l2 is not None else None
  # use our new variables
  result_node = ListNode(val1 + val2)
  result_node.next = self.addTwoNumbers(next1, next2)
```

**Next we should handle the easier of the two carry cases**
When two numbers sums to a value greater or equal to 10 then we need to carry 1 to the next number
```python
# account for the carry
def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry = 0) -> ListNode:
  # base case and edge cases

  # account for when the sum is greater or equal to 10
  addition = val1 + val2 + carry
  next_carry = 0
  if addition >= 10:
    next_carry = 1
    addition -= 10

  result_node = ListNode(addition)
  # pass the next carry on
  result_node.next = self.addTwoNumbers(next1, next2, next_carry)
  return result_node
```

Finally we can account for when the carry happens on the last node and we need to add an additional node  
We can add an additional check in our base case

```python
if head1 is None and head2 is None:
  if carry == 1:
    return ListNode(1)
  else:
    return None
```

Our final solution looks like this

```python
def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry = 0) -> ListNode:
  if l1 is None and l2 is None:
    if carry == 1:
      return ListNode(1)
    else:
      return None

  val1 = 0 if l1 is None else l1.val
  val2 = 0 if l2 is None else l2.val

  next1 = l1.next if l1 is not None else None
  next2 = l2.next if l2 is not None else None
  addition = val1 + val2 + carry
  next_carry = 0

  if addition >= 10:
      next_carry = 1
      addition -= 10

  result_node = ListNode(addition)
  result_node.next = self.addTwoNumbers(next1, next2, next_carry)
  return result_node
```