from typing import List
from math import prod
import numpy as np

N_COINS = 3
uint256 = int
int128 = int
A_PRECISION = 1

def _get_D(_xp: List[uint256], _amp: uint256) -> uint256:
    """
    D invariant calculation in non-overflowing integer operations
    iteratively
    A * sum(x_i) * n**n + D = A * D * n**n + D**(n+1) / (n**n * prod(x_i))
    Converging solution:
    D[j+1] = (A * n**n * sum(x_i) - D[j]**(n+1) / (n**n prod(x_i))) / (A * n**n - 1)
    """
    S: uint256 = 0
    Dprev: uint256 = 0

    for _x in _xp:
        S += _x
    if S == 0:
        return 0

    D: uint256 = S
    Ann: uint256 = _amp * N_COINS
    for _i in range(255):
        D_P: uint256 = D
        for _x in _xp:
            D_P = D_P * D / (_x * N_COINS)  # If division by 0, this will be borked: only withdrawal will work. And that is good
        Dprev = D
        D = (Ann * S + D_P * N_COINS) * D / ((Ann - 1) * D + (N_COINS + 1) * D_P)
        # print(Dprev, D)
        # Equality with the precision of 1
        if D > Dprev:
            if D - Dprev <= 1:
                return D
        else:
            if Dprev - D <= 1:
                return D
    # convergence typically occurs in 4 rounds or less, this should be unreachable!
    # if it does happen the pool is borked and LPs can withdraw via `remove_liquidity`
    raise Exception("Convergence not reached")


def test_D():
    amp = 2000
    xp = [100, 1000, 5000]
    n = 3
    d = _get_D(_xp = xp, _amp = amp)
    print(d)
    print(amp * sum(xp) * n**n + d)
    print(amp * d * n**n + d**(n+1) / (n**n * np.prod(xp)))
    ## the above 2 value should be close enough... the invariant



def _get_y(i: int128, j: int128, x: uint256, _xp: List[uint256], amp: int) -> uint256:
    """
    Calculate x[j] if one makes x[i] = x
    Done by solving quadratic equation iteratively.
    x_1**2 + x_1 * (sum' - (A*n**n - 1) * D / (A * n**n)) = D ** (n + 1) / (n ** (2 * n) * prod' * A)
    x_1**2 + b*x_1 = c
    x_1 = (x_1**2 + c) / (2*x_1 + b)
    """
    # x in the input is converted to the same price/precision

    assert i != j       # dev: same coin
    assert j >= 0       # dev: j below zero
    assert j < N_COINS  # dev: j above N_COINS

    # should be unreachable, but good for safety
    assert i >= 0
    assert i < N_COINS

    A: uint256 = amp
    D: uint256 = _get_D(_xp, A)
    Ann: uint256 = A * N_COINS
    c: uint256 = D
    S: uint256 = 0
    _x: uint256 = 0
    y_prev: uint256 = 0

    for _i in range(N_COINS):
        if _i == i:
            _x = x
        elif _i != j:
            _x = _xp[_i]
        else:
            continue
        S += _x
        c = c * D / (_x * N_COINS)
    c = c * D * A_PRECISION / (Ann * N_COINS)
    b: uint256 = S + D * A_PRECISION / Ann  # - D
    y: uint256 = D
    for _i in range(255):
        y_prev = y
        y = (y*y + c) / (2 * y + b - D)
        if abs(y - y_prev) <= 1:
            return y
    raise Exception("Convergence not reached")

def test_y():
    amp = 2000
    ii = 0
    jj = 1
    xx = 105
    xpxp = [100, 1000, 5000]
    d = _get_D(_xp = xpxp, _amp = amp)
    print(xpxp, d)
    yy = _get_y(ii, jj, xx, xpxp, amp)
    print(yy)
    new_xp = [xx, yy, 5000]
    d = _get_D(_xp = new_xp, _amp = amp)
    print(new_xp, d)

test_y()