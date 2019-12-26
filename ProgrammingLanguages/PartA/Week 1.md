# Week 1
## Course Motivation
* Next 4-5 weeks will use:
	* ML Language
	* Emacs
	* Read-eval-print-loop(REPL) for evaluating programs
* Focus on homework only after installing the environment
* Working in strange environments is a life skill

### An Example
```java
class IntBinaryTree {
    int i;
    IntBinaryTree left;
    IntBinaryTree right;

    IntBinaryTree(int _i, IntBinaryTree _left, IntBinaryTree _right){
        i = _i;
        left = _left;
        right = _right;
    }

    int sumAll() {
        int ans = this.i;

        if(left != null){
            ans = ans + left.sumAll()
        }

        if(right != null){
            ans = ans + right.sumAll()
        }

        return ans;
    }

    static int maxArray(int []array) {
        int ans = array[0];

        for(int i = 0; i < array.length; i++) {
            if (array[i] > ans)
                ans = array[i];
        }

        return ans
    }
}
```

- - - -

## About the course
This course is an introduction to the basic concepts of programming languages, with a strong emphasis on functional programming. The course uses the languages ML (in Part A), Racket (in Part B), and Ruby (in Part C) as vehicles for teaching the concepts, but the real intent is to teach enough about how any language “fits together” to make you more effective programming in any language — and in learning new ones.
This course is neither particularly theoretical nor just about programming specifics — it will give you a framework for understanding how to use language constructs effectively and how to design correct and elegant programs. By using different languages, you will learn to think more deeply than in terms of the particular syntax of one language. The emphasis on functional programming is essential for learning how to write robust, reusable, composable, and elegant programs. Indeed, many of the most important ideas in modern languages have their roots in functional programming. Get ready to learn a fresh and beautiful way to look at software and how to have fun building it.

### Course Goals
* Internalize an accurate understanding of what functional and object-oriented programs mean
* Develop the skills necessary to learn new programming languages quickly
* Master specific languages concepts such that they  can recognise them in strange guises
* Lean to evaluate the power and elegance of programming languages and their constructs
* Attain reasonable proficiency in the ML, Racket and Ruby languages — and, as a by-product, become more proficient in languages they already know

### Approximate List of Specific Course Topics - Part A
* Syntax vs. semantics vs. idioms vs. libraries vs. tools
* ML basics (bindings, conditionals, records, functions)
* Recursive functions and recursive types
* Benefits of no mutation
* Algebraic datatypes, pattern matching
* Tail recursion
* Higher-order functions; closures
* Lexical scope
* Currying
* Syntactic sugar
* Equivalence and effects
* Parametric polymorphism and container types
* Type inference
* Abstract types and modules



#coursera/programming languages##partA##Week1#