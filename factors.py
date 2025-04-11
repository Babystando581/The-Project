def factor(num):
    count = 0
    factors_arr = []
    for i in range(num + 1):
        if i == 0:
            ...
        else:
            if num % i == 0:
                factors_arr.append(i)
                count += 1
    return num, count, factors_arr


all_factors = []
top = [0, 0]
length = int(input())

full_range = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

while full_range >= 10 ** length:
    full_range = full_range // 10

for i in range(full_range):
    print(i)
    if factor(i)[1] > top[1]:
        top = factor(i)
        all_factors = factor(i)[2]

print(top)
