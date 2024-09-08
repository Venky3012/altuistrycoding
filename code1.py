def is_step(num):
    if num < 10:
        return True
    pre_dig = num % 10
    num //= 10

    while num > 0:
        cur_dig = num % 10
        if abs(cur_dig - pre_dig) != 1:
            return False
        pre_dig = cur_dig
        num //= 10

    return True

def find_stepping_numbers(n, m):
    step = []
    for num in range(n, m + 1):
        if is_step(num):
            step.append(num)
    
    return step

n, m = map(int, input().split())

res = find_stepping_numbers(n, m)


print(res)
