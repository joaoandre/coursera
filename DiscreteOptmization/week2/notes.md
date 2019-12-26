# Week 2

## Knapsack Problem

The **knapsack problem** or **rucksack problem** is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. It derives its name from the problem faced by someone who is constrained by a fixed-size knapsack and must fill it with the most valuable items.

The problem often arises in resource allocation where there are financial constraints and is studied in fields such as combinatorics, computer science, complexity theory, cryptography and applied mathematics.

The knapsack problem has been studied for more than a century, with early works dating as far back as 1897. The name "knapsack problem" dates back to the early works of mathematician Tobias Dantzig (1884–1956), and refers to the commonplace problem of packing the most valuable or useful items without overloading the luggage.

## Approachs

### Greedy Algorithms
 - Sort the inputs by weight(get the least heavy first)
 - Sort the inputs by value(get the mos valuable first)
 - Sort the inputs by value density($/KG)(get the most dense first)

### Modeling

 Given a set of items $I, each item $i \in I$ characterized by its weight $w_{i}$ and value $v_{i}$ and a knapsack with capacity $k$ find the subset of items in $I$ that has maximum value and does not exceed the capacity $k$ of the knapsack.

 - Choose sime decision variables
 - Express the problem constraints in terms of these variables

The result of these steps is an optimization model.

### Decision Variable

 - $x_{i}$ denotes whether item $i$ is selected in the solution
   - $x_{i} = 1$  means the item is selected
   - $x_{i} = 0$ means that it is not selected

### Problem constraint
 - The selected item cannot exceed the capacity of the knapsack $\sum_{i \in I} w_{i}x_{i} \le K$

 ### Object Function

  - Captures the total value of the selected items $\sum_{i \in I} v_{i}x_{i}$

### The model

Maximize $\sum_{i \in I} v_{i}x_{i}$

subject to $\sum_{i \in I} w_{i}x_{i} \le K$

$x_{i} \in {0,1} (i \in I)$

### Exponential Growth

 - How many possible configurations?
   - (0,0,....,0), (0,0,....,1), ..., (1,1,....,1)
 - Not all solutions are feasible
 - How many in total?
   - $2^{\lvert I \rvert}$

# Dynamic Programming

 - Widely used optimization technique
   - For certain classes of problems
   - Heavily used in computational biology
 - Basic principe
   - Divide and Conquer
   - Bottom up computation

 - Basic conventions and notations
   - Assume that $I = {1,2,...,n}$
   - $O(K,J)$ denotes the optimal solution to the knapsack problem with capacity $K$ and items $[1..j]$
 - Assume that we know how to solve
   - $O(k,j-1)$ for all $k \in 0..K$

$O(k,j) = max(O(k,j-1), v_{j} + O(k-w_{j}, j-1))$ if $w_{j} \le k$

$O(k,j) = O(k,j-1)$ otherwise

$O(k,0) = 0$ for all $k$

```python
def O(k, j) {
    if j == 0:
        return 0
    elif(w[j] <= k)
        return max(O(k,j-1), v[j] + O(k-w[j],j-1))
    else:
        return O(k,j-1)
}
```

- How efficient is this?
  - It computes the same expression many times

## Relaxation, branch and bound

### One Dimensional Knapsack

Maximize $45x_{1}+48x_{2}+35x_{3}$

Subject to $x_{1}+8x_{2}+3x_{3} \le 10$

$x_{i} \in {0,1} (i \in 1..3)$

 - Iterative two steps
   - branching
   - bounding

 - Branching
   - Split the problem into a number of subproblems

 - Bounding
   - find an **optimistic estimate** of the best solution to the subproblem
     - Maximization: Upper Bound
     - Minimization: Lower Bound

 - How to find this optimistic estimate?
   - Relaxation!

 - What can we relax?
   - We can relax the capacity constraint
   - We can take a fraction of an item

Maximize $45x_{1}+48x_{2}+35x_{3}$

Subject to $x_{1}+8x_{2}+3x_{3} \le 10$

$0 \le x_{i} \le 1 (i \in 1..3)$

 - This is called the linear relaxation

 - Can we solve a knapsack when we can take parts of the items?
   - Order the items by decreasing value of $V_{i}/W_{i}$
   - Select a fraction of the last item

 - Why is correct?

 Let $x_{i} = y_{i}/v_{i}$

 Maximize $\sum_{i \in 1..j}y_{i}$

 Subject to $\sum_{i \in 1..j} \frac{w_{i}}{v_{i}}y_{i} \le K$

 $0 \le y_{i} \le 1 (i \in 1..j)$
