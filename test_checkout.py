from Checkout import checkout
import pytest

@pytest.fixture()
def co():
    co= checkout()
    co.addItemPrice("a",1)
    co.addItemPrice("b",2)
    return co

def test_calculateTotal(co):
    co.addItemPrice("a",1)
    co.addItem("a")
    assert co.calculateTotal() == 1

def test_calculateTotalWithMultipleItems(co):
    co.addItem("a")
    co.addItem("b")
    assert co.calculateTotal() == 3

def test_canAddDiscountRule(co):
    co.addDiscount("a",3,2)

def test_canApplyDiscountRule(co):
    co.addDiscount("a",3,2)
    co.addItem("a")
    co.addItem("a")
    co.addItem("a")
    assert co.calculateTotal() == 2

def test_ExceptionWithBadItem(co):
    with pytest.raises(Exception):
        co.addItem("c")