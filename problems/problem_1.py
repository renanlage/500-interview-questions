"""
Problem 1
Find pair with given sum in the array

Given an unsorted array of integers, find a pair with given sum in it.

http://www.techiedelight.com/find-pair-with-given-sum-array/
"""


def naive_pair_with_sum(arr, sum_):
    """
    Naive implementation checking sum for every pair in arr with O(n2) complexity.
    """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == sum_:
                return i, j


def ordered_pair_with_sum(arr, sum_):
    """
    Orders arr and loop it from start and end simultaneously with O(n.log(n)) complexity.
    """
    sorted_arr = sorted(arr)

    low = 0
    high = len(sorted_arr) - 1

    while low < high:
        current_sum = sorted_arr[low] + sorted_arr[high]

        if current_sum == sum_:
            return arr.index(sorted_arr[low]), arr.index(sorted_arr[high])
        elif current_sum < sum_:
            low += 1
        else:
            high -= 1


def hash_pair_with_sum(arr, sum_):
    """
    Loops array and check if difference from sum already exists in hash, if not add element to hash. O(n) complexity.
    """
    hash_ = {}

    for i in range(len(arr)):
        diff = sum_ - arr[i]
        if diff in hash_:
            return i, hash_[diff]

        hash_[arr[i]] = i
