# Variables can be used to store data:
var = 3
# Variables can contain any type of data, such as strigns, ints, floats, bools, lists, tuples, sets, etc
var2 = 9
# You can print the variables:
print(var, var2)
# If you use the same name for an other variable, the previous variable will be overwritten:
var2 = 2

# you can use:
# += to add something to it:
var3 = "caca"
var3 += "pipi"
print(var3)
# /= to divide it:
var4 = 98
var4 /= 17
print(var4)

# *= to multiply it:
var5 = 4
var5 *= 5

# -= to subtract it.
var6 = 11
var6 -= 4

# You can typecast a variable:
intvar = 80
strvar = str(intvar)
print(type(strvar), type(intvar))
