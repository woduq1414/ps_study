import sys



input = sys.stdin.readline


# 소인수분해
def divide(num):
    if num == 1:
        return {}

    result = {}

    divider = 2
    while divider * divider <= num:

        if num % divider == 0:
            num //= divider

            if divider in result:
                result[divider] += 1
            else:
                result[divider] = 1

        else:

            divider += 1

    if num in result:
        result[num] += 1
    else:
        result[num] = 1



    return result

n = int(input())
lis = list(map(int, input().split()))

final_result = {}
for num in lis:
    res = divide(num)

    for k, v in res.items():
        if k in final_result:
            final_result[k] = max(final_result[k], v)
        else:
            final_result[k] = v

total_product = 1
for k, v in final_result.items():
    total_product *= k ** v

print(total_product * 2)