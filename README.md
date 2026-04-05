# COP4533_assignment3


# Programming Assignment 3 dynamic programming

Student: Ibrahim Zbib
UFID: 79090242




## How to run:
```python3  src/solution.py <input_file> ```

### Run the program with an input file:
The /data folder holds the input and output files. /src folder holds the main program.
  ``` python3 src/solution.py data/example.in```
### Verify the outputs match:
``` python3 src/solution.py data/example.in | diff - data/example.out ```
no output in the terminal means that the output matches 

### Assumptions:
- Input matches the spec exactly
- all characters in the string appear in the alphabet, characters not in the alphabet get value 0. 

# Question 1: empirical comparison
Ten input files were created with string lengths ranging from 25 to 1000, with |A| = |B| for each case. The alphabet used was 10 characters (a–j) with randomly assigned values. Runtime was measured by calling the solve function directly

![Runtime Graph](data/runtime_graph.png)





  