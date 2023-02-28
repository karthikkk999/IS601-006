from MyCalc import MyCalc

calc = MyCalc()

def test_number_add_number():
    assert calc.calculate(6,4,'+') == 10
    assert calc.calculate(3,4,'+') == 7
    assert calc.calculate(2,4,'+') == 6
    #UCID: sk3374
    #Date: 2/25/23 8:30 PM
    #function test_number_add_number() tests the addition of two numbers 
    #In the assert statement we call the calculate() function which calls add() based on passed operator (i.e '+')
    #we compare the result the calculate() returns with the expected result and mark the check as failed or passed in the assert.
    #we perform this check using several asserts with different data

def test_ans_add_number(): 
    calc.calculate(2,4,'+')
    assert calc.calculate("ans",3,'+')  == 9
    assert calc.calculate("ans",1,'+')  == 10
    assert calc.calculate("ans",4,'+')  == 14
    #UCID: sk3374
    #Date: 2/25/23 8:39 PM
    #function test_ans_add_number() tests the addition with previous result using ans as num1 
    #In the assert statement we call the calculate() function which calls add() based on passed operator (i.e '+')
    #we compare the result the calculate() returns with the expected result and mark the check as failed or passed in the assert.
    #we perform this check using several asserts with different data

def test_number_sub_number():
    assert calc.calculate(1,0,'-') == 1
    assert calc.calculate(10,5,'-') == 5
    assert calc.calculate(2,9,'-') == -7
    #UCID: sk3374
    #Date: 2/25/23 8:46 PM
    #function test_number_sub_number() tests the subtraction of two numbers 
    #In the assert statement we call the calculate() function which calls sub() based on passed operator (i.e '-')
    #we compare the result the calculate() returns with the expected result and mark the check as failed or passed in the assert.
    #we perform this check using several asserts with different data

def test_ans_sub_number():
    calc.calculate(2,9,'-')
    assert calc.calculate("ans",-7,'-') == 0
    assert calc.calculate("ans",5,'-') == -5
    assert calc.calculate("ans",-6,'-') == 1
    #UCID: sk3374
    #Date: 2/25/23 8:55 PM
    #function test_ans_sub_number() tests the subtraction with previous result using ans as num1 
    #In the assert statement we call the calculate() function which calls sub() based on passed operator (i.e '-')
    #we compare the result the calculate() returns with the expected result and mark the check as failed or passed in the assert.
    #we perform this check using several asserts with different data

def test_number_mult_number():
    assert calc.calculate(13,3,'*') == 39
    assert calc.calculate(30,-2,'*') == -60
    assert calc.calculate(3,2,'*') == 6
    #UCID: sk3374
    #Date: 2/25/23 9:13 PM
    #function test_number_mult_number() tests the multiplication of two numbers 
    #In the assert statement we call the calculate() function which calls mul() based on passed operator (i.e '*')
    #we compare the result the calculate() returns with the expected result and mark the check as failed or passed in the assert.
    #we perform this check using several asserts with different data

def test_ans_mult_number():
    calc.calculate(3,2,'*')
    assert calc.calculate("ans",3,'*') == 18
    assert calc.calculate("ans",0.5,'*') == 9
    assert calc.calculate("ans",3,'*') == 27
    #UCID: sk3374
    #Date: 2/25/23 9:23 PM
    #function test_ans_mult_number() tests the muliplicaton with the previous result using ans as num1 
    #In the assert statement we call the calculate() function which calls mul() based on passed operator (i.e '*')
    #we compare the result the calculate() returns with the expected result and mark the check as failed or passed in the assert.
    #we perform this check using several asserts with different data

def test_number_div_number():
    assert calc.calculate(100,2,'/') == 50
    assert calc.calculate(69,3,'/') == 23
    assert calc.calculate(18,9,'/') == 2
    #UCID: sk3374
    #Date: 2/25/23 9:30 PM
    #function test_number_div_number() tests the division using two numbers 
    #In the assert statement we call the calculate() function which calls div() based on passed operator (i.e '/')
    #we compare the result the calculate() returns with the expected result and mark the check as failed or passed in the assert.
    #we perform this check using several asserts with different data

def test_ans_div_number():
    calc.calculate(18,9,'/')
    assert calc.calculate("ans",4,'/') == 0.5
    assert calc.calculate("ans",0.5,'/') == 1
    assert calc.calculate("ans",1000,'/') == 0.001
    #UCID: sk3374
    #Date: 2/25/23 9:30 PM
    #function test_ans_div_number() tests the division by using the previous number as the divident (ans as num1) 
    #In the assert statement we call the calculate() function which calls div() based on passed operator (i.e '/')
    #we compare the result the calculate() returns with the expected result and mark the check as failed or passed in the assert.
    #we perform this check using several asserts with different data