# Git_Expert
A funny python script to convert your string to GitHub contribution calendar
## Overview

GitHub takes the input of the string you are considering and gives you a csv file, including the days you have to contribute. 

In fact, GitExpert helps you to contribute to GitHub with a specific and regular schedule so that at the end of a certain period of time (for example, one year) your contribution map becomes the text of your choice.

**Input sample:**

>I Love GitHub

**Output sample:**

![alt text](https://github.com/Amirmoradi94/Git_Expert/blob/main/output.jpg)
---
## Run
You can parse the commands through command line argument.
> python3 main.py -input [insert your text] -mode ['o' or 'p']
```
parser.add_argument("-mode", "--mode", help = "Result (p: table preview -- o: csv output)", type=str)

parser.add_argument("-input", "--input", help = "Input text", type=str)
```

## Dependency
Before anything, make sure to have following libraries and packages.\
*numpy*\
*csv*\
*tkinter*
