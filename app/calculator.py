import operator
import re

op = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}

def calculations(a,operator,b):
    try:
        return op[operator](a,b)
    except KeyError:
        return('Invalid inputs3')

def calculate(expression):
    expression = ''.join(expression.split())  
    lst = re.split(r'(\d*\.?\d+)',expression)
    lst = list(filter(None, lst))
    # lst = [ele for ele in lst if ele.strip()]
    print(lst)
    if not lst[0].replace('.','',1).isnumeric():
        return 'Invalid input1'
    elif not lst[-1].replace('.','',1).isnumeric():
         return 'Invalid input2'
    else:
        for i in range(len(lst)): 
            if lst[i].replace('.','',1).isnumeric():
                lst[i] = float(lst[i])
        while(len(lst)>1):
            value = calculations(lst[0],lst[1],lst[2])
            new_lst = lst[3:]
            new_lst.insert(0,value)            
            lst = new_lst 
        return lst[0]  
