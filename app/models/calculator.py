from jinja2 import Template
import operator

op = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}

def calculations(a,b,operator):
    try:
        return op[operator](a,b)
    except KeyError:
        return('Invalid inputs')

a = int(input('Enter a first number : '))
b = int(input('Enter a second number : '))
operator = input('Enter a operator : ')
result = calculations(a,b,operator)
tm = Template('Calculated value {{result}}')
msg = tm.render(result=result)
print(msg)

def calculate(expression):
    print(expression)
    pass

# op = {
#        '+':lambda x,y:x+y,
#        '-':lambda x,y:x-y,
#        '/':lambda x,y:x/y,
#        '*':lambda x,y:x*y 
#        }
# print(op['+'](2,3))  
