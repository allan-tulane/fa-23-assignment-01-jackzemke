

# CMPS 2200 Assignment 1

**Name:** Jack Zemke 


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
    - No. In order for some function $f(n) \in O(g(n))$, it's dominant term must be less than or equal to the dominant term of $g(n)$. $2^{n+1} \ge 2^n$, thus $2^{n+1} \notin O(2^n)$.
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?
    - No. Similar to the previous problem, in order for some function $f(n) \in O(g(n))$, it's dominant term must be less than or equal to the dominant term of $g(n)$. $2^{2^n} \ge 2^n$, thus $2^{2^n} \notin O(2^n)$.
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?
    - No. Again similar to the previous problem, in order for some function $f(n) \in O(g(n))$, it's dominant term must be less than or equal to the dominant term of $g(n)$. $n^{1.01} \ge \mathrm{log}^2 n$, thus $n^{1.01} \notin \mathrm{log}^2 n$
  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
    - Yes. For some function $f(n) \in \Omega(g(n))$, there must exist a natural number $c$ such that $cg(n) \le f(n)$ for all $n$. $n^{1.01} \ge \mathrm{log}^2 n$ for all $n \ge 1$, therefore $n^{1.01} \in \Omega(\mathrm{log}^2 n)$
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
    - No. In order for some function $f(n) \in O(g(n))$, it's dominant term must be less than or equal to the dominant term of $g(n)$. $\sqrt{n} \ge O((\mathrm{log} n)^3)$, thus $\sqrt{n} \notin O((\mathrm{log} n)^3)$
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
      - Yes. For some function $f(n) \in \Omega(g(n))$, there must exist a natural number $c$ such that $cg(n) \le f(n)$ for all $n$. $\sqrt{n} \ge \Omega((\mathrm{log} n)^3)$ for all $n$, therefore $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$

  


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words? 
    - This function takes in the upper bound of the fibonacci sequence, $x$, as its only argument. It then recursively adds the two preceding numbers, recursively calling itself until it reaches the principal preceding number, 1. Once the recursive function reaches that base case (1), it returns the sum of all  numbers $n$ such that $1\le n \le x$

.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  
    - Work: $ \in O(n) $ because the implementation must sequentially run through the entire list.  
    - Span: $ \in O(n) $ for the same reason as above, the longest trail of dependancies is the entire list, as the implementation must iterate through every element in the list.

.  

  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
    - Because the list is analyzed sequentially, the algorithm cannot analyze an element until it analyzes the one before it. This means that the work is linearly dependent on the size of the list. The Work is given as $O(n)$
    - Similarly, the longest chain of dependent operations in this case is the full length of the list, as each operation is dependent on the one before it. Therefore, the span is given as $O(n)$
    

.  

  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  
    - The work of this algorithm would be given by the recurrence relation $W(n) = 2W(n/2) + 1$, because the input list is recursively split into two halves, and two new threads are related. Each thread does a constant amount of work, which would be to simply check if the element is a key and adds to the longest run. This recurrence is $O(n)$. It has the same work as the sequential implementation because it still needs to make the same amount of comparisons, analyzing each element in the original list. 
    - The span of this algorithm is given by the recurrence relation $S(n) = S(n/2) + n$, because the parallelization allows for multiple operations to occur at once. This means that the span is dependent on the tree depth, which can be given by $O(\log_{2} n) \in O(\log n)$
