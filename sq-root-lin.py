#a program to find square root of a positive integer using exhaustive enumeration.

x = int(input('Enter an integer: '));
e = 0.01;
step = e**2;
num_guesses = 0;
ans = 0.0

while ((abs(ans**2 - x) >= e) and (ans <= x)):
    ans += step;
    num_guesses += 1;

print('number of guesses: ', num_guesses);
if (abs(ans**2) - x >= e):
    print('failed on sqrt of ', x);
else:
    print(ans, 'is close to the sqrt of ', x);
