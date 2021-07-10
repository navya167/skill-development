def recursive_total(lst):
    print(lst)
    total = 0
    for ele in lst:
        if type(ele) == type([]):
            # total = total + recursive_total(ele) // ex for recursive function 
            total = total + sum(ele)
        else:
            total = total + ele
        
    return total




print(recursive_total([1,2,[3,4],[5,6]]))