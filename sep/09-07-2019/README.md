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
class Dog do
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

In python we use dunder init
```python
class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
```
 **In order to have access to self in python classes we must pass self as the first argument**
***

If our Dog class had a bark method we could access it by writing d.bark('Alvin')
```python
def bark(self, person):
  return print(self.name + ' barks at ' + person)

d = Dog('Fido', 3)
d.bark('alvin') # => Fido barks at alvin
```

But that is a syntantic sugar for
```python
Dog.bark(d, 'alvin') # also outputs => Fido barks at alvin
```
Which is why we take self as the first argument

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
A linked list is a collection of nodes where a node contains just a value and a pointer to the next node. The last node in a linked list points to ```None``` or whichever languages equivalent

leetcode provides us the definition of a node below
**Definition for singly-linked list**
```python3
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```

Given a simple list node where we want a pointing to b which points to c we can write
```python3
```