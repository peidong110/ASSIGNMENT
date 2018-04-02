/*
Consider the following function written in Python 3 (recalling that range(x, y), in
Python, refers to the sequence of values starting at x, counting up by 1s, and stopping
at y-1.
for a in range(1, n+1):
  for b in range(1, a+1):
    for c in range(1, b):
      foo()


If n has a value of 2000, how many times will the function foo() be called and how
many times will the function bar() be called? You must solve this problem using
Sigma notation (i.e., you must derive an expression that uses Sigma notation to specify
how many times each of these functions will be called, and then you must find a closed
form for this expression and evaluate for n = 2000). You must show all your work
*/
x = 0
def foo():
	global x 
	x += 1
	return str(x)
	
for i in range(1,2001):
	for j in range(1, i+1):
		for k in range(1,j):
			foo()
	val = i / 2000
	c = round(val,2) * 100
	print(str(c)+" %"+"    This is x :"+str(i) +"This is the current Number :"+ str(x))
	
