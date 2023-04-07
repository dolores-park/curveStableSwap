from typing import List
from math import prod
import numpy as np
from decimal import *
import math

N_COINS = 3
AMP = 2000
XP = [Decimal('166779052483518040606936781'), Decimal('176436300459666993630412800'), Decimal('90388358930128992036978688')]
D = Decimal('433593946932329643560529432.8771858505794947204518883024152572372')
getcontext().prec = 64

def _get_y(i, j, x):

    # print("current XP and D: ")
    # print(XP, D)

    assert i != j       # dev: same coin
    assert j >= 0       # dev: j below zero
    assert j < N_COINS  # dev: j above N_COINS

    # should be unreachable, but good for safety
    assert i >= 0
    assert i < N_COINS

    A = AMP
    Ann = A * N_COINS
    c = D
    S = 0
    _x = 0
    y_prev = 0

    for _i in range(N_COINS):
        if _i == i:
            _x = x
        elif _i != j:
            _x = XP[_i]
        else:
            continue
        S += _x
        c = c * D / (_x * N_COINS)
    c = c * D / (Ann * N_COINS)
    b = S + D / Ann  - D # - D

    print(-b, b)
    
    y1 = (-b + (b**2 + 4*c).sqrt()) / 2
    y2 = (-b - (b**2 + 4*c).sqrt()) / 2
    print(y1)
    print(y2)

yyy = _get_y(1, 0, Decimal('176436300459667993630412800'))
print(yyy)