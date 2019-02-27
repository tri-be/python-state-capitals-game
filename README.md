## Challenges

1. Write a function named `sum_to()` that takes a number parameter `n` and returns the sum of the numbers from 1 to n. For example:

```python
sum_to(6)  # returns 21
sum_to(10) # returns 55
```

2. Write a function named `largest()` that takes a list parameter and returns the largest element in that list. You can assume the list contents are all *positive* numbers. For example:

```python
largest([10, 4, 2, 231, 91, 54])  # returns 231
largest([1,2,3,4,0])  # returns 4
```

3. Write a function named `occurances()` that takes two string parameters and counts the number of occurrances of the second string inside the first string. For example:

```python
occurances('fleep floop', 'e')   # returns 2
occurances('fleep floop', 'p')   # returns 2
occurances('fleep floop', 'ee')  # returns 1
occurances('fleep floop', 'fe')  # returns 0
```

4. Write a function named `product()` that takes an *arbitrary* number of parameters, multiplies them all together, and returns the product. (HINT: Review your notes on `*args`).