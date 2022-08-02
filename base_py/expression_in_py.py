from asyncio import constants


# constants 

print(123)

print('T')

print("Hello constants")

# constants in py are number letter or string 
# which are fixed values

# constants string are surround in the ' or "


# variable in py 

a = 5
print(a+5)

a = a * 2 *( a - 1)

print( a )


# when we string operators together Py must know which one to do
# first which called "operator precedence"

# a = 1 + 2 * 3 - 4 / 5 ** 2
# a = 1 + ( 2 * 3 ) - ( 4 / ( 5 ** 2 ) )

# the about statements a the same order 

# Operator Precedence rules (top to bottom)

# Parenthesis ()
# Power **
# Multiplication * /
# Addition +  - 
# Left to right  a + b + c 

# rei

x = 1 + 2 ** 3 / 4 * 5 
print ( x ) 


# Note

# Remember the top to bottom rule
# When write code - use parenthesis
# Keep the mathematical expressions simple enough - make its easy to understand
# Break long series of mathmatical operations up to make them more clear

# DATA TYPE IN PY

print( type(x) ) #Ask py type of x 

# Type conversions in Py

# Put int and float in an expression the int type is 'implicitly converted' into float

# U also control this with the built-in func int() or float()

print ( float( 99 ) + 0.5)

print ( type (50 - int(1.5)) )

# in python 3 the result of division is auto convert to float type 

# string conversion 

str = '123'
print ( type( int(str)))

# if the str contain the letter <> numberic the line 76 will return error 


# input statement

nam = input('Your name ? ')

print("Hello ", nam)

