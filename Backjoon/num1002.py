# num1002.py

test_count = int(input())
for _ in range(test_count):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    sum_r2=(r1+r2)**2
    diff_r2=abs((r1-r2))**2


    dx = x1 - x2
    dy = y1 - y2
    d2 = (dx**2 + dy**2)


    if x1==x2 and y1==y2 and r1==r2:
        print(-1)

    elif d2 > sum_r2 or d2 < diff_r2 or (d2 == 0 and r1 != r2):
        print(0)

    elif d2==sum_r2 or d2==diff_r2:
        print(1)
    
    else: print(2)    