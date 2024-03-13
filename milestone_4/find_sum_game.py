# Complexity O(n^2)
def find_sum(target: int, li: list) -> tuple:
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if li[i] + li[j] == target:
                return li[i], li[j]


# Complexity O(n)
def find_sum_fast(target: int, li: list) -> tuple:
    while len(li):
        i = li.pop(0)
        if target - i in li:
            return i, target - i


print(find_sum(9, [1, 2, 3, 4, 5]))
print(find_sum_fast(4, [1, 2, 3, 4, 5]))
