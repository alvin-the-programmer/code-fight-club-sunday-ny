# 09-22-2019: General problems

## Topics Covered:

- Time Complexity
  - Worst case
  - Average case
  - Best case
- Problems
  - [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
  - Prime Facorization
  - [Ugly Number](https://leetcode.com/problems/ugly-number/)


## Short Notes about time complexity

Big O and time complexity are topics that we should be familar with now. For 
example if someone asked us what the time complexity of merge sort is we know 
that it's **N log(N)**.  

But if someone asked us what's the Big O time complexity of quicksort answering 
**N log(N)** would be wrong. Quick sort actually has a time complexity of 
**N<sup>2</sup>** in the worst case.

Why is it so slow if it's called quick sort? It's actually fast in the average 
case; having a time complexity of **N log(N)**. We represent average case with 
the greek letter theta. So we say quick sort has a big theta of **N log(N)** or 
`Θ(N log(N))`

For the best case we use omega. For example bubble sort has a best case time 
complexity of big omega of **N** or `Ω(N)`
