# Without Using Temporary Variable
x = input('Enter value of x : ')
y = input('Enter value of y : ')

x, y = y, x
print('Enter value of x :',x)
print('Enter value of y :',y)
