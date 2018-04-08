def calc(number):
    sum = 0
    for n in number:
        sum = sum + n*n
    return sum 
print(calc([1,2,3]))