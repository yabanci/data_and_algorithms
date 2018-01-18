def two_sum(nums, target):
    """
    :type strs: (list[int], int)
    :rtype: list[int]
    """
    seen = {}
    for ind, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], ind]
        seen[num] = ind


def reverse_integer(x):
    """
    :type strs: int
    :rtype: int
    """
    digits = []
    is_positive = True if x > 0 else False
    x = -1 * x if not is_positive else x
    while x != 0:
        digits.append(x % 10)
        x = x // 10
    exps = [len(digits) - 1 - ind for ind, _ in enumerate(digits)]
    exps = [10 ** i for i in exps]
    result = sum([a * b for a,b in zip(digits, exps)])
    result = -1 * result if not is_positive else result
    if result < -(2 ** 31) or result > (2 ** 31 - 1):
        return 0
    return result


def get_int_length(x):
    """For positive only"""
    """
    :type strs: int
    :rtype: int
    """
    if x < 0:
        raise ValueError("Negative numbers are not accepted!")
    count = 1
    while x // 10 ** count > 0:
        count += 1
    return count


def palindrome_integer(x):
    """Negatives cannot be palindrome, did not use str to keep O(1) space"""
    """
    :type strs: int
    :rtype: bool
    """
    if x < 0:
        return False
    tens = get_int_length(x) - 1
    if tens == 0:
        return True
    start = 0
    end = tens
    while start < end:
        front = (x // 10 ** (tens - start)) % 10
        back = (x // 10 ** (tens - end)) % 10
        if front != back:
            return False
        start += 1
        end -= 1
    return True


def roman_to_int(x):
    """
    :type strs: str
    :rtype: int
    """
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    negs = {'I': {'V', 'X'}, 'X': {'L', 'C'}, 'C': {'D', 'M'}}
    res = 0
    for ind, ch in enumerate(x):
        val = roman_map[ch]
        if ch in negs and ind + 1 < len(x) and x[ind + 1] in negs[ch]:
            val *= -1
        res += val
    return res


def longest_common_prefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    """Assume all the strs have a common prefix otherwise return empty string"""
    if not strs:
        return ''
    prefix = strs[0]
    for s in strs:
        ind = 0
        while ind < len(s) and ind < len(prefix) and s[ind] == prefix[ind]:
            ind += 1
        prefix = prefix[:ind]
    return prefix


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    co = 0
    r = ListNode(0)
    temp = r
    prev = r
    while not (l1 is None and l2 is None):
        d1 = l1.val if l1 else 0
        d2 = l2.val if l2 else 0
        total = d1 + d2 + co
        s = total % 10
        co = total // 10
        temp.val = s
        next_node = ListNode(0)
        temp.next = next_node
        prev = temp
        temp = next_node
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    temp.val = co
    prev.next = None if not co else temp
    return r


def valid_parenthesis(s):
    """
    :type s: str
    :rtype: bool
    """
    parens = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in pairs and (not parens or pairs[ch] != parens[-1]):
            return False
        elif ch in pairs and pairs[ch] == parens[-1]:
            parens.pop()
        else:
            parens.append(ch)
    if parens:
        return False
    return True


def remove_duplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 1:
        return len(nums)
    prev = nums[0]
    prev_pt = 0
    for i, num in enumerate(nums[1:], 1):
        if num != prev:
            prev_pt += 1
            nums[prev_pt] = num
            prev = num
    return prev_pt + 1, nums


def length_of_longest_non_repeating_substring(s):
    """
    :type s: str
    :rtype: int
    """
    used_chars = {}
    head = max_len = 0
    for i, ch in enumerate(s):
        if ch in used_chars and head <= used_chars[ch]:
            head = used_chars[ch] + 1
        else:
            max_len = max(max_len, i - head + 1)
        used_chars[ch] = i
    return max_len


pals = set([''])
def is_pal(s):
    if len(s) <= 1:
        pals.add(s)
        return True
    if len(s) == 2 and s[0] == s[1]:
        pals.add(s)
        return True
    if s[0] == s[-1] and (s[1:-1] in pals or is_pal(s[1:-1])):
        pals.add(s)
        return True
    return False


def longest_palindromic_substring(s):
    """
    :type s: str
    :rtype: str
    """
    max_pal = ''
    for pal_len in range(1, len(s) + 1):
        for i in range(len(s) - pal_len + 1):
            if s[i:i + pal_len] != max_pal and is_pal(s[i:i + pal_len]):
                max_pal = s[i:i + pal_len]
    return max_pal


def plus_one(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    digits = [str(x) for x in digits]
    num = int(''.join(digits))
    num += 1
    return [int(x) for x in str(num)]


def is_power_of_two(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        return False
    if n == 1:
        return True
    while n % 2 == 0:
        n = n / 2
        if n == 1:
            return True
    return False


def is_power_of_three(n):
    """
    :type n: int
    :rtype: bool
    """
    if n < 1:
        return False
    while n % 3 == 0:
        n = n / 3
    return n == 1


def reverse_vowels(s):
    """
    :type s: str
    :rtype: str
    """
    vows = 'aeiouAEIOU'
    evows = []
    for ch in s:
        if ch in vows:
            evows.append(ch)
    new_chars = []
    for ch in s:
        if ch in vows:
            new_chars.append(evows.pop())
        else:
            new_chars.append(ch)
    return ''.join(new_chars)

GTARGET = 1
def guess(num):
    if num == GTARGET:
        return 0
    elif num < GTARGET:
        return 1
    else:
        return -1


def guess_number(n):
    """
    :type n: int
    :rtype: int
    """
    if guess(n) == 0:
        return n
    min_g = 1
    max_g = n
    g = (n + 1) // 2
    resp = guess(g)
    while resp != 0:
        if resp == 1:
            min_g = max(min_g, g)
            g = (g + max_g) // 2
        elif resp == -1:
            max_g = min(max_g, g)
            g = (g + min_g) // 2
        resp = guess(g)
    return g


def first_uniq_char(s):
    """
    :type s: str
    :rtype: int
    """
    chars = {}  # {ch: [count, ind]}
    for ind, ch in enumerate(s):
        if ch in chars:
            chars[ch][0] += 1
        else:
            chars[ch] = [1, ind]
    mind = len(s)
    for k, v in chars.items():
        if v[0] == 1 and v[1] < mind:
            mind = v[1]
    if mind == len(s):
        return -1
    return mind


def find_missing_numbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    arr = [0] * len(nums)
    for num in nums:
        arr[num - 1] = 1
    res = []
    for ind, num in enumerate(arr):
        if num == 0:
            res.append(ind + 1)
    return res


def island_perimeter(grid):
    per = 0
    for rind, row in enumerate(grid):
        for cind, col in enumerate(row):
            if col == 1:
                per += 4
                if rind - 1 >= 0 and grid[rind - 1][cind] == 1:
                    per -= 1
                if rind + 1 < len(grid) and grid[rind + 1][cind] == 1:
                    per -= 1
                if cind - 1 >= 0 and row[cind - 1] == 1:
                    per -= 1
                if cind + 1 < len(row) and row[cind + 1] == 1:
                    per -= 1
    return per


def judge_circle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    UD = 0
    LR = 0
    for ch in moves:
        if ch == 'U':
            UD += 1
        elif ch == 'D':
            UD -= 1
        elif ch == 'R':
            LR += 1
        elif ch == 'L':
            LR -= 1
    return (UD, LR) == (0, 0)
    # one liner:
    # return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')


def anagram_mapping1(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: List[int]
    """
    P = []
    for val in A:
        P.append(B.index(val))
    return P


def anagram_mapping2(A, B):
    Bmap = {}
    for ind, val in enumerate(B):
        Bmap[val] = ind
    P = []
    for val in A:
        P.append(Bmap[val])
    return P


def letter_combinations(digits):
    digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if not digits:
        return []
    if len(digits) == 1:
        return list(digit_map[digits[0]])
    sub_letters = letter_combinations(digits[1:])
    res = []
    for ch in digit_map[digits[0]]:
        for comb in sub_letters:
            res.append(ch + comb)
    return res


def generate_parenthesis(n):
    if n == 0:
        return []
    if n == 1:
        return ['()']
    prev = generate_parenthesis(n-1)
    new_set = set()
    for paren in prev:
        new_set.add('()' + paren)
        new_set.add(paren + '()')
        new_set.add('(' + paren + ')')
    return list(new_set)


def my_pow(x, n):
    if n == 0:
        return 1
    res = 1
    for i in range(n):
        res *= x
    return res


def get_perms(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    perms = get_perms(nums[1:])
    res = []
    for perm in perms:
        for i in range(len(perm) + 1):
            new_perm = perm[:]
            new_perm.insert(i, nums[0])
            res.append(new_perm)
    return res


def next_permutation_full_brute(nums):
    unsorted_perms = get_perms(nums)
    all_perms_int = [int(''.join([str(x) for x in perm])) for perm in unsorted_perms]
    deduped = list(set(all_perms_int))
    deduped.sort()
    current = int(''.join([str(x) for x in nums]))
    c = deduped.index(current)
    if c == len(deduped) - 1:
        return deduped[0]
    return deduped[c + 1]


def next_permutation_in_place(nums):
    
