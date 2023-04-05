from web3 import Web3
import json
import asyncio
import threading
from decimal import *
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/85904b7115794ecfabbd00f61782cf62'))

contract_address = '0xbEbc44782C7dB0a1A60Cb6fe97d0b483032FF1C7'
contract_abi = json.loads(
    '[{"name":"TokenExchange","inputs":[{"type":"address","name":"buyer","indexed":true},{"type":"int128","name":"sold_id","indexed":false},{"type":"uint256","name":"tokens_sold","indexed":false},{"type":"int128","name":"bought_id","indexed":false},{"type":"uint256","name":"tokens_bought","indexed":false}],"anonymous":false,"type":"event"},{"name":"AddLiquidity","inputs":[{"type":"address","name":"provider","indexed":true},{"type":"uint256[3]","name":"token_amounts","indexed":false},{"type":"uint256[3]","name":"fees","indexed":false},{"type":"uint256","name":"invariant","indexed":false},{"type":"uint256","name":"token_supply","indexed":false}],"anonymous":false,"type":"event"},{"name":"RemoveLiquidity","inputs":[{"type":"address","name":"provider","indexed":true},{"type":"uint256[3]","name":"token_amounts","indexed":false},{"type":"uint256[3]","name":"fees","indexed":false},{"type":"uint256","name":"token_supply","indexed":false}],"anonymous":false,"type":"event"},{"name":"RemoveLiquidityOne","inputs":[{"type":"address","name":"provider","indexed":true},{"type":"uint256","name":"token_amount","indexed":false},{"type":"uint256","name":"coin_amount","indexed":false}],"anonymous":false,"type":"event"},{"name":"RemoveLiquidityImbalance","inputs":[{"type":"address","name":"provider","indexed":true},{"type":"uint256[3]","name":"token_amounts","indexed":false},{"type":"uint256[3]","name":"fees","indexed":false},{"type":"uint256","name":"invariant","indexed":false},{"type":"uint256","name":"token_supply","indexed":false}],"anonymous":false,"type":"event"},{"name":"CommitNewAdmin","inputs":[{"type":"uint256","name":"deadline","indexed":true},{"type":"address","name":"admin","indexed":true}],"anonymous":false,"type":"event"},{"name":"NewAdmin","inputs":[{"type":"address","name":"admin","indexed":true}],"anonymous":false,"type":"event"},{"name":"CommitNewFee","inputs":[{"type":"uint256","name":"deadline","indexed":true},{"type":"uint256","name":"fee","indexed":false},{"type":"uint256","name":"admin_fee","indexed":false}],"anonymous":false,"type":"event"},{"name":"NewFee","inputs":[{"type":"uint256","name":"fee","indexed":false},{"type":"uint256","name":"admin_fee","indexed":false}],"anonymous":false,"type":"event"},{"name":"RampA","inputs":[{"type":"uint256","name":"old_A","indexed":false},{"type":"uint256","name":"new_A","indexed":false},{"type":"uint256","name":"initial_time","indexed":false},{"type":"uint256","name":"future_time","indexed":false}],"anonymous":false,"type":"event"},{"name":"StopRampA","inputs":[{"type":"uint256","name":"A","indexed":false},{"type":"uint256","name":"t","indexed":false}],"anonymous":false,"type":"event"},{"outputs":[],"inputs":[{"type":"address","name":"_owner"},{"type":"address[3]","name":"_coins"},{"type":"address","name":"_pool_token"},{"type":"uint256","name":"_A"},{"type":"uint256","name":"_fee"},{"type":"uint256","name":"_admin_fee"}],"stateMutability":"nonpayable","type":"constructor"},{"name":"A","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":5227},{"name":"get_virtual_price","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":1133537},{"name":"calc_token_amount","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"uint256[3]","name":"amounts"},{"type":"bool","name":"deposit"}],"stateMutability":"view","type":"function","gas":4508776},{"name":"add_liquidity","outputs":[],"inputs":[{"type":"uint256[3]","name":"amounts"},{"type":"uint256","name":"min_mint_amount"}],"stateMutability":"nonpayable","type":"function","gas":6954858},{"name":"get_dy","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"int128","name":"i"},{"type":"int128","name":"j"},{"type":"uint256","name":"dx"}],"stateMutability":"view","type":"function","gas":2673791},{"name":"get_dy_underlying","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"int128","name":"i"},{"type":"int128","name":"j"},{"type":"uint256","name":"dx"}],"stateMutability":"view","type":"function","gas":2673474},{"name":"exchange","outputs":[],"inputs":[{"type":"int128","name":"i"},{"type":"int128","name":"j"},{"type":"uint256","name":"dx"},{"type":"uint256","name":"min_dy"}],"stateMutability":"nonpayable","type":"function","gas":2818066},{"name":"remove_liquidity","outputs":[],"inputs":[{"type":"uint256","name":"_amount"},{"type":"uint256[3]","name":"min_amounts"}],"stateMutability":"nonpayable","type":"function","gas":192846},{"name":"remove_liquidity_imbalance","outputs":[],"inputs":[{"type":"uint256[3]","name":"amounts"},{"type":"uint256","name":"max_burn_amount"}],"stateMutability":"nonpayable","type":"function","gas":6951851},{"name":"calc_withdraw_one_coin","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"uint256","name":"_token_amount"},{"type":"int128","name":"i"}],"stateMutability":"view","type":"function","gas":1102},{"name":"remove_liquidity_one_coin","outputs":[],"inputs":[{"type":"uint256","name":"_token_amount"},{"type":"int128","name":"i"},{"type":"uint256","name":"min_amount"}],"stateMutability":"nonpayable","type":"function","gas":4025523},{"name":"ramp_A","outputs":[],"inputs":[{"type":"uint256","name":"_future_A"},{"type":"uint256","name":"_future_time"}],"stateMutability":"nonpayable","type":"function","gas":151919},{"name":"stop_ramp_A","outputs":[],"inputs":[],"stateMutability":"nonpayable","type":"function","gas":148637},{"name":"commit_new_fee","outputs":[],"inputs":[{"type":"uint256","name":"new_fee"},{"type":"uint256","name":"new_admin_fee"}],"stateMutability":"nonpayable","type":"function","gas":110461},{"name":"apply_new_fee","outputs":[],"inputs":[],"stateMutability":"nonpayable","type":"function","gas":97242},{"name":"revert_new_parameters","outputs":[],"inputs":[],"stateMutability":"nonpayable","type":"function","gas":21895},{"name":"commit_transfer_ownership","outputs":[],"inputs":[{"type":"address","name":"_owner"}],"stateMutability":"nonpayable","type":"function","gas":74572},{"name":"apply_transfer_ownership","outputs":[],"inputs":[],"stateMutability":"nonpayable","type":"function","gas":60710},{"name":"revert_transfer_ownership","outputs":[],"inputs":[],"stateMutability":"nonpayable","type":"function","gas":21985},{"name":"admin_balances","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"uint256","name":"i"}],"stateMutability":"view","type":"function","gas":3481},{"name":"withdraw_admin_fees","outputs":[],"inputs":[],"stateMutability":"nonpayable","type":"function","gas":21502},{"name":"donate_admin_fees","outputs":[],"inputs":[],"stateMutability":"nonpayable","type":"function","gas":111389},{"name":"kill_me","outputs":[],"inputs":[],"stateMutability":"nonpayable","type":"function","gas":37998},{"name":"unkill_me","outputs":[],"inputs":[],"stateMutability":"nonpayable","type":"function","gas":22135},{"name":"coins","outputs":[{"type":"address","name":""}],"inputs":[{"type":"uint256","name":"arg0"}],"stateMutability":"view","type":"function","gas":2220},{"name":"balances","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"uint256","name":"arg0"}],"stateMutability":"view","type":"function","gas":2250},{"name":"fee","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2171},{"name":"admin_fee","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2201},{"name":"owner","outputs":[{"type":"address","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2231},{"name":"initial_A","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2261},{"name":"future_A","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2291},{"name":"initial_A_time","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2321},{"name":"future_A_time","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2351},{"name":"admin_actions_deadline","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2381},{"name":"transfer_ownership_deadline","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2411},{"name":"future_fee","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2441},{"name":"future_admin_fee","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2471},{"name":"future_owner","outputs":[{"type":"address","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2501}]')

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

curve_token_contract_address = '0x6c3F90f043a72FA612cbac8115EE7e52BDe6E490'
curve_token_contract_abi = json.loads(
    '[{"name":"Transfer","inputs":[{"type":"address","name":"_from","indexed":true},{"type":"address","name":"_to","indexed":true},{"type":"uint256","name":"_value","indexed":false}],"anonymous":false,"type":"event"},{"name":"Approval","inputs":[{"type":"address","name":"_owner","indexed":true},{"type":"address","name":"_spender","indexed":true},{"type":"uint256","name":"_value","indexed":false}],"anonymous":false,"type":"event"},{"outputs":[],"inputs":[{"type":"string","name":"_name"},{"type":"string","name":"_symbol"},{"type":"uint256","name":"_decimals"},{"type":"uint256","name":"_supply"}],"stateMutability":"nonpayable","type":"constructor"},{"name":"set_minter","outputs":[],"inputs":[{"type":"address","name":"_minter"}],"stateMutability":"nonpayable","type":"function","gas":36247},{"name":"set_name","outputs":[],"inputs":[{"type":"string","name":"_name"},{"type":"string","name":"_symbol"}],"stateMutability":"nonpayable","type":"function","gas":178069},{"name":"totalSupply","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":1211},{"name":"allowance","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"address","name":"_owner"},{"type":"address","name":"_spender"}],"stateMutability":"view","type":"function","gas":1549},{"name":"transfer","outputs":[{"type":"bool","name":""}],"inputs":[{"type":"address","name":"_to"},{"type":"uint256","name":"_value"}],"stateMutability":"nonpayable","type":"function","gas":74832},{"name":"transferFrom","outputs":[{"type":"bool","name":""}],"inputs":[{"type":"address","name":"_from"},{"type":"address","name":"_to"},{"type":"uint256","name":"_value"}],"stateMutability":"nonpayable","type":"function","gas":111983},{"name":"approve","outputs":[{"type":"bool","name":""}],"inputs":[{"type":"address","name":"_spender"},{"type":"uint256","name":"_value"}],"stateMutability":"nonpayable","type":"function","gas":39078},{"name":"mint","outputs":[{"type":"bool","name":""}],"inputs":[{"type":"address","name":"_to"},{"type":"uint256","name":"_value"}],"stateMutability":"nonpayable","type":"function","gas":75808},{"name":"burnFrom","outputs":[{"type":"bool","name":""}],"inputs":[{"type":"address","name":"_to"},{"type":"uint256","name":"_value"}],"stateMutability":"nonpayable","type":"function","gas":75826},{"name":"name","outputs":[{"type":"string","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":7823},{"name":"symbol","outputs":[{"type":"string","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":6876},{"name":"decimals","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":1481},{"name":"balanceOf","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"address","name":"arg0"}],"stateMutability":"view","type":"function","gas":1665}]'
)

contract_curve = w3.eth.contract(address=curve_token_contract_address, abi=curve_token_contract_abi)


POLLING_INTERVAL = 10
N_COINS = 3
FEE = 1000000 / 10**10 ## hardcoded for now
AMP = 2000 ## hardcoded for now
DAI_multiplier = 1e12
PRECISION = Decimal(1e18)

## [DAI, USDC, USDT], in-order
XP = [
    Decimal(contract.caller().balances(0)),
    Decimal(contract.caller().balances(1) * DAI_multiplier),
    Decimal(contract.caller().balances(2) * DAI_multiplier)]

getcontext().prec = 64

CURRENT_EVENT = None

def _get_D():
    global XP

    S = 0
    Dprev = 0

    for _x in XP:
        S += _x
    if S == 0:
        return 0

    D = S
    Ann = AMP * N_COINS
    for _i in range(255):
        D_P = D
        for _x in XP:
            D_P = D_P * D / (_x * N_COINS)
        Dprev = D
        D = (Ann * S + D_P * N_COINS) * D / ((Ann - 1) * D + (N_COINS + 1) * D_P)
        if D > Dprev:
            if D - Dprev <= 1:
                return D
        else:
            if Dprev - D <= 1:
                return D
    raise Exception("Convergence not reached")

D = _get_D()

def _get_y(i, j, x):

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
    b = S + D / Ann  # - D
    y = D
    for _i in range(255):
        y_prev = y
        y = (y*y + c) / (2 * y + b - D)
        if abs(y - y_prev) <= 1:
            return y
    raise Exception("Convergence not reached")

def handle_event(event):
    global CURRENT_EVENT, D, XP

    CURRENT_EVENT = event
    print("Server received an event: ... ")
    print(event)

    ## recalculate D
    D = _get_D()
    ## recalculate XP
    XP = [
        Decimal(contract.caller().balances(0)),
        Decimal(contract.caller().balances(1) * DAI_multiplier),
        Decimal(contract.caller().balances(2) * DAI_multiplier)]

async def log_loop(event_filter, poll_interval):
    while True:
        for PairCreated in event_filter.get_new_entries():
            handle_event(PairCreated)
        await asyncio.sleep(poll_interval)

def loop_in_thread(loop):
    global CURRENT_EVENT
    event_filters = [contract.events.TokenExchange.create_filter(fromBlock='latest'),
                    contract.events.AddLiquidity.create_filter(fromBlock='latest'),
                    contract.events.RemoveLiquidity.create_filter(fromBlock='latest'),
                    contract.events.RemoveLiquidityImbalance.create_filter(fromBlock='latest'),
                    contract.events.RemoveLiquidityOne.create_filter(fromBlock='latest')]

    asyncio.set_event_loop(loop)
    try:
        print("Listening for events on Curve.fi ...")
        loop.run_until_complete(
            asyncio.gather(
                *[log_loop(event_filter, POLLING_INTERVAL) for event_filter in event_filters]))
    finally:
        loop.close()


def calc_virt_price():
    curve_total_supply = contract_curve.caller().totalSupply()
    print(D * PRECISION / Decimal(curve_total_supply)) 

def calc_dy(i, j, dx):
    x = XP[i] + dx * Decimal(DAI_multiplier)
    y = _get_y(i, j, x)
    dy = XP[j] - y
    fee = Decimal(FEE) * dy
    print((dy - fee) / Decimal(DAI_multiplier))

def main():

    loop = asyncio.get_event_loop()
    t = threading.Thread(target=loop_in_thread, args=(loop,))
    t.start()

    COMMANDS = ['get_virtual_price', 'get_dy']

    while True:
        command = input("type your command, followed by args: ")
        command = command.split()
        if command[0] not in COMMANDS:
            print("command not supported... try again")
        if command[0] == 'get_virtual_price':
            print("calculating virtual price of this 3pool...")
            calc_virt_price()
        if command[0] == 'get_dy':
            if len(command) != 4:
                print("incorrect amount of arguments")
                continue
            print("calculating dy with supplied arguments")
            i, j, dx = int(command[1]), int(command[2]), int(command[3])
            calc_dy(i, j, dx)

    print("next steps")

main()