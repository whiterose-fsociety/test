# test_wallet.py
import pytest
from wallet import Wallet,InsufficientAmount
@pytest.fixture
def my_wallet():
    """Returns a Wallet Instance With A Zero Balance"""
    return Wallet()

@pytest.mark.parametrize("earned,spent,expected",[
    (30, 10, 20),
    (20, 2, 18),
])
def test_transaction(my_wallet,earned,spent,expected):
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected
