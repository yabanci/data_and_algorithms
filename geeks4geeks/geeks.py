# Given an unsorted array of non-negative integers, find a continuous sub-array which adds to a given number.


def subarray_for_sum(arr, s):
    low = high = 0
    temp_sum = arr[0]
    while True:
        if temp_sum == s:
            return low + 1, high + 1
        elif temp_sum < s:
            if high == len(arr) - 1:
                return -1
            high += 1
            temp_sum += arr[high]
        else:
            temp_sum -= arr[low]
            low += 1


# def main():
#     test_count = int(input())
#     results = []
#     for _ in range(test_count):
#         _, s = [int(x) for x in input().split()]
#         arr = [int(x) for x in input().split()]
#         res = subarray_for_sum(arr, s)
#         results.append(res)
#     for result in results:
#         if result != -1:
#             print(*result, sep=' ')
#         else:
#             print(result)


# You are given an array A containing 2*N+2 positive numbers, out of which 2*N numbers exist in pairs whereas the
# other two number occur exactly once and are distinct. You need to find the other two numbers and print them in
# ascending order.

def find_distinct_nums(arr):
    arr_set = set()
    for i in arr:
        if i not in arr_set:
            arr_set.add(i)
        else:
            arr_set.remove(i)
    return sorted(list(arr_set))


# def main():
#     test_count = int(input())
#     results = []
#     for _ in range(test_count):
#         _ = [int(x) for x in input().split()]
#         arr = [int(x) for x in input().split()]
#         res = find_distinct_nums(arr)
#         results.append(res)
#     for result in results:
#         print(*result, sep=' ')


def check_string_pattern(s, p):
    current = prev = p[0]
    current_ind = 0
    not_ok = set(p)
    not_ok.remove(current)
    for t in s:
        if t == current:
            prev = current
            if current_ind + 1 < len(p):
                current_ind += 1
                current = p[current_ind]
            not_ok = set(p)
            not_ok.remove(current)
            if prev in not_ok:
                not_ok.remove(prev)
        elif t in not_ok:
            return False
    return True


def main():
    tests = [("engineers rock", "er"),
             ("engineers rock", "egr"),
             ("engineers rock", "gsr")]
    for s, p in tests:
        print(check_string_pattern(s, p))


if __name__ == '__main__':
    main()
