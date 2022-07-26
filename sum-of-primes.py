from math import sqrt;



def is_prime(x):
    if x <= 1:
        return False;
    
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False;
    
    return True;

sum = 0; nos = 0;
for i in range(3, 999, 2):
    if is_prime(i) == True:
        sum += i;
        nos += 1;
        
print(f'{sum}')
print(f'numer of prime nos = {nos}')