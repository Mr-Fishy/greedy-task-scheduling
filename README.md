# Greedy Task Scheduling with Deadlines & Penalties

## Description

This project implements an efficient greedy algorithm to solve the unit-time task scheduling problem. In this classic optimization problem, the objective is to maximize the retained profit (or equivalently, minimzie the total penalty)

### The Problem

Given a set $S$ of $n$ unit-time tasks. Each task $a_i \in S$ has:

* A strict integer deadline $d_i$, where $1 \leq d_i \leq n$. The task must be completed by this deadline to avoid a penalty.
* A penalty $w_i \geq 0$, which is incurred if the task is not finished by time $d_i$.

The goal is to find a valid schedule for these tasks that minimizes the total penalty incurred for missed deadlines. Because the total penalty of all tasks is a constant, minimizing the penalty of late tasks is mathematically equivalent to maximizing the sum of the penalties of the tasks completed on time. A schedule is valid if no two tasks overlap in time and each task takes exactly one unit of time.

### Implementation

The problem can be solved greedily by sorting the tasks by penalty and iteratively scanning backwards from each task's deadline to find an empty slot. Although this repo implements an alternative method. By sorting by deadline and using a Min-Heap, it is possible to iteratively build the optimal schedule while moving forward in time.

**Algorithm Steps:**  

1. **Sort:** Sort all tasks in monotonically increasing order of their deadlines $d_i$.
2. **Initialize Heap:** Create an empty Min-Heap to track the penalties of the tasks currently accepted into the schedule.
3. **Iterate and Evaluate:** For each task in the sorted list:
   * Push the task's penalty onto the Min-Heap.
   * Check the size of the heap. Because each task takes exactly one unit of time, the current size of the heap represents the time required to complete all currently accepted tasks.
   * If `heap.size() > d_i`, too many tasks have been scheduled to meet the deadline. To resolve this, `pop` the minimum element from the Min-Heap. This greedily discards the task with the lowest penalty from the accepted pool, freeing up the necessary time slot.
4. **Final Calculation:** Once iteration is complete, the heap contains the tasks that will be completed on time. The sum of the penalties of the popped tasks represents the minimum total penalty.

**Complexity:**  

* **Time Complexity:** $O(n \log{n})$. Sorting the tasks takes $O(n \log{n})$. Inserting into and popping from the heap takes $O(\log{n})$ time, which occurs at most $n$ times. Therefore, the overall time complexity is $O(n \log{n})$.
* **Space Complexity:** $O(n)$ to store the sorted tasks and the Min-Heap data structure.

### References / Further Reading

T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein, Introduction to Algorithms, Fourth Edition. MIT Press, 2022.

D. Mount, “CMSC 451: Lecture 5 Greedy Algorithms for Scheduling,” 2025. [Online]. Available: [https://www.cs.umd.edu/class/spring2025/cmsc451-0101/Lects/lect05-greedy-sched.pdf](https://www.cs.umd.edu/class/spring2025/cmsc451-0101/Lects/lect05-greedy-sched.pdf)

## How To Run

## Runtime Sample
