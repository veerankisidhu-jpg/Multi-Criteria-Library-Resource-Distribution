# Multi-Criteria-Library-Resource-Distribution
# Multi-Criteria Library Resource Distribution
Name:V.Siva Sambhavi
Roll number:N26V01A0389  
section:05 
## 1. Project Description

The Multi-Criteria Library Resource Distribution system is a Python-based application designed to distribute available book copies among different library branches.

The system analyses book availability, borrowing demand, and branch-wise requirements. It allocates copies according to the supplied priority rules and calculates unmet demand.

This project demonstrates the use of basic Python programming concepts such as dictionaries, lists, loops, conditional statements, functions of built-in operations, and arithmetic calculations.

## 2. Objectives

- Analyse the availability of books in the library.
- Identify borrowing demand for each book at different branches.
- Allocate available copies according to priority rules.
- Calculate the number of copies allocated to each branch.
- Identify unmet demand for each book and branch.
- Generate an overall resource distribution summary.

## 3. Problem Statement

A library system contains multiple branches with different book requirements. The number of available copies is limited, and the demand for books may exceed the available resources.

The objective is to develop a Python program that distributes available book copies among library branches based on priority and demand.

The program must calculate the allocated copies, remaining unmet demand, and overall distribution statistics.

## 4. Assumptions

1. The library has three branches:
   - Central Library
   - North Branch
   - South Branch

2. Each book has a fixed number of available copies.

3. Each branch has a specified demand for every book.

4. Books are assigned a priority number, where a smaller number indicates higher priority.

5. For each book, branches with higher demand receive copies first.

6. A branch cannot receive more copies than its demand.

7. Available copies cannot be exceeded during allocation.

8. All input values are hypothetical and used for demonstration.

## 5. Priority Rules

The program follows these rules:

1. Books are assigned priority levels.
2. Higher-priority books are processed before lower-priority books.
3. For each book, branches are arranged according to their demand.
4. Copies are allocated to the branch with the highest demand first.
5. Allocation continues until all available copies are distributed or demand is satisfied.
6. Unmet demand is calculated as:

   Unmet Demand = Branch Demand - Allocated Copies

## 6. Algorithm

1. Start the program.
2. Define the library branches.
3. Store book availability, priority, and branch-wise demand.
4. Initialize allocation results.
5. For each book:
   - Read the available copies.
   - Read the demand of each branch.
   - Calculate total demand.
   - Arrange branches in descending order of demand.
   - Allocate copies without exceeding availability or branch demand.
   - Calculate unmet demand.
   - Store the allocation results.
6. Display the allocation for each book.
7. Calculate total available copies.
8. Calculate total allocated copies.
9. Calculate total unmet demand.
10. Display branch-wise allocation totals.
11. Stop the program.

## 7. Pseudocode

```text
BEGIN

    DEFINE branches

    DEFINE books with:
        available copies
        priority
        branch-wise demand

    FOR each book:
        READ available copies
        READ branch-wise demand

        SET remaining copies = available copies

        SORT branches by demand in descending order

        FOR each branch in sorted order:
            IF remaining copies > 0:
                allocation = MIN(branch demand,
                                remaining copies)

                remaining copies =
                    remaining copies - allocation

        FOR each branch:
            unmet demand =
                branch demand - allocated copies

        DISPLAY book allocation
        DISPLAY unmet demand

    CALCULATE total available copies
    CALCULATE total allocated copies
    CALCULATE total unmet demand

    DISPLAY overall summary

END
```

## 8. Python Concepts Used

- Variables and data types
- Lists
- Dictionaries
- Nested data structures
- `for` loops
- `if` statements
- `min()` function
- `sum()` function
- `sort()` function
- Arithmetic operators
- String formatting and output statements

## 9. Input Data

| Book | Available | Central | North | South |
|---|---:|---:|---:|---:|
| Python Programming | 20 | 12 | 10 | 8 |
| Data Structures | 15 | 8 | 12 | 10 |
| Operating Systems | 10 | 6 | 7 | 5 |

## 10. Test Cases

| Test Case | Available | Demand | Expected Result |
|---|---:|---|---|
| 1 | 10 | 4, 3, 2 | All demand satisfied |
| 2 | 5 | 4, 4, 4 | 5 allocated, 7 unmet |
| 3 | 0 | 3, 2, 1 | 0 allocated, 6 unmet |
| 4 | 15 | 5, 5, 5 | All demand satisfied |
| 5 | 8 | 10, 0, 0 | 8 allocated, 2 unmet |

## 11. Expected Output

```text
MULTI-CRITERIA LIBRARY RESOURCE DISTRIBUTION

Book: Python Programming
Priority: 1
Available Copies: 20
Total Demand: 30

Branch-wise Allocation:
Central Library - Demand: 12 | Allocated: 12 | Unmet: 0
North Branch - Demand: 10 | Allocated: 8 | Unmet: 2
South Branch - Demand: 8 | Allocated: 0 | Unmet: 8

Total Allocated: 20
Total Unmet Demand: 10
Status: Demand Not Fully Satisfied
```

The complete program displays similar results for all books and provides an overall summary.

## 12. Conclusion

The Multi-Criteria Library Resource Distribution system successfully analyses book availability and branch-wise borrowing demand.

It allocates available copies based on demand priority and calculates unmet demand for each branch.

The project demonstrates how Python can be used to solve resource allocation problems using lists, dictionaries, loops, conditional statements, and basic calculations.

The system can be extended to include more library branches, additional book categories, user-defined priorities, and interactive input.
