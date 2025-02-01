# Overview

Data structures are different ways to store data in memory. In this section, we
will be discussing each one in detail, as well as recommending problems to 
practice each one. 

Before that though, we need to learn the language we use in computer science to
describe performance.

## Algorithmic Analysis

To be able to determine the performance of an algorithm there are two things we
need to take into account:

* **Time**: refers to the amount of compute opperations of the algorithm. Higher
  complexity means that the algorithm will take more time to excecute.
* **Space**: refers to the amount of memory allocated by the algorithm. Higher
complexity means more bytes used.

However, algorithms will behave differently depending on the data they are
processing. That is why, we need a tool that describes their complexity.

### Big O

Big O is a function that describes the complexity of the algorithm in terms of
an algebraic expression. Such expression represents how the time/space
complexity scales as the input grows.

We will discuss the more common complexities in an effort to understand how this
works, but before that, here is a couple rules:

#### Rules

##### Drop the constants

If your complexity turns out to be O(3n), where n is the size of your input, a
complexity of O(n) is good enough to describe it.

It does not matter how big the constant is. That is because it will not change
the behavior of the algorithm when it tends to infinity. A complexity of O(n)
will always be smaller than a compleity of O(n^2), and the O(n^2) will always
be smaller than O(n^3), and so on.

##### Drop the smaller terms
If your complexity turns out to be O(3n + 9), where n is the size of your
input, a complexity of O(n) is good enough to describe it.

It does not matter how big the smaller term is, it will always be smaller and
will not change how it meassures against other complexities when it tends to
infinity.


#### Complexity Rankings

1. Constant Complexity O(1): The best.
    * Time: It means your algorithm time is always the same and does not depend
      on your input. You might only use arithmetic and logic opperations, and
      maybe fixed size loops.
    * Space: It means your algorithm memory allocation is constant. You might
      only use a couple variables or a fixed size data structure.

2. Logarithmic Complexity O(log(n)): Good.


#### Constant Complexity

#### Linear Complexity

#### Squared Complexity

#### Logarithmic Complexity

#### Exponential Complexity

#### Factorial Complexity
