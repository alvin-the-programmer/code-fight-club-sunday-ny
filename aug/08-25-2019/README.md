# 08-25-2019: Combinatorics

## Topics Covered:
+ Basics of Python3
    + colons and whitespace sensitivity
    + dynamically/strongly typed
    + `for item in collection` iterators
    + list comprehensions
+ Case Problem: Given a set of n things
    + generate all 2^n combinations
    + generate all n! permutations
+ [Leetcode #60](https://leetcode.com/problems/permutation-sequence/)


## Miscellaneous Notes

### Dynamically typed vs Statically typed Language

Dynamically typed means we do not have to specify a type when declaring a variable. Statically typed means we must specify what type a variable will contain, and we cannot diverge from this.

+ Dynamically typed: JavaScript, Ruby, Python, ...
+ Statically typed: Java, C/C++, ...

### Weak vs Strong typing

Type coercion is where a value may be **implicitly** converted into a different type in order to perform an operation. A weakly typed language has type coercion. A strongly typed language does not have type coercion.

+ Strongly typed: Ruby, Python, Java, C/C++, ...
+ Weakly typed: JavaScript, ...

Note that Dynamic/Static typing is a distinct feature from Weak/Strong typing. JavaScript is Dynamic & Weak, while Ruby is Dynamic & Strong.

### Python Trivia

+ List - similar to a Ruby Array or a JavaScript Array, use brackets `[]`
+ Dict - similar to a Ruby Hash or a JavaScript Array, use braces `{}`
+ Tuple - an immutable list, use parens `()`


### Case Problem: Combinations

Given a collection of n things, return all possible combinations of elements. A combination is a set where order does not matter, no duplicate items, and we don't have to take every item.

Example:

```python
master_list = ['a', 'b', 'c']
combinations(master_list) # =>
# [
#     []
#     ['a']
#     ['b']
#     ['c']
#     ['a', 'b']
#     ['a', 'c']
#     ['b', 'c']
#     ['a', 'b', 'c']
# ]
```

There will be `2^n` combinations given a collection of `n` things. Why? Because for every item, we make a binary (2) decision to either include or exclude this item in the combination.

### Case Problem: Permutations

Given a collection of n things, return all possible permutations of elements. A permutation is an ordered set, where we must take every item exactly once.

```python
master_list = ['a', 'b', 'c']
permutations(master_list) # =>
# [
#     ['a', 'b', 'c'],
#     ['a', 'c', 'b'],
#     ['b', 'a', 'c'],
#     ['b', 'c', 'a'],
#     ['c', 'b', 'a'],
#     ['c', 'a', 'b']
# ]
```

There will be  `n!` permutations given a collection of `n` things. Why? Because for every item, we decide **where** to insert it into the permutation. In other words:
+ the first item `a` can only be placed in 1 position because the set is empty: `a`
+ the second item `b` can be placed in 2 possible positions because it can come before the `a` or after the `a`: `ab` or `ba`
+ the third item `c` can be placed in 3 possible positions because it can come before the the first, between the first and second, or after the second:
    + insert `c` into `ab`: `cab`, `acb`, `abc`,
    + insert `c` into `ba`: `cba`, `bca`, `bac`.

Notice the growing number of options for where to insert. It is given by: `1 * 2 * 3 * ... * (n - 1) *  n = n!`
