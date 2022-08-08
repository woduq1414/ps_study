import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

min_num, max_num = 10 ** 10, - 10 ** 10


def func(lis, output, c):
    global nums

    if c == 0:
        return

    for num in lis:
        temp = lis[:]
        output_new = output[:]

        output_new.append(num)
        if c == 1:

            result = nums[0]
            for i in range(len(output_new)):
                if output_new[i] == 0:
                    result += nums[i + 1]
                elif output_new[i] == 1:
                    result -= nums[i + 1]
                elif output_new[i] == 2:
                    result *= nums[i + 1]
                elif output_new[i] == 3:
                    if result < 0:
                        result = -(abs(-result // nums[i + 1]))
                    else:
                        result //= nums[i + 1]
            global max_num, min_num
            if result > max_num:
                max_num = result
            if result < min_num:
                min_num = result

        temp.remove(num)

        func(temp, output_new, c - 1)


func([0] * op[0] + [1] * op[1] + [2] * op[2] + [3] * op[3], [], n - 1)
print(max_num)
print(min_num)
