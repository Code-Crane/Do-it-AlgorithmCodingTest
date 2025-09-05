# num1003.py

zero_case = 0
one_case = 0

def fibonacci(n):
    global zero_case, one_case

    if n == 0:
        zero_case += 1
    elif n == 1:
        one_case += 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

test_count = int(input())

for _ in range(test_count):
    n = int(input())
    zero_case = 0  
    one_case = 0
    fibonacci(n)
    print(zero_case, one_case)
    
    