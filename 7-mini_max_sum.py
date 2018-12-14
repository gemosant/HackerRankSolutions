#!/bin/python3
import sys

def duplicate_array(arr):
    duplicate = []

    for i in range(0, len(arr)):
        duplicate.append(arr[i])

    return duplicate

arr = list(map(int, input().strip().split(' ')))

mini = min(arr)
maxi = max(arr)

max_sum = -9223372036854775808
min_sum = 9223372036854775807

for i in range(0, len(arr)):
    sum = 0
    aux_arr = duplicate_array(arr)
    aux_arr.remove(aux_arr[i])
    for num in aux_arr:
        sum = sum + num

    if (sum > max_sum):
        max_sum = sum
    if (sum < min_sum):
        min_sum = sum

print(min_sum, max_sum)
