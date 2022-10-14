#1
'''test_list = []
for i in range(5):
    number = int(input(f'Enter number #{i + 1}: '))
    test_list += [number]
print(test_list)'''

#2
'''A = [1, 2, 3, 4, 5]
A.pop()
print(A)'''

#3

'''A = []
for i in range(10):
    number = int(input(f'Enter number #{i + 1}: '))
    A += [number]
print(f'List А: {A}')
N = int(input(f'Enter number N: '))
print(f'N in A = {A.count(N)} times')'''

#4

'''N = int(input('Enter number: '))
A = []
for i in range(N):
    number = int(input(f'Enter number #{i + 1}: '))
    A += [number]
print(f'List А: {A}')
A.reverse()
print(f'List A reverse sequence: {A}')'''

#5

'''A = []
C = []
for i in range(5):
    number = int(input(f'Enter number #{i + 1}: '))
    A += [number]
print(f'List A: {A}')
for n in A:
    if n > 5:
        C.append(n)
print(f'List C : {C}')'''

#6

'''N = int(input('Enter list number: '))
A = []
for i in range(N):
    number = int(input(f'Enter number #{i + 1}: '))
    A += [number]
print(f'List А: {A}')
mininum = A[0]
maxinum = A[0]
for n in A:
    if n < mininum:
        mininum = n
    if n > maxinum:
        maxinum = n
print(f'Minimum number = {mininum}')
print(f'Maximum number = {maxinum}')'''

#7

input_str=input("Enter text: ")
input_str=list(input_str)
for elem in list(input_str):
    if elem.isdigit():
        digit_elem=True
        break
    else:
        digit_elem=False
for elem in list(input_str):
    if not elem.isdigit():
        input_str.remove(elem)
if digit_elem==True:
    print(len(input_str))
