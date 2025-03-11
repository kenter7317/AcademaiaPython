from numpy.ma.core import multiply, add, subtract, divide
a= input()
b= input()
result = a+b
func_list = [multiply, add, subtract, divide]
print(result)
print(a, "+", b, "=", result)
