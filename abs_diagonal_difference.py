import sys
import math

"""
Here We calculate the Absolute diagonal difference
in an nxn square matrix

@input
3
11 2 4
4 5 6
10 8 -12
@Output

15

"""

import sys
import math

def diag_diff():
    n = int(input().strip())
    a = []
    for a_i in range(n):
        a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
        a.append(a_t)

    ldsum=0
    rdsum=0
    for r in range(len(a)):
        row=a[r]
        ldsum+=row[r]
        rdsum+=row[(len(row)-1)-r]
    return int(math.fabs(ldsum-rdsum))
