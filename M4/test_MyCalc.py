from MyCalc import MyCalc

calc = MyCalc

def test_add():
    check = calc.add(3,4)
    assert check == 7

def test_add_ans():
    check = calc.add("ans",3)
    assert check == 10
