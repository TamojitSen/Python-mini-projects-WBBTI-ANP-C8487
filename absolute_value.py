n = int(input("Enter a number: "))
if(n<0):
    abs = (-1)*n
    print(f'Number: {n}, Absolute Value: {abs}')
else:
    print(f'Number: {n}, Absolute Value: {n}')