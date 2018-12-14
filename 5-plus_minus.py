import sys
from decimal import*

n = int(input().strip())

arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

negative, positive, zero = 0, 0, 0

for integer in arr:
    if(integer > 0):
        positive += 1
    elif(integer < 0):
        negative += 1
    else:
        zero += 1

fraction_of_positives = Decimal(positive) / Decimal(n)
fraction_of_positives_with_precision = format(fraction_of_positives, '.6f')
print(fraction_of_positives_with_precision)

fraction_of_negatives = Decimal(negative) / Decimal(n)
fraction_of_negatives_with_precision = format(fraction_of_negatives, '.6f')
print(fraction_of_negatives_with_precision)

fraction_of_zeros = Decimal(zero) / Decimal(n)
fraction_of_zeros_with_precision = format(fraction_of_zeros, '.6f')
print(fraction_of_zeros_with_precision)
