#To test whether an integer greater than 2 is prime or not. 
#If not prime then prnts the largest divisor.
# concept
# (samllerst-divisor)*(largest-divisor) = number

x = int(input('Enter an integer greater than 2: '));

smallest_divisor = None;

y = int(x/2) + 1;

for guess in range(2, y):
    if x % guess == 0:
        smallest_divisor = guess;
        break;
        
if smallest_divisor != None:
    l_d = int(x/ smallest_divisor);
    print(f'the largest divisor of {x} is {l_d}');
else:
    print(f'{x} is a prime number.')