from MyCalc import MyCalc

calc = MyCalc()

def test_number_add_number():
    check = calc.calculate(3,4,'+')
    assert check == 7
    #UCID: sk3374
    #Date: 2/25/23 8:30 PM
    #function test_number_add_number() calls calculate() function using an object calc of class MyClass
    #we use test parameters 3,4,+ for testing addition.
    #then we use assert to compare the result the function returns and the expected result (i.e 7 in our case)
    
def test_ans_add_number(): 
    check = calc.calculate("ans",3,'+')
    assert check == 10
    #UCID: sk3374
    #Date: 2/25/23 8:39 PM
    #function test_ans_add_number() calls calculate() function using an object calc of class MyClass
    #we use test parameters "ans",3,- for testing addition when we "ans" as num1.
    #then we use assert to compare the result the function returns and the expected result (i.e 10 in our case)    

def test_number_sub_number():
    check = calc.calculate(2,9,'-')
    assert check == -7
    #UCID: sk3374
    #Date: 2/25/23 8:46 PM
    #function test_number_sub_number() calls calculate() function using an object calc of class MyClass
    #we use test parameters 2,9,- for testing subtraction.
    #then we use assert to compare the result the function returns and the expected result (i.e -7 in our case)

def test_ans_sub_number():
    check = calc.calculate("ans",-7,'-')
    assert check == 0
    #UCID: sk3374
    #Date: 2/25/23 8:55 PM
    #function test_ans_sub_number() calls calculate() function using an object calc of class MyClass
    #we use test parameters "ans",-7,- for testing subtraction when we "ans" as num1.
    #then we use assert to compare the result the function returns and the expected result (i.e 0 in our case)

def test_number_mult_number():
    check = calc.calculate(3,2,'*')
    assert check == 6
    #UCID: sk3374
    #Date: 2/25/23 9:13 PM
    #function test_number_mult_number() calls calculate() function using an object calc of class MyClass
    #we use test parameters 3,2,* for testing multiplication.
    #then we use assert to compare the result the function returns and the expected result (i.e 6 in our case)

def test_ans_mult_number():
    check = calc.calculate("ans",3,'*')
    assert check == 18
    #UCID: sk3374
    #Date: 2/25/23 9:23 PM
    #function test_ans_mult_number() calls calculate() function using an object calc of class MyClass
    #we use test parameters "ans",3,'*' for testing multiplication when "ans" is used as num1.
    #then we use assert to compare the result the function returns and the expected result (i.e 18 in our case)

def test_number_div_number():
    check = calc.calculate(18,9,'/')
    assert check == 2
    #UCID: sk3374
    #Date: 2/25/23 9:30 PM
    #function test_number_div_number() calls calculate() function using an object calc of class MyClass
    #we use test parameters 18,9,/ for testing division.
    #then we use assert to compare the result the function returns and the expected result (i.e 2 in our case)

def test_ans_div_number():
    check = calc.calculate("ans",4,'/')
    assert check == 0.5
    #UCID: sk3374
    #Date: 2/25/23 9:30 PM
    #function test_ans_div_number() calls calculate() function using an object calc of class MyClass
    #we use test parameters "ans",4,/ for testing division.
    #then we use assert to compare the result the function returns and the expected result (i.e 0.5 in our case)
