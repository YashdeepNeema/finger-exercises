# A program that asks the user to enter an integer and prints 
# two integers: root and pwr, such that 1<pwr<6 and 
# root^pwr is equal to integer.

x = int(input('Enter an integer: '));

root = None; pwr = None;

for i in range(int(x/2)):
    for j in range(2, 6):
        if i**j == x:
            root = i;
            pwr = j;
if root != None and pwr != None:
    print(f'root: {root}')
    print(f'pwr: {pwr}')
else:
    print('no such pair of root and pwr exists.')
            