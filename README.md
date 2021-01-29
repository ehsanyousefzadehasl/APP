# Advanced Programming in Python
This repository aims at making the reader fluent in python language. If you need to review the fundamentals go [here](https://github.com/ehsanyousefzadehasl/PF) which reviews python syntax with exercises.

Also, here there are some exxercises that summarises for you basic python.
- [Favorite genres to be counted and sorted based on two keys with different orders](code/03-favorite-genres.py)
- [To show a number that its prime dividers count is max in a given lists](code/04-max_num_of_prime_divider.py)

- [String operations and sorting based on two keys](code/05-olympiad_list.py)
- [Detecting capitalized words in several sentences](code/06-index_words_in_a_paragraph.py)
- [a translator using dictionary](code/07-pocket_translator.py)

## Introduction
### lambda, map, filter
After learning the basic structures of a programming language like conditionals flows, variables etc. the programmer can develop whatever the project needs. However,being able to use advanced structures of a language is something different, like **LAMBDA FUNCTIONS** in python language. Also, learning advanced programming paradigms, like OOP in this course are considered.

In the following snippet, it is shown how **lambda** make a programmer's life much easier. The following program detects the odd and even numbers in a given list. Actually map applies a function to each of the elements of a given list.

```python
a = [1, 2, 3, 4, 12, 12, 324, 45]
list(map(lambda x: "even" if x % 2 == 0 else "odd",a))
# output: ['odd', 'even', 'odd', 'even', 'even', 'even', 'even', 'odd']
```

FILTERs are another useful structure in python as it's shown in the following snippet.

```python
[1, 2, 3, 4, 12, 12, 324, 45]
list(filter(lambda x: x%2 == 0, a))
# output: [2, 4, 12, 12, 324]
```

### Generators
Generators are used to **create iterators**, but with a different approach. Generators are simple functions which return an iterable set of items, one at a time, in a special way. When an iteration over a set of item starts using the for statement, the generator is run. Once the generator's function code reaches a "yield" statement, the generator yields its execution back to the for loop, returning a new value from the set. The generator function can generate as many values (possibly infinite) as it wants, yielding each one in its turn.
```python
import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))
# output
# And the next number is... 13!
# And the next number is... 22!
# And the next number is... 15!
# And the next number is... 25!
# And the next number is... 20!
# And the next number is... 23!
# And the next number is... 7!
```

```python
def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
# output
# Good, The fib function is a generator.
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
```

Generators are memory efficient (they are returning on demand) compared to the iterators and also code size efficient.

## OOP
In this paradigm, every object in the real world is going to be modeled as a class in the digtial world. Relationships can be defined between classes, for example consider we want to develop a system for a university to keep the information of the university's staff. If we start with a "person" class and have first_name, last_name, birth_date, national_ID properties, and some getters and setters for them, in another class like professor, we can inheret these attributes and functions, and no need to write them again.
