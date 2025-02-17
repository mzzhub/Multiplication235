# A Pandigital Equation
Generating solutions for a pandigital multiplication puzzle. 

## Conditions
- Product of a two digit number and a tree digit number is a five ditit number.
- Considering leading zeros as a digit.
- Use each from 0 to 9 digit exactly once.

## Code breakdown
- Created a list `digits` containing numbers from 0 to 9
- Creaded a list `permutations` containing all the possible permutations from the list  "digits" usning `itertools.permutations`
- Now `permutations` is a list that contains 3628800 lists.
- By looping through the list "permutations"
    - Made a two-gigit `a` number from 0th to 1st index.
    - Made a three-digit `b` number from 2nd to 4th index.
    - Made a five-digit `c` number from 5th to 9th index.
- Check if the condition `a*b=c` and display the solutions
