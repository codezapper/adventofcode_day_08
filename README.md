# Solution for Advent of code, day 08

For a description of the problem see: https://adventofcode.com/2018/day/8

## Requirements

### Dependencies

- To run the program itself no external dependency is needed
- To run the tests with the `pytest` command, the `unittest` library is needed

### Input

- The program assumes that an external file named `input.txt` is present. If it is not, a message will be displayed.
- The format of the input file is assumed to be a single line containing non-negative integers, separated by a space.
- Only the first line of the file is considered, the rest is not taken into consideration.

## Execution

- To program can be run with `python3 meta_sum.py`.
- Using the provided `input.txt` file, the result is `38722`, which the site accepts as a correct answer.

## Description of the algorithm

- The program uses a recursive function to progressively extract the nodes from the tree, removing them in the process, starting with the nodes that have no children.
- This mutates the original input, but provides faster processing time because of having less amount of data to process at each step. It's obviously possible to call the function by passing a copy of the original data.
