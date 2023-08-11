import pytest
from account import Account

def test_deposit():
    account = Account("John")
    assert account.deposit(100) == True
    assert account.get_balance() == 100

def test_withdraw():
    account = Account("John")
    account.deposit(100)
    assert account.withdraw(50) == True
    assert account.get_balance() == 50

def test_invalid_withdraw():
    account = Account("John")
    account.deposit(100)
    assert account.withdraw(150) == False
    assert account.get_balance() == 100

def test_get_name():
    account = Account("John")
    assert account.get_name() == "John"
