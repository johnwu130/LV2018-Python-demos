"""
This is a very basic Python example.  We can define a function in Python for LabVIEW to call
using the LabVIEW 2018 Python node.  Here we have a few functions, "add" and "square".  From LabVIEW,
we give 2 floating point numbers 'a' and 'b'.  The result 'c' is returned to LabVIEW.
"""


def add(a,b): 
	
	c = a+b;
	
	return c;
	
	
	
	
	
def square(a,b):
	
	c=a**2+b**2;
	
	return c;
	
	
	
	
	