# Discrete Optmization

## Introduction
Discrete Optimization is the most important field that no one has heard of. It is the science behind high-efficiency manufacturing, inventory management, energy markets, and sports scheduling, just to name a few. This course provides an introductory overview of to the science of Discrete Optimization and through programming assignments gives you first hand experience of what it is like to solve these types of problems. By its nature, Discrete Optimization is challenging but that is what makes it fun and rewarding.

This course is designed to emulate the real world. Imagine that you are working at a brand new startup, ready to change the world, BUT you have been put in charge of solving a knapsack problem. Every one knows this is a hard problem. So, how are you going to solve it? By any means necessary and then you will gain the admiration of your colleagues by sharing your fantastic knapsack solutions with them.

This course takes the same approach. We provide you with a problem and some test cases. You must find a way to solve that problem, by any means you like, and show us how good your work is by sending us a solution. We evaluate your solution and provide feedback regarding its quality. If you are happy with your grade then you are done, but if you want to improve your solution, or just get stuck, the techniques discussed in the lecture videos will be very helpful.

This course assumes you are comfortable writing computer programs, as this is the primary means for solving these problems. The remainder of the course material is self contained and there are no other prerequisites. That said, solving these problem is not usually easy. We expect a typical student to require 10 hours of work on each assignment in order to succeed in this course. Such a major commitment may be daunting, but students often find the authentic learning process of the assignments is very rewarding.

Your commitment to the assignments will not be without reward. Earning a certificate in this course demonstrates you have truly learned the foundations of discrete optimization. Receiving 90% or more on all of the assignments will indicate that you are ready to explore much more advanced topics in Discrete Optimization and should consider pursuing a degree in this area.

## Course Philosophy
This course is not like other courses. The content is very flexible and you are free to design your own plan of study. You can think of this course as a play ground where you can discover how to solve challenging optimization problems. To help you explore the possibilities, we provide a collection of video lectures on different optimization paradigms:

 - Constraint Programming (CP)
 - Local Search (LS)
 - Linear Programming (LP)
 - Mixed Integer Programming (MIP)

You are free to explore these topics as little or as much as you like. To receive a certificate in this course, you must produce high quality solutions to the optimization assignments. Within the guidelines of the collaboration policy, how you achieve these high quality solutions is entirely up to you. There are many paths of study that will lead to receiving a certificate in this course. For example, you may choose to become an expert in just one paradigm (Constraint Programming, Local Search, or Mixed Integer Programming), and only have a basic of understanding of the other paradigms. This "specialist" approach is a successful path to completion. On the other hand, you may become a "generalist" and explore combinations of the different paradigms. This is also a successful path to completion. The choice is yours, just have fun!

You are not alone in this course, it is an optimization community. We encourage you to participate in that community and help each other as much as possible (within the collaboration policy guidelines).

## Course Format
This course is comprised of video lectures and programming assignments. It is designed to be self contained. You will not need to use external material to pass the course. However, this is a challenging course. The course is designed to run in a eight week time frame. Each week, we recommend building your knowledge base by spending between 1 to 3 hours watching the video lectures and progressing on the assignments by spending 10 to 15 hours exploring the programming assignments. You simply cannot learn the challenges of optimization without trying to solve real problems. A large portion of your learning will occur while implementing the assignments and discussing the assignments in the forums.

The student community of this course is essential. We encourage all students to participate significantly in the class forums. Sharing your learning experience and what approaches did and did-not work for you will help you and others to enjoy the challenging joinery of completing this course.

The course was designed to be free form. Although the Coursera platform has a week-by-week structure, you should feel free to design your own course of study and explore the material as you see fit. However, all of this freedom has a price. It is your responsibility to stay on track if you wish to complete the course with a certificate. Warning: the assignments are hard! And they increase in difficulty. You cannot wait until the end of the course to start the assignments. Over the entire run of the course, we expect a successful student to spend at least 70 hours coding.

This course is not about rebuilding the wheel. General purpose optimization tools exist that implement many of the fundamental concepts covered in the lectures. Students are welcome to use general purpose optimization tools in their assignments. The lectures and these tools complement each other as it is essential to understand the underlying technology of these optimization tools. For example, a student wishing to implement a branch and bound search with a linear relaxation need not re-implement the simplex algorithm. You are free to build your search on top of an existing library (e.g. CLP). Please refer to the optimization tools content in Week 3 and the collaboration policy for more guidelines about integrating existing general purpose optimization tools.

## Grading Rubric
Each assignment studies one optimization problem. Your task is to demonstrate the quality of your solution on several instances of that optimization problem. Each problem instance is called an assignment part. Each part is graded on a 10 point scale and the total grade for that assignment is the sum of each part. The rubric of each assignment part is as follows,

 - 0 points - for submitting junk or infeasible solutions
 - 3 points - for submitting low quality solutions
 - 7 points - for submitting good quality solutions
 - 10 points - for submitting great quality solutions

The precise thresholds for each of these grades varies for each problem and part. The grader feedback will clearly indicate how close you are to reaching the next point level.

Each assignment can be submitted an unlimited amount of times over the run of the course and the grade is the best of all submissions. This gives you the freedom to explore many approaches to the assignments without penalty. To get great results on all of the assignment parts you may even use different approaches on each of the assignment parts!

## Collaboration Policy
This class is a community and we encourage as much collaboration as possible within that community. However, to ensure the best learning experience for everyone, we must place some limits on what you can share. There are two guiding principles at the core of fair collaborations,

 1. Your code and algorithms should be your own.
 2. Do not share your code or problem solutions with anyone (including any public forum)

Both of these policies are designed to prevent students from skipping the coding part of the course, which is the essential learning component. Copying code goes as far as downloading binaries that solve the problem of any assignment. This is a core difference from general purpose optimization tools. Tools that solve a wide range of problems are permitted, but tools that are specialized to one specific problem constitute code sharing. You are not permitted to share your solutions because they can be easily used by other students to cheat.

Examples of what not to do:

```
Look at this awesome solution to the first knapsack problem!

18 0
1 1 0 0
```

The text above is a violation of the solution sharing policy.
```python
# Look at this great python code for solving the knapsack problem!

value = 0;
weight = 0;
taken = []
for i in range(0, items):
   if(weight + weights[i] <= capacity):
      taken.append(1)
      value += values[i]
      weight += weights[i]
   else:
      taken.append(0)
```

The code above is a violation of the code sharing policy.

```cpp
// Look at this great comet model for solving the knapsack problem!

Solver m();
var{int} x[Items](m,0..1);

maximize
    sum(i in Items) v[i]*x[i]
subject to {
   m.post(sum (i in Items) w[i]*x[i] <= K);
} using {
  label(x);
  cout << x << endl;
}
```

Sharing a model, like the one above, is a violation of the code sharing policy because someone could easily download Comet and run this model to complete the assignment.

## Notable exceptions:

```
My algorithm found that the optimal solution knapsack problem ks_4_0 is 18.
Can you believe that!?
```

This value alone is not sufficient for cheating. So it is allowed in the collaboration policy. In fact, this kind of sharing is encouraged!

```python
# Here is my python parser for the knapsack assignment input data but
# it has a bug.  Please help me!

lines = inputData.split('\n')
firstLine = lines[0].split()
items = int(firstLine[0])
capacity = int(firstLine[1])
values = []
weights = []
for i in range(0,items):
   line = lines[i] parts = line.split()
   values.append(int(parts[0]))
   weights.append(int(parts[1])
```


This kind of code does not directly relate to the optimization algorithm. You can safely post it without violating the collaboration policy.

```cpp
// Here is a Comet implementation of the 8-Queens model discussed on slide 31
// of the CP 1 lecture.

import cotfd;
Solver m();
range R = 1..8;
var{int} row[i in R](m,R);
solve {
   forall(i in R, j in R : i < j){
      m.post(row[i] != row[j]);
      m.post(row[i] != row[j] + (j-i));
      m.post(row[i] != row[j] - (j-i));
   }
} using {
   label(row);
   cout << row << endl;
}
```

Code mentioned in the lectures can most often be shared freely without consequence. In fact, we encourage you to share implementations of examples from the lectures! However, you should not share code for examples which are also assignments (e.g. implementations of knapsack or graph coloring models from the lectures).

**On a final note:** Please take reasonable security precautions. For example, do not provide your programming assignment credentials to anyone. If you think your programming assignment password may have been compromised, generate a new one.

## Supplementary Material
This course is only a brief introduction to the world of optimization and we hope it is just the beginning of your involvement in the field. In the resources tab you will find collections of materials that supplement the core course material (i.e. the video lectures and assignments). We hope these materials will help you throughout the course and afterwards to continue your involvement with the optimization community.

A brief explanation of each of the supplementary materials:

 - Additional Materials - materials for learning more about optimization
 - Community - avenues to get involved with the optimization community

**A final note:** We encourage you to use external resources to learn more about optimization during the course. However, we discourage you from reading the latest academic papers relating to the problems in a particular assignment. The bulk of the learning in this course is the discovery process you will have while implementing the assignments. Copying a solution from an academic paper side steps the core learning objectives of this course.
