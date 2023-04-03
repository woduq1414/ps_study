import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

n = int(input())

s = input()

arr = list(map(int, input().split()))

T = int(input())

arr_max_left = []
arr_max_right = []

arr_max = []
arr_max_sum = []
arr_group_idx = []

prev_char = None

group_idx = -1
cnt = 1
arr_max_sum_v = 0
for i in range(n):
    if s[i] != prev_char:

        arr_max_left.append(arr[i])
        if prev_char is not None:
            arr_max.append({"char": prev_char, "max": arr_max_left[i - 1], "index": i - 1})
            arr_max_sum_v += arr_max_left[i - 1]
            arr_max_sum += [arr_max_sum_v] * cnt

        cnt = 1

        group_idx += 1
    else:
        arr_max_left.append(max(arr[i], arr_max_left[i - 1]))
        cnt += 1

    arr_group_idx.append(group_idx)
    prev_char = s[i]

arr_max.append({"char": prev_char, "max": arr_max_left[n - 1], "index": n - 1})
arr_max_sum_v += arr_max_left[n - 1]
arr_max_sum += [arr_max_sum_v] * cnt



prev_char = None
for i in range(n):
    if s[n - 1 - i] != prev_char:
        arr_max_right.append(arr[n - 1 - i])
    else:
        arr_max_right.append(max(arr[n - 1 - i], arr_max_right[i - 1]))

    prev_char = s[n - 1 - i]

arr_max_right = arr_max_right[::-1]

# print(arr_max_left)
# print(arr_max_right)
# print(arr_max)
# print(arr_max_sum)

# print(arr_group_idx)

for _ in range(T):
    l, r = map(int, input().split())

    l -= 1
    r -= 1


    left_c_flag = False
    if arr_group_idx[l] != 0:
        if arr_max[arr_group_idx[l] - 1]["index"] + 1 == l:
            left_c_flag = True

    else:
        if l == 0:
            left_c_flag = True

    right_c_flag = False

    if arr_group_idx[r] != len(arr_max) - 1:
        if arr_max[arr_group_idx[r]]["index"] == r:
            right_c_flag = True

    else:
        if r == n - 1:
            right_c_flag = True


    result = 0

    if arr_group_idx[r] - 1 > arr_group_idx[l]:
        result += arr_max_sum[arr_max[arr_group_idx[r] - 1]["index"]] - arr_max_sum[arr_max[arr_group_idx[l]]["index"]]

    # print("@", arr_max_sum[arr_max[arr_group_idx[r] - 1]["index"]], arr_max_sum[arr_max[arr_group_idx[l]]["index"]])

    if arr_max[arr_group_idx[l]]["char"] != arr_max[arr_group_idx[r]]["char"]:
        winner = arr_max[arr_group_idx[l]]["char"]

        if left_c_flag:
            result += arr_max[arr_group_idx[l]]["max"]
        else:
            result += arr_max_right[l]
        if right_c_flag:
            result += arr_max[arr_group_idx[r]]["max"]
        else:
            result += arr_max_left[r]
        print(winner, result, sep=" ")
    else:
        if arr_group_idx[l] == arr_group_idx[r]:
            print("YK", 0, sep=" ")
            continue

        if left_c_flag:
            left_res = arr_max[arr_group_idx[l]]["max"]
        else:
            left_res = arr_max_right[l]

        if right_c_flag:
            right_res = arr_max[arr_group_idx[r]]["max"]
        else:
            right_res = arr_max_left[r]

        if left_res > right_res:
            winner = arr_max[arr_group_idx[l]]["char"]
            result += left_res
        elif left_res < right_res:
            winner = "Y" if arr_max[arr_group_idx[l]]["char"] == "K" else "K"
            result += right_res
        else:
            winner = "YK"
            result += left_res

        print(winner, result, sep=" ")