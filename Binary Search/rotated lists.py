# You are given list of numbers, obtained by rotating a sorted list an unknown number of times.
# Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list.
# Your function should have the worst-case complexity of O(log N), where N is the length of the list.
# You can assume that all the numbers in the list are unique.

# Example: The list[5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list[0, 2, 3, 4, 5, 6, 9] 3 times.
# We define "rotating a list" as removing the last element of the list and adding it before the first element.
# E.g. rotating the list[3, 2, 4, 1] produces[1, 3, 2, 4].
# "Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].

from jovian.pythondsa import evaluate_test_cases


def count_rotations(nums) -> int:
    start: int = 0
    end: int = len(nums)-1

    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        return 0

    while start <= end:
        mid: int = (start+end)//2

        if nums[start] < nums[end]:
            return len(nums)

        if mid < end and nums[mid] > nums[mid+1]:
            return mid+1

        if mid > start and nums[mid] < nums[mid-1]:
            return mid

        if nums[mid] <= nums[start]:
            end = mid-1

        else:
            start = mid+1
    return -1


tests = []

tests.append({
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
})
# A list of size 8 rotated 5 times.
tests.append({
    'input': {
        'nums': [4, 5, 6, 7, 8, 1, 2, 3]
    },
    'output': 5
})
# A list that was rotated just once.
tests.append({
    'input': {
        'nums': [7, 3, 5]
    },
    'output': 1
})
# A list that was rotated n-1 times, where n is the size of the list.
tests.append({
    'input': {
        'nums': [2, 3, 4, 5, 6, 7, 8, 1]
    },
    'output': 7
})
# A list that was rotated n times, where n is the size of the list
tests.append({
    'input': {
        'nums': [1, 2, 3, 4, 5, 6, 7, 8]
    },
    'output': 8
})
# An empty list.
tests.append({
    'input': {
        'nums': []
    },
    'output': -1
})
# A list containing just one element.
tests.append({
    'input': {
        'nums': [6]
    },
    'output': 0
})

print(evaluate_test_cases(count_rotations, tests))
