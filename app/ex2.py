lst = [1,2,3,4,5,6]

lst1 = []
for num in lst:
    if num % 2 != 0:
        lst1.append(num)
print(f'Implementing by method 1 - {lst1}')

def oddNum(num):
    if num % 2 != 0 :
        return num
lst2 = list(filter(oddNum,lst))
print(f'Implementing by method 2 - {lst2}')


lst3 = list(filter(lambda x:(x % 2 != 0),lst))
print(f'Efficient way - {lst3}') 