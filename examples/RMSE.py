#!/usr/bin/env python3

# -------
# RMSE.py
# -------

import functools
import math
import sys
import time

print("RMSE.py")
print(sys.version)
print()

def sqre_diff (x, y) :
    return (x - y) ** 2

def rmse_while (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    s = len(a)
    i = 0
    v = 0
    while i != s :
        v += sqre_diff(a[i], p[i])
        i += 1
    return math.sqrt(v / s)

def rmse_for_zip_range (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    s = len(a)
    v = 0
    for i in range(s) :
        v += sqre_diff(a[i], p[i])
        i += 1
    return math.sqrt(v / s)

def rmse_for_zip (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    s = len(a)
    z = zip(a, p)
    v = 0
    for x, y in z :
        v += sqre_diff(x, y)
    return math.sqrt(v / s)

def rmse_reduce (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    s = len(a)
    z = zip(a, p)
    v = functools.reduce(lambda v, a : v + sqre_diff(a[0], a[1]), z, 0.0)
    return math.sqrt(v / s)

def rmse_sum_map (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    s = len(a)
    v = sum(map(sqre_diff, a, p))
    return math.sqrt(v / s)

def rmse_sum_list_zip (a, p) :
    """
    O(n) in space
    O(n) in time
    """
    s = len(a)
    z = zip(a, p)
    v = sum([sqre_diff(x, y) for x, y in z])
    return math.sqrt(v / s)

def rmse_sum_gen_zip (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    s = len(a)
    z = zip(a, p)
    v = sum((sqre_diff(x, y) for x, y in z))
    return math.sqrt(v / s)

def test (f) :
    print(f.__name__)
    assert(str(f((2, 3, 4), (2, 3, 4))) == "0.0")
    assert(str(f((2, 3, 4), (3, 4, 5))) == "1.0")
    assert(str(f((2, 3, 4), (4, 3, 2))) == "1.632993161855452")
    a = 1000000 * [1]
    p = 1000000 * [5]
    b = time.clock()
    assert(str(f(a, p)) == "4.0")
    e = time.clock()
    print("%5.3f" % ((e - b) * 1000), "milliseconds")
    print()

test(rmse_while)
test(rmse_for_zip_range)
test(rmse_for_zip)
test(rmse_reduce)
test(rmse_sum_map)
test(rmse_sum_list_zip)
test(rmse_sum_gen_zip)

print("Done.")

"""
RMSE.py
3.3.3 (default, Jan 19 2014, 10:13:09)
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.2.79)]

rmse_while
501.339 milliseconds

rmse_for_zip_range
497.844 milliseconds

rmse_for_zip
423.167 milliseconds

rmse_reduce
545.354 milliseconds

rmse_sum_map
430.414 milliseconds

rmse_sum_list_zip
383.953 milliseconds

rmse_sum_gen_zip
402.718 milliseconds

Done.
"""
