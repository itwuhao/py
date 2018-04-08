while True:
    name=input('Enter name:')
    if name =='stop':
        break
    age=input('Enter age:')
    print('hello',name,'->',int(age) **2)