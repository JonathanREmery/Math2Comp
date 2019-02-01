To use this download math2comp.py put it in the same directory as the python file you want to use it in and type `import math2comp` then you can use it's convertToFunction() method by typing `math2comp.convertToFunction(function)` the converToFunction method takes a string in the form of a mathematical function for example I used a function I made to calculate how many months have passed between to dates for example 
`>>> import math2comp
>>> exec(math2comp.convertToFunction("M(m1, m2, y1, y2) = |12(y2-y1)+|m2-m1||"))
>>> M(1, 1, 2018, 2019)
12
>>> `

As you can see it worked surroung the math2comp.converToFunction in exec to actually make a python function out of it.
If you want to see what it will be executing you can print what math2comp.convertToFunction returns for example.
`>>> import math2comp
>>> print math2comp.convertToFunction("M(m1, m2, y1, y2) = |12(y2-y1)+|m2-m1||")
def M(m1, m2, y1, y2): return abs(12*(y2-y1)+abs(m2-m1))
>>> `

So as you can see it just converts a mathematical function to a python function.
